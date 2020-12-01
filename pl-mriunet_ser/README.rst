pl-mriunet_ser
================================

.. image:: https://travis-ci.org/FNNDSC/mriunet_ser.svg?branch=master
    :target: https://travis-ci.org/FNNDSC/mriunet_ser

.. image:: https://img.shields.io/badge/python-3.8%2B-blue.svg
    :target: https://github.com/FNNDSC/pl-mriunet_ser/blob/master/setup.py

.. contents:: Table of Contents


Abstract
--------

An automation tool for taining and inference of 3D U-Net.


Description
-----------

``mriunet_ser`` (ser for serial) is a ChRIS-based application that trains and inferences multiple subjects using 3D U-Net (`pl-mricnn <https://github.com/FNNDSC/pl-mricnn>`_) in a sequential order. It is designed for docking the output of `pl-mgz2labels <https://github.com/TingyiZhang/pl-mgz2labels>`_ and saving time of the tedious, repetitive process of training and inference using brain MRI label-wise data.


Usage
-----

.. code::

    python mriunet_ser.py
        [--version]
        [--mode]
        [--epochs]
        <inputDir> <outputDir>


Arguments
~~~~~~~~~

.. code::
    
    [--man]
    If specified, print (this) man page and exit.
    
    [--version]
    If specified, print version number and exit.

    [--mode]
    (Required) 1: Training, 2: Prediction
    
    [--epochs]
    (Optional) Default epoch number is 5


Run
---

Using Python3
~~~~~~~~~~
Mode 1 (training):

.. code:: bash

    Python3 pl-mriunet_ser/mriunet_ser.py --mode 1 --epochs <epoch number> <input dir> <output dir>

Mode 2 (predict):

.. code:: bash

    Python3 pl-mriunet_ser/mriunet_ser.py --mode 2 <input dir> <output dir>


Using ``docker run``
~~~~~~~~~~~~~~~~~~~
First, you need to build a docker image.

.. code:: bash

    docker build -t mriunet_ser .

Mode 1 (training):

.. code:: bash

    docker run --rm                             \
        -v $(pwd)/<input dir>:/incoming -v $(pwd)/<output dir>:/outgoing      \
        mriunet_ser mriunet_ser.py                        \
        --mode 1                        \
        --epochs <epoch number>                        \
        /incoming /outgoing

Mode 2 (predict):

.. code:: bash

    docker run --rm                            \
        -v $(pwd)/<input dir>:/incoming -v $(pwd)/<output dir>:/outgoing      \
        mriunet_ser mriunet_ser.py                        \
        --mode 2                        \
        /incoming /outgoing

Development
-----------

You can fork or clone this repo and change the code in mriunet_ser.py. Then build a local Docker image using:

.. code:: bash

    docker build -t local/pl-mriunet_ser .

Or push to your Docker Hub.

Examples
--------
``docker run`` is recommended.

.. code:: bash

    docker build -t mriunet_ser .

Mode 1 (training):

.. code:: bash

    docker run --rm                             \
        -v $(pwd)/<input dir>:/incoming -v $(pwd)/<output dir>:/outgoing      \
        mriunet_ser mriunet_ser.py                        \
        --mode 1                        \
        --epochs <epoch number>                        \
        /incoming /outgoing

Mode 2 (predict):

.. code:: bash

    docker run --rm                             \
        -v $(pwd)/<input dir>:/incoming -v $(pwd)/<output dir>:/outgoing      \
        mriunet_ser mriunet_ser.py                        \
        --mode 2                        \
        /incoming /outgoing


Trouble shooting
----------------
1. Make sure that the *output directory* is world writable. You can do it by ```chmod 777 <output dir>```.

2. Try to remove the ``.DS_store`` file in the input directory.
