#!/usr/bin/env python
# -*- coding:utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="leetool",
    version="0.1.0",
    packages=find_packages(),
    zip_safe=False,
    scripts=["script/test_printer.py"],
    description="tool for lijiancai",
    long_description="tool for lijiancai",
    author="lijiancai",
    author_email="958000432@qq.com",
    license="GPL",
    keywords=("test", "egg"),
    platforms="Independant",
    entry_points = {"console_scripts":["singer = app.singer:main"]},
    url="",
)