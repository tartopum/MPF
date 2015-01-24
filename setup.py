from setuptools import setup, find_packages

import mpf
 


packages = [
    "mpf",
    "mpf.models",
    "mpf.processors",
    "mpf.utils",
    "mpf.views",
    "mpf.workers"
]

classifiers = [
    "Programming Language :: Python"
]

setup(
    name="mpf",
    version=mpf.__version__,
    packages=packages,
    author="Vayel",
    description="",
    long_description="",
    license="MIT",
    classifiers=classifiers
)
