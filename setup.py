#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from glob import glob
from os.path import basename, splitext
from setuptools import setup, find_packages

setup(
    name='your_project',
    version='0.1.0',
    description='',
    author='',
    author_email='',
    license='',
    keywords='',
    url='',

    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    python_requires='>=3.8',
    include_package_data=True,
    install_requires=[
        'langchain>=0.0.330',
        'langchain_experimental>=0.0.37',
        'anthropic>=0.5.0',
        'playwright>=1.39.0',
        'beautifulsoup4>=4.12.2',
        'tiktoken>=0.5.1',
    ],
    extras_require={
        'test': [
            'pytest>=7.4.3',
        ],
    },
    setup_requires=[
        'pytest-runner',
    ],
    entry_points={
        'console_scripts': [
            'get_articles_on_topic = your_project.cli:get_articles_on_topic',
        ]
    },
)
