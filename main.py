"""Main entry point for the Rice Disease Telegram Bot."""
import os
import sys
import logging

from src.config import Config
from src.logging_config import setup_logging
from src.prediction_service import PredictionService
from src.bot_handler import TelegramBotHandler

logger = logging.getLogger(__name__)


def validate_startup():
    """Validate configuration and required files before starting."""
    errors = []
    
    # Validate configuration
    try:
        Config.validate()
    except ValueError as e:
        errors.append(str(e))
    
    # Check if model file exists
    if not os.path.exists(Config.MODEL_PATH):
        errors.append(
            f"Model file not found at {Config.MODEL_PATH}\n"
            f"  Please train the model first by running: python train_model.py"
        )
    
    if errors:
        print("❌ Startup validation failed:\n")
        for error in errors:
            print(error)
        print("\nPlease fix the above issues and try again.")
        sys.exit(1)


def main():
    """Main function to start the bot."""
    # Setup logging
    setup_logging()
    
    print("\n" + "=" * 60)
    print("🌾 RICE DISEASE TELEGRAM BOT")
    print("   For Cambodian Farmers")
    print("=" * 60)
    logger.info("Starting Rice Disease Telegram Bot...")
    
    # Validate startup requirements
    try:
        validate_startup()
        logger.info("Startup validation passed")
    except Exception as e:
        logger.error(f"Startup validation failed: {e}")
        sys.exit(1)
    
    # Initialize prediction service
    try:
        logger.info("Initializing prediction service...")
        prediction_service = PredictionService(Config.MODEL_PATH)
        logger.info("Prediction service initialized")
    except Exception as e:
        logger.error(f"Failed to initialize prediction service: {e}")
        sys.exit(1)
    
    # Initialize bot handler
    try:
        logger.info("Initializing bot handler...")
        bot_handler = TelegramBotHandler(Config.TELEGRAM_BOT_TOKEN, prediction_service)
        logger.info("Bot handler initialized")
    except Exception as e:
        logger.error(f"Failed to initialize bot handler: {e}")
        sys.exit(1)
    
    # Start bot
    try:
        logger.info("Starting bot polling...")
        bot_handler.start_bot()
    except KeyboardInterrupt:
        logger.info("\n👋 Bot stopped by user")
    except Exception as e:
        logger.error(f"Bot crashed: {e}", exc_info=True)
        sys.exit(1)


if __name__ == '__main__':
    main()
