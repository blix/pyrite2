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

from gettext import ngettext
import argparse, sys
argparse.ngettext = ngettext
from pyrite.commands import standard_commands
from pyrite import HelpError

class ExceptionalArgumentParser(argparse.ArgumentParser):
    def __init__(self, *args, **named):
        stream = None
        if 'stream' in named:
            stream = named.pop('stream')
        argparse.ArgumentParser.__init__(self, *args, **named)
        self.eap_stream = stream

    def _print_message(self, message, f):
        print(message, file=self.eap_stream)

    def print_help(self):
        module = self.get_default('module')
        mod = __import__('pyrite.commands.' + module, fromlist=['Command'])
        desc = mod.Command.__doc__
        self.description = desc
        argparse.ArgumentParser.print_help(self)

    def error(self, message):
        cmd = self.get_default('command')
        module = self.get_default('module')
        raise HelpError(argparse.Namespace(command=cmd,
                                           module=module,
                                           verbose=False))

def run():
    try:
        parser = ExceptionalArgumentParser(stream=sys.stderr, prog='Pyrite')
        # add debug arguments
        subparsers = parser.add_subparsers(title='commands',
                                description='The most common commands are:')
        for name in sorted(standard_commands):
            params = standard_commands[name]
            p = subparsers.add_parser(name, help=params['help'],
                                    aliases=params['aliases'],
                                    stream=sys.stderr)
            for flags, flag_params in params['arguments']:
                p.add_argument(*flags, **flag_params)
            p.set_defaults(module=params['module'], command=name)
        ns = parser.parse_args()
        mod = __import__('pyrite.commands.' + ns.module, fromlist=['Command'])
        cmd = mod.Command(ns, sys.stdout, None, None)
        cmd.run()
    except HelpError as e:
        import pyrite.commands.help_command as help_command
        # get version string
        version = '.1'
        help = help_command.Command(e.namespace, sys.stderr, None, None)
        help.set_version(version)
        help.run()

    