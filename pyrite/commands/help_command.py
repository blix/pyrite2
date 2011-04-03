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

class HelpCommand(AbstractCommand):
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

    def print_generic_help(self):
        self.print_header()
        
        self.stream.write('Basic commands...\n')
        for name in sorted(standard_commands):
            params = standard_commands[name]
            if self.ns.verbose or params['shortlist']:
                print(' {0:<10}: {1}'.format(name, params['help']))
        self.stream.write('\n')
        if not self.ns.verbose:
            self.stream.write('For more commands use "pyt help"\n')
        self.stream.write('For more information on a specific command use'
                          ' "pyt help <command>"\n\n')

    def print_command_help():
        pass
