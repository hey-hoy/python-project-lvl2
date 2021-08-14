"""Script to start gendiff."""
import argparse


def main():
    """Run gendiff."""
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    parser.parse_args()


if __name__ == '__main__':
    main()
