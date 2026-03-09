from cli import parse_args
from banner import show_banner
from targets import load_targets
from scanner import run_scan
from reporter import save_report


def main():

    args = parse_args()

    show_banner()

    targets = load_targets(args)

    print(f"Targets Loaded : {len(targets)}")
    print(f"Threads        : {args.threads}\n")

    results = run_scan(targets, args.threads)

    save_report(results, args.output)


if __name__ == "__main__":
    main()
