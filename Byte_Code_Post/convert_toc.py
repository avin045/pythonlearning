from setuptools import setup
from Cython.Build import cythonize

setup(
    name='Conert to C',
    ext_modules=cythonize("main.pyx")
)

# py convert_toc.py build_ext --inplace
# nix-env -iA nixpkgs.patchelf
