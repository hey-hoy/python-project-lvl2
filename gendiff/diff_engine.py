"""JSON gendiff."""
import json


def generate_diff(file1, file2):
    """Run gendiff."""
    diff = '{\n'
    with open(file1) as open_file1:
        with open(file2) as open_file2:
            json1 = json.load(open_file1)
            json2 = json.load(open_file2)
            for key in sorted(json1.keys() | json2.keys()):
                if key in json1.keys():
                    if key in json2.keys():
                        if json1[key] == json2[key]:
                            diff += '    {0}: {1}\n'.format(key, json1[key])
                        else:
                            diff += '  - {0}: {1}\n'.format(key, json1[key])
                            diff += '  + {0}: {1}\n'.format(key, json2[key])
                    else:
                        diff += '  - {0}: {1}\n'.format(key, json1[key])
                else:
                    diff += '  + {0}: {1}\n'.format(key, json2[key])
    diff += '}'
    return diff
