"""Custom exceptions for the Rice Disease Bot."""


class InvalidImageError(Exception):
    """Raised when image cannot be processed."""
    pass


class ModelError(Exception):
    """Raised when model operations fail."""
    pass
