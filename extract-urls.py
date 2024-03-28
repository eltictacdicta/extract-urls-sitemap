import requests
from bs4 import BeautifulSoup

def extract_urls(sitemap_url):
    response = requests.get(sitemap_url)
    soup = BeautifulSoup(response.content, 'xml')
    urls = [element.text for element in soup.find_all('loc')]
    return urls

def write_urls_to_file(urls, filename):
    with open(filename, 'w') as f:
        for url in urls:
            f.write(url + '\n')

def process_sitemap(sitemap_url):
    urls = extract_urls(sitemap_url)
    all_urls = []
    for url in urls:
        if 'sitemap' in url:
            all_urls.extend(process_sitemap(url))
        else:
            all_urls.append(url)
    return all_urls

# Procesa sitemaps.txt
with open('sitemaps.txt', 'r') as f:
    sitemap_urls = f.read().splitlines()

all_urls = []
for sitemap_url in sitemap_urls:
    all_urls.extend(process_sitemap(sitemap_url))

write_urls_to_file(all_urls, 'urls.txt')