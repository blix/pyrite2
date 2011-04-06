/*
Pyrite - A Python based UI for the git source code management system.
Copyright (C) 2011  Govind Salinas govind@sophiasuchtig.com.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/

#ifndef __REPOSITORY_H__
#define __REPOSITORY_H__

#include <Python.h>
#include <git2.h>

typedef struct {
    PyObject_HEAD
    git_repository *repo;
    int bare;
    int initialized;
} Repository;

extern PyTypeObject gitlib2_RepositoryType;

#endif  /* __REPOSITORY_H__ */