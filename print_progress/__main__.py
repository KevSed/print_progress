from .progress import print_progress
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument(iteration)
parser.add_argument(total)


def main():
    args = parser.parse_args()

    print_progress(args.iteration, args.total)


if __name__ == '__main__':
    main()
