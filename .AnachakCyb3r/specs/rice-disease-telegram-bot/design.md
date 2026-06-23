# Design Document

## Overview

The Rice Disease Telegram Bot is a Python-based application that integrates Telegram's Bot API with a deep learning image classification model. The system uses a convolutional neural network (CNN) trained on the provided rice leaf disease dataset to classify images into five categories. The bot is designed to be simple, accessible, and focused on the core disease detection feature for Cambodian farmers.

## Architecture

The system follows a modular architecture with three main layers:

1. **Presentation Layer**: Telegram Bot interface that handles user interactions
2. **Business Logic Layer**: Message processing, command handling, and response formatting
3. **Model Layer**: Image classification using a trained CNN model

```
┌─────────────────────────────────────────────────────────────┐
│                        Telegram API                          │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                     Bot Handler                              │
│  - Command Processing (/start, /help)                       │
│  - Image Reception & Validation                             │
│  - Response Formatting (Khmer)                              │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                  Prediction Service                          │
│  - Image Preprocessing                                       │
│  - Model Inference                                           │
│  - Result Post-processing                                    │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                   CNN Model (TensorFlow/PyTorch)            │
│  - Pre-trained or Custom CNN                                │
│  - 5-class Classification                                    │
└─────────────────────────────────────────────────────────────┘
```

## Components and Interfaces

### 1. Bot Handler Component

**Responsibility**: Manages all Telegram bot interactions and message routing

**Key Classes**:
- `TelegramBotHandler`: Main bot controller
  - `handle_start_command()`: Processes /start command
  - `handle_help_command()`: Processes /help command
  - `handle_photo_message()`: Processes incoming images
  - `send_response()`: Sends formatted messages to users

**Dependencies**: 
- `python-telegram-bot` library
- `PredictionService`
- `MessageFormatter`

**Interface**:
```python
class TelegramBotHandler:
    def __init__(self, token: str, prediction_service: PredictionService)
    async def handle_start_command(update: Update, context: ContextTypes.DEFAULT_TYPE)
    async def handle_photo_message(update: Update, context: ContextTypes.DEFAULT_TYPE)
    def start_bot()
```

### 2. Prediction Service Component

**Responsibility**: Handles image processing and disease classification

**Key Classes**:
- `PredictionService`: Coordinates prediction workflow
  - `preprocess_image()`: Prepares image for model input
  - `predict()`: Runs inference and returns results
  - `get_disease_info()`: Retrieves disease information

**Dependencies**:
- TensorFlow/Keras or PyTorch
- PIL/OpenCV for image processing
- Trained model file

**Interface**:
```python
class PredictionService:
    def __init__(self, model_path: str)
    def preprocess_image(image_bytes: bytes) -> np.ndarray
    def predict(image: np.ndarray) -> PredictionResult
    def get_disease_info(disease_name: str, language: str = 'km') -> str
```

### 3. Model Component

**Responsibility**: Deep learning model for disease classification

**Architecture**: 
- Input: 224x224x3 RGB images (standard CNN input size)
- Base: Transfer learning with MobileNetV2 or EfficientNet (lightweight for deployment)
- Output: 5-class softmax layer

**Classes**:
- `bacterial_leaf_blight` (index 0)
- `brown_spot` (index 1)
- `healthy` (index 2)
- `rice_blast` (index 3)
- `tunggro_virus` (index 4)

### 4. Message Formatter Component

**Responsibility**: Formats bot responses in Khmer language

**Key Classes**:
- `MessageFormatter`: Handles message localization
  - `format_welcome_message()`: Creates welcome text
  - `format_prediction_result()`: Formats classification results
  - `format_error_message()`: Creates error messages

**Interface**:
```python
class MessageFormatter:
    @staticmethod
    def format_welcome_message() -> str
    @staticmethod
    def format_prediction_result(result: PredictionResult) -> str
    @staticmethod
    def format_error_message(error_type: str) -> str
```

### 5. Configuration Component

**Responsibility**: Manages application configuration

**Configuration Parameters**:
- `TELEGRAM_BOT_TOKEN`: Bot API token from BotFather
- `MODEL_PATH`: Path to trained model file
- `CONFIDENCE_THRESHOLD`: Minimum confidence for reliable predictions (default: 0.6)
- `IMAGE_SIZE`: Input image dimensions (default: 224x224)
- `MAX_IMAGE_SIZE_MB`: Maximum upload size (default: 10MB)

## Data Models

### PredictionResult

```python
@dataclass
class PredictionResult:
    disease_name: str
    confidence: float
    all_probabilities: Dict[str, float]
    is_confident: bool  # True if confidence > threshold
```

### DiseaseInfo

```python
@dataclass
class DiseaseInfo:
    name_en: str
    name_km: str
    description_km: str
    symptoms_km: List[str]
```

## Error Handling

### Error Categories

1. **User Input Errors**:
   - Invalid file format (not an image)
   - Image too large
   - Corrupted image file
   - Response: User-friendly Khmer message with guidance

2. **Model Errors**:
   - Model file not found
   - Prediction failure
   - Response: Generic error message, log details for admin

3. **Network Errors**:
   - Telegram API connection issues
   - Image download failures
   - Response: Retry mechanism with exponential backoff

4. **Configuration Errors**:
   - Missing API token
   - Invalid configuration
   - Response: Fail fast at startup with clear error message

### Error Handling Strategy

```python
try:
    # Process image
    result = prediction_service.predict(image)
    await send_result(result)
except InvalidImageError as e:
    await send_error_message("invalid_image")
except ModelError as e:
    logger.error(f"Model error: {e}")
    await send_error_message("processing_failed")
except Exception as e:
    logger.error(f"Unexpected error: {e}")
    await send_error_message("generic_error")
```

## Testing Strategy

### Unit Tests

1. **Message Formatter Tests**:
   - Verify Khmer text formatting
   - Test all message types (welcome, results, errors)

2. **Prediction Service Tests**:
   - Test image preprocessing with various formats
   - Mock model predictions and verify result formatting
   - Test confidence threshold logic

3. **Configuration Tests**:
   - Verify configuration loading
   - Test validation of required parameters

### Integration Tests

1. **Bot Handler Integration**:
   - Test command handling with mock Telegram updates
   - Verify image processing pipeline
   - Test error propagation

2. **End-to-End Flow**:
   - Simulate user sending /start command
   - Simulate user sending image
   - Verify complete response flow

### Model Testing

1. **Accuracy Testing**:
   - Evaluate model on validation set from dataset
   - Target: >85% accuracy on test set

2. **Inference Performance**:
   - Measure prediction time
   - Target: <5 seconds per image

### Manual Testing

1. **Telegram Bot Testing**:
   - Test with real Telegram account
   - Verify Khmer text displays correctly
   - Test with various rice leaf images
   - Test error scenarios (invalid files, etc.)

## Deployment Considerations

### Initial Deployment (MVP)

- **Platform**: Local machine or simple cloud VM (e.g., DigitalOcean, AWS EC2)
- **Runtime**: Python 3.9+
- **Process Management**: systemd or PM2 for keeping bot running
- **Model Storage**: Local file system
- **Logging**: File-based logging with rotation

### Environment Variables

```bash
TELEGRAM_BOT_TOKEN=your_bot_token_here
MODEL_PATH=./models/rice_disease_model.h5
CONFIDENCE_THRESHOLD=0.6
LOG_LEVEL=INFO
```

### Dependencies

```
python-telegram-bot>=20.0
tensorflow>=2.12.0  # or pytorch>=2.0.0
pillow>=9.0.0
numpy>=1.23.0
python-dotenv>=1.0.0
```

## Future Enhancements (Out of Scope for MVP)

- Treatment recommendations for each disease
- Multi-language support (English, Khmer)
- User history and analytics
- Image quality validation before prediction
- Batch processing for multiple images
- Integration with agricultural extension services
- Database for storing user interactions
