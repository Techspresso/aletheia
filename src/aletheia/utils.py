import re
from bs4 import BeautifulSoup
import requests

def remove_answer_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def extract_titles_from_urls(urls):
    
    titles = []
    
    for url in urls:

        response = requests.get(url)
        html = response.text
        
        soup = BeautifulSoup(html, 'html.parser')
        
        h1 = soup.find('h1')
        title = h1.text if h1 else None
        
        titles.append(title)
        
    return titles