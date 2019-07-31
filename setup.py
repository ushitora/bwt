from setuptools import setup, find_packages

setup(
    name='bwt',
    version='0.0.1',
    description='Package for burrows-wheeler transform',
    author='Ryu Wakimoto',
    install_requires=[],
    url='https://github.com/ushitora/bwt',
    packages=find_packages(exclude=('tests', 'docs')),
    test_suite='tests'
)