from os import path
from setuptools import setup

with open(path.join(path.dirname(path.abspath(__file__)), 'README.rst')) as f:
    readme = f.read()

setup(
    name             = 'mgz2labels',
    version          = '0.1',
    description      = 'MGZ label-wise converter',
    long_description = readme,
    author           = 'tingyizhang',
    author_email     = 'tingyi97@gmail.com',
    url              = 'http://wiki',
    packages         = ['mgz2labels'],
    install_requires = ['chrisapp~=1.1.6'],
    test_suite       = 'nose.collector',
    tests_require    = ['nose'],
    license          = 'MIT',
    zip_safe         = False,
    python_requires  = '>=3.8',
    entry_points     = {
        'console_scripts': [
            'mgz2labels = mgz2labels.__main__:main'
            ]
        }
)
