"""Тест сравнения файлов."""
import json
import pytest
from gendiff.diff_engine import generate_diff


@pytest.fixture()
def make_files(tmpdir_factory):
    """Создание проверочных файлов."""
    json_data1 = {
        'host': 'hexlet.io',
        'timeout': 50,
        'proxy': '123.234.53.22',
        'follow': False
    }
    file_path1 = tmpdir_factory.mktemp('data').join('1.json')
    with file_path1.open('w') as open_file1:
        json.dump(json_data1, open_file1)

    json_data2 = {
        'timeout': 20,
        'verbose': True,
        'host': 'hexlet.io'
    }
    file_path2 = tmpdir_factory.mktemp('data').join('2.json')
    with file_path2.open('w') as open_file2:
        json.dump(json_data2, open_file2)
    return [file_path1, file_path2]


def test_generate_diff(make_files):
    """Тест сравнения файлов."""
    file_path1, file_path2 = make_files
    assert generate_diff(file_path1, file_path2) == """{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}"""
