"""JSON and YAML gendiff."""
from gendiff.parser import parser
from gendiff.formatter.stylish import stylish
from gendiff.formatter.plain import plain
from gendiff.formatter.json_formatter import json


def dict_nodes_diff(node1, node2):
    """Return dictionary with difference of 2 dictionaries."""
    result_dict = {}
    for key in sorted(node1.keys() | node2.keys()):
        result_dict[key] = {}
        if key in node1.keys() & node2.keys():
            value1 = node1[key]
            value2 = node2[key]
            if isinstance(value1, dict) and isinstance(value2, dict):
                result_dict[key] = dict_nodes_diff(value1, value2)
            elif value1 == value2:
                result_dict[key]['hold'] = value1
            else:
                result_dict[key]['del'] = value1
                result_dict[key]['add'] = value2
        elif key in node1.keys():
            result_dict[key]['del'] = node1[key]
        else:
            result_dict[key]['add'] = node2[key]
    return result_dict


def generate_diff(file1, file2, formatter=stylish):
    """Run gendiff."""
    dict1 = parser(file1)
    dict2 = parser(file2)
    diff = dict_nodes_diff(dict1, dict2)
    if formatter == 'stylish':
        formatter = stylish
    if formatter == 'plain':
        formatter = plain
    if formatter == 'json':
        formatter = json
    return formatter(diff)
