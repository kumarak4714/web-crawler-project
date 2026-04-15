import requests
from bs4 import BeautifulSoup
from collections import deque

from crawler.utils import is_same_domain, get_full_url, normalize_phone
from crawler.extractor import extract_phone_numbers


def crawl_website(start_url, max_pages=20):
    visited = set()
    queue = deque([start_url])
    phone_numbers = set()

    while queue and len(visited) < max_pages:
        url = queue.popleft()

        if url in visited:
            continue

        print(f"Crawling: {url}")
        visited.add(url)

        try:
            response = requests.get(url, timeout=5)
            soup = BeautifulSoup(response.text, "html.parser")

            # Extract phone numbers
            text = soup.get_text()
            numbers = extract_phone_numbers(text)

            for num in numbers:
                phone_numbers.add(normalize_phone(num))

            # Extract links
            for link_tag in soup.find_all("a", href=True):
                full_url = get_full_url(url, link_tag["href"])

                if is_same_domain(start_url, full_url):
                    if full_url not in visited:
                        queue.append(full_url)

        except Exception as e:
            print(f"Error: {e}")

    return phone_numbers