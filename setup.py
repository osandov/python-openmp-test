import os
import sysconfig

from setuptools import setup
from setuptools.extension import Extension

os.environ["CC"] = "clang"
os.environ["LDSHARED"] = sysconfig.get_config_var("LDSHARED").replace("gcc", "clang")

setup(
    name="myomp",
    version="0.0.0",
    ext_modules=[
        Extension(
            name="myomp",
            sources=["myomp.c"],
            extra_compile_args=["-fopenmp"],
            extra_link_args=["-fopenmp"],
        )
    ],
)
