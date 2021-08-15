"""Test of generate_diff."""
import pytest
from gendiff.diff_engine import generate_diff
from shutil import copy2


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
        r'C:\python-project-lvl2\gendiff\tests\fixtures\1_1.json',
        r'C:\python-project-lvl2\gendiff\tests\fixtures\1_2.json',
        'json'
    )


@pytest.fixture()
def copy_yaml_files(tmpdir_factory):
    """Copy yaml files."""
    return copy_files(
        tmpdir_factory,
        r'C:\python-project-lvl2\gendiff\tests\fixtures\2_1.yaml',
        r'C:\python-project-lvl2\gendiff\tests\fixtures\2_2.yaml',
        'yaml'
    )


def test_generate_diff_json(copy_json_files):
    """Test diff json files."""
    file_path1, file_path2 = copy_json_files
    result_path = r'C:\python-project-lvl2\gendiff\tests\fixtures\1_3.txt'
    with open(result_path, 'r') as opened_file:
        result_string = opened_file.read()
    assert generate_diff(file_path1, file_path2) == result_string


def test_generate_diff_yaml(copy_yaml_files):
    """Test diff yaml files."""
    file_path1, file_path2 = copy_yaml_files
    result_path = r'C:\python-project-lvl2\gendiff\tests\fixtures\1_3.txt'
    with open(result_path, 'r') as opened_file:
        result_string = opened_file.read()
    assert generate_diff(file_path1, file_path2) == result_string
