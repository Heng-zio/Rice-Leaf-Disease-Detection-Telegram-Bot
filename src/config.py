"""Configuration management for the Rice Disease Telegram Bot."""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """Application configuration."""
    
    # Required configuration
    TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    MODEL_PATH = os.getenv('MODEL_PATH', './models/rice_disease_model.h5')
    
    # Optional configuration with defaults
    CONFIDENCE_THRESHOLD = float(os.getenv('CONFIDENCE_THRESHOLD', '0.6'))
    IMAGE_SIZE = int(os.getenv('IMAGE_SIZE', '224'))
    MAX_IMAGE_SIZE_MB = int(os.getenv('MAX_IMAGE_SIZE_MB', '10'))
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    
    @classmethod
    def validate(cls):
        """Validate required configuration parameters."""
        errors = []
        
        if not cls.TELEGRAM_BOT_TOKEN:
            errors.append("TELEGRAM_BOT_TOKEN is required but not set")
        elif not cls._is_valid_token_format(cls.TELEGRAM_BOT_TOKEN):
            errors.append("TELEGRAM_BOT_TOKEN format is invalid")
        
        if not cls.MODEL_PATH:
            errors.append("MODEL_PATH is required but not set")
        
        if cls.CONFIDENCE_THRESHOLD < 0 or cls.CONFIDENCE_THRESHOLD > 1:
            errors.append("CONFIDENCE_THRESHOLD must be between 0 and 1")
        
        if errors:
            raise ValueError(f"Configuration validation failed:\n" + "\n".join(f"  - {e}" for e in errors))
    
    @staticmethod
    def _is_valid_token_format(token):
        """Check if token has valid format (basic check)."""
        if not token or len(token) < 20:
            return False
        # Telegram bot tokens typically contain a colon
        return ':' in token
