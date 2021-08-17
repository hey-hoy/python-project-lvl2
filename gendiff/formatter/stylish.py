"""Stylish formatter."""
import json


def format_dict(element, tabulation):
    """Json format dictionary element."""
    if isinstance(element, dict):
        form_dict = json.dumps(element, indent=4)
        form_dict = form_dict.replace('\n', '\n' + tabulation)
        return form_dict.replace('\"', '')
    if isinstance(element, bool):
        if element:
            return 'true'
        return 'false'
    if element is None:
        return 'null'
    return str(element)


def dict_node_stylish(node, node_name='', cur_tab=''):
    """Recursive make styled all nodes from dictionary."""
    result_str = ''
    if 'hold' in node.keys():
        formatted_dict = format_dict(node['hold'], cur_tab)
        result_str += cur_tab[:-2] + '  '
        result_str += node_name + ': ' + formatted_dict + '\n'
    if 'del' in node.keys():
        formatted_dict = format_dict(node['del'], cur_tab)
        result_str += cur_tab[:-2] + '- '
        result_str += node_name + ': ' + formatted_dict + '\n'
    if 'add' in node.keys():
        formatted_dict = format_dict(node['add'], cur_tab)
        result_str += cur_tab[:-2] + '+ '
        result_str += node_name + ': ' + formatted_dict + '\n'
    if result_str:
        return result_str
    if node_name:
        result_str += cur_tab + node_name + ': {\n'
    result_str += ''.join(list(map(
        dict_node_stylish,
        node.values(),
        node.keys(),
        [cur_tab + '    '] * len(node.keys())
    )))
    if node_name:
        result_str += cur_tab + '}\n'
    return result_str


def stylish(diff_dict):
    """Make styled string from dictionary with difference of 2 dictionaries."""
    if dict_node_stylish(diff_dict) == '':
        return '----------------------------\n'
    return '{\n' + dict_node_stylish(diff_dict).replace(',\n', '\n') + '}'
