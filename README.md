# Laravel File Manager Auditor v2

High-performance security auditing tool for detecting misconfiguration in **Laravel File Manager** installations.

This tool is designed for **security testing, auditing, and authorized penetration testing** only.

---

# Features

* High-speed concurrent scanning
* Laravel framework detection
* Laravel File Manager endpoint audit
* CIDR and domain list scanning
* Modern CLI interface
* Progress bar visualization
* JSON report output
* Modular architecture

---


Laravel-File-Manager-Auditor/
│
├── main.py
├── cli.py
├── scanner.py
├── detectors.py
├── targets.py
├── reporter.py
├── banner.py
├── utils.py
│
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
│
└── examples
    └── domains.txt

    
# Supported Checks

The scanner checks the following endpoints:

/file-manager/
/file-manager/initialize
/file-manager/content
/file-manager/upload

It identifies potential **misconfiguration or exposed endpoints** that may require further security review.

---

# Project Structure

lfm_audit/

main.py
cli.py
banner.py
targets.py
detectors.py
scanner.py
reporter.py
utils.py

Each module is responsible for a specific component of the scanning pipeline.

---

# Installation

Clone the repository:

git clone [https://github.com/yourusername/lfm-auditor](https://github.com/B4ckR3d/Laravel-File-Manager-Auditor/)
cd Laravel-File-Manager-Auditor

Install dependencies:

pip install -r requirements.txt

Or manually install:

pip install requests tqdm

---

# Usage

Scan a single target:

python main.py -t https://example.com

Scan multiple domains:

python main.py -f domains.txt

Scan an IP range (CIDR):

python main.py --cidr 192.168.1.0/24

Specify number of threads:

python main.py -f domains.txt --threads 200

Save report to custom file:

python main.py -f domains.txt -o report.json

---

# Example CLI Output

Laravel File Manager Auditor v2

Targets Loaded : 120
Threads : 100

Scanning...

██████████████████████████░░░░░░░░░░░░░ 68%

[+] Laravel detected : https://example.com
[!] Potential exposure : https://demo.site
[-] Not Laravel : https://randomsite.net

---

# Example JSON Report

[
{
"target": "https://example.com",
"laravel": true,
"filemanager": {
"initialize": 200,
"content": 401,
"upload": 405
}
}
]

---

# Legal Disclaimer

This tool is provided for **educational and security auditing purposes only**.

Do not use this tool against systems without **explicit authorization**.
The author is not responsible for any misuse or illegal activity.

---

# Roadmap

Planned improvements for future versions:

* Async scanner engine
* HTML security report
* Laravel version fingerprinting
* Subdomain enumeration integration
* Resume scanning
* Rich CLI dashboard
* Docker support

---

# Contributing

Contributions are welcome.

If you would like to improve the tool:

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

---

# License

MIT License
