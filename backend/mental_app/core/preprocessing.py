import re

def clean_text(text):
    text = str(text)
    text = re.sub(r"http\S+", "", text)   # remove URLs
    text = re.sub(r"<.*?>", "", text)     # remove HTML
    text = re.sub(r"\s+", " ", text).strip()
    return text