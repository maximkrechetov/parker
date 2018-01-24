# coding: utf8

from pathlib import Path
from .config import OUTPUT_FILE_EXTENSIONS


class BaseFileValidator:
    def __init__(self, path, validators):
        self.file = Path(path)
        self.validators = validators or []

    # Сама валидация
    def validate(self):
        for validator in self.validators:
            getattr(self, '_validate_file_' + validator, None)()

    # Проверка существования файла
    def _validate_file_existence(self):
        if not self.file.exists():
            raise IOError('File is not exists')

    # Проверка на то, что файл является файлом
    def _validate_file_exactly(self):
        if not self.file.is_file():
            raise IOError('This is not file')


class InputFileValidator(BaseFileValidator):
    # Проверка расширения на xml
    def _validate_file_xml_extension(self):
        if not self.file.suffix == '.xml':
            raise IOError('File has wrong format. Only XML accepted.')


class OutputFileValidator(BaseFileValidator):
    # Проверка на соответствие файла отчета расширениям из конфига
    def _validate_file_extension(self):
        if not (self.file.suffix in OUTPUT_FILE_EXTENSIONS):
            raise IOError('File has wrong format. Only TXT or RTF accepted.')
