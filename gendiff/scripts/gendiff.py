"""Script to start gendiff."""
import argparse
import sys
from pathlib import Path
from gendiff import generate_diff
from gendiff import stylish


def main():
    """Run gendiff."""
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    first_file = Path(args.first_file).resolve()
    second_file = Path(args.second_file).resolve()
    if args.format:
        print(generate_diff(first_file, second_file, args.format))
    else:
        print(generate_diff(first_file, second_file, stylish))


if __name__ == '__main__':

    main()
