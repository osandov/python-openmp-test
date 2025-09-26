#include <Python.h>

static struct PyModuleDef drgnmodule = {
	PyModuleDef_HEAD_INIT,
	"myomp",
	NULL,
	-1,
};

PyMODINIT_FUNC PyInit_myomp(void)
{
	#pragma omp parallel num_threads(2)
	{
		asm volatile("" ::: "memory");
	}
	return PyModule_Create(&drgnmodule);
}
