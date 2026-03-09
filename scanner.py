from concurrent.futures import ThreadPoolExecutor
from rich.live import Live
from stats import ScanStats
from detectors import detect_laravel
import requests
from urllib.parse import urljoin

headers = {"User-Agent": "LFM-Audit/2.0"}

def run_scan(targets, threads):

    stats = ScanStats(len(targets))
    results = []

    def scan_target(target):

        if not target.startswith("http"):
            target = "http://" + target

        result = {
            "target": target,
            "laravel": False,
            "filemanager": {}
        }

        try:

            if detect_laravel(target):

                stats.update_laravel()

                result["laravel"] = True

                r = requests.get(
                    urljoin(target,"/file-manager/initialize"),
                    headers=headers,
                    timeout=6
                )

                if r.status_code == 200:
                    stats.update_misconfig()

        except:
            pass

        stats.update_scanned()
        return result

    with Live(stats.render(), refresh_per_second=4) as live:

        with ThreadPoolExecutor(max_workers=threads) as executor:

            futures = [executor.submit(scan_target, t) for t in targets]

            for f in futures:
                results.append(f.result())
                live.update(stats.render())

    return results
