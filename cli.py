import argparse

def parse_args():

    parser = argparse.ArgumentParser(
        description="Laravel File Manager Security Auditor"
    )

    parser.add_argument("-t","--target")
    parser.add_argument("-f","--file")
    parser.add_argument("--cidr")
    parser.add_argument("--threads", type=int, default=100)
    parser.add_argument("-o","--output", default="report.json")

    return parser.parse_args()
