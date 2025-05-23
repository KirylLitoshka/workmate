import argparse


def get_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("files", type=str, nargs="*", default=[],  help="File paths")
    parser.add_argument(
        "--report", type=str, default=None, nargs='?', const="no_args", help="Report type"
    )
    return parser.parse_args()
