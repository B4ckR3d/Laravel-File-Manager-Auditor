import requests
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
from detectors import detect_laravel
from urllib.parse import urljoin

headers = {
    "User-Agent": "LFM-Audit/2.0"
}

def check_filemanager(base):

    endpoints = {
        "initialize": "/file-manager/initialize",
        "content": "/file-manager/content",
        "upload": "/file-manager/upload"
    }

    data = {}

    for name, ep in endpoints.items():

        try:
            r = requests.get(urljoin(base, ep), headers=headers, timeout=6)
            data[name] = r.status_code
        except:
            data[name] = None

    return data


def scan_target(target):

    if not target.startswith("http"):
        target = "http://" + target

    result = {
        "target": target,
        "laravel": False,
        "filemanager": {}
    }

    try:

        result["laravel"] = detect_laravel(target)

        if result["laravel"]:
            result["filemanager"] = check_filemanager(target)

    except:
        pass

    return result


def run_scan(targets, threads):

    results = []

    with ThreadPoolExecutor(max_workers=threads) as executor:

        futures = []

        for t in targets:
            futures.append(executor.submit(scan_target, t))

        for f in tqdm(futures):
            results.append(f.result())

    return results
