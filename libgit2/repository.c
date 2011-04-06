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
#include <structmember.h>
#include "repository.h"

static void Repository_dealloc(Repository* self)
{
    if (self->repo)
    {
        git_repository_free(self->repo);
        self->repo = NULL;
    }
    Py_TYPE(self)->tp_free((PyObject*)self);
}

static int Repository_init(Repository *self, PyObject *args, PyObject *kwds)
{
    /* Hmm, I don't think I need to do anything since all the
      interesting stuff would go into _open and _create
    */
    return 0;
}

static PyObject *Repository_open(Repository *self, PyObject *args,
                                 PyObject *kwds)
{
    PyObject *pypath=NULL, *bare=NULL;
    const char *path = NULL;
    int error = 0;

    if (self->initialized)
    {
        return Py_None;
    }
    self->initialized = 1;

    static char *kwlist[] = {"path", "bare", NULL};

    if (! PyArg_ParseTupleAndKeywords(args, kwds, "|O&O", kwlist,
                                      PyUnicode_FSConverter, &pypath, &bare))
    {
        return NULL;
    }

    if (path)
    {
        path = PyBytes_AS_STRING(pypath);
        error = git_repository_open(&(self->repo), path);
        if (error || !self->repo)
        {
            PyErr_SetString(PyExc_ValueError,
                            "Location is not in a git repository");
            return NULL;
        }
    }
    
    self->bare = PyObject_IsTrue(bare);

    return Py_None;
}

static PyMethodDef Repository_methods[] = {
    {"open", (PyCFunction)Repository_open, METH_VARARGS | METH_KEYWORDS,
    "Open an existing Git repository"},
    {NULL}  /* Sentinel */
};

PyTypeObject gitlib2_RepositoryType = {
    PyVarObject_HEAD_INIT(NULL, 0)
    "gitlib2.Repository",      /* tp_name */
    sizeof(Repository),        /* tp_basicsize */
    0,                         /* tp_itemsize */
    (destructor)Repository_dealloc,        /* tp_dealloc */
    0,                         /* tp_print */
    0,                         /* tp_getattr */
    0,                         /* tp_setattr */
    0,                         /* tp_reserved */
    0,                         /* tp_repr */
    0,                         /* tp_as_number */
    0,                         /* tp_as_sequence */
    0,                         /* tp_as_mapping */
    0,                         /* tp_hash  */
    0,                         /* tp_call */
    0,                         /* tp_str */
    0,                         /* tp_getattro */
    0,                         /* tp_setattro */
    0,                         /* tp_as_buffer */
    Py_TPFLAGS_DEFAULT |
        Py_TPFLAGS_BASETYPE,        /* tp_flags */
    "",                        /* tp_doc */
    0,		               /* tp_traverse */
    0,		               /* tp_clear */
    0,		               /* tp_richcompare */
    0,		               /* tp_weaklistoffset */
    0,		               /* tp_iter */
    0,		               /* tp_iternext */
    Repository_methods,             /* tp_methods */
    0,             /* tp_members */
    0,                         /* tp_getset */
    0,                         /* tp_base */
    0,                         /* tp_dict */
    0,                         /* tp_descr_get */
    0,                         /* tp_descr_set */
    0,                         /* tp_dictoffset */
    (initproc)Repository_init,      /* tp_init */
    0,                         /* tp_alloc */
    PyType_GenericNew,                 /* tp_new */

};

