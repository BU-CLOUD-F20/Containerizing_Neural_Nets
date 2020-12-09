#!/usr/bin/env python                                            
#
# img2report ds ChRIS plugin app
#
# (c) 2016-2020 Fetal-Neonatal Neuroimaging & Developmental Science Center
#                   Boston Children's Hospital
#
#              http://childrenshospital.org/FNNDSC/
#                        dev@babyMRI.org
#


import os
import sys
import numpy as np
import collections
import re
import pandas as pd
import pickle
from skimage.io import imread
from yattag import Doc
sys.path.append(os.path.dirname(__file__))

from chrisapp.base import ChrisApp


Gstr_title = """

 _                  _____                           _   
(_)                / __  \                         | |  
 _ _ __ ___   __ _ `' / /'_ __ ___ _ __   ___  _ __| |_ 
| | '_ ` _ \ / _` |  / / | '__/ _ \ '_ \ / _ \| '__| __|
| | | | | | | (_| |./ /__| | |  __/ |_) | (_) | |  | |_ 
|_|_| |_| |_|\__, |\_____/_|  \___| .__/ \___/|_|   \__|
              __/ |               | |                   
             |___/                |_|                   

"""

Gstr_synopsis = """

(Edit this in-line help for app specifics. At a minimum, the 
flags below are supported -- in the case of DS apps, both
positional arguments <inputDir> and <outputDir>; for FS apps
only <outputDir> -- and similarly for <in> <out> directories
where necessary.)

    NAME

       img2report.py 

    SYNOPSIS

        python img2report.py                                         \\
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
                fnndsc/pl-img2report img2report                        \
                /incoming /outgoing

    DESCRIPTION

        `img2report.py` ...

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


class Img2report(ChrisApp):
    """
    An app to ...
    """
    AUTHORS                 = 'BU EC528 F20 Team <dev@babyMRI.org>'
    SELFPATH                = os.path.dirname(os.path.abspath(__file__))
    SELFEXEC                = os.path.basename(__file__)
    EXECSHELL               = 'python3'
    TITLE                   = 'A report generator for brain MRI images'
    CATEGORY                = ''
    TYPE                    = 'ds'
    DESCRIPTION             = 'An app to ...'
    DOCUMENTATION           = 'http://wiki'
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

        if not os.path.exists(options.outputdir):
            os.mkdir(options.outputdir)

        print('Convert images to numpy arrays...')
        self.convert_to_npy(options)
        print('Conversion finished.')

        npy_list = [npy for npy in os.listdir(options.outputdir + '/') if npy.endswith('.npy')]
        for npy in npy_list:
            npy_file = np.load(os.path.join(options.outputdir, npy))
            print(npy_file.shape)
            npy_file = npy_file.astype(np.uint32)

            data_list = npy_file.flatten()
            counter = collections.Counter(data_list)

            # Load Look Up file
            print("Loading look up file from FreeSurferColorLUT.txt")
            l_column_names = ["#No", "LabelName", "R", "G", "B"]
            df_FSColorLUT = pd.DataFrame(columns=l_column_names)
            with open('FreeSurferColorLUT.txt') as f:
                for line in f:
                    if line and line[0].isdigit():
                        line = re.sub(' +', ' ', line)
                        l_line = line.split(' ')
                        l_labels = l_line[:5]
                        df_FSColorLUT.loc[len(df_FSColorLUT)] = l_labels

            report_path = ("%s/%s.%s" % (options.outputdir, 'report_' + npy.split('.')[0], 'html'))

            # Write and Save report
            print("Writing report as %s" % report_path)
            f = open(report_path, 'a')
            f.truncate(0)
            report_columns = ['Index', 'Label Name', 'Volume (in cc)']
            rep = pd.DataFrame(columns=report_columns)
            line_count = 1

            # Create an HTML report
            doc, tag, text = Doc().tagtext()
            with tag('html'):
                with tag('head'):
                    with tag('link', rel='stylesheet',
                             href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css"):
                        with tag('style'):
                            text('body{margin:0 100; background:whitesmoke;}')
                with tag('body'):
                    with tag('h1'):
                        text('Brain Segmentation Report')
                    with tag('table', id='main', klass='table table-striped table-hover', text='report'):
                        with tag('thead', klass='thead-dark'):
                            with tag('tr'):
                                with tag('th', scope='col'):
                                    text('Index')
                                with tag('th', scope='col'):
                                    text('Label Name')
                                with tag('th', scope='col'):
                                    text('Volume (in cc)')
                        for k in sorted(counter.keys()):
                            res_df = df_FSColorLUT.loc[df_FSColorLUT['#No'] == str(k), ['LabelName']]

                            with tag('tr'):
                                with tag('td'):
                                    text(line_count)
                                with tag('td'):
                                    text(res_df['LabelName'].to_string(index=False))
                                with tag('td'):
                                    text(round(counter[k] / 1000, 1))
                            line_count = line_count + 1
            result = doc.getvalue()
            f.write(result)

            f = open(report_path, 'r')
            print(f.read())
            print("Reports saved")

    def convert_to_npy(self, options):
        input_dir = options.inputdir
        input_list = [subject for subject in os.listdir(input_dir) if os.path.isdir(os.path.join(input_dir, subject))]
        total = len(input_list) * 256
        count = 0
        for subject in input_list:
            result = []
            img_dir = input_dir + '/' + subject + '/'
            img_list = sorted(os.listdir(img_dir))
            pixel = pickle.load(open('pixel_LUT', 'rb'))
            for img in img_list:
                img_npy = imread(img_dir + img).astype(np.uint16)
                for i in range(0, 255):
                    for j in range(0, 255):
                        if img_npy[i, j] in pixel.keys():
                            img_npy[i, j] = pixel[img_npy[i, j]]
                count += 1
                print("{0}/{1}".format(count, total), end='\r')
                result.append(img_npy)
            result = np.array(result)
            result = np.transpose(result, (1, 2, 0))
            np.save(options.outputdir + '/' + subject + '.npy', result)

    def show_man_page(self):
        """
        Print the app's man page.
        """
        print(Gstr_synopsis)


if __name__ == "__main__":
    chris_app = Img2report()
    chris_app.launch()
