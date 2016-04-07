import os


def current_directory():
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


def file_directory_exists(pathname):
    """
    This is a function to check if the specified path has the directory or filename.
    :rtype: bool
    """
    path = os.path.exists(pathname)
    return path

filename = "README.md"
print current_directory()
print file_abs_path(filename)
print file_directory_exists(file_abs_path(filename))
