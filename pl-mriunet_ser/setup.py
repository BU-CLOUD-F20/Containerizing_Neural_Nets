from os import path
from setuptools import setup

with open(path.join(path.dirname(path.abspath(__file__)), 'README.rst')) as f:
    readme = f.read()

setup(
    name             = 'mriunet_ser',
    version          = '0.1',
    description      = 'An app to ...',
    long_description = readme,
    author           = 'BU EC528 F20 Team',
    author_email     = 'dev@babyMRI.org',
    url              = 'http://wiki',
    packages         = ['mriunet_ser'],
    install_requires = ['chrisapp~=1.1.6'],
    test_suite       = 'nose.collector',
    tests_require    = ['nose'],
    license          = 'MIT',
    zip_safe         = False,
    python_requires  = '>=3.8',
    entry_points     = {
        'console_scripts': [
            'mriunet_ser = mriunet_ser.__main__:main'
            ]
        }
)
