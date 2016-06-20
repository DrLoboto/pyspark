from setuptools import setup, find_packages


setup(name='pyspark',
    version='1.6.1.1',
    author='Apache Software Foundation',
    license='Apache License 2.0',
    description='PySpark python package',
    long_description='Library provides high-level APIs in Python and an optimized engine that supports general computation graphs for data analysis.',
    install_requires=[
        'py4j==0.9'
    ],
    packages=find_packages())
