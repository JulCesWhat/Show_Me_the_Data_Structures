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

    if not os.path.isdir(path):
        return []

    files = []

    current_files = os.listdir(path)

    for file in current_files:
        if os.path.isdir(path + "/" + file):
            files += find_files(suffix, path + "/" + file)
        elif file.endswith(suffix):
            files.append(path + "/" + file)

    return files


if __name__ == "__main__":
    test_result_1 = find_files(".c", "./testdir")
    print(test_result_1)
    # ['./testdir/subdir3/subsubdir1/b.c', './testdir/t1.c', './testdir/subdir5/a.c', './testdir/subdir1/a.c']

    test_result_2 = find_files(".doc", "./testdir")
    print(test_result_2)
    # []

    test_result_3 = find_files(".c", "./testdir/t1.c")
    print(test_result_3)
    # []