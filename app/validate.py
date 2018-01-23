from pathlib import Path


class BaseFileValidator:
    def __init__(self, path, validators):
        self.file = Path(path)
        self.validators = validators or []

    def validate(self):
        for validator in self.validators:
            getattr(self, '_validate_file_' + validator, None)()

    def _validate_file_existence(self):
        if not self.file.exists():
            raise IOError('File is not exists')

    def _validate_file_exactly(self):
        if not self.file.is_file():
            raise IOError('This is not file')


class InputFileValidator(BaseFileValidator):
    def _validate_file_xml_extension(self):
        if not self.file.suffix == '.xml':
            raise IOError('File has wrong format. Only XML accepted.')


class OutputFileValidator(BaseFileValidator):
    def _validate_file_extension(self):

        if not (self.file.suffix in ['.txt', '.rtf']):
            raise IOError('File has wrong format. Only TXT or RTF accepted.')
