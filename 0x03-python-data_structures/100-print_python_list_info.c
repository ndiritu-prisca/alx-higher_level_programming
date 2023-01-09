#include <Python.h>
#include <stdio.h>

/**
  * print_python_list_info - a function that prints information about
  * a python list object
  * @p: pointer to generic PyObject which is of PyListObject type
  * Return: nothing
  */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t listSize = Pylist_Size();
}
