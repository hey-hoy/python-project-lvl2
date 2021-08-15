"""JSON and YAML parser."""
import json
import yaml


def parser(file_to_parse):
    """Parse file to dictionary."""
    with open(file_to_parse) as opened_file:
        if str(file_to_parse)[-5:] == '.json':
            dict_data = json.load(opened_file)
        if str(file_to_parse)[-5:] == '.yaml':
            dict_data = yaml.safe_load(opened_file)
        if str(file_to_parse)[-4:] == '.yml':
            dict_data = yaml.safe_load(opened_file)
    return dict_data
