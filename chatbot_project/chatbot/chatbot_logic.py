# chatbot/chatbot_logic.py
import json
import re
from django.conf import settings
import os

# Load translations from JSON file
with open(os.path.join(settings.BASE_DIR, 'chatbot/translations.json'), 'r', encoding='utf-8') as file:
    translations = json.load(file)

def detect_language(text):
    if re.search(r'[a-zA-Z]', text):
        return 'en'  # English
    elif re.search(r'[\u0900-\u097F]', text):
        return 'hi'  # Hindi (Devanagari script)
    elif re.search(r'[\u0A00-\u0A7F]', text):
        return 'pa'  # Punjabi (Gurmukhi script)
    else:
        return 'en'  # Default to English if undetermined

def normalize_text(text):
    return re.sub(r'\W+', ' ', text.lower()).strip()

def find_best_response(query, user_language):
    if user_language not in translations:
        user_language = 'en'
    
    localized_questions = list(translations[user_language].keys())
    localized_answers = translations[user_language]

    best_match = None
    max_overlap = 0
    best_answer = None

    query_words = set(normalize_text(query).split())
    
    for q in localized_questions:
        question_words = set(normalize_text(q).split())
        overlap = len(query_words & question_words)
        
        if overlap > max_overlap:
            max_overlap = overlap
            best_match = q
            best_answer = localized_answers[q]

    if not best_answer:
        best_answer = "I'm sorry, I couldn't understand that. Can you try rephrasing?"
    return best_answer
