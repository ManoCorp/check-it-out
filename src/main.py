# Create a command line parser with argparse that parses config file and file format

import argparse
import os
import sys
import logging
import json
import helper
from integrations import integration_interface
from templater import Templater, Types

# Set up logging
logging.basicConfig(level=logging.INFO)


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Re-format your output')
    parser.add_argument('-i', '--input-file', type=str, required=True,
                    help='Path to the file to be processed')
    parser.add_argument('-f', '--input-format', type=str, required=True,
                    help=f'File format ({", ".join(helper.input_formats)})')
    parser.add_argument('-s', '--output-integration', type=str, required=True,
                    help=f'Output integration ({", ".join(helper.output_integration.keys())})')
    parser.add_argument('-d', '--dest', type=str, required=True,
                    help=f'Final destination of the output integration')
    parser.add_argument('-t', '--template-file', type=str, required=True,
                    help='Jinja2 template file')
    parser.add_argument('-p', '--output-format', type=str, required=True,
                    help=f'Output format ({", ".join(helper.output_formats)})')
    
    return parser.parse_args()

def is_valid_args(args: argparse.Namespace) -> bool:
    valid = True
    if not os.path.exists(args.input_file):
        logging.error(f'Input file {args.input_file} does not exist')
        valid = False
    if not os.path.exists(args.template_file):
        logging.error(f'Template file {args.template_file} does not exist')
        valid = False
    if args.input_format not in helper.input_formats:
        logging.error(f'Input format {args.input_format} is not supported')
        valid = False
    if args.output_format not in helper.output_formats:
        logging.error(f'Output format {args.output_format} is not supported')
        valid = False
    if args.output_integration not in helper.output_integration:
        logging.error(f'Output source {helper.output_integration.keys()} is not supported')
        valid = False
    return valid

def get_integation(name) -> integration_interface.IntegrationInterface:
    return helper.output_integration[name]

def main():
    args = get_args()
    if not is_valid_args(args):
        sys.exit(1)
    
    integration_class = get_integation(args.output_integration)
    integration = integration_class(args.dest)
    
    template = Templater(args.template_file, args.output_format)
    template.handler(json.load(open(args.input_file)), Types[args.output_format.upper()].value)


if __name__ == '__main__':
    main()