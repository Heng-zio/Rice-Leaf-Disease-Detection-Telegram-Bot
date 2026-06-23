# 🌾 Rice Disease Telegram Bot

A Telegram chatbot that helps Cambodian farmers identify rice leaf diseases using AI image classification. The bot can detect 5 types of rice conditions:

- **Bacterial Leaf Blight** (ជំងឺស្លឹកស្រូវរលាកបាក់តេរី)
- **Brown Spot** (ជំងឺស្លឹកស្រូវពណ៌ត្នោត)
- **Healthy** (ស្លឹកស្រូវមានសុខភាពល្អ)
- **Rice Blast** (ជំងឺស្លឹកស្រូវផ្សិត)
- **Tunggro Virus** (ជំងឺស្រូវតុងរ៉ូ)

## Features

- 📸 Image-based disease detection
- 🇰🇭 Full Khmer language support
- 🤖 Easy-to-use Telegram interface
- 🎯 High accuracy CNN model using transfer learning
- ⚡ Fast predictions (< 10 seconds)

## Prerequisites

- Python 3.9 or higher
- Telegram account
- Rice leaf disease dataset (organized in folders)

## Setup Instructions

### 1. Get a Telegram Bot Token

1. Open Telegram and search for [@BotFather](https://t.me/botfather)
2. Send `/newbot` command
3. Follow the instructions to create your bot
4. Copy the bot token (looks like: `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`)

### 2. Clone and Install

```bash
# Install dependencies
pip install -r requirements.txt
```

### 3. Configure Environment

Create a `.env` file in the project root:

```bash
cp .env.example .env
```

Edit `.env` and add your bot token:

```
TELEGRAM_BOT_TOKEN=your_bot_token_here
MODEL_PATH=./models/rice_disease_model.h5
CONFIDENCE_THRESHOLD=0.6
LOG_LEVEL=INFO
```

### 4. Prepare Dataset

Organize your rice disease images in the following structure:

```
dataset/
├── bacterial_leaf_blight/
│   ├── image1.jpg
│   ├── image2.jpg
│   └── ...
├── brown_spot/
│   └── ...
├── healthy/
│   └── ...
├── rice_blast/
│   └── ...
└── tunggro_virus/
    └── ...
```

### 5. Train the Model

```bash
python train_model.py
```

This will:
- Load and augment your dataset
- Train a MobileNetV2-based CNN model
- Save the best model to `./models/rice_disease_model.h5`
- Display training progress and accuracy

Training may take 30-60 minutes depending on your dataset size and hardware.

### 6. Run the Bot

```bash
python main.py
```

You should see:

```
🌾 Rice Disease Telegram Bot Starting...
✅ Startup validation passed
✅ Prediction service initialized
✅ Bot handler initialized
✅ Bot is running! Press Ctrl+C to stop.
```

## Usage

1. Open Telegram and search for your bot (use the username you created with BotFather)
2. Send `/start` to begin
3. Take a photo of a rice leaf or send an existing image
4. Wait for the bot to analyze the image
5. Receive the disease classification result in Khmer

## Commands

- `/start` - Start the bot and see welcome message
- `/help` - Get help and usage instructions

## Project Structure

```
.
├── src/
│   ├── __init__.py
│   ├── bot_handler.py          # Telegram bot logic
│   ├── config.py                # Configuration management
│   ├── constants.py             # Disease classes and names
│   ├── exceptions.py            # Custom exceptions
│   ├── logging_config.py        # Logging setup
│   ├── message_formatter.py     # Khmer message formatting
│   ├── models.py                # Data models
│   └── prediction_service.py    # Disease prediction logic
├── models/
│   └── rice_disease_model.h5    # Trained model (after training)
├── dataset/                      # Your training images
├── logs/                         # Application logs
├── main.py                       # Application entry point
├── train_model.py                # Model training script
├── requirements.txt              # Python dependencies
├── .env                          # Configuration (create this)
└── README.md                     # This file
```

## Troubleshooting

### Bot doesn't respond

- Check that your bot token is correct in `.env`
- Make sure the bot is running (`python main.py`)
- Check logs in `logs/bot.log` for errors

### Model not found error

- Train the model first: `python train_model.py`
- Check that `MODEL_PATH` in `.env` points to the correct file

### Low accuracy predictions

- Ensure your dataset has enough images (at least 100 per class)
- Check that images are clear and properly labeled
- Try training for more epochs
- Consider collecting more diverse training data

### Image processing errors

- Ensure images are in common formats (JPG, PNG)
- Check that images are not corrupted
- Try with a different image

### Connection errors

- Check your internet connection
- Verify the bot token is valid
- Check if Telegram is accessible in your region

## Configuration Options

Edit `.env` to customize:

- `TELEGRAM_BOT_TOKEN` - Your bot token (required)
- `MODEL_PATH` - Path to trained model (default: `./models/rice_disease_model.h5`)
- `CONFIDENCE_THRESHOLD` - Minimum confidence for reliable predictions (default: `0.6`)
- `IMAGE_SIZE` - Input image size for model (default: `224`)
- `LOG_LEVEL` - Logging level: DEBUG, INFO, WARNING, ERROR (default: `INFO`)

## Technical Details

- **Framework**: python-telegram-bot 20.0+
- **ML Framework**: TensorFlow 2.12+
- **Model Architecture**: MobileNetV2 with custom classification head
- **Image Processing**: PIL (Pillow)
- **Language**: Python 3.9+

## Future Enhancements

- Treatment recommendations for each disease
- Multi-language support (English + Khmer)
- User history and analytics
- Batch image processing
- Integration with agricultural extension services

## License

This project is created for educational and agricultural support purposes.

## Support

For issues or questions, check the logs in `logs/bot.log` or review the troubleshooting section above.

---

Made with ❤️ for Cambodian farmers 🌾
