from bs4 import BeautifulSoup
import logging
from urllib.parse import urljoin
import requests

logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', level=logging.INFO)

class webCrawler:
    def __init__(self, urls=[]):
        self.observed_urls = []
        self.urls_to_observe = urls

    def download_url(self, url):
        return requests.get(url).text

    def get_urls(self, url, html):
        soup = BeautifulSoup(html, 'html.parser')
        for link in soup.find_all('a'):
            path = link.get('href')
            if path and path.startswith('/'):
                path = urljoin(url, path)
            yield path
    
    def add_url_to_observe(self, url):
        if url not in self.observed_urls and url not in self.urls_to_observe:
            self.urls_to_observe.append(url)
    
    def crawl(self, url):
        html = self.download_url(url)
        for url in self.get_urls(url, html):
            self.add_url_to_observe(url)
    
    def run(self):
        while self.urls_to_observe:
            url = self.urls_to_observe.pop(0)
            logging.info(f'Crawling: {url}')
            try:
                self.crawl(url)
            except Exception:
                logging.exception(f'Failed to crawl: {url}')
            finally:
                self.observed_urls.append(url)

if __name__ == '__main__':
    webCrawler(urls=['https://www.stackoverflow.com/']).run()