from pathlib import Path


class InputFileValidator:
    def __init__(self, input_path):
        self.input_file = Path(input_path)

    def validate(self):
        # Check file is exist
        if not self.input_file.exists():
            raise IOError('File is not exists')

        # Check file is really file (LOL)
        if not self.input_file.is_file():
            raise IOError('This is not file')

        # Check file extension
        if not self.input_file.suffix == '.xml':
            raise IOError('File has wrong format. Only XML accepted.')
