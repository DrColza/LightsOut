import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="lightsout",

    description="python version of the 1995 Handheld Game 'Lights out' produced by Tiger.",

    author="Colin Burgess",

    packages=find_packages(),

    package_dir={"src": "src"},

    version='0.1.0',
)
