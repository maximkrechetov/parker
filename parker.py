import argparse
from app import __version__
from app.validate import InputFileValidator, OutputFileValidator
from app.xml_parser import XmlParser

print('Parker light parser version ' + __version__ + ' started.')

parser = argparse.ArgumentParser()
parser.add_argument('input_path', help='Path of XML file')
parser.add_argument('output_path', help='Path to save report file')

args = parser.parse_args()
input_path = args.input_path
output_path = args.output_path

print(input_path)
print(output_path)

input_validator = InputFileValidator(input_path, ['existence', 'exactly', 'xml_extension'])
input_validator.validate()

output_validator = OutputFileValidator(output_path, ['extension'])
output_validator.validate()

xml_parser = XmlParser(input_path, output_path)
xml_parser.parse()
