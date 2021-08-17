"""Json formatter."""
import json as json_import


def json(diff_dict):
    """Make json from dictionary with difference of 2 dictionaries."""
    return json_import.dumps(diff_dict, indent=4)
