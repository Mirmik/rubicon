#!/usr/bin/env python3

from wheel.bdist_wheel import bdist_wheel as bdist_wheel_
from setuptools import setup, Extension, Command
from distutils.util import get_platform

import glob
import sys
import os

directory = os.path.dirname(__file__)

setup(
    name="rubicon",
    packages=["rubicon"],
    version="0.0.1",
    license="MIT",
    description="Terminal",
    author="mirmik",
    author_email="netricks@protonmail.ru",
    url="https://github.com/mirmik/rubicon",
    long_description=open(os.path.join(directory, "README.md"), "r").read(),
    long_description_content_type="text/markdown",
    keywords=["testing", "terminal"],
    classifiers=[],
    package_data={},
    include_package_data=True,
    entry_points={"console_scripts": ["rubicon=rubicon.__main__:main"]},
)
