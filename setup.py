#!/usr/bin/env python
from setuptools import setup, find_packages

# long desc
with open("README.md", "r") as des:
    l_desc = des.read()

# read the dependencies from requirements.txt
with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

setup(
    name='jadwal-shalat-kemenag',
    version='0.1.1',
    url='https://github.com/thesuhu/jadwal-shalat-kemenag',
    author='The Suhu',
    author_email='thesuhu@protonmail.com',
    description='Jadwal shalat untuk wilayah Indonesia berdasarkan data dari website https://bimasislam.kemenag.go.id/jadwalshalat',
    long_description=l_desc,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=requirements,
)
