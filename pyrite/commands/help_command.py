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

from pyrite.commands import AbstractCommand, standard_commands

help_string = 'Pyrite Distributed SCM (git based)'

class Command(AbstractCommand):
    """
    Shows a list of commands or help for a command.
    """

    def __init__(self, *args, **named):
        AbstractCommand.__init__(self, *args, **named)
        self.version = ''
        self.argparser = None

    def run(self):
        if not self.ns.command:
            self.print_generic_help()
        else:
            self.print_command_help()

    def set_version(self, version):
        self.version = version

    def print_header(self):
        print('{0} version: {1}\n'.format(help_string, self.version), file=self.stream)

    def print_simple_list(self, full):
        for name in sorted(standard_commands):
            params = standard_commands[name]
            if full or params['shortlist']:
                format = ' {0:<10}: {help}'
                print(format.format(name, **params), file=self.stream)

    def print_extended_list(self):
        for name in sorted(standard_commands):
            params = standard_commands[name]
            format = '{}'
            l = len(params['aliases'])
            if l:
                format = '{0} ({1}{2})'.format(format, '{},' * (l - 1), '{}')
            format += ':\n\t{help}'
            print(format.format(name, *params['aliases'], **params),
                  file=self.stream)

    def print_generic_help(self, full=False):
        self.print_header()
        
        print('Basic commands...', file=self.stream)
        if self.ns.verbose:
            self.print_extended_list()
        else:
            self.print_simple_list(full)        
        print('', file=self.stream)
        if not full:
            print('For more commands use "pyt help"', file=self.stream)
        elif not self.ns.verbose:
            print('For a full list including aliases use '
                              '"pyt help -v"', file=self.stream)
        print('For more information on a specific command use'
                          ' "pyt help <command>"\n', file=self.stream)

    def set_argparser(self, argparser):
        self.argparser = argparser

    def print_command_help(self):
        if not self.ns.subcommand:
            self.print_generic_help(True)
        else:
            self.argparser.parse_args([self.ns.subcommand, '--help'])
