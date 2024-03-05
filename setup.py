import glob

from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup


setup(
    name="pyab3p",
    version="0.1.0",
    author="Benedikt Fuchs",
    description="Python bindings for Ab3p",
    ext_modules=[
        Pybind11Extension(
            "pyab3p",
            sources=["main.cpp", *glob.glob("ab3P_source/*.cpp")],
            extra_compile_args=["-w"],
        )
    ],
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
)
