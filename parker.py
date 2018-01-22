import argparse
from app import __version__
from app.validate import InputFileValidator
from app.xml_parser import XmlParser

print('Parker light parser version ' + __version__ + ' started.')

parser = argparse.ArgumentParser()
parser.add_argument('input_path', help='Path of XML file')
parser.add_argument('output_path', help='Path to save report file')

args = parser.parse_args()
input_path = args.input_path

print(input_path)
print(args.output_path)

validator = InputFileValidator(input_path)
validator.validate()

xml_parser = XmlParser(input_path)
xml_parser.parse()

