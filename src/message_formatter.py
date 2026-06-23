"""Message formatter for multi-language support."""
from src.models import PredictionResult
from src.constants import DISEASE_NAMES_KM, DISEASE_NAMES_EN


class MessageFormatter:
    """Formats bot messages in multiple languages."""
    
    # Disease information in Khmer
    DISEASE_INFO_KM = {
        'bacterial_leaf_blight': {
            'description': 'ជាប្រភេទជម្ងឺ ដែលរីករាលដាលខ្លាំង និងធ្វើការបំផ្លាញយ៉ាងខ្លាំងក្លាមកលើដំណាំស្រូវ។',
            'symptoms': []
        },
        'brown_spot': {
            'description': 'ជម្ងឺអុតត្នោត នេះមានការរីករាលដាលយ៉ាងខ្លាំងលើផលិតកម្មដំណាំស្រូវ។ ការរីករាលដាលនេះ យើងសង្កេតឃើញមាននៅលើ ស្លឹក គែមនៃស្លឹក និង គ្រាប់ស្រូវ។',
            'symptoms': []
        },
        'healthy': {
            'description': 'ស្លឹកស្រូវរបស់អ្នកមានសុខភាពល្អ! មិនមានសញ្ញាជំងឺទេ។',
            'symptoms': []
        },
        'Not rice leaf': {
            'description': 'នេះមិនមែនជាស្លឹកស្រូវទេ។ សូមផ្ញើរូបភាពស្លឹកស្រូវដើម្បីវិភាគជំងឺ។',
            'symptoms': []
        },
        'rice_blast': {
            'description': 'ជម្ងឺនេះមានការរីករាលដាលខ្លាំងជាងគេនៅលើដំណាំស្រូវ។ ជាពិសេសវាអាចកើត និងរីករាលដាល នៅគ្រប់សរីរាង្គរបស់ស្រូវ (ដើម ស្លឹក កួរស្រូវគ្រាប់ស្រូវ)។',
            'symptoms': []
        },
        'tungro_disease': {
            'description': 'ជម្ងឺនេះអាចត្រូវបានចម្លងដោយសត្វល្អិតទៅរុក្ខជាតិ។',
            'symptoms': []
        }
    }
    
    # Disease information in English
    DISEASE_INFO_EN = {
        'bacterial_leaf_blight': {
            'description': 'This is a type of disease that spreads rapidly and causes severe damage to rice crops.',
            'symptoms': []
        },
        'brown_spot': {
            'description': 'Brown Spot disease spreads extensively on rice crop production. This spread is observed on leaves, leaf edges, and rice grains.',
            'symptoms': []
        },
        'healthy': {
            'description': 'Your rice leaves are healthy! No signs of disease.',
            'symptoms': []
        },
        'Not rice leaf': {
            'description': 'This is not a rice leaf. Please send a rice leaf photo to analyze diseases.',
            'symptoms': []
        },
        'rice_blast': {
            'description': 'This disease spreads more extensively than others on rice crops. It can occur and spread to all parts of the rice plant (stem, leaves, panicles, and grains).',
            'symptoms': []
        },
        'tungro_disease': {
            'description': 'This disease can be transmitted by insects to plants.',
            'symptoms': []
        }
    }
    
    @staticmethod
    def format_welcome_message(lang='en') -> str:
        """Format welcome message in selected language."""
        if lang == 'km':
            return (
                "👋 សូមស្វាគមន៍មកកាន់បតវិភាគជំងឺលើស្លឹកស្រូវ! 🌾\n\n"
                "ខ្ញុំអាចជួយអ្នកវិភាគទៅលើជំងឺដែលកើតលើស្លឹកស្រូវ។\n\n"
                "📸 របៀបប្រើប្រាស់:\n"
                "១. ថតរូបស្លឹកស្រូវរបស់អ្នក\n"
                "២. ផ្ញើរូបភាពមកខ្ញុំ\n"
                "៣. រង់ចាំលទ្ធផលវិភាគ\n\n"
                "ខ្ញុំនឹងប្រាប់អ្នកថាតើស្រូវរបស់អ្នកមានជំងឺអ្វីនឹងមានសុខភាពល្អរឺអត់។\n\n"
                "⚠️ បញ្ជាក់: សូមផ្ញើរូបភាពដែលច្បាស់ហើយមានស្លឹកស្រូវតែមួយសន្លឹកដើម្បីអោយការវិភាគកាន់តែច្បាស់លាស់។\n\n"
                "🌐 ប្តូរភាសា: ចុចប៊ូតុងខាងក្រោម"
            )
        else:  # English
            return (
                "👋 Welcome to Rice Leaf Disease Detection Bot! 🌾\n\n"
                "I can help you analyze diseases that occur on rice leaves.\n\n"
                "📸 How to use:\n"
                "1. Take a photo of your rice leaf\n"
                "2. Send the photo to me\n"
                "3. Wait for the analysis result\n\n"
                "I will tell you if your rice has a disease or is healthy.\n\n"
                "⚠️ Note: Please send a clear image with only one rice leaf for more accurate analysis.\n\n"
                "🌐 Change language: Click button below"
            )
    
    @staticmethod
    def format_help_message(lang='en') -> str:
        """Format help message in selected language."""
        if lang == 'km':
            return (
                "ℹ️ ជំនួយ\n\n"
                "ប៊ូតនេះអាចកំណត់ជំងឺស្រូវទាំង៥ប្រភេទ:\n"
                "• ជំងឺបាក់តេរីស្រពោនស្លឹក\n"
                "• ជំងឺអុតត្នោត\n"
                "• ជំងឺខ្នារអំបោះត្នោត\n"
                "• ជំងឺទង់គ្រោ\n"
                "• គ្មានជំងឺ\n\n"
                "គ្រាន់តែផ្ញើរូបភាពស្លឹកស្រូវមកខ្ញុំ!\n\n"
                "🌐 ប្តូរភាសា: ចុចប៊ូតុងខាងក្រោម"
            )
        else:  # English
            return (
                "ℹ️ Help\n\n"
                "This bot can detect 5 types of rice conditions:\n"
                "• Bacterial Leaf Blight\n"
                "• Brown Spot\n"
                "• Rice Blast\n"
                "• Tungro Disease\n"
                "• Healthy\n\n"
                "Just send me a rice leaf photo!\n\n"
                "🌐 Change language: Click button below"
            )
    
    @staticmethod
    def format_prediction_result(result: PredictionResult, lang='en') -> str:
        """Format prediction result in selected language."""
        confidence_percent = result.confidence * 100
        
        # Determine confidence level text
        if confidence_percent < 50:
            confidence_level_en = "Low Confidence"
            confidence_level_km = "ទាប"
        elif confidence_percent < 80:
            confidence_level_en = "Medium Confidence"
            confidence_level_km = "មធ្យម"
        else:
            confidence_level_en = "High Confidence"
            confidence_level_km = "ខ្ពស់"
        
        if lang == 'km':
            disease_name = DISEASE_NAMES_KM.get(result.disease_name, result.disease_name)
            message = f"🔍 លទ្ធផលវិភាគ:\n\n"
            message += f"📊 ជំងឺ: {disease_name}\n"
            message += f"✅ ភាពជឿជាក់: {confidence_level_km}\n\n"
            
            disease_info = MessageFormatter.DISEASE_INFO_KM.get(result.disease_name, {})
            description = disease_info.get('description', '')
            
            if description:
                message += f"📝 ព័ត៌មាន:\n{description}\n"
        else:  # English
            disease_name = DISEASE_NAMES_EN.get(result.disease_name, result.disease_name)
            message = f"🔍 Analysis Result:\n\n"
            message += f"📊 Disease: {disease_name}\n"
            message += f"✅ Confidence: {confidence_level_en}\n\n"
            
            disease_info = MessageFormatter.DISEASE_INFO_EN.get(result.disease_name, {})
            description = disease_info.get('description', '')
            
            if description:
                message += f"📝 Information:\n{description}\n"
        
        return message
    
    @staticmethod
    def format_error_message(error_type: str, lang='en') -> str:
        """Format error message in selected language."""
        if lang == 'km':
            error_messages = {
                'invalid_image': (
                    "❌ មិនអាចដំណើរការរូបភាពបានទេ។\n\n"
                    "សូមផ្ញើរូបភាពស្លឹកស្រូវដែលច្បាស់លាស់។"
                ),
                'processing_failed': (
                    "❌ មានបញ្ហាក្នុងការវិភាគរូបភាព។\n\n"
                    "សូមព្យាយាមម្តងទៀត ឬផ្ញើរូបភាពផ្សេង។"
                ),
                'generic_error': (
                    "❌ មានកំហុសកើតឡើង។\n\n"
                    "សូមព្យាយាមម្តងទៀតក្រោយពេលបន្តិច។"
                ),
                'no_image': (
                    "❌ សូមផ្ញើរូបភាពស្លឹកស្រូវ។\n\n"
                    "ខ្ញុំត្រូវការរូបភាពដើម្បីវិភាគជំងឺ។"
                )
            }
        else:  # English
            error_messages = {
                'invalid_image': (
                    "❌ Cannot process the image.\n\n"
                    "Please send a clear rice leaf photo."
                ),
                'processing_failed': (
                    "❌ Problem analyzing the image.\n\n"
                    "Please try again or send a different photo."
                ),
                'generic_error': (
                    "❌ An error occurred.\n\n"
                    "Please try again later."
                ),
                'no_image': (
                    "❌ Please send a rice leaf photo.\n\n"
                    "I need an image to analyze the disease."
                )
            }
        
        return error_messages.get(error_type, error_messages['generic_error'])
    
    @staticmethod
    def format_processing_message(lang='en') -> str:
        """Format processing acknowledgment message in selected language."""
        if lang == 'km':
            return "⏳ កំពុងវិភាគរូបភាព... សូមរង់ចាំបន្តិច។"
        else:
            return "⏳ Analyzing image... Please wait."
    
    @staticmethod
    def format_fertilizer_recommendation(disease_name: str, lang='en') -> str:
        """Format fertilizer recommendation for the disease with specific purchase links."""
        disease_display_name = DISEASE_NAMES_KM.get(disease_name, disease_name) if lang == 'km' else DISEASE_NAMES_EN.get(disease_name, disease_name)
        
        # Disease-specific fertilizer recommendations
        fertilizer_specs = {
            'bacterial_leaf_blight': {
                'km': {
                    'fertilizers': '• ជី NPK 15-15-15 (ជីសមាមាត្រ)\n• ជីប៉ូតាស្យូម (K) ខ្ពស់ NPK 13-13-21\n• ជីផូស្វាត (P) DAP 18-46-0\n• ជីសរីរាង្គ (ជីគោ ជីមាន់)',
                    'search_term': 'ជីស្រូវ NPK 15-15-15',
                    'note': 'សម្រាប់ជំងឺបាក់តេរី ត្រូវការជីប៉ូតាស្យូមខ្ពស់ដើម្បីបង្កើនភាពធន់'
                },
                'en': {
                    'fertilizers': '• NPK 15-15-15 (Balanced fertilizer)\n• High Potassium (K) NPK 13-13-21\n• Phosphate (P) DAP 18-46-0\n• Organic fertilizer (cow/chicken manure)',
                    'search_term': 'NPK 15-15-15 rice fertilizer',
                    'note': 'For bacterial disease, high potassium is needed to boost resistance'
                }
            },
            'brown_spot': {
                'km': {
                    'fertilizers': '• ជី NPK 16-20-0 (ផូស្វាតខ្ពស់)\n• ជីយូរ៉េ (Urea) 46-0-0\n• ជីប៉ូតាស្យូម (K) MOP 0-0-60\n• ជីសរីរាង្គ',
                    'search_term': 'ជីស្រូវ NPK 16-20-0',
                    'note': 'សម្រាប់ជំងឺអុតត្នោត ត្រូវការជីផូស្វាតនិងអាហ្សិតសមស្រប'
                },
                'en': {
                    'fertilizers': '• NPK 16-20-0 (High Phosphate)\n• Urea 46-0-0\n• Potassium (K) MOP 0-0-60\n• Organic fertilizer',
                    'search_term': 'NPK 16-20-0 rice fertilizer',
                    'note': 'For brown spot, balanced phosphate and nitrogen are needed'
                }
            },
            'rice_blast': {
                'km': {
                    'fertilizers': '• ជី NPK 12-24-12 (ផូស្វាតខ្ពស់)\n• ជីប៉ូតាស្យូម (K) NPK 13-13-21\n• ជីផូស្វាត TSP 0-46-0\n• ជីសរីរាង្គ',
                    'search_term': 'ជីស្រូវ NPK 12-24-12',
                    'note': 'សម្រាប់ជំងឺខ្នារអំបោះត្នោត កាត់បន្ថយអាហ្សិត បង្កើនផូស្វាត'
                },
                'en': {
                    'fertilizers': '• NPK 12-24-12 (High Phosphate)\n• Potassium (K) NPK 13-13-21\n• Phosphate TSP 0-46-0\n• Organic fertilizer',
                    'search_term': 'NPK 12-24-12 rice fertilizer',
                    'note': 'For rice blast, reduce nitrogen and increase phosphate'
                }
            },
            'tungro_disease': {
                'km': {
                    'fertilizers': '• ជី NPK 15-15-15 (ជីសមាមាត្រ)\n• ជីប៉ូតាស្យូម (K) ខ្ពស់ NPK 13-13-21\n• ជីសរីរាង្គ (ជីមាន់ ជីគោ)\n• ជីមីក្រូអេឡេម៉ង់ (Zinc, Boron)',
                    'search_term': 'ជីស្រូវ NPK 15-15-15',
                    'note': 'សម្រាប់ជំងឺទង់គ្រោ ត្រូវការជីសមាមាត្រនិងមីក្រូអេឡេម៉ង់'
                },
                'en': {
                    'fertilizers': '• NPK 15-15-15 (Balanced fertilizer)\n• High Potassium (K) NPK 13-13-21\n• Organic fertilizer (chicken/cow manure)\n• Micronutrients (Zinc, Boron)',
                    'search_term': 'NPK 15-15-15 rice fertilizer',
                    'note': 'For tungro virus, balanced fertilizer and micronutrients are needed'
                }
            },
            'healthy': {
                'km': {
                    'fertilizers': '• ជី NPK 16-16-8 (ថែរក្សា)\n• ជីយូរ៉េ (Urea) 46-0-0\n• ជីសរីរាង្គ',
                    'search_term': 'ជីស្រូវ NPK 16-16-8',
                    'note': 'សម្រាប់ស្រូវមានសុខភាពល្អ ប្រើជីថែរក្សាធម្មតា'
                },
                'en': {
                    'fertilizers': '• NPK 16-16-8 (Maintenance)\n• Urea 46-0-0\n• Organic fertilizer',
                    'search_term': 'NPK 16-16-8 rice fertilizer',
                    'note': 'For healthy rice, use regular maintenance fertilizer'
                }
            },
            'Not rice leaf': {
                'km': {
                    'fertilizers': 'មិនអាចផ្តល់ការណែនាំបានទេ - នេះមិនមែនជាស្លឹកស្រូវ',
                    'search_term': '',
                    'note': 'សូមផ្ញើរូបភាពស្លឹកស្រូវដើម្បីទទួលបានការណែនាំអំពីជី'
                },
                'en': {
                    'fertilizers': 'Cannot provide recommendation - this is not a rice leaf',
                    'search_term': '',
                    'note': 'Please send a rice leaf photo to get fertilizer recommendations'
                }
            }
        }
        
        # Get disease-specific info
        disease_info = fertilizer_specs.get(disease_name, fertilizer_specs['healthy'])
        lang_info = disease_info.get(lang, disease_info['en'])
        
        if lang == 'km':
            header = f"<b>🧪 ជីដែលត្រូវប្រើ</b>\n<b>{disease_display_name}</b>\n\n"
            
            content = f"<b>📋 ណែនាំប្រភេទជី:</b>\n\n{lang_info['fertilizers']}\n\n"
            content += f"<b>💡 ចំណាំ:</b>\n{lang_info['note']}\n\n"
            content += "<b>⚠️ សំខាន់:</b>\nសូមប្រើជីតាមការណែនាំរបស់\nអ្នកជំនាញកសិកម្ម"
            
        else:  # English
            header = f"🧪 Fertilizer Recommendation - {disease_display_name}\n\n"
            
            content = f"📋 Recommended Fertilizers:\n{lang_info['fertilizers']}\n\n"
            content += f"💡 Note: {lang_info['note']}\n\n"
            content += "⚠️ Please follow recommendations from agricultural experts"
        
        return header + content
    
    @staticmethod
    def format_disease_all_info(disease_name: str, lang='en') -> str:
        """Format ALL disease information combined (symptoms, causes, prevention, fertilizer)."""
        disease_display_name = DISEASE_NAMES_KM.get(disease_name, disease_name) if lang == 'km' else DISEASE_NAMES_EN.get(disease_name, disease_name)
        
        # Get all sections including fertilizer
        symptoms = MessageFormatter.format_disease_detail(disease_name, 'symptoms', lang)
        causes = MessageFormatter.format_disease_detail(disease_name, 'causes', lang)
        prevention = MessageFormatter.format_disease_detail(disease_name, 'prevention', lang)
        fertilizer = MessageFormatter.format_fertilizer_recommendation(disease_name, lang)
        
        # Combine them cleanly without separators
        combined = f"{symptoms}\n\n{causes}\n\n{prevention}\n\n{fertilizer}"
        return combined
    
    @staticmethod
    def format_disease_detail(disease_name: str, info_type: str, lang='en') -> str:
        """Format detailed disease information based on type."""
        disease_display_name = DISEASE_NAMES_KM.get(disease_name, disease_name) if lang == 'km' else DISEASE_NAMES_EN.get(disease_name, disease_name)
        
        # Bacterial Leaf Blight detailed information
        if disease_name == 'bacterial_leaf_blight':
            if lang == 'km':
                if info_type == 'symptoms':
                    header = f"<b>🐛 រោគសញ្ញា</b>\n<b>{disease_display_name}</b>\n\n"
                    content = (
                        "✓ សញ្ញាលេចឡើងជាស្នាមបន្ទះវែងៗ\n"
                        "   ពណ៌ស ឬលឿង នៅលើគែមស្លឹក\n\n"
                        "✓ រីករាលដាលលើស្លឹកទាំងមូល\n"
                        "   ពីលើចុះក្រោម\n\n"
                        "✓ ពេលរាលដាលខ្លាំង ប្រែពណ៌ទៅជា\n"
                        "   ប្រផេះ រួចក្លាយជាពណ៌ស ស្ងួតងាប់\n\n"
                        "✓ ពេលព្រឹកមានទឹកសន្សើម ឃើញមាន\n"
                        "   សំបុកបាក់តេរីត្រង់កន្លែងកើតជំងឺ"
                    )
                elif info_type == 'causes':
                    header = f"<b>🔬 ភ្នាក់ងារបង្កជំងឺ</b>\n<b>{disease_display_name}</b>\n\n"
                    content = (
                        "✓ បង្កដោយបាក់តេរី\n\n"
                        "✓ ជ្រៀតចូលតាមរន្ធស្គូម៉ាត\n"
                        "   ស្នាមរបួស និងតាមឬស\n\n"
                        "✓ ឆ្លងតាមទឹកភ្លៀង\n"
                        "   ឬការបញ្ចូលទឹក\n\n"
                        "✓ អាកាសធាតុក្តៅហើយសើម\n"
                        "   (22-31 អង្សាសេ)\n\n"
                        "✓ ប្រភពចំលង៖\n"
                        "   - គល់ជញ្ជាំង\n"
                        "   - គ្រាប់កើតជំងឺ\n"
                        "   - ទឹកដែលមានមេរោគ"
                    )
                elif info_type == 'prevention':
                    header = f"<b>🛡️ វិធានការទប់ស្កាត់</b>\n<b>{disease_display_name}</b>\n\n"
                    content = (
                        "✓ ជៀសវាងការយកគ្រាប់ដែលមាន\n"
                        "   ជំងឺធ្វើពូជ\n\n"
                        "✓ បំផ្លាញគល់ជញ្ជាំងដែលកើតជំងឺ\n\n"
                        "✓ ជៀសវាងការបោះបង់កាកសំណល់រុក្ខជាតិដែលកើតជំងឺក្នុងប្រភពទឹកសំរាប់ស្រោចស្រព"
                    )
                else:
                    return "ព័ត៌មានមិនមាន។"
            else:  # English
                if info_type == 'symptoms':
                    header = f"<b>🐛 Symptoms - {disease_display_name}</b>\n\n"
                    content = (
                        "• Symptoms appear as long streaks, white or yellow, resembling water-soaked spots on leaf edges and tips\n\n"
                        "• Spreads across entire leaves from top to bottom\n\n"
                        "• When severely spread, turns grayish then white, dries and dies\n\n"
                        "• In the morning with dew, bacterial ooze can be seen at infection sites"
                    )
                elif info_type == 'causes':
                    header = f"<b>🔬 Causes - {disease_display_name}</b>\n\n"
                    content = (
                        "• Caused by the bacterium Xanthomonas campestris pv.oryzae\n\n"
                        "• Bacteria enter through stomata, wounds, and roots, growing inside the plant\n\n"
                        "• Spreads through rain or irrigation water\n\n"
                        "• Hot and humid weather (22-31°C) is suitable for spread\n\n"
                        "• Sources of infection: stubble, infected seeds, and water containing pathogens"
                    )
                elif info_type == 'prevention':
                    header = f"<b>🛡️ Prevention & Control - {disease_display_name}</b>\n\n"
                    content = (
                        "• Avoid using infected seeds for planting\n\n"
                        "• Destroy infected stubble\n\n"
                        "• Avoid dumping infected plant residues in irrigation water sources"
                    )
                else:
                    return "Information not available."
        
        # Rice Blast detailed information
        elif disease_name == 'rice_blast':
            if lang == 'km':
                if info_type == 'symptoms':
                    header = f"<b>🐛 រោគសញ្ញា</b>\n<b>{disease_display_name}</b>\n\n"
                    content = (
                        "✓ លើស្លឹក មានស្នាមចំណុចរាងពងក្រពើ\n"
                        "   ពណ៌ត្នោតប្រផេះ សណ្ឋានដូចភ្នែកមនុស្ស\n\n"
                        "✓ ចំណុចទាំងនោះអាចរីកលូតវែង\n"
                        "   រលាយចូលគ្នា\n\n"
                        "✓ បើរាលដាលដល់ស្រទាប់ស្លឹក\n"
                        "   អាចបណ្តាលអោយស្លឹកងាប់\n\n"
                        "✓ លើដើម និងកួរមានចំណុចខ្មៅ\n"
                        "   រីករាលដាលលឿន រលួយ បាក់ងាប់\n\n"
                        "✓ កួរស្រូវអាចមានពណ៌ស គ្មានដាក់គ្រាប់"
                    )
                elif info_type == 'causes':
                    header = f"<b>🔬 ភ្នាក់ងារបង្កជំងឺ</b>\n<b>{disease_display_name}</b>\n\n"
                    content = (
                        "✓ បង្កដោយផ្សិត\n\n"
                        "✓ ប្រភពចំលង៖\n"
                        "   - គ្រាប់ពូជ\n"
                        "   - កាកសំណល់រុក្ខជាតិ\n"
                        "   - ស្មៅអំបូរក្រាមីណេ"
                    )
                elif info_type == 'prevention':
                    header = f"<b>🛡️ វិធានការទប់ស្កាត់</b>\n<b>{disease_display_name}</b>\n\n"
                    content = (
                        "✓ ដាំពូជដែលធន់នឹងជំងឺ\n\n"
                        "✓ គួរបាចជីអាហ្សិតជាមួយជីផូស្វាត\n\n"
                        "✓ ភ្ជួរលប់គល់ជញ្ជាំងក្រោយពេលប្រមូលផល\n"
                        "   សំអាតស្មៅក្នុងស្រែ\n\n"
                        "✓ អាចប្រើថ្នាំសំលាប់ផ្សិត\n"
                        "   ក្នុងករណីធ្ងន់ធ្ងរ"
                    )
                else:
                    return "ព័ត៌មានមិនមាន។"
            else:  # English
                if info_type == 'symptoms':
                    header = f"<b>🐛 Symptoms - {disease_display_name}</b>\n\n"
                    content = (
                        "• On leaves, there are oval-shaped spots with grayish-brown color, gray center and brown edges with pointed ends on both sides resembling a human eye\n\n"
                        "• These spots can expand and merge together\n\n"
                        "• If spread to the leaf layer, it can cause leaf death; in severe cases, rice does not produce panicles\n\n"
                        "• On stems and panicles, there are small black spots in ring shapes that spread quickly, rot, break and die\n\n"
                        "• Rice panicles may turn white without grains; black spots can appear on grains and husks"
                    )
                elif info_type == 'causes':
                    header = f"<b>🔬 Causes - {disease_display_name}</b>\n\n"
                    content = (
                        "• Caused by the fungus Pyricularia oryzae\n\n"
                        "• Source of infection: through seeds, plant residues, and Gramineae weeds"
                    )
                elif info_type == 'prevention':
                    header = f"<b>🛡️ Prevention & Control - {disease_display_name}</b>\n\n"
                    content = (
                        "• Plant resistant varieties\n\n"
                        "• Apply nitrogen fertilizer with phosphate\n\n"
                        "• Burn stubble after harvest, clean weeds in fields, on bunds and in canals\n\n"
                        "• Fungicides can be used in severe cases; spray before rice flowering"
                    )
                else:
                    return "Information not available."
        
        # Tungro Disease detailed information
        elif disease_name == 'tungro_disease':
            if lang == 'km':
                if info_type == 'symptoms':
                    header = f"<b>🐛 រោគសញ្ញា - {disease_display_name}</b>\n\n"
                    content = (
                        "✓ ស្លឹកពណ៌លឿង ឬលឿងទឹកក្រូច ចាប់ផ្តើមពីចុងស្លឹក\n\n"
                        "✓ ដើមតូច មិនលូតលាស់ល្អ\n\n"
                        "✓ ចំនួនពន្លកតិច\n\n"
                        "✓ កួរតូច គ្រាប់តិច ឬគ្មានគ្រាប់\n\n"
                        "✓ ស្លឹកមានពណ៌លឿងឆ្អិតៗ"
                    )
                elif info_type == 'causes':
                    header = f"<b>🔬 ភ្នាក់ងារបង្កនៃជំងឺ - {disease_display_name}</b>\n\n"
                    content = (
                        "✓ បង្កដោយវីរុសទង់គ្រោ (Tungro virus)\n\n"
                        "✓ ចម្លងដោយសត្វល្អិតឈ្មោះ កណ្តៀរស្រូវពណ៌បៃតង (Green leafhopper)\n\n"
                        "✓ រីករាលដាលលឿននៅតំបន់មានសត្វល្អិតច្រើន\n\n"
                        "✓ ប្រភពចំលង៖ ស្រូវដែលកើតជំងឺ និងសត្វល្អិតដែលមានវីរុស"
                    )
                elif info_type == 'prevention':
                    header = f"<b>🛡️ វិធានការទប់ស្កាត់ និង កម្ចាត់ - {disease_display_name}</b>\n\n"
                    content = (
                        "✓ ដាំពូជដែលធន់នឹងជំងឺ\n\n"
                        "✓ បំផ្លាញស្រូវដែលកើតជំងឺ\n\n"
                        "✓ គ្រប់គ្រងសត្វល្អិតកណ្តៀរស្រូវ\n\n"
                        "✓ ដាំស្រូវក្នុងពេលដំណាលគ្នា\n\n"
                        "✓ ប្រើថ្នាំសំលាប់សត្វល្អិតតាមការណែនាំ"
                    )
                else:
                    return "ព័ត៌មានមិនមាន។"
            else:  # English
                if info_type == 'symptoms':
                    header = f"<b>🐛 Symptoms - {disease_display_name}</b>\n\n"
                    content = (
                        "• Yellow or orange-yellow leaves starting from leaf tips\n\n"
                        "• Stunted growth\n\n"
                        "• Reduced number of tillers\n\n"
                        "• Small panicles with few or no grains\n\n"
                        "• Mottled yellow leaves"
                    )
                elif info_type == 'causes':
                    header = f"<b>🔬 Causes - {disease_display_name}</b>\n\n"
                    content = (
                        "• Caused by Tungro virus\n\n"
                        "• Transmitted by green leafhopper insects\n\n"
                        "• Spreads rapidly in areas with high insect populations\n\n"
                        "• Sources of infection: infected rice plants and virus-carrying insects"
                    )
                elif info_type == 'prevention':
                    header = f"<b>🛡️ Prevention & Control - {disease_display_name}</b>\n\n"
                    content = (
                        "• Plant resistant varieties\n\n"
                        "• Destroy infected rice plants\n\n"
                        "• Control green leafhopper populations\n\n"
                        "• Plant rice synchronously\n\n"
                        "• Use insecticides as recommended"
                    )
                else:
                    return "Information not available."
        
        # Not Rice Leaf information
        elif disease_name == 'Not rice leaf':
            if lang == 'km':
                if info_type == 'symptoms':
                    header = f"<b>⚠️ {disease_display_name}</b>\n\n"
                    content = "នេះមិនមែនជាស្លឹកស្រូវទេ។ សូមផ្ញើរូបភាពស្លឹកស្រូវដើម្បីវិភាគជំងឺ។"
                elif info_type == 'causes':
                    header = f"<b>⚠️ {disease_display_name}</b>\n\n"
                    content = "រូបភាពនេះមិនមែនជាស្លឹកស្រូវទេ។"
                elif info_type == 'prevention':
                    header = f"<b>⚠️ {disease_display_name}</b>\n\n"
                    content = "សូមផ្ញើរូបភាពស្លឹកស្រូវច្បាស់លាស់ដើម្បីទទួលបានការវិភាគ។"
                else:
                    return "ព័ត៌មានមិនមាន។"
            else:  # English
                if info_type == 'symptoms':
                    header = f"<b>⚠️ {disease_display_name}</b>\n\n"
                    content = "This is not a rice leaf. Please send a rice leaf photo to analyze diseases."
                elif info_type == 'causes':
                    header = f"<b>⚠️ {disease_display_name}</b>\n\n"
                    content = "This image is not a rice leaf."
                elif info_type == 'prevention':
                    header = f"<b>⚠️ {disease_display_name}</b>\n\n"
                    content = "Please send a clear rice leaf photo to get analysis."
                else:
                    return "Information not available."
        
        # Brown Spot detailed information
        elif disease_name == 'brown_spot':
            if lang == 'km':
                if info_type == 'symptoms':
                    header = f"<b>🐛 រោគសញ្ញា</b>\n<b>{disease_display_name}</b>\n\n"
                    content = (
                        "✓ កើតលើស្រទាប់ស្លឹក និងសំបកគ្រាប់\n\n"
                        "✓ មានស្នាមចំណុចពណ៌ត្នោត\n"
                        "   រាងមូល ឬរាងពងក្រពើ\n\n"
                        "✓ ចំណុចតូចៗពណ៌ត្នោត\n\n"
                        "✓ ស្នាមធំៗពណ៌ត្នោតចាស់នៅគែម\n"
                        "   ផ្នែកកណ្តាលលឿងភ្លាវ ស្រអាប់"
                    )
                elif info_type == 'causes':
                    header = f"<b>🔬 ភ្នាក់ងារបង្កជំងឺ</b>\n<b>{disease_display_name}</b>\n\n"
                    content = (
                        "✓ បង្កដោយផ្សិត\n\n"
                        "✓ ផ្សិតជ្រៀតចូលតាមរន្ធស្គូម៉ាត\n\n"
                        "✓ រាលដាលខ្លាំងពេលសីតុណ្ហភាព\n"
                        "   20-25 អង្សាសេ\n\n"
                        "✓ ដីស្ងួត ដីខ្វះជាតិអាហ្សិត\n"
                        "   អាចអោយស្រូវឆាប់ទទួលជំងឺ\n\n"
                        "✓ ប្រភពចំលង៖\n"
                        "   - គ្រាប់ពូជ\n"
                        "   - កាកសំណល់រុក្ខជាតិ\n"
                        "   - ស្មៅ"
                    )
                elif info_type == 'prevention':
                    header = f"<b>🛡️ វិធានការទប់ស្កាត់</b>\n<b>{disease_display_name}</b>\n\n"
                    content = (
                        "✓ ដាំពូជដែលធន់នឹងជំងឺ\n\n"
                        "✓ ធ្វើអនាម័យស្រែ\n"
                        "   បំបាត់ស្មៅ កាកសំណល់រុក្ខជាតិ\n\n"
                        "✓ ភ្ជួរលប់ ឬដុតគល់ជញ្ជាំង\n"
                        "   ក្រោយពេលមានកើតជំងឺរាតត្បាតខ្លាំង\n\n"
                        "✓ បញ្ចូលទឹកនៅពេលស្រូវដុះពន្លក\n\n"
                        "✓ សំអាតគ្រាប់ពូជដោយត្រាំទឹក\n"
                        "   24 ម៉ោង រួចកំដៅ 53-57 អង្សាសេ\n"
                        "   រយៈពេល 10 នាទី\n\n"
                        "✓ អាចប្រើថ្នាំសំលាប់ផ្សិត\n"
                        "   នៅដំណាក់កាលលូតលាស់"
                    )
                else:
                    return "ព័ត៌មានមិនមាន។"
            else:  # English
                if info_type == 'symptoms':
                    header = f"<b>🐛 Symptoms - {disease_display_name}</b>\n\n"
                    content = (
                        "• Occurs on leaf blades and grain husks\n\n"
                        "• On leaf blades, there are round or oval brown spots\n\n"
                        "• On leaves, spots are round or elongated resembling sesame seeds\n\n"
                        "• Small spots are brown, while larger spots have dark brown edges with pale yellow, dry, or grayish centers"
                    )
                elif info_type == 'causes':
                    header = f"<b>🔬 Causes - {disease_display_name}</b>\n\n"
                    content = (
                        "• Caused by the fungus Helminthosporium oryzae\n\n"
                        "• Infection spread: Fungus penetrates plants through epidermis and stomata of leaves\n\n"
                        "• Fungus spreads strongly at temperatures of 20-25°C and humidity above 90%\n\n"
                        "• Dry soil and nitrogen-deficient soil can make rice more susceptible to this disease\n\n"
                        "• Seeds, plant residues with mycelium, and weeds are important sources of disease transmission"
                    )
                elif info_type == 'prevention':
                    header = f"<b>🛡️ Prevention & Control - {disease_display_name}</b>\n\n"
                    content = (
                        "• Plant disease-resistant varieties\n\n"
                        "• Practice field sanitation to eliminate fungal hosts (weeds, plant residues)\n\n"
                        "• Burn or plow stubble after severe disease outbreaks\n\n"
                        "• Flood fields when rice is tillering\n\n"
                        "• Clean seeds by soaking them in water for 24 hours, then heat at 53-57°C for 10 minutes, then cool immediately\n\n"
                        "• Fungicides can be used during growth stages similar to blast disease"
                    )
                else:
                    return "Information not available."
        
        # Healthy rice detailed information
        elif disease_name == 'healthy':
            if lang == 'km':
                if info_type == 'symptoms':
                    header = f"<b>🌱 ស្លឹកស្រូវមានសុខភាពល្អ</b>\n<b>{disease_display_name}</b>\n\n"
                    content = (
                        "✓ ស្លឹកពណ៌បៃតងស្រស់\n\n"
                        "✓ គ្មានស្នាមប្រឡាក់ ឬចំណុចលើស្លឹក\n\n"
                        "✓ ស្លឹកមានរាងធម្មតា មិនកោង\n\n"
                        "✓ គ្មានការស្ងួតនៅគែម\n\n"
                        "✓ ពណ៌ស្លឹកស្មើគ្នាទូទាំង"
                    )
                elif info_type == 'causes':
                    header = f"<b>🌱 កត្តាធ្វើអោយមានសុខភាពល្អ</b>\n<b>{disease_display_name}</b>\n\n"
                    content = (
                        "✓ ការថែទាំល្អ\n\n"
                        "✓ ទឹកគ្រប់គ្រាន់\n\n"
                        "✓ ជីសមាមាត្រ\n\n"
                        "✓ គ្មានសត្វល្អិតបំផ្លាញ\n\n"
                        "✓ អាកាសធាតុអំណោយផល"
                    )
                elif info_type == 'prevention':
                    header = f"<b>🌱 ការថែរក្សាបន្ត</b>\n<b>{disease_display_name}</b>\n\n"
                    content = (
                        "✓ បន្តការថែទាំបច្ចុប្បន្ន\n\n"
                        "✓ ត្រួតពិនិត្យជាទៀងទាត់\n\n"
                        "✓ ការពារពីសត្វល្អិត\n\n"
                        "✓ ថែរក្សាប្រព័ន្ធស្រោចស្រព\n\n"
                        "✓ ប្រើជីតាមកាលកំណត់"
                    )
                else:
                    return "ព័ត៌មានមិនមាន។"
            else:  # English
                if info_type == 'symptoms':
                    header = f"<b>🌱 Healthy Rice Leaf Signs</b>\n<b>{disease_display_name}</b>\n\n"
                    content = (
                        "• Fresh green leaf color\n\n"
                        "• No spots or stains on leaves\n\n"
                        "• Normal leaf shape, not curled\n\n"
                        "• No drying at leaf edges\n\n"
                        "• Uniform leaf color throughout"
                    )
                elif info_type == 'causes':
                    header = f"<b>🌱 Factors for Good Health</b>\n<b>{disease_display_name}</b>\n\n"
                    content = (
                        "• Good care and management\n\n"
                        "• Adequate water supply\n\n"
                        "• Balanced fertilizer application\n\n"
                        "• No pest damage\n\n"
                        "• Favorable weather conditions"
                    )
                elif info_type == 'prevention':
                    header = f"<b>🌱 Maintaining Health</b>\n<b>{disease_display_name}</b>\n\n"
                    content = (
                        "• Continue current good practices\n\n"
                        "• Regular monitoring and inspection\n\n"
                        "• Protect from pests and diseases\n\n"
                        "• Maintain irrigation system\n\n"
                        "• Apply fertilizer according to schedule"
                    )
                else:
                    return "Information not available."
        
        else:
            # Placeholder for other diseases
            if lang == 'km':
                if info_type == 'symptoms':
                    header = f"<b>🐛 រោគសញ្ញា - {disease_display_name}</b>\n\n"
                    content = "ព័ត៌មានលម្អិតអំពីរោគសញ្ញានឹងត្រូវបានបន្ថែមឆាប់ៗនេះ"
                elif info_type == 'causes':
                    header = f"<b>🔬 ភ្នាក់ងារបង្កនៃជំងឺ - {disease_display_name}</b>\n\n"
                    content = "ព័ត៌មានលម្អិតអំពីភ្នាក់ងារបង្កនឹងត្រូវបានបន្ថែមឆាប់ៗនេះ"
                elif info_type == 'prevention':
                    header = f"<b>🛡️ វិធានការទប់ស្កាត់ និង កម្ចាត់ - {disease_display_name}</b>\n\n"
                    content = "ព័ត៌មានលម្អិតអំពីវិធានការទប់ស្កាត់នឹងត្រូវបានបន្ថែមឆាប់ៗនេះ"
                else:
                    return "ព័ត៌មានមិនមាន។"
            else:  # English
                if info_type == 'symptoms':
                    header = f"<b>🐛 Symptoms - {disease_display_name}</b>\n\n"
                    content = "Detailed symptom information will be added soon"
                elif info_type == 'causes':
                    header = f"<b>🔬 Causes - {disease_display_name}</b>\n\n"
                    content = "Detailed cause information will be added soon"
                elif info_type == 'prevention':
                    header = f"<b>🛡️ Prevention & Control - {disease_display_name}</b>\n\n"
                    content = "Detailed prevention information will be added soon"
                else:
                    return "Information not available."
        
        return header + content

    @staticmethod
    def format_treatment_and_fertilizer(disease_name: str, lang='en') -> str:
        """Format combined treatment (prevention & control) and fertilizer information."""
        disease_display_name = DISEASE_NAMES_KM.get(disease_name, disease_name) if lang == 'km' else DISEASE_NAMES_EN.get(disease_name, disease_name)
        
        # Get prevention/control information
        prevention_info = MessageFormatter.format_disease_detail(disease_name, 'prevention', lang)
        
        # Get fertilizer information
        fertilizer_info = MessageFormatter.format_fertilizer_recommendation(disease_name, lang)
        
        # Combine with a clean separator
        if lang == 'km':
            header = f"<b>💊 ការព្យាបាល</b>\n<b>{disease_display_name}</b>\n\n"
            separator = "\n\n"
        else:
            header = f"<b>💊 Treatment</b>\n<b>{disease_display_name}</b>\n\n"
            separator = "\n\n"
        
        # Extract content from prevention_info (remove its header)
        prevention_content = prevention_info.split('\n\n', 1)[1] if '\n\n' in prevention_info else prevention_info
        
        # Extract content from fertilizer_info (remove its header)
        fertilizer_content = fertilizer_info.split('\n\n', 1)[1] if '\n\n' in fertilizer_info else fertilizer_info
        
        # Combine everything
        combined = header + prevention_content + separator + fertilizer_content
        
        return combined
