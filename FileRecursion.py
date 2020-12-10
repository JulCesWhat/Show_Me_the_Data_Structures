import os


# Locally save and call this file ex.py ##

# Code to demonstrate the use of some of the OS modules in python


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    files = []

    current_files = os.listdir(path)

    for file in current_files:
        if os.path.isdir(path + "/" + file):
            files += find_files(suffix, path + "/" + file)
        elif file.endswith(suffix):
            files.append(path + "/" + file)

    return files


test_result = find_files(".c", "./testdir")
print(test_result)