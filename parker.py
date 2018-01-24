# coding: utf8

import argparse
from app import __version__
from app.validate import InputFileValidator, OutputFileValidator
from app.xml_parser import XmlParser
from app.config import INPUT_FILE_VALIDATORS, OUTPUT_FILE_VALIDATORS

print('Parker light parser version ' + __version__ + ' started.')

parser = argparse.ArgumentParser()
parser.add_argument('input_path', help='Path of XML file')
parser.add_argument('output_path', help='Path to save report file')

args = parser.parse_args()
input_path = args.input_path
output_path = args.output_path

print('Input path:' + input_path)
print('Output path:' + output_path)

input_validator = InputFileValidator(input_path, INPUT_FILE_VALIDATORS)
input_validator.validate()

output_validator = OutputFileValidator(output_path, OUTPUT_FILE_VALIDATORS)
output_validator.validate()

xml_parser = XmlParser(input_path, output_path)
xml_parser.parse()
