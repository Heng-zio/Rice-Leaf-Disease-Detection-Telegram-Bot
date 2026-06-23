"""Constants for the Rice Disease Telegram Bot."""

# Disease class names and their indices
DISEASE_CLASSES = {
    0: 'bacterial_leaf_blight',
    1: 'brown_spot',
    2: 'healthy',
    3: 'rice_blast',
    4: 'tungro_disease'
}

# Reverse mapping for convenience
CLASS_TO_INDEX = {v: k for k, v in DISEASE_CLASSES.items()}

# Disease names in English
DISEASE_NAMES_EN = {
    'bacterial_leaf_blight': 'Bacterial Leaf Blight',
    'brown_spot': 'Brown Spot',
    'healthy': 'Healthy',
    'rice_blast': 'Rice Blast',
    'tungro_disease': 'Tungro Disease',
    'not_rice_leaf': 'Not Rice Leaf'
}

# Disease names in Khmer
DISEASE_NAMES_KM = {
    'bacterial_leaf_blight': 'ជំងឺបាក់តេរីស្រពោនស្លឹក',
    'brown_spot': 'ជំងឺអុតត្នោត',
    'healthy': 'គ្មានជំងឺ',
    'rice_blast': 'ជំងឺខ្នារអំបោះត្នោត',
    'tungro_disease': 'ជំងឺទង់គ្រោ',
    'not_rice_leaf': 'មិនមែនស្លឹកស្រូវ'
}
