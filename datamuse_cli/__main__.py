from .cli import DataMuseCli
from argparse import ArgumentParser

__version__ = "0.0.3"

ap = ArgumentParser(
    "datamuse-cli",
    description="A command line interface that displays results from the Datamuse API",
)
ap.add_argument(
    "word",
    type=str,
    nargs="*",
    help="<word>",
)
ap.add_argument(
    "-m", "--max", type=int, default=15, help="maximum number of words to display"
)
ap.add_argument("-v", "--version", action="version", version="%(prog)s v" + __version__)
args = ap.parse_args()


def main():
    DataMuseCli(args.word, args.max)


if __name__ == "__main__":
    main()
