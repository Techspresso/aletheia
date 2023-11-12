import re
from bs4 import BeautifulSoup
import requests

def remove_answer_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def extract_titles_from_urls(url):
    # TODO need to handle cases where the tile isn't in a h1 tag
    response = requests.get(url[0])
    html = response.text  
    soup = BeautifulSoup(html, 'html.parser') 
    h1 = soup.find('h1')
    title = h1.text if h1 else None
    return title
