"""Init."""
from gendiff.diff_engine import generate_diff
from gendiff.formatter.stylish import stylish
from gendiff.formatter.plain import plain
from gendiff.formatter.json_formatter import json
from pkgutil import extend_path

__path__ = extend_path(__path__, __name__)
__path__.reverse()
