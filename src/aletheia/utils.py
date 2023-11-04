import re

def remove_answer_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)