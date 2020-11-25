#!/usr/bin/env python                                            
#
# heatmap ds ChRIS plugin app
#
# (c) 2016-2020 Fetal-Neonatal Neuroimaging & Developmental Science Center
#                   Boston Children's Hospital
#
#              http://childrenshospital.org/FNNDSC/
#                        dev@babyMRI.org
#



import os
# import importlib.metadata
import numpy as np
from matplotlib import pyplot as plt
from skimage.io import imread
from chrisapp.base import ChrisApp


Gstr_title = """

 _                _                         
| |              | |                        
| |__   ___  __ _| |_ _ __ ___   __ _ _ __  
| '_ \ / _ \/ _` | __| '_ ` _ \ / _` | '_ \ 
| | | |  __/ (_| | |_| | | | | | (_| | |_) |
|_| |_|\___|\__,_|\__|_| |_| |_|\__,_| .__/ 
                                     | |    
                                     |_|    
"""

Gstr_synopsis = """

(Edit this in-line help for app specifics. At a minimum, the 
flags below are supported -- in the case of DS apps, both
positional arguments <inputDir> and <outputDir>; for FS apps
only <outputDir> -- and similarly for <in> <out> directories
where necessary.)

    NAME

       heatmap.py 

    SYNOPSIS

        python heatmap.py                                         \\
            [-h] [--help]                                               \\
            [--json]                                                    \\
            [--man]                                                     \\
            [--meta]                                                    \\
            [--savejson <DIR>]                                          \\
            [-v <level>] [--verbosity <level>]                          \\
            [--version]                                                 \\
            <inputDir>                                                  \\
            <outputDir> 

    BRIEF EXAMPLE

        * Bare bones execution

            docker run --rm -u $(id -u)                             \
                -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing      \
                fnndsc/pl-heatmap heatmap                        \
                /incoming /outgoing

    DESCRIPTION

        `heatmap.py` ...

    ARGS

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
"""


class Heatmap(ChrisApp):
    """
    An app to examine the inference differences between predictions and ground truth masks for low contrast images
    """
    AUTHORS                 = 'Ken Krebs <kenkrebs@bu.edu>'
    SELFPATH                = '/usr/local/bin'
    SELFEXEC                = 'heatmap'
    EXECSHELL               = 'python'
    TITLE                   = 'A ChRIS plugin app'
    CATEGORY                = ''
    TYPE                    = 'ds'
    DESCRIPTION             = 'An app to examine the inference differences between predictions and ground truth masks for low contrast images'
    DOCUMENTATION           = 'heatmap'
    VERSION                 = '0.1'
    ICON                    = '' # url of an icon image
    LICENSE                 = 'Opensource (MIT)'
    MAX_NUMBER_OF_WORKERS   = 1  # Override with integer value
    MIN_NUMBER_OF_WORKERS   = 1  # Override with integer value
    MAX_CPU_LIMIT           = '' # Override with millicore value as string, e.g. '2000m'
    MIN_CPU_LIMIT           = '' # Override with millicore value as string, e.g. '2000m'
    MAX_MEMORY_LIMIT        = '' # Override with string, e.g. '1Gi', '2000Mi'
    MIN_MEMORY_LIMIT        = '' # Override with string, e.g. '1Gi', '2000Mi'
    MIN_GPU_LIMIT           = 0  # Override with the minimum number of GPUs, as an integer, for your plugin
    MAX_GPU_LIMIT           = 0  # Override with the maximum number of GPUs, as an integer, for your plugin

    # Use this dictionary structure to provide key-value output descriptive information
    # that may be useful for the next downstream plugin. For example:
    #
    # {
    #   "finalOutputFile":  "final/file.out",
    #   "viewer":           "genericTextViewer",
    # }
    #
    # The above dictionary is saved when plugin is called with a ``--saveoutputmeta``
    # flag. Note also that all file paths are relative to the system specified
    # output directory.
    OUTPUT_META_DICT = {}

    def define_parameters(self):
        """
        Define the CLI arguments accepted by this plugin app.
        Use self.add_argument to specify a new app argument.
        """

    def run(self, options):
        """
        Define the code to be run by this plugin app.
        """
        
        print(Gstr_title)
        print('Version: %s' % self.get_version())
        self.load_images(options)

    def show_man_page(self):
        """
        Print the app's man page.
        """
        print(Gstr_synopsis)

    def load_images(self, options):
        img = []
        for filename in os.listdir(options.inputdir):
            img.append(options.inputdir +'/' +filename)
            
        img1 = imread(img[0]).astype(np.uint8)
        img2 = imread(img[1]).astype(np.uint8)
        
        self.create_heatmap(options, img1, img2)

    def create_heatmap(self, options, img1, img2):
        heat_map = np.zeros([256,256],dtype=np.uint16)
        for i in range(0,255):
            for j in range(0,255):
                heat_map[i][j] = abs(img2[i][j]-img1[i][j])
                
            
            
        fig = plt.figure(figsize=(14,16))
        plt.imshow(heat_map,cmap='hot')
        outputfile = options.outputdir + '/' + 'heat_map.png'
        plt.savefig(outputfile)

# ENTRYPOINT
if __name__ == "__main__":
    chris_app = Heatmap()
    chris_app.launch()