'''
Create a locally pip installable package for the src directory.
This is useful for testing and development purposes.
'''

from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
)
