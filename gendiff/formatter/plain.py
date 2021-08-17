"""Plain formatter."""


def format_complex_values(element):
    """Format complex value."""
    if isinstance(element, dict):
        return '[complex value]'
    if isinstance(element, str):
        return "'{0}'".format(element)
    if isinstance(element, bool):
        if element:
            return 'true'
        return 'false'
    if element is None:
        return 'null'
    return str(element)


def dict_node_plain_formatter(node, node_name='', cur_path=''):
    """Recursive make styled all nodes from dictionary."""
    result_str = ''
    if 'del' in node.keys() and 'add' in node.keys():
        formatted_value1 = format_complex_values(node['del'])
        formatted_value2 = format_complex_values(node['add'])
        result_str += "Property '" + (cur_path + '.' + node_name if cur_path else node_name)
        result_str += "' was updated. From " + formatted_value1 + ' to ' + formatted_value2 + '\n'
        return result_str
    if 'del' in node.keys():
        result_str += "Property '" + (cur_path + '.' + node_name if cur_path else node_name)
        result_str += "' was removed\n"
        return result_str
    if 'add' in node.keys():
        formatted_value = format_complex_values(node['add'])
        result_str += "Property '" + (cur_path + '.' + node_name if cur_path else node_name)
        result_str += "' was added with value: " + formatted_value + '\n'
        return result_str
    if result_str or 'hold' in node.keys():
        return result_str
    result_str += ''.join(list(map(
        dict_node_plain_formatter,
        node.values(),
        node.keys(),
        [cur_path + '.' + node_name if cur_path else node_name] * len(node.keys())
    )))
    return result_str


def plain(diff_dict):
    """Make plain diff from dictionary with difference of 2 dictionaries."""
    return dict_node_plain_formatter(diff_dict)[:-1]
