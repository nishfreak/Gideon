import os


def current_dir():
    """
    This is a function to retrieve the current working directory.
    :rtype: string
    """
    path = os.getcwd()
    return path


def file_abs_path(file_name):
    """
    This is a function to retrieve the absolute path of a specified filename.
    :rtype: string
    """
    path = os.path.abspath(file_name)
    return path


def file_dir_exists(path_name):
    """
    This is a function to check if the specified path has the directory or file.
    :rtype: bool
    """
    path = os.path.exists(path_name)
    return path


def check_if_dir(path_name):
    """
    This is a function to check if the specified path belongs to a directory.
    :rtype: bool
    """
    path = os.path.isdir(path_name)
    return path


def count_files(path_name):
    count = len([name for name in os.listdir(path_name) if os.path.isfile(name)])
    return count


def list_dir_contents(path_name):
    contents = os.listdir(path_name)
    return contents


def show_dir_tree(path_name):
    for root, dirs, files in os.walk(path_name):
        level = root.replace(path_name, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))


filename = "README.md"
print current_dir()
print file_abs_path(filename)
print file_dir_exists(file_abs_path(filename))
print check_if_dir(current_dir())
print count_files(current_dir())
print list_dir_contents(current_dir())
path = "/home/nishant/Documents/final project"
show_dir_tree(path)