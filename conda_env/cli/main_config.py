# -*- coding: utf-8 -*-
# Copyright (C) 2012 Anaconda, Inc
# SPDX-License-Identifier: BSD-3-Clause
from argparse import RawDescriptionHelpFormatter


from .main_vars import configure_parser as configure_vars_parser

config_description = '''
Configure a conda environment
'''

config_example = '''
examples:
    conda env config vars list
    conda env config --append channels conda-forge
'''

def configure_parser(sub_parsers):
    config_parser = sub_parsers.add_parser(
        'config',
        formatter_class=RawDescriptionHelpFormatter,
        description=config_description,
        help=config_description,
        epilog=config_example,
    )
    config_subparser = config_parser.add_subparsers()
    configure_vars_parser(config_subparser)
