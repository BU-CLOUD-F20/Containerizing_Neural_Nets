from os import path
from setuptools import setup

with open(path.join(path.dirname(path.abspath(__file__)), 'README.rst')) as f:
    readme = f.read()

setup(
    name             = 'heatmap',
    version          = '0.1',
    description      = 'An app to examine the inference differences between predictions and ground truth masks for low contrast images',
    long_description = readme,
    author           = 'Ken Krebs',
    author_email     = 'kenkrebs@bu.edu',
    url              = 'heatmap',
    packages         = ['heatmap'],
    install_requires = ['chrisapp~=1.1.6', 'numpy'],
    test_suite       = 'nose.collector',
    tests_require    = ['nose'],
    license          = 'MIT',
    zip_safe         = False,
    python_requires  = '>=3.8',
    scripts          = ['heatmap/heatmap.py'])
     

