import argparse

from pod_devops_demo import __version__, greet


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="pod-devops-demo")
    p.add_argument("--version", action="version", version=__version__)
    sub = p.add_subparsers(dest="cmd", required=True)

    g = sub.add_parser("greet", help="Print greeting")
    g.add_argument("name", nargs="?", default="world")
    return p


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    if args.cmd == "greet":
        print(greet(args.name))
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
