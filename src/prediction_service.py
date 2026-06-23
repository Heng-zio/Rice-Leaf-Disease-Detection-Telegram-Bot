"""Prediction service for rice disease classification."""
import numpy as np
from PIL import Image
import io
import os
import tensorflow as tf
from tensorflow import keras

from src.models import PredictionResult
from src.constants import DISEASE_CLASSES, DISEASE_NAMES_EN
from src.config import Config
from src.exceptions import InvalidImageError, ModelError


class PredictionService:
    """Service for predicting rice diseases from images using two-stage approach."""
    
    def __init__(self, model_path: str = None):
        """Initialize prediction service with trained models."""
        if model_path is None:
            model_path = Config.MODEL_PATH
        
        # Load rice leaf classifier (stage 1: not_rice_leaf vs rice_leaf)
        classifier_path = './models/not_rice_leaf_classifier.h5'
        if os.path.exists(classifier_path):
            print(f"Loading rice leaf classifier from {classifier_path}...")
            try:
                self.classifier_model = keras.models.load_model(classifier_path)
                print("✅ Rice leaf classifier loaded successfully")
            except Exception as e:
                print(f"⚠️ Warning: Failed to load classifier: {e}")
                self.classifier_model = None
        else:
            print(f"⚠️ Warning: Classifier not found at {classifier_path}")
            self.classifier_model = None
        
        # Load disease classification model (stage 2: disease types)
        print(f"Loading disease model from {model_path}...")
        try:
            self.disease_model = keras.models.load_model(model_path)
            print("✅ Disease model loaded successfully")
        except Exception as e:
            raise ModelError(f"Failed to load disease model: {e}")
        
        self.image_size = Config.IMAGE_SIZE
        self.confidence_threshold = Config.CONFIDENCE_THRESHOLD
    
    def preprocess_image(self, image_bytes: bytes) -> np.ndarray:
        """
        Preprocess image for model input.
        
        Args:
            image_bytes: Raw image bytes
            
        Returns:
            Preprocessed image array ready for model
        """
        try:
            # Open image from bytes
            image = Image.open(io.BytesIO(image_bytes))
            
            # Convert to RGB if needed
            if image.mode != 'RGB':
                image = image.convert('RGB')
            
            # Resize to model input size
            image = image.resize((self.image_size, self.image_size))
            
            # Convert to array and normalize
            image_array = np.array(image)
            image_array = image_array / 255.0  # Normalize to [0, 1]
            
            # Add batch dimension
            image_array = np.expand_dims(image_array, axis=0)
            
            return image_array
            
        except Exception as e:
            raise InvalidImageError(f"Failed to preprocess image: {e}")
    
    def predict(self, image_bytes: bytes) -> PredictionResult:
        """
        Predict disease from image using two-stage approach.
        
        Stage 1: Check if it's a rice leaf or not
        Stage 2: If rice leaf, classify the disease
        
        Args:
            image_bytes: Raw image bytes
            
        Returns:
            PredictionResult with disease classification
        """
        # Preprocess image
        image_array = self.preprocess_image(image_bytes)
        
        # Stage 1: Check if it's a rice leaf
        if self.classifier_model is not None:
            try:
                classifier_predictions = self.classifier_model.predict(image_array, verbose=0)
                classifier_probs = classifier_predictions[0]
                
                # Index 0: not_rice_leaf, Index 1: rice_leaf
                not_rice_leaf_prob = float(classifier_probs[0])
                rice_leaf_prob = float(classifier_probs[1])
                
                # If it's not a rice leaf (with high confidence)
                if not_rice_leaf_prob > 0.7:  # 70% threshold
                    return PredictionResult(
                        disease_name='not_rice_leaf',
                        confidence=not_rice_leaf_prob,
                        all_probabilities={
                            'not_rice_leaf': not_rice_leaf_prob,
                            'rice_leaf': rice_leaf_prob
                        },
                        is_confident=True
                    )
            except Exception as e:
                print(f"⚠️ Classifier prediction failed: {e}, proceeding to disease model")
        
        # Stage 2: It's a rice leaf, classify the disease
        try:
            predictions = self.disease_model.predict(image_array, verbose=0)
            probabilities = predictions[0]
        except Exception as e:
            raise ModelError(f"Disease prediction failed: {e}")
        
        # Get predicted class
        predicted_index = np.argmax(probabilities)
        predicted_disease = DISEASE_CLASSES[predicted_index]
        confidence = float(probabilities[predicted_index])
        
        # Create probability dictionary
        all_probabilities = {
            DISEASE_CLASSES[i]: float(probabilities[i])
            for i in range(len(DISEASE_CLASSES))
        }
        
        # Check if prediction is confident
        is_confident = confidence >= self.confidence_threshold
        
        return PredictionResult(
            disease_name=predicted_disease,
            confidence=confidence,
            all_probabilities=all_probabilities,
            is_confident=is_confident
        )
    
    def get_disease_info(self, disease_name: str, language: str = 'km') -> str:
        """
        Get disease information.
        
        Args:
            disease_name: Name of the disease
            language: Language code ('en' or 'km')
            
        Returns:
            Disease information string
        """
        # This is handled by MessageFormatter, but kept for interface compatibility
        from src.message_formatter import MessageFormatter
        disease_info = MessageFormatter.DISEASE_INFO.get(disease_name, {})
        return disease_info.get('description', '')



