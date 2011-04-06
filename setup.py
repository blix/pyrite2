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

from distutils.core import setup, Extension

module1 = Extension('libgit2',
                    sources = ['libgit2/repository.c',
                               'libgit2/module.c',],
                    library_dirs=['/usr/local/lib'],
                    libraries = ['git2',],)

setup (name = 'libgit2',
       version = '.1',
       description = 'libgit2 for Python',
       ext_modules = [module1])