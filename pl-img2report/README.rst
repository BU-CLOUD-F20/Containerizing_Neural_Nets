pl-img2report
================================

.. image:: https://travis-ci.org/FNNDSC/img2report.svg?branch=master
    :target: https://travis-ci.org/FNNDSC/img2report

.. image:: https://img.shields.io/badge/python-3.8%2B-blue.svg
    :target: https://github.com/FNNDSC/pl-img2report/blob/master/setup.py

.. contents:: Table of Contents


Abstract
--------

An app to generate brain volume text report.


Description
-----------

``img2report`` is a ChRIS-based application that convert brain PNG images to volume text report. It first convert image's pixel value to the real label id. And use FreeSurfer LUT to generate a text report in HTML format. This app is for docking the output of `pl-mriunet <https://github.com/TingyiZhang/pl-mriunet_ser>`_ (prediction images).


Usage
-----

.. code::

    python img2report.py
        [-h|--help]
        [--json] [--man] [--meta]
        [--savejson <DIR>]
        [-v|--verbosity <level>]
        [--version]
        <inputDir> <outputDir>


Arguments
~~~~~~~~~

Run
~~~

You need you need to specify input and output directories using the `-v` flag to `docker run`.


.. code:: bash

    docker build -t img2report .

.. code:: bash

    docker run --rm -ti -v $(pwd)/<intput dir>:/incoming -v $(pwd)/<output dir>:/outgoing                       \
        img2report img2report.py                                    \
        /incoming /outgoing

Development
-----------

Build the Docker container:

.. code:: bash

    docker build -t img2report .

Examples
--------

.. code:: bash

    docker run --rm -ti -v $(pwd)/<intput dir>:/incoming -v $(pwd)/<output dir>:/outgoing                       \
        img2report img2report.py                                    \
        /incoming /outgoing
