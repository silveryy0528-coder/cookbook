'''
Create a locally pip installable package for the src directory.
This is useful for testing and development purposes.
'''

from setuptools import find_packages, setup

VERSION = "0.0.0"

setup(
    name='src',
    version=VERSION,
    packages=find_packages(),
    url="https://github.com/silveryy0528-coder/cookbook",
    author="Yan Guo"
)
