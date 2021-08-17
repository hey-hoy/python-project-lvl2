"""Test of generate_diff."""
import pytest
from gendiff.diff_engine import generate_diff
from shutil import copy2
import sys
from os import sep
from gendiff.formatter.plain import plain
from gendiff.formatter.json_formatter import json
FIXTURE_PATH = sys.path[0] + sep + 'gendiff' + sep + 'tests' + sep + 'fixtures' + sep


def copy_file(temp_dir, extension, fixture_path):
    """Copy one file."""
    file_name = fixture_path.split(sep)[-1].split('.')[0]
    new_file_path = temp_dir.join(file_name + '.' + extension)
    copy2(fixture_path, new_file_path)
    return new_file_path


def copy_files(tmpdir_factory, extension, *args):
    """Copy fixtures."""
    temp_dir = tmpdir_factory.mktemp('data')
    return [
        copy_file(temp_dir, extension, file_path) for file_path in args
    ]


@pytest.fixture()
def copy_json_files(tmpdir_factory):
    """Copy json files."""
    return copy_files(
        tmpdir_factory,
        'json',
        FIXTURE_PATH + '1_1.json',
        FIXTURE_PATH + '1_2.json',
        FIXTURE_PATH + '3_1.json',
        FIXTURE_PATH + '3_2.json'
    )


def test_generate_diff_json(copy_json_files):
    """Test diff json files."""
    file_paths = copy_json_files
    result_path = FIXTURE_PATH + '1_6.txt'
    with open(result_path, 'r') as opened_file1:
        result_string = opened_file1.read()
        assert generate_diff(file_paths[1], file_paths[0]) == result_string
    result_path = FIXTURE_PATH + '1_4.txt'
    with open(result_path, 'r') as opened_file2:
        result_string = opened_file2.read()
        assert generate_diff(file_paths[0], file_paths[1], plain) == result_string
    result_path = FIXTURE_PATH + '1_5.txt'
    with open(result_path, 'r') as opened_file3:
        result_string = opened_file3.read()
        assert generate_diff(file_paths[0], file_paths[1], json) == result_string
    result_path = FIXTURE_PATH + '3_3.txt'
    with open(result_path, 'r') as opened_file4:
        result_string = opened_file4.read()
        assert generate_diff(file_paths[2], file_paths[3]) == result_string
    result_path = FIXTURE_PATH + '3_4.txt'
    with open(result_path, 'r') as opened_file5:
        result_string = opened_file5.read()
        assert generate_diff(file_paths[2], file_paths[3], plain) == result_string
    result_path = FIXTURE_PATH + '3_5.txt'
    with open(result_path, 'r') as opened_file6:
        result_string = opened_file6.read()
        assert generate_diff(file_paths[2], file_paths[3], json) == result_string


@pytest.fixture()
def copy_yaml_files(tmpdir_factory):
    """Copy yaml files."""
    return copy_files(
        tmpdir_factory,
        'yaml',
        FIXTURE_PATH + '2_1.yaml',
        FIXTURE_PATH + '2_2.yaml',
        FIXTURE_PATH + '4_1.yaml',
        FIXTURE_PATH + '4_2.yaml'
    )


def test_generate_diff_yaml(copy_yaml_files):
    """Test diff yaml files."""
    file_paths = copy_yaml_files
    result_path = FIXTURE_PATH + '1_3.txt'
    with open(result_path, 'r') as opened_file1:
        result_string = opened_file1.read()
        assert generate_diff(file_paths[0], file_paths[1]) == result_string
    result_path = FIXTURE_PATH + '1_4.txt'
    with open(result_path, 'r') as opened_file2:
        result_string = opened_file2.read()
        assert generate_diff(file_paths[0], file_paths[1], plain) == result_string
    result_path = FIXTURE_PATH + '1_5.txt'
    with open(result_path, 'r') as opened_file3:
        result_string = opened_file3.read()
        assert generate_diff(file_paths[0], file_paths[1], json) == result_string
    result_path = FIXTURE_PATH + '3_3.txt'
    with open(result_path, 'r') as opened_file4:
        result_string = opened_file4.read()
        assert generate_diff(file_paths[2], file_paths[3]) == result_string
    result_path = FIXTURE_PATH + '3_4.txt'
    with open(result_path, 'r') as opened_file5:
        result_string = opened_file5.read()
        assert generate_diff(file_paths[2], file_paths[3], plain) == result_string
    result_path = FIXTURE_PATH + '3_5.txt'
    with open(result_path, 'r') as opened_file6:
        result_string = opened_file6.read()
        assert generate_diff(file_paths[2], file_paths[3], json) == result_string
