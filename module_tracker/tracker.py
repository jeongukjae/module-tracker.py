from glob import glob

from .analyzer import parse_file


def track_glob(glob_pattern: str):
    modules = set()

    for file_name in _get_files_from(glob_pattern):
        modules.update(parse_file(file_name))

    return sorted(list(modules))


def track_directory(directory):
    pass


def _get_files_from(glob_pattern):
    return glob(glob_pattern, recursive=True)
