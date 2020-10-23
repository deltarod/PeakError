#define PY_SSIZE_T_CLEAN
#define NPY_NO_DEPRECATED_API NPY_1_9_API_VERSION
#include <Python.h>
#include <numpy/arrayobject.h>
#include "PeakError.h"

static PyObject *
PeakErrorInterface(PyObject *self, PyObject *args)
{
    PyArrayObject *peak_start, *peak_end,
    *region_start, *region_end, *region_ann;

    int *peak_count, *region_count;

    if(!PyArg_ParseTuple(args, "O!O!iO!O!O!i",
                         &PyArray_Type, &peak_start,
                         &PyArray_Type, &peak_end,
                         &peak_count,
                         &PyArray_Type, &region_start,
                         &PyArray_Type, &region_end,
                         &PyArray_Type, &region_ann,
                         &region_count))
    {
        return NULL;
    }

    if(PyArray_TYPE(peak_start)!=NPY_INT){
        PyErr_SetString(PyExc_TypeError,
                        "peak_start must be numpy.ndarray type int");
        return NULL;
    }

    if(PyArray_TYPE(peak_end)!=NPY_INT){
        PyErr_SetString(PyExc_TypeError,
                        "peak_end must be numpy.ndarray type int");
        return NULL;
    }
    if(PyArray_TYPE(region_start)!=NPY_INT){
        PyErr_SetString(PyExc_TypeError,
                        "region_start must be numpy.ndarray type int");
        return NULL;
    }

    if(PyArray_TYPE(region_end)!=NPY_INT){
        PyErr_SetString(PyExc_TypeError,
                        "region_end must be numpy.ndarray type int");
        return NULL;
    }

    if(PyArray_TYPE(region_ann)!=NPY_INT){
        PyErr_SetString(PyExc_TypeError,
                        "region_ann must be numpy.ndarray type int");
        return NULL;
    }

    npy_intp col_dim = PyArray_DIM(region_start, 0);
    PyArrayObject *tp, *fp, *possible_tp, *possible_fp;

    tp = PyArray_ZEROS(1, &col_dim, NPY_INT, 0);
    int *tpA = (int*)PyArray_DATA(tp);
    fp = PyArray_ZEROS(1, &col_dim, NPY_INT, 0);
    int *fpA = (int*)PyArray_DATA(fp);
    possible_tp = PyArray_ZEROS(1, &col_dim, NPY_INT, 0);
    int *possible_tpA = (int*)PyArray_DATA(possible_tp);
    possible_fp = PyArray_ZEROS(1, &col_dim, NPY_INT, 0);
    int *possible_fpA = (int*)PyArray_DATA(possible_fp);

    int *peak_startA = (int*)PyArray_DATA(peak_start);
    int *peak_endA = (int*)PyArray_DATA(peak_end);
    int *region_startA = (int*)PyArray_DATA(region_start);
    int *region_endA = (int*)PyArray_DATA(region_end);
    int *region_annA = (int*)PyArray_DATA(region_ann);

    int status = PeakError(peak_startA, peak_endA, peak_count,
                           region_startA, region_endA, region_annA,
                           region_count,
                           tpA, fpA,
                           possible_tpA, possible_fpA);


    if(status == ERROR_UNDEFINED_ANNOTATION){
        PyErr_SetString(PyExc_ValueError,
                        "undefined annotation");
    }
    if(status == ERROR_REGIONS_NOT_INCREASING){
        PyErr_SetString(PyExc_ValueError,
                        "regions not increasing");
    }
    if(status == ERROR_PEAKS_NOT_INCREASING){
        PyErr_SetString(PyExc_ValueError,
                        "peaks not increasing");
    }
    if(status == ERROR_OVERLAPPING_PEAKS){
        PyErr_SetString(PyExc_ValueError,
                        "overlapping peaks");
    }
    if(status == ERROR_OVERLAPPING_REGIONS){
        PyErr_SetString(PyExc_ValueError,
                        "overlapping regions");
    }
    if(status != 0){
        return NULL;
    }

    return Py_BuildValue("{s:N,s:N,s:N,s:N}",
                         "tp", tp,
                         "fp", fp,
                         "possible_tp", possible_tp,
                         "possible_fp", possible_fp);
}

static PyMethodDef Methods[] = {
        {"interface", PeakErrorInterface, METH_VARARGS,
                        "Label Error calculation for peaks within a region"},
        {NULL, NULL, 0, NULL}
};

static struct PyModuleDef moduleDef =
        {
        PyModuleDef_HEAD_INIT,
        "PeakErrorInterface",
        "A Python extension for PeakError",
        -1,
        Methods
        };


PyMODINIT_FUNC
PyInit_PeakErrorInterface(void)
{
    PyObject *module;
    module = PyModule_Create(&moduleDef);
    if(module == NULL) return NULL;
    import_array();//necessary from numpy otherwise we crash with segfault
    return module;
}



