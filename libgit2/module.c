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
#include <Python.h>
#include "repository.h"


static struct PyModuleDef libgit2 = {
    PyModuleDef_HEAD_INIT,
    "libgit2",      /* name of module */
    NULL,           /* module documentation, may be NULL */
    -1,             /* size of per-interpreter state of the module,
                    or -1 if the module keeps state in global variables. */
    NULL,
    NULL,
    NULL,
    NULL,
    NULL
};

PyMODINIT_FUNC PyInit_libgit2(void)
{
    PyObject *m;

    if (PyType_Ready(&gitlib2_RepositoryType) < 0)
        return NULL;

    m = PyModule_Create(&libgit2);
    if (m == NULL)
    {
        return NULL;
    }
    
    Py_INCREF(&gitlib2_RepositoryType);
    PyModule_AddObject(m, "Repository", (PyObject *)&gitlib2_RepositoryType);
    return m;
}
