
class FileDoesNotExist(Exception):
    """ Raised when the input file does not exist"""
    def __init__(self, file_path):
        self.message = f"Input file '{file_path}' does not exist!"
        super().__init__(self.message)
