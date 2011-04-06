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

import os
from pyrite import libgit2

class Repository(libgit2.Repository):
    def __init__(self, path=None, bare=False):
        self._location = path and path or os.getcwd()
        self._is_bare = bare
        self._work_tree = None
        self._git_dir = None
        self._git_dir = self.get_git_dir()
        libgit2.Repository.__init__(self)
        if self._git_dir:
            self.open(self._git_dir, bare)

    def _is_git_dir(self, d):
        """ This is taken from the git setup.c:is_git_directory
            function."""

        if os.path.isdir(d) and \
                os.path.isdir(os.path.join(d, 'objects')) and \
                os.path.isdir(os.path.join(d, 'refs')):
            headref = os.path.join(d, 'HEAD')
            return os.path.isfile(headref) or \
                    (os.path.islink(headref) and
                    os.readlink(headref).startswith('refs'))
        return False

    def get_git_dir(self):
        if not self._git_dir:
            self._git_dir = os.getenv('GIT_DIR')
            if self._git_dir and self._is_git_dir(self._git_dir):
                return self._git_dir
            curpath = self._location
            while curpath:
                if self._is_git_dir(curpath):
                    self._git_dir = curpath
                    self._is_bare = True
                    break
                gitpath = os.path.join(curpath, '.git')
                if self._is_git_dir(gitpath):
                    self._git_dir = gitpath
                    self._is_bare = False
                    break
                curpath, dummy = os.path.split(curpath)
                if not dummy:
                    break
        return self._git_dir

    def get_work_tree(self):
        if not self._work_tree and not self._is_bare:
            self._work_tree = os.getenv('GIT_WORK_TREE')
            if not self._work_tree or not os.path.isdir(self._work_tree):
                self._work_tree = os.path.abspath(
                                    os.path.join(self._git_dir, '..'))
        return self._work_tree
