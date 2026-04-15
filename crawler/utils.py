from urllib.parse import urlparse, urljoin
import re

def is_same_domain(base_url, target_url):
    return urlparse(base_url).netloc == urlparse(target_url).netloc

def get_full_url(base_url, link):
    return urljoin(base_url, link)

def normalize_phone(phone):
    phone = re.sub(r"[^\d+]", "", phone)

    if phone.startswith("91") and not phone.startswith("+91"):
        phone = "+" + phone
    elif len(phone) == 10:
        phone = "+91" + phone

    return phone