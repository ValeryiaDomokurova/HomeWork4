import re


def fix_duplicates(sentence):
    pattern = r'\b(\w+)\b\s+\b\1\b'
    return re.sub(pattern, r'\1', sentence)
