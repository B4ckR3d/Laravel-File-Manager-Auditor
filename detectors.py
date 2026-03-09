import requests
from urllib.parse import urljoin

def detect_laravel(base):

    indicators = [
        "/login",
        "/vendor",
        "/storage"
    ]

    for i in indicators:

        try:
            r = requests.get(urljoin(base, i), timeout=5)

            if "laravel" in r.text.lower():
                return True

        except:
            pass

    return False
