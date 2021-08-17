"""Script to start gendiff."""
import argparse
from gendiff import generate_diff
from gendiff import stylish


def main():
    """Run gendiff."""
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    if args.format:
        print(generate_diff(args.first_file, args.second_file, args.format))
    else:
        print(generate_diff(args.first_file, args.second_file, stylish))


if __name__ == '__main__':
    main()
