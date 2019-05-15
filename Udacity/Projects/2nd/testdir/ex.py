import os

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
    for r, d, f in os.walk(path):
        for file in f:
            if file.endswith(suffix):
                files.append(os.path.join(r, file))

    return files

print(find_files(".c", ".")) # will return 4 file paths
