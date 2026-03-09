from urllib.parse import urlparse


def normalize_url(url):

    if not url.startswith("http"):
        url = "http://" + url

    return url.rstrip("/")
