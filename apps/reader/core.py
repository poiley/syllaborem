from . import FILETYPES, pdfplumber, textract, os

class Reader:
    def __init__(self):
        pass

    def read_file(self, file_dir):
        # Check if the directory supplied is valid
        if not os.path.isfile(file_dir):
            return 'Invalid file directory'

        # Use python's built in library for handling paths as strings
        file_name, file_extension = os.path.splitext(file_dir)
        file_extension = file_extension[1:]

        # Ensure that the file extension is within our list of pre-approved types
        if file_extension in FILETYPES:
            if file_extension == 'pdf':
                file_contents = ''
                file = pdfplumber.open(file_dir)

                for page in file.pages:
                    for character in page.chars:
                        file_contents += character['text']
                    file_contents += '\n'

                return file_contents
            elif file_extension == 'txt':
                return textract.process(file_dir)
