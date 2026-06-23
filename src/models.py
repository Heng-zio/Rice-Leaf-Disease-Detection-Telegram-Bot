"""Data models for the Rice Disease Telegram Bot."""
from dataclasses import dataclass
from typing import Dict, List


@dataclass
class PredictionResult:
    """Result of disease prediction."""
    disease_name: str
    confidence: float
    all_probabilities: Dict[str, float]
    is_confident: bool


@dataclass
class DiseaseInfo:
    """Information about a rice disease."""
    name_en: str
    name_km: str
    description_km: str
    symptoms_km: List[str]
