from setuptools import setup
from pybind11.setup_helpers import Pybind11Extension, build_ext
from os.path import join

ext_modules = [
    Pybind11Extension(
        "simdstring",
        [
            join("third-party", "SIMDString", "SIMDString.cpp"),
            "main.cpp",
        ],
    )
]

setup(
    name="simdstring",
    version="0.0.1",
    url="https://github.com/alpertunga-bile/simdstring_python",
    description="Python wrap for the SIMDString repository",
    include_dirs=[join("third-party", "SIMDString")],
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    python_requires=">=3.7",
)
