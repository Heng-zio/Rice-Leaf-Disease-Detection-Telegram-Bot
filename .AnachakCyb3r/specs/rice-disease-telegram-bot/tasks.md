# Implementation Plan

- [x] 1. Set up project structure and dependencies
  - Create Python project directory structure (src/, models/, config/, tests/)
  - Create requirements.txt with all necessary dependencies
  - Create .env.example file for configuration template
  - Create .gitignore for Python project
  - _Requirements: 6.1, 6.2_

- [x] 2. Implement configuration management
  - Create config.py module to load environment variables
  - Implement validation for required configuration parameters (TELEGRAM_BOT_TOKEN, MODEL_PATH)
  - Add default values for optional parameters (CONFIDENCE_THRESHOLD, IMAGE_SIZE)
  - _Requirements: 6.1, 6.2, 6.3_

- [x] 3. Create data models and constants
  - Define PredictionResult dataclass with disease_name, confidence, all_probabilities, is_confident fields
  - Define DiseaseInfo dataclass with name_en, name_km, description_km, symptoms_km fields
  - Create constants file with disease class names and indices mapping
  - _Requirements: 3.1, 4.2_

- [x] 4. Implement message formatter for Khmer language support
  - Create MessageFormatter class with static methods
  - Implement format_welcome_message() with Khmer welcome text and usage instructions
  - Implement format_prediction_result() to display disease name, confidence, and description in Khmer
  - Implement format_error_message() for various error types (invalid_image, processing_failed, generic_error)
  - Create disease information dictionary with Khmer descriptions for all 5 disease types
  - _Requirements: 1.1, 1.2, 3.4, 4.1, 4.2, 4.3, 5.3_

- [x] 5. Build CNN model training pipeline
  - Create data loading script to read images from dataset folders (bacterial_leaf_blight, brown_spot, healthy, rice_blast, tunggro_virus)
  - Implement data augmentation (rotation, flip, zoom) to increase dataset size
  - Split dataset into training (70%), validation (15%), and test (15%) sets
  - Create model architecture using transfer learning with MobileNetV2 base
  - Add custom classification head with 5-class softmax output
  - Implement training loop with early stopping and model checkpointing
  - Train model and save best weights to models/ directory
  - _Requirements: 3.1_

- [ ]* 5.1 Evaluate model performance
  - Generate confusion matrix on test set
  - Calculate accuracy, precision, recall, and F1-score for each disease class
  - Verify model achieves >85% accuracy target
  - _Requirements: 3.1_

- [x] 6. Implement prediction service
  - Create PredictionService class with model loading in __init__
  - Implement preprocess_image() to resize, normalize, and convert image to model input format
  - Implement predict() method to run inference and return PredictionResult
  - Implement get_disease_info() to retrieve Khmer disease information based on predicted class
  - Add confidence threshold check (default 0.6) to set is_confident flag
  - _Requirements: 2.2, 3.1, 3.2, 3.5, 4.2_

- [ ]* 6.1 Add prediction service unit tests
  - Test image preprocessing with different image formats (JPEG, PNG)
  - Mock model predictions and verify PredictionResult creation
  - Test confidence threshold logic with various confidence values
  - _Requirements: 3.1, 3.2, 3.5_

- [x] 7. Implement Telegram bot handler
  - Create TelegramBotHandler class with bot token and PredictionService initialization
  - Implement handle_start_command() to send welcome message in Khmer
  - Implement handle_help_command() to send usage instructions
  - Implement handle_photo_message() to download image, validate format, and process through PredictionService
  - Add image acknowledgment message within 2 seconds of receipt
  - Implement send_response() to format and send prediction results to user
  - Add error handling for non-image files with appropriate Khmer error message
  - _Requirements: 1.1, 1.2, 1.3, 2.1, 2.2, 2.3, 2.4, 3.3, 3.4, 3.5_

- [ ]* 7.1 Add bot handler unit tests
  - Test command handlers with mock Telegram Update objects
  - Test photo message handling with mock image data
  - Test error handling for invalid file types
  - Verify response formatting and timing requirements
  - _Requirements: 1.1, 1.2, 1.3, 2.1, 2.2, 2.3, 2.4_

- [x] 8. Implement error handling and logging
  - Create custom exception classes (InvalidImageError, ModelError)
  - Add try-catch blocks in bot handler for graceful error handling
  - Implement logging configuration with file rotation
  - Add error logging with timestamps and details for all exceptions
  - Implement reconnection logic for Telegram API connection failures
  - _Requirements: 5.1, 5.2, 5.3, 5.4_

- [x] 9. Create main application entry point
  - Create main.py to initialize configuration, prediction service, and bot handler
  - Add startup validation for API token and model file existence
  - Implement bot.start_bot() to begin polling for messages
  - Add graceful shutdown handling
  - _Requirements: 6.1, 6.2, 6.3_

- [x] 10. Create deployment documentation
  - Write README.md with setup instructions
  - Document how to obtain Telegram Bot token from BotFather
  - Document environment variable configuration
  - Add instructions for installing dependencies and running the bot
  - Include troubleshooting section for common issues
  - _Requirements: 6.1, 6.2_
