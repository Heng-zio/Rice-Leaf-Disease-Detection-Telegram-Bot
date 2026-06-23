"""Telegram bot handler for rice disease detection."""
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes

from src.prediction_service import PredictionService
from src.message_formatter import MessageFormatter
from src.exceptions import InvalidImageError, ModelError
from src.constants import DISEASE_NAMES_KM, DISEASE_NAMES_EN

logger = logging.getLogger(__name__)


class TelegramBotHandler:
    """Handles Telegram bot interactions."""
    
    def __init__(self, token: str, prediction_service: PredictionService):
        """
        Initialize bot handler.
        
        Args:
            token: Telegram bot token
            prediction_service: Service for disease prediction
        """
        self.token = token
        self.prediction_service = prediction_service
        self.app = None
        self.user_languages = {}  # Store user language preferences (user_id -> lang)
    
    async def handle_start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /start command."""
        try:
            user_id = update.effective_user.id
            
            # ALWAYS show language selection first when /start is pressed
            message = "🌾🌾🌾\n\nPlease select your language:\nសូមជ្រើសរើសភាសារបស់អ្នក:"
            
            # HORIZONTAL BUTTON LAYOUT - Both buttons on same row as requested
            keyboard = [
                [
                    InlineKeyboardButton("🇬🇧 English", callback_data='lang_en_start'),
                    InlineKeyboardButton("🇰🇭 ខ្មែរ", callback_data='lang_km_start')
                ]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            await update.message.reply_text(message, reply_markup=reply_markup)
            logger.info(f"Sent language selection to user {user_id}")
        except Exception as e:
            logger.error(f"Error in start command: {e}")
            lang = self.user_languages.get(update.effective_user.id, 'en')
            await update.message.reply_text(MessageFormatter.format_error_message('generic_error', lang))
    
    async def handle_help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /help command."""
        try:
            user_id = update.effective_user.id
            lang = self.user_languages.get(user_id, 'en')
            help_message = MessageFormatter.format_help_message(lang)
            
            # HORIZONTAL BUTTON LAYOUT - Both buttons on same row as requested
            keyboard = [
                [
                    InlineKeyboardButton("🇬🇧 English", callback_data='lang_en_start'),
                    InlineKeyboardButton("🇰🇭 ខ្មែរ", callback_data='lang_km_start')
                ]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            await update.message.reply_text(help_message, reply_markup=reply_markup)
            logger.info(f"Sent help message to user {user_id} in {lang}")
        except Exception as e:
            logger.error(f"Error in help command: {e}")
            lang = self.user_languages.get(update.effective_user.id, 'en')
            await update.message.reply_text(MessageFormatter.format_error_message('generic_error', lang))
    
    async def handle_english_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /english command to switch to English."""
        try:
            user_id = update.effective_user.id
            self.user_languages[user_id] = 'en'
            await update.message.reply_text(
                "🇬🇧 Language changed to English!\n\n"
                "Send /start to see the welcome message."
            )
            logger.info(f"User {user_id} switched to English")
        except Exception as e:
            logger.error(f"Error in english command: {e}")
    
    async def handle_khmer_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /khmer command to switch to Khmer."""
        try:
            user_id = update.effective_user.id
            self.user_languages[user_id] = 'km'
            await update.message.reply_text(
                "🇰🇭 ប្តូរភាសាជាខ្មែរ!\n\n"
                "ផ្ញើ /start ដើម្បីមើលសារស្វាគមន៍។"
            )
            logger.info(f"User {user_id} switched to Khmer")
        except Exception as e:
            logger.error(f"Error in khmer command: {e}")
    
    async def handle_language_button(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle language selection button clicks."""
        query = update.callback_query
        await query.answer()
        
        try:
            user_id = query.from_user.id
            
            # Check if this is first-time language selection
            is_first_time = query.data.endswith('_start')
            
            # Get selected language from callback data
            if query.data.startswith('lang_en'):
                self.user_languages[user_id] = 'en'
                lang = 'en'
                logger.info(f"User {user_id} selected English")
            elif query.data.startswith('lang_km'):
                self.user_languages[user_id] = 'km'
                lang = 'km'
                logger.info(f"User {user_id} selected Khmer")
            else:
                return
            
            # Always show welcome message in selected language with change language button
            welcome_message = MessageFormatter.format_welcome_message(lang)
            
            # Add change language button (VERTICAL LAYOUT)
            if lang == 'km':
                button_text = "🌐 ប្តូរភាសា"
            else:
                button_text = "🌐 Change Language"
            
            keyboard = [[InlineKeyboardButton(button_text, callback_data='back_to_language')]]
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            await query.edit_message_text(text=welcome_message, reply_markup=reply_markup)
            
        except Exception as e:
            logger.error(f"Error handling language button: {e}")
    
    async def handle_disease_info_button(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle disease information button clicks."""
        query = update.callback_query
        
        try:
            user_id = query.from_user.id
            lang = self.user_languages.get(user_id, 'en')
            
            # Parse callback data: info_<type>_<disease_name>
            parts = query.data.split('_', 2)
            if len(parts) < 3:
                await query.answer()
                return
            
            info_type = parts[1]  # symptoms, causes, prevention, or treatment
            disease_name = parts[2]
            
            # Get specific disease information section
            if info_type == 'treatment':
                # Combined treatment & fertilizer information
                info_message = MessageFormatter.format_treatment_and_fertilizer(disease_name, lang)
            else:
                info_message = MessageFormatter.format_disease_detail(disease_name, info_type, lang)
            
            # Create back button (VERTICAL LAYOUT)
            if lang == 'km':
                back_button_text = "🔙 ត្រឡប់ក្រោយ"
            else:
                back_button_text = "🔙 Back"
            
            keyboard = [[InlineKeyboardButton(back_button_text, callback_data=f'back_{disease_name}')]]
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            # Edit the same message and answer callback simultaneously for faster response
            await query.answer()
            await query.edit_message_text(text=info_message, reply_markup=reply_markup, parse_mode='HTML')
            
            logger.info(f"User {user_id} requested {info_type} for {disease_name}")
            
        except Exception as e:
            logger.error(f"Error handling disease info button: {e}")
    
    async def handle_back_button(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle back button to return to main disease info buttons or language selection."""
        query = update.callback_query
        
        try:
            user_id = query.from_user.id
            lang = self.user_languages.get(user_id, 'en')
            
            # Check if going back to language selection
            if query.data == 'back_to_language':
                # Show language selection again (PURE BILINGUAL MESSAGE)
                message = "🌾🌾🌾\n\nPlease select your language:\nសូមជ្រើសរើសភាសារបស់អ្នក:"
                
                # HORIZONTAL BUTTON LAYOUT - Both buttons on same row as requested
                keyboard = [
                    [
                        InlineKeyboardButton("🇬🇧 English", callback_data='lang_en_start'),
                        InlineKeyboardButton("🇰🇭 ខ្មែរ", callback_data='lang_km_start')
                    ]
                ]
                reply_markup = InlineKeyboardMarkup(keyboard)
                
                await query.answer()
                await query.edit_message_text(text=message, reply_markup=reply_markup)
                logger.info(f"User {user_id} went back to language selection")
                return
            
            # Parse callback data: back_<disease_name>
            parts = query.data.split('_', 1)
            if len(parts) != 2:
                await query.answer()
                return
            
            disease_name = parts[1]
            
            # Get the original prediction result from context
            result_message = context.user_data.get('last_result_message', '')
            
            # If we don't have the stored message, recreate it
            if not result_message:
                disease_display_name = DISEASE_NAMES_KM.get(disease_name, disease_name) if lang == 'km' else DISEASE_NAMES_EN.get(disease_name, disease_name)
                if lang == 'km':
                    result_message = f"🔍 លទ្ធផលវិភាគ:\n\n📊 ជំងឺ: {disease_display_name}"
                else:
                    result_message = f"🔍 Analysis Result:\n\n📊 Disease: {disease_display_name}"
            
            # Recreate the 3-button menu with the original result message (STRICT VERTICAL LAYOUT)
            if lang == 'km':
                keyboard = [
                    [InlineKeyboardButton("🐛 រោគសញ្ញា", callback_data=f'info_symptoms_{disease_name}')],
                    [InlineKeyboardButton("🔬 ភ្នាក់ងារបង្កជំងឺ", callback_data=f'info_causes_{disease_name}')],
                    [InlineKeyboardButton("💊 ការព្យាបាល", callback_data=f'info_treatment_{disease_name}')],
                    [InlineKeyboardButton("🔄 វិភាគម្តងទៀត", callback_data='analyze_again')]
                ]
            else:
                keyboard = [
                    [InlineKeyboardButton("🐛 Symptoms", callback_data=f'info_symptoms_{disease_name}')],
                    [InlineKeyboardButton("🔬 Causes", callback_data=f'info_causes_{disease_name}')],
                    [InlineKeyboardButton("💊 Treatment", callback_data=f'info_treatment_{disease_name}')],
                    [InlineKeyboardButton("🔄 Analyze Again", callback_data='analyze_again')]
                ]
            
            reply_markup = InlineKeyboardMarkup(keyboard)
            await query.answer()
            await query.edit_message_text(text=result_message, reply_markup=reply_markup)
            logger.info(f"User {user_id} went back to main buttons for {disease_name}")
            
        except Exception as e:
            logger.error(f"Error handling back button: {e}")
    
    async def handle_photo_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle photo messages."""
        user_id = update.effective_user.id
        lang = self.user_languages.get(user_id, 'en')
        
        try:
            # Send acknowledgment message
            processing_msg = await update.message.reply_text(
                MessageFormatter.format_processing_message(lang)
            )
            logger.info(f"Received photo from user {user_id}")
            
            # Get the largest photo
            photo = update.message.photo[-1]
            
            # Download photo
            photo_file = await photo.get_file()
            photo_bytes = await photo_file.download_as_bytearray()
            
            logger.info(f"Downloaded photo from user {user_id}, size: {len(photo_bytes)} bytes")
            
            # Predict disease
            result = self.prediction_service.predict(bytes(photo_bytes))
            
            logger.info(
                f"Prediction for user {user_id}: {result.disease_name} "
                f"(confidence: {result.confidence:.2f})"
            )
            
            # Format and send result
            result_message = MessageFormatter.format_prediction_result(result, lang)
            
            # Store the result message for later use
            context.user_data['last_result_message'] = result_message
            context.user_data['last_disease_name'] = result.disease_name
            
            # Add buttons based on result (STRICT VERTICAL LAYOUT - Each button on its own row)
            if result.disease_name == 'not_rice_leaf':
                # For not rice leaf, only show analyze again button
                if lang == 'km':
                    keyboard = [
                        [InlineKeyboardButton("🔄 វិភាគម្តងទៀត", callback_data='analyze_again')]
                    ]
                else:
                    keyboard = [
                        [InlineKeyboardButton("🔄 Analyze Again", callback_data='analyze_again')]
                    ]
                reply_markup = InlineKeyboardMarkup(keyboard)
                await update.message.reply_text(result_message, reply_markup=reply_markup)
            elif result.disease_name != 'healthy':
                # For diseases, show 3 information buttons vertically
                if lang == 'km':
                    keyboard = [
                        [InlineKeyboardButton("🐛 រោគសញ្ញា", callback_data=f'info_symptoms_{result.disease_name}')],
                        [InlineKeyboardButton("🔬 ភ្នាក់ងារបង្កជំងឺ", callback_data=f'info_causes_{result.disease_name}')],
                        [InlineKeyboardButton("💊 ការព្យាបាល", callback_data=f'info_treatment_{result.disease_name}')],
                        [InlineKeyboardButton("🔄 វិភាគម្តងទៀត", callback_data='analyze_again')]
                    ]
                else:
                    keyboard = [
                        [InlineKeyboardButton("🐛 Symptoms", callback_data=f'info_symptoms_{result.disease_name}')],
                        [InlineKeyboardButton("🔬 Causes", callback_data=f'info_causes_{result.disease_name}')],
                        [InlineKeyboardButton("💊 Treatment", callback_data=f'info_treatment_{result.disease_name}')],
                        [InlineKeyboardButton("🔄 Analyze Again", callback_data='analyze_again')]
                    ]
                reply_markup = InlineKeyboardMarkup(keyboard)
                await update.message.reply_text(result_message, reply_markup=reply_markup)
            else:
                # For healthy rice, only show "Analyze Again" button
                if lang == 'km':
                    keyboard = [
                        [InlineKeyboardButton("🔄 វិភាគម្តងទៀត", callback_data='analyze_again')]
                    ]
                else:
                    keyboard = [
                        [InlineKeyboardButton("🔄 Analyze Again", callback_data='analyze_again')]
                    ]
                reply_markup = InlineKeyboardMarkup(keyboard)
                await update.message.reply_text(result_message, reply_markup=reply_markup)
            
            # Delete processing message
            await processing_msg.delete()
            
        except InvalidImageError as e:
            logger.warning(f"Invalid image from user {user_id}: {e}")
            await update.message.reply_text(MessageFormatter.format_error_message('invalid_image', lang))
        except ModelError as e:
            logger.error(f"Model error for user {user_id}: {e}")
            await update.message.reply_text(MessageFormatter.format_error_message('processing_failed', lang))
        except Exception as e:
            logger.error(f"Unexpected error for user {user_id}: {e}", exc_info=True)
            await update.message.reply_text(MessageFormatter.format_error_message('generic_error', lang))
    
    async def handle_analyze_again_button(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle analyze again button click."""
        query = update.callback_query
        await query.answer()
        
        user_id = query.from_user.id
        lang = self.user_languages.get(user_id, 'en')
        
        try:
            if lang == 'km':
                message = "📸 សូមផ្ញើរូបភាពស្លឹកស្រូវថ្មីមួយទៀត ដើម្បីវិភាគជំងឺ។"
            else:
                message = "📸 Please send another rice leaf photo to analyze."
            
            await query.edit_message_text(text=message)
            logger.info(f"User {user_id} requested to analyze again")
            
        except Exception as e:
            logger.error(f"Error handling analyze again button: {e}")
    
    async def handle_non_photo_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle non-photo messages."""
        try:
            user_id = update.effective_user.id
            lang = self.user_languages.get(user_id, 'en')
            await update.message.reply_text(MessageFormatter.format_error_message('no_image', lang))
        except Exception as e:
            logger.error(f"Error handling non-photo message: {e}")
    
    def start_bot(self):
        """Start the bot."""
        logger.info("Starting Telegram bot...")
        
        # Create application
        self.app = Application.builder().token(self.token).build()
        
        # Add handlers
        self.app.add_handler(CommandHandler("start", self.handle_start_command))
        self.app.add_handler(CommandHandler("help", self.handle_help_command))
        self.app.add_handler(CommandHandler("english", self.handle_english_command))
        self.app.add_handler(CommandHandler("khmer", self.handle_khmer_command))
        self.app.add_handler(CallbackQueryHandler(self.handle_language_button, pattern='^lang_'))
        self.app.add_handler(CallbackQueryHandler(self.handle_back_button, pattern='^back_'))
        self.app.add_handler(CallbackQueryHandler(self.handle_analyze_again_button, pattern='^analyze_again'))
        self.app.add_handler(CallbackQueryHandler(self.handle_disease_info_button, pattern='^info_'))
        self.app.add_handler(MessageHandler(filters.PHOTO, self.handle_photo_message))
        self.app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_non_photo_message))
        
        # Start polling
        logger.info("Bot is running! Press Ctrl+C to stop.")
        self.app.run_polling(allowed_updates=Update.ALL_TYPES)
