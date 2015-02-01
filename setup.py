import os
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

import mpf



class Tox(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
        
    def run_tests(self):
        # Import here, cause outside the eggs aren't loaded
        import tox
        errcode = tox.cmdline(self.test_args)
        sys.exit(errcode)
 
def strip_comments(l):
    return l.split('#', 1)[0].strip()

def reqs(*f):
    return list(filter(None, [strip_comments(l) for l in open(os.path.join(os.getcwd(), *f)).readlines()]))


install_requires = reqs("requirements.txt")

packages = ["mpf"]

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
    classifiers=classifiers,
    install_requires=install_requires,
    include_package_data=True
)
