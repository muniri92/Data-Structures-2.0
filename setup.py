# coding=utf-8
from setuptools import setup

setup(
    name="Binary Search Tree",
    description="Python 401 Binary Search Tree",
    version=0.1,
    author=["Nadia Bahrami", "Munir Ibrahim"],
    author_email=["nadia.bahrami@gmail.com"],
    license="MIT",
    py_modules=["bst"],
    package_dir={"": "src"},
    install_requires=[],
    extras_require={"test": ["pytest", "pytest-xdist", "tox"]},
)
