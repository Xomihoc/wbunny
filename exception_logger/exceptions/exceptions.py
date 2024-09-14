class DirectoryError(Exception):
    pass


class NotDirectory(DirectoryError):
    pass


class DirectoryNotSpecified(DirectoryError):
    pass
