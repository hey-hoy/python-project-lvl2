"""Test of generate_diff."""
import pytest
from gendiff.diff_engine import generate_diff
from shutil import copy2
import sys
from os import sep
FIXTURE_PATH = sys.path[0] + sep + 'fixtures' + sep


def copy_files(tmpdir_factory, file1, file2, extension):
    """Copy fixtures."""
    temp_dir = tmpdir_factory.mktemp('data')
    file_path1 = temp_dir.join('1.' + extension)
    copy2(file1, file_path1)
    file_path2 = temp_dir.join('2.' + extension)
    copy2(file2, file_path2)
    return [file_path1, file_path2]


@pytest.fixture()
def copy_json_files(tmpdir_factory):
    """Copy json files."""
    return copy_files(
        tmpdir_factory,
        FIXTURE_PATH + '1_1.json',
        FIXTURE_PATH + '1_2.json',
        'json'
    )


@pytest.fixture()
def copy_yaml_files(tmpdir_factory):
    """Copy yaml files."""
    return copy_files(
        tmpdir_factory,
        FIXTURE_PATH + '2_1.yaml',
        FIXTURE_PATH + '2_2.yaml',
        'yaml'
    )


@pytest.fixture()
def copy_json_files2(tmpdir_factory):
    """Copy json files."""
    return copy_files(
        tmpdir_factory,
        FIXTURE_PATH + '3_1.json',
        FIXTURE_PATH + '3_2.json',
        'json'
    )


@pytest.fixture()
def copy_yaml_files2(tmpdir_factory):
    """Copy yaml files2."""
    return copy_files(
        tmpdir_factory,
        FIXTURE_PATH + '4_1.yaml',
        FIXTURE_PATH + '4_2.yaml',
        'yaml'
    )


def test_generate_diff_json(copy_json_files):
    """Test diff json files."""
    file_path1, file_path2 = copy_json_files
    result_path = FIXTURE_PATH + '1_3.txt'
    with open(result_path, 'r') as opened_file:
        result_string = opened_file.read()
    assert generate_diff(file_path1, file_path2) == result_string


def test_generate_diff_yaml(copy_yaml_files):
    """Test diff yaml files."""
    file_path1, file_path2 = copy_yaml_files
    result_path = FIXTURE_PATH + '1_3.txt'
    with open(result_path, 'r') as opened_file:
        result_string = opened_file.read()
    assert generate_diff(file_path1, file_path2) == result_string


def test_generate_diff_json2(copy_json_files2):
    """Test diff json files2."""
    file_path1, file_path2 = copy_json_files2
    result_path = FIXTURE_PATH + '3_3.txt'
    with open(result_path, 'r') as opened_file:
        result_string = opened_file.read()
    assert generate_diff(file_path1, file_path2) == result_string


def test_generate_diff_yaml2(copy_yaml_files2):
    """Test diff yaml files2."""
    file_path1, file_path2 = copy_yaml_files2
    result_path = FIXTURE_PATH + '3_3.txt'
    with open(result_path, 'r') as opened_file:
        result_string = opened_file.read()
    assert generate_diff(file_path1, file_path2) == result_string
