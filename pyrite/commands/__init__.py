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

class AbstractCommand(object):
    def __init__(self, namespace, stream, config, repo):
        self.ns = namespace
        self.stream = stream
        self.config = config
        self.repo = repo

    def run(self):
        pass

standard_commands = {
    'status': {
        'aliases': ['st'],
        'arguments': [
          (('-c', '--color'), {'help': 'Enable color display.',
                                   'action': 'store_true'}),
          (('--amend',), {
                    'help': 'Show what would an ammended commit would do.',
                    'action': 'store_true'})
        ],
        'module': 'status',
        'help': 'Show status of the working set.',
        'shortlist': True,
    },
    'help': {
        'aliases': [],
        'arguments': [
            (['-v', '--verbose'], {'help': 'Print full help and aliases.',
                                   'action': 'store_true'}),
            (['subcommand'], {'help': 'Command to get help on.'}),
        ],
        'module': 'help_command',
        'help': 'View the general help or help for a command.',
        'shortlist': True,
    }
}