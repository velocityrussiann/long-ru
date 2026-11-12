"""VELOCITY LONGFORM - 16:9 chapter lesson, brand and motion constants."""

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

OUTPUT_DIR = BASE_DIR / "output"
LESSONS_DIR = OUTPUT_DIR / "lessons"
HISTORY_DIR = OUTPUT_DIR / "history"
SCENE_DIR = BASE_DIR / "scene"

VIDEO_WIDTH = 1920
VIDEO_HEIGHT = 1080
FPS = 30

TARGET_CHAPTERS = 8
PHRASES_PER_CHAPTER = 7
TARGET_PHRASES = TARGET_CHAPTERS * PHRASES_PER_CHAPTER

# ---------------------------------------------------------------- brand

BRAND = "VELOCITY RUSSIAN"
BRAND_LOCKUP_TOP = "VELOCITY"
BRAND_LOCKUP_BOTTOM = "RUSSIAN"
HANDLE = "@velocityrussian"
MASCOT_NAME = "Velo"

# ==== LANGUAGE PACK START ====
LANGUAGE = {'code': 'ru',
 'name': 'Russian',
 'native_name': 'Русский',
 'history_key': 'russian',
 'english_voice': 'en-US-AvaNeural',
 'english_fallback_voice': 'en-US-GuyNeural',
 'native_voice': 'ru-RU-DmitryNeural',
 'native_fallback_voice': 'ru-RU-SvetlanaNeural',
 'native_engine': 'edge',
 'native_lang_code': 'ru',
 'english_rate': '-4%',
 'native_rate': '-10%',
 'english_pitch': '+0Hz',
 'native_pitch': '+0Hz',
 'native_label': 'РУССКИЙ',
 'translit_label': 'SAY IT LIKE',
 'flag': 'ru',
 'greeting': 'Привет!',
 'encouragement': 'Отлично!',
 'rtl': False,
 'char_tiles': False,
 'script_font': '',
 'glyphs': 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'}
# ==== LANGUAGE PACK END ====

# ==== CATEGORIES START ====
CATEGORIES = {'Motivation': 'Мотивация',
 'Love': 'Любовь',
 'Success': 'Успех',
 'Wisdom': 'Мудрость',
 'Happiness': 'Счастье',
 'Self Improvement': 'Самосовершенствование',
 'Gratitude': 'Благодарность',
 'Friendship': 'Дружба',
 'Hope': 'Надежда',
 'Creativity': 'Творчество',
 'Inner Peace': 'Внутренний покой',
 'Confidence': 'Уверенность',
 'Perseverance': 'Настойчивость',
 'Inspiration': 'Вдохновение',
 'Positive Life': 'Позитивная жизнь',
 'Courage': 'Смелость',
 'Kindness': 'Доброта',
 'Patience': 'Терпение',
 'Forgiveness': 'Прощение',
 'Strength': 'Сила',
 'Joy': 'Радость',
 'Balance': 'Баланс',
 'Growth': 'Рост',
 'Purpose': 'Цель',
 'Mindfulness': 'Осознанность',
 'Travel & Airport': 'Путешествия и аэропорт',
 'Ordering Food & Dining': 'Заказ еды и рестораны',
 'Shopping & Prices': 'Покупки и цены',
 'Asking for Directions': 'Как спросить дорогу',
 'Hotel & Accommodation': 'Отель и проживание',
 'Daily Routine': 'Повседневная жизнь',
 'Meeting People & Greetings': 'Знакомство и приветствия',
 'Emergency & Health': 'Чрезвычайные ситуации и здоровье',
 'Public Transportation': 'Общественный транспорт',
 'Work & Office': 'Работа и офис',
 'Weather & Small Talk': 'Погода и светская беседа',
 'Coffee Shop & Bakery': 'Кофейня и пекарня',
 'Family & Home': 'Семья и дом',
 'Hobbies & Free Time': 'Хобби и свободное время',
 'Dating & Romance': 'Знакомства и романтика',
 'Phone Calls & Messages': 'Телефонные звонки и сообщения',
 'Banking & Money': 'Банки и деньги',
 'Doctor & Pharmacy': 'Врач и аптека',
 'Sports & Fitness': 'Спорт и фитнес',
 'Celebrations & Parties': 'Праздники и вечеринки',
 'Feelings & Emotions': 'Чувства и эмоции',
 'Agreeing & Disagreeing': 'Согласие и несогласие',
 'Making Plans': 'Планирование',
 'Common Native Slang': 'Распространенный местный сленг',
 'Cultural Traditions': 'Культурные традиции'}
# ==== CATEGORIES END ====

CATEGORY_NAMES = list(CATEGORIES.keys())

AI_MODEL = os.getenv("AI_MODEL", "openai/gpt-5.4-nano")
AI_FALLBACK_MODEL = os.getenv("AI_FALLBACK_MODEL", "gemini-fast")
POLLINATIONS_API_KEY = os.getenv("POLLINATIONS_API_KEY", "")

# ---------------------------------------------------------------- timing (seconds)

INTRO_DURATION = 7.2
CHAPTER_INTRO_DURATION = 4.4
OUTRO_DURATION = 13.0

EN_CARD_IN = 0.70
GAP_EN_NATIVE = 0.60
NATIVE_CARD_LEAD = 0.40
GAP_BEFORE_REPEAT = 1.00
TAIL_HOLD = 1.30

# ---------------------------------------------------------------- palette

INK = "#30303A"
MUTED = "#8A8A8A"
CREAM = "#FFF8E7"
GREEN = "#58CC02"
GREEN_DARK = "#46A302"
GREEN_DEEP = "#3D8F00"
BLUE = "#1CB0F6"
PURPLE = "#7C5CFF"
ORANGE = "#FF7A00"
RED = "#FF4B4B"
YELLOW = "#F5A700"
TEAL = "#00A889"
PINK = "#E056A0"

# ==== HASHTAGS START ====
HASHTAGS = ['#learnrussian',
 '#russianlessons',
 '#russianforbeginners',
 '#languagelearning',
 '#russianvocabulary',
 '#velocityrussian',
 '#dailyrussian',
 '#russian',
 '#learnlanguages',
 '#speakrussian']
# ==== HASHTAGS END ====
