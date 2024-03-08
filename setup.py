import glob
from pathlib import Path

from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup


setup(
    name="pyab3p",
    version="0.1.0",
    author="Benedikt Fuchs",
    author_email="benedikt.fuchs.staw@hotmail.com",
    description="Python bindings for Ab3p",
    url="https://github.com/hu-ner/pyab3p",
    long_description=Path("README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    ext_modules=[
        Pybind11Extension(
            "pyab3p",
            sources=[
                "ab3p_source/MPtok.cpp",
                "ab3p_source/runn.cpp",
                "ab3p_source/FBase.cpp",
                "ab3p_source/Hash.cpp",
                "ab3p_source/AbbrStra.cpp",
                "ab3p_source/AbbrvE.cpp",
                "ab3p_source/Ab3P.cpp",
                "main.cpp",
            ],
        )
    ],
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
    setuptools_git_versioning={
        "enabled": True,
    },
    setup_requires=["setuptools-git-versioning"],
)
