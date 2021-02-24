from . import FILETYPES, textract, os

class Reader:
    def __init__(self):
        pass

    def read_file(self, file_dir):
        # Check if the directory supplied is valid
        if not os.path.isdir(file_dir):
            return 'Invalid file directory'

        # Use python's built in library for handling paths as strings
        file_name, file_extension = os.path.splitext(file_dir)
        file_extension = file_extension[1:]

        # Ensure that the file extension is within our list of pre-approved types
        if file_extension in FILETYPES:
            if file_extension == 'pdf':
                return textract.process(file_dir)
