pl-heatmap
================================

.. image:: https://travis-ci.org/FNNDSC/heatmap.svg?branch=master
    :target: https://travis-ci.org/FNNDSC/heatmap

.. image:: https://img.shields.io/badge/python-3.8%2B-blue.svg
    :target: https://github.com/FNNDSC/pl-heatmap/blob/master/setup.py

.. contents:: Table of Contents


Abstract
--------

An app to examine the inference differences between voxel predictions and ground truth masks for low contrast images.


Description
-----------

``heatmap`` is a ChRIS-based application that displays the difference between training masks and inference labels for low contrast, grayscale images. The plugin    initiates a 256x256 numpy array of zeros and and changes each pixel value according the the absolute difference between the training mask and inference image.  The plugin takes a directory with two images (the training mask and inference image of the same voxel) as input, and an empty directory for output as arguments. 

Usage
-----

.. code::

    python heatmap.py
        [-h|--help]
        [--json] [--man] [--meta]
        [--savejson <DIR>]
        [-v|--verbosity <level>]
        [--version]
        <inputDir> <outputDir>


Arguments
~~~~~~~~~

.. code::

    [-h] [--help]
    If specified, show help message and exit.
    
    [--json]
    If specified, show json representation of app and exit.
    
    [--man]
    If specified, print (this) man page and exit.

    [--meta]
    If specified, print plugin meta data and exit.
    
    [--savejson <DIR>] 
    If specified, save json representation file to DIR and exit. 
    
    [-v <level>] [--verbosity <level>]
    Verbosity level for app. Not used currently.
    
    [--version]
    If specified, print version number and exit. 


Getting inline help is:

.. code:: bash

    docker run --rm fnndsc/pl-heatmap heatmap --man

Run
~~~

This ```plugin can be run two modes: natively as a python package or as a containerized docker image.

You need you need to specify input and output directories using the `-v` flag to `docker run`.


.. code:: bash

    docker run --rm -u $(id -u)                             \
        -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing      \
        fnndsc/pl-heatmap heatmap                        \
        /incoming /outgoing


Using Docker Run
----------------

Build the Docker container:

.. code:: bash

    docker build -t local/pl-heatmap .

To run using docker, be sure to assign an "input" directory to /incoming and an output directory to /outgoing. The input directory should have two images: a training mask and inference image of the same voxel. The output directory should be empty, make sure that the $(pwd)/out directory is world writable!

.. code:: bash

    mkdir in out && chmod 777 out
    docker run --rm -u $(id -u)                            \
        -v $(pwd)/in:/incoming -v $(pwd)/out/:/outgoing    \
        local/pl-heatmap heatmap.py                        \
        /incoming /outgoing


Examples
--------
.. code:: bash
    mkdir in out && chmod 777 out
    docker run --rm -u $(id -u)                            \
        -v $(pwd)/in:/incoming -v $(pwd)/out/:/outgoing    \
        local/pl-heatmap heatmap.py                        \
        /incoming /outgoing

.. image:: https://raw.githubusercontent.com/FNNDSC/cookiecutter-chrisapp/master/doc/assets/badge/light.png
    :target: https://chrisstore.co
