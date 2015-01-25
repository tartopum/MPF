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
 


packages = [
    "mpf",
    "mpf.models",
    "mpf.processors",
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
    classifiers=classifiers,
    tests_require=['tox'],
    cmdclass = {'test': Tox}
)
