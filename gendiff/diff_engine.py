"""JSON and YAML gendiff."""
from gendiff.parser import parser


def generate_diff(file1, file2):
    """Run gendiff."""
    diff = '{\n'
    dict1 = parser(file1)
    dict2 = parser(file2)
    for key in sorted(dict1.keys() | dict2.keys()):
        if key in dict1.keys():
            if key in dict2.keys():
                if dict1[key] == dict2[key]:
                    diff += '    {0}: {1}\n'.format(key, dict1[key])
                else:
                    diff += '  - {0}: {1}\n'.format(key, dict1[key])
                    diff += '  + {0}: {1}\n'.format(key, dict2[key])
            else:
                diff += '  - {0}: {1}\n'.format(key, dict1[key])
        else:
            diff += '  + {0}: {1}\n'.format(key, dict2[key])
    diff += '}'
    return diff
