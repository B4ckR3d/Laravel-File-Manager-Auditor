import json


def save_report(results, filename):

    with open(filename, "w") as f:
        json.dump(results, f, indent=4)

    print(f"\nReport saved -> {filename}")
