import os
from pathlib import Path

# =====================================================
# Project Directories
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
MODEL_DIR = BASE_DIR / "models"
LOG_DIR = BASE_DIR / "logs"

# =====================================================
# Data Files
# =====================================================

INTENTS_FILE = DATA_DIR / "intents.csv"

# =====================================================
# Model Files
# =====================================================

MODEL_FILE = MODEL_DIR / "model.pkl"
TFIDF_FILE = MODEL_DIR / "tfidf.pkl"
LABEL_ENCODER_FILE = MODEL_DIR / "label_encoder.pkl"

# =====================================================
# Log Files
# =====================================================

CHAT_LOG_FILE = LOG_DIR / "chat_history.csv"

# =====================================================
# Machine Learning Configuration
# =====================================================

CONFIDENCE_THRESHOLD = 0.50

# =====================================================
# LLM Configuration
# =====================================================

LLM_MODEL = "llama-3.1-8b-instant"

# =====================================================
# API Configuration
# =====================================================

HOST = "0.0.0.0"
PORT = 5000
DEBUG = True

# =====================================================
# Groq Configuration
# =====================================================

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

LLM_MODEL = "llama-3.1-8b-instant"