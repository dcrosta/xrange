from distribute_setup import use_setuptools
use_setuptools()

from setuptools import setup

setup(
    name='xrange.py',
    version='1.0',
    author='Dan Crosta',
    author_email='dcrosta@late.am',
    url='http://pypi.python.org/pypi/xrange.py',
    license='BSD',
    py_modules=['xrange'],

    setup_requires=['nose'],
    tests_require=['coverage'],
    test_suite='test_xrange',
)
