#!/usr/bin/env python
from setuptools import setup, find_packages

# read the dependencies from requirements.txt
with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

setup(
    name='jadwal-shalat-kemenag',
    version='0.1.0',
    url='',
    author='The Suhu',
    author_email='thesuhu@protonmail.com',
    description='Jadwal shalat untuk wilayah Indonesia berdasarkan data dari website https://bimasislam.kemenag.go.id/jadwalshalat',
    packages=find_packages(),
    install_requires=requirements,
)
