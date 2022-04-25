class User:
    """ User class. Represent a user in the file system.

    :ivar str username: Name of the user
    :ivar int password: User's password.
    :ivar bool manager: Is the user manager or not.
    """
    def __init__(self, username, password, manager=False):
        self.username = username
        self.password = password
        self.manager = manager


class FileSystem:
    """ FileSystem class. To hold all directories.

    :ivar list root: Holds all directories.
    """
    def __init__(self):
        self.root = []

    def mkdir(self, path):
        self.root.append(Directory(path))


class Directory:
    """ Directory class. Represent directory in the file system.

    :ivar str name: Name of the directory.
    :ivar list files_list: Holds the files
    """
    def __init__(self, name):
        self.name = name
        self.files_list = []

    def add_file(self, file):
        self.files_list.append(file)

    def remove_file(self, file_name):
        for index, file in enumerate(self.files_list):
            if file.name == file_name:
                self.files_list.pop(index)


class File:
    """ File class. Represent a file in the file system.

    :ivar str name: Name of the file.
    :ivar int weight: Size in KB of the file
    :ivar str content: The content pf the file
    :ivar str composer: Name of the file composer
    """
    def __init__(self, file_name, weight, content, composer):
        self.name = file_name
        self.weight = weight
        self.content = content
        self.composer = composer

    def read(self, user):
        if self.composer == user.username or user.managr:
            return self.content
        else:
            return None


class TextFile(File):

    def __init__(self, weight, content, composer):
        super().__init__(weight, content, composer)

    def count(self, sentence):
        return self.content.count(sentence)


class BinaryFile(File):
    def __init__(self, weight, content, composer):
        super().__init__(weight, content, composer)


class ImageFile(BinaryFile):
    def __init__(self, weight, content, composer):
        super().__init__(weight, content, composer)

    def get_dimensions(self):
        pass
