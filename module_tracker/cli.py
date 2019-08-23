import argparse

from .tracker import track_glob

parser = argparse.ArgumentParser()
parser.add_argument("glob_pattern", help="glob pattern of packages", type=str)


def main():
    arguments = parser.parse_args()
    print(*track_glob(arguments.glob_pattern), sep="\n")
    return 0
