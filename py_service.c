#define PY_SSIZE_T_CLEAN
#include <python.h>
#include "py_service_api.h"
#include <Windows.h>

SERVICE_TABLE_ENTRY* g_ServiceTable;

static PyObject* py_service_start(PyObject*, PyObject*);

static PyObject* g_py_service_func;

static PyMethodDef py_serviceMethods[] = {
    {"start", (PyCFunction)&py_service_start, METH_VARARGS, NULL},
    {0,0,0,0}
};
static struct PyModuleDef py_servicemodule = {
    PyModuleDef_HEAD_INIT,
    "py_service",   /* name of module */
    NULL, /* module documentation, may be NULL */
    -1,       /* size of per-interpreter state of the module,
                 or -1 if the module keeps state in global variables. */
    py_serviceMethods
};

PyMODINIT_FUNC PyInit_py_service(void)
{
    return PyModule_Create(&py_servicemodule);
}

static PyObject* callback = NULL;

static PyObject* py_service_start(PyObject* self, PyObject* args)
{
    PyObject* temp;

    if (PyArg_ParseTuple(args, "O:set_callback", &temp)) {
        if (!PyCallable_Check(temp)) {
            PyErr_SetString(PyExc_TypeError, "parameter must be callable");
            return NULL;
        }
        g_callback = temp;
        
        
    }
    
    g_ServiceTable = (SERVICE_TABLE_ENTRY[])
    {
        {SERVICE_NAME, (LPSERVICE_MAIN_FUNCTION)ServiceMain},
        {NULL, NULL}
    };

    if (StartServiceCtrlDispatcher(g_ServiceTable) == FALSE)
    {
        return GetLastError();
    }

    return NULL;
}
