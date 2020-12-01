pl-mgz2labels
================================

.. image:: https://travis-ci.org/FNNDSC/mgz2labels.svg?branch=master
    :target: https://travis-ci.org/FNNDSC/mgz2labels

.. image:: https://img.shields.io/badge/python-3.8%2B-blue.svg
    :target: https://github.com/FNNDSC/pl-mgz2labels/blob/master/setup.py

.. contents:: Table of Contents


Abstract
--------

MGZ label-wise converter


Description
-----------

``mgz2labels`` is a ChRIS-based application whose backbone is `pl-mgz_converter <https://github.com/FNNDSC/pl-mgz_converter>`_. The input file structure is the same as pl-mgz_converter. The output will be 193 labels for each subject in separated folder, and 193 .npy files for each label. The output of this plugin is set to be used for `pl-mricnn <https://github.com/FNNDSC/pl-mricnn>`_ training.


Usage
-----

Using Python3
~~~~~~~~~~~~

.. code::
    python3 mgz2labels/mgz2labels.py <inputDir> <outputDir>

Using ``docker run``
~~~~~~~~~~~~~~~~~~~

.. code:: bash
    docker build -t mgz2labels .

.. code:: bash

    docker run --rm -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing                              \
        mgz2labels mgz2labels.py                                    \
        /incoming /outgoing


Development
-----------

Build the Docker container:

.. code:: bash

    docker build -t mgz2labels .

.. code:: bash

    docker run --rm -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing                              \
        mgz2labels mgz2labels.py                                    \
        /incoming /outgoing

Examples
--------

.. code:: bash

    docker build -t mgz2labels .

.. code:: bash

    docker run --rm -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing                              \
        mgz2labels mgz2labels.py                                    \
        /incoming /outgoing


Trouble Shooting
--------
Try to remove all ``.DS_Store`` files in the input directory
