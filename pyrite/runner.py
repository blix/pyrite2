#Pyrite - A Python based UI for the git source code management system.
#Copyright (C) 2011  Govind Salinas govind@sophiasuchtig.com.
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

import argparse, sys
from pyrite.commands import standard_commands


def run():
    parser = argparse.ArgumentParser(prog='Pyrite')
    # add debug arguments
    subparsers = parser.add_subparsers(title='commands', description='The most common commands are:')
    for name in sorted(standard_commands):
        params = standard_commands[name]
        p = subparsers.add_parser(name, help=params['help'], aliases=params['aliases'])
        for arg in params['arguments']:
            p.add_argument(*arg)
        p.set_defaults(module=params['module'])
    if len(sys.argv) < 2:
        parser.print_help()
    else:
        parser.parse_args()

    