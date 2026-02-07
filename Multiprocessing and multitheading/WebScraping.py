import threading
import requests
from bs4 import BeautifulSoup

urls = ['https://www.langchain.com/', 'https://pypi.org/project/beautifulsoup4/']

def fetch_content(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content, 'html.parser')
    print(f'Fetch {len(soup.text)} charecters from {url}')

threads = []

for url in urls:
    thread = threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join() 


print('All web pages fetched.')