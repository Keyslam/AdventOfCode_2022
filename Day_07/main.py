from __future__ import annotations
from dataclasses import dataclass
import re


@dataclass
class File:
    size: int


class Directory:
    parent: Directory
    name: str
    sub_folders: dict[str, Directory]
    files: dict[str, File]

    def __init__(self, parent: Directory, name: str):
        self.parent = parent
        self.name = name
        self.sub_folders = dict()
        self.files = dict()

    def add_file(self, name: str, file: File):
        self.files[name] = file

    def add_directory(self, name: str, directory: Directory):
        self.sub_folders[name] = directory

    def get_directory(self, name: str) -> Directory:
        return self.sub_folders[name]

    def get_size(self) -> int:
        size_of_sub_folders = sum(map(lambda x: self.sub_folders[x].get_size(), self.sub_folders))
        size_of_files = sum(map(lambda x: self.files[x].size, self.files))

        return size_of_sub_folders + size_of_files


def parse():
    root = Directory(None, "/")
    current_directory = root

    for line in open("input.txt"):
        change_directory_action = re.match("(\$ cd) (\S+)", line)
        create_directory_action = re.match("(dir) (\S+)", line)
        create_file_action = re.match("(\d+) (\S+)", line)

        if create_file_action is not None:
            size = int(line.split()[0])
            name = line.split()[1]
            file = File(size)
            current_directory.add_file(name, file)

        if create_directory_action is not None:
            name = line.split()[1]
            directory = Directory(current_directory, name)
            current_directory.add_directory(name, directory)

        if change_directory_action is not None:
            path = line.split()[2]
            if path == "/":
                # Ignore
                pass
            elif path == "..":
                current_directory = current_directory.parent
            else:
                current_directory = current_directory.get_directory(path)

    return root


def get_directories_smaller_than(output: [Directory], directory: Directory, size: int):
    if directory.get_size() <= size:
        output.append(directory)

    for sub_folder_name in directory.sub_folders:
        sub_folder = directory.sub_folders[sub_folder_name]
        get_directories_smaller_than(output, sub_folder, size)


def one():
    root = parse()
    output: [Directory] = []
    get_directories_smaller_than(output, root, 100000)
    result = sum(map(lambda x: x.get_size(), output))
    print(result)


def two():
    root = parse()
    output: [Directory] = []
    get_directories_smaller_than(output, root, 100000000000)
    used_space = root.get_size()
    total_space = 70000000
    space_for_update = 30000000
    space_left = total_space - used_space
    space_needed = space_for_update - space_left

    r = list(filter(
        lambda x: x[1] >= space_needed
    , map(
        lambda x: (x, x.get_size()), output)
    ))
    r.sort(key=lambda x: x[1])

    print(r[0][1])


if __name__ == '__main__':
    one()
    two()
