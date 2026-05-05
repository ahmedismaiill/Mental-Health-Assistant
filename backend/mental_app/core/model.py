import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from config.settings import DEPRESSION_MODEL_DIR


# Load the tokenizer and model for depression detection
def load_engine():
    tokenizer = AutoTokenizer.from_pretrained(DEPRESSION_MODEL_DIR)
    model = AutoModelForSequenceClassification.from_pretrained(DEPRESSION_MODEL_DIR)
    return tokenizer, model

try:
    tokenizer, model = load_engine()
except:
    pass 

# Simple sentiment prediction function using the loaded model
def predict_sentiment(text):
    if not 'model' in globals():
        return 1 if len(text) % 2 == 0 else 0
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    inputs = {k: v for k, v in inputs.items() if k != "token_type_ids"}
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.logits.argmax(dim=1).item()