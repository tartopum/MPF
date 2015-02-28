import os
import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand

import mpf



# Test
class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)
        
# README
readme = ""

with open("README.md", "r") as f:
    readme = f.read()

# Packages
packages = [
    "mpf"
]

# Requirements
def strip_comments(l):
    return l.split("#", 1)[0].strip()

def reqs(*f):
    return list(filter(None, [strip_comments(l) for l in open(os.path.join(os.getcwd(), *f)).readlines()]))
    
requirements = reqs("requirements.txt")

test_requirements = reqs("requirements-dev.txt")
test_requirements = requirements + test_requirements[1:]


setup(
    name="mpf",
    version=mpf.__version__,
    description="",
    long_description=readme,
    author="Vayel",
    author_email="vincent.lefoulon@free.fr",
    url="https://github.com/Vayel/MPF",
    packages=packages,
    package_dir={"mpf": "mpf"},
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords="mpf",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4"
    ],
    cmdclass={"test": PyTest},
    tests_require=test_requirements
)
