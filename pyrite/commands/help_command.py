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
    pyt help <command>
    
    Shows list of commands or help for a command.
    """

    def __init__(self, *args, **named):
        AbstractCommand.__init__(self, *args, **named)
        self.version = ''

    def run(self):
        if not self.ns.command:
            self.print_generic_help()
        else:
            self.print_command_help()

    def set_version(self, version):
        self.version = version

    def print_header(self):
        self.stream.write(help_string + ' version: ' + self.version)
        self.stream.write('\n\n')

    def print_simple_list(self, full):
        for name in sorted(standard_commands):
            params = standard_commands[name]
            if full or params['shortlist']:
                format = ' {0:<10}: {help}\n'
                self.stream.write(format.format(name, **params))

    def print_extended_list(self):
        for name in sorted(standard_commands):
            params = standard_commands[name]
            format = '{}'
            l = len(params['aliases'])
            if l:
                format = '{0} ({1}{2})'.format(format, '{},' * (l - 1), '{}')
            format += ':\n\t{help}\n'
            self.stream.write(format.format(name, *params['aliases'], **params))

    def print_generic_help(self, full=False):
        self.print_header()
        
        self.stream.write('Basic commands...\n')
        if self.ns.verbose:
            self.print_extended_list()
        else:
            self.print_simple_list(full)        
        self.stream.write('\n')
        if not full:
            self.stream.write('For more commands use "pyt help"\n')
        elif not self.ns.verbose:
            self.stream.write('For a full list including aliases use '
                              '"pyt help -v"\n')
        self.stream.write('For more information on a specific command use'
                          ' "pyt help <command>"\n\n')

    def print_command_help(self):
        if self.ns.command == 'help':
            self.print_generic_help(True)
            return
