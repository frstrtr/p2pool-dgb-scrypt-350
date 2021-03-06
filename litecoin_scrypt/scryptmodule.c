#include <Python.h>

//#include "scrypt.h"

//fix
// scryptmodule.c: In function ‘scrypt_getpowhash’:
// scryptmodule.c:15:5: warning: implicit declaration of function ‘scrypt_1024_1_1_256’ [-Wimplicit-function-declaration]
//    15 |     scrypt_1024_1_1_256((char *)PyString_AsString((PyObject*) input), output);
//       |     ^~~~~~~~~~~~~~~~~~~

void scrypt_1024_1_1_256(const char *input, char *output);

// end of fix

static PyObject *scrypt_getpowhash(PyObject *self, PyObject *args)
{
    char *output;
    PyObject *value;
    PyStringObject *input;
    if (!PyArg_ParseTuple(args, "S", &input))
        return NULL;
    Py_INCREF(input);
    output = PyMem_Malloc(32);

    scrypt_1024_1_1_256((char *)PyString_AsString((PyObject *)input), output);
    Py_DECREF(input);
    value = Py_BuildValue("s#", output, 32);
    PyMem_Free(output);
    return value;
}

static PyMethodDef ScryptMethods[] = {
    {"getPoWHash", scrypt_getpowhash, METH_VARARGS, "Returns the proof of work hash using scrypt"},
    {NULL, NULL, 0, NULL}};

PyMODINIT_FUNC initltc_scrypt(void)
{
    (void)Py_InitModule("ltc_scrypt", ScryptMethods);
}
