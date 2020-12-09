#!/usr/bin/env python                                            
#
# mgz2labels ds ChRIS plugin app
#
# (c) 2016-2020 Fetal-Neonatal Neuroimaging & Developmental Science Center
#                   Boston Children's Hospital
#
#              http://childrenshospital.org/FNNDSC/
#                        dev@babyMRI.org
#

import os
import shutil
import sys

import imageio
import nibabel as nib
import numpy as np
import pickle
from data3D import create_train_data
from tqdm import tqdm

sys.path.append(os.path.dirname(__file__))

# import the Chris app superclass
from chrisapp.base import ChrisApp


Gstr_title = """
                      _____  _       _          _     
                     / __  \| |     | |        | |    
 _ __ ___   __ _ ____`' / /'| | __ _| |__   ___| |___ 
| '_ ` _ \ / _` |_  /  / /  | |/ _` | '_ \ / _ \ / __|
| | | | | | (_| |/ / ./ /___| | (_| | |_) |  __/ \__ \
|_| |_| |_|\__, /___|\_____/|_|\__,_|_.__/ \___|_|___/
            __/ |                                     
           |___/  
"""

Gstr_synopsis = """

(Edit this in-line help for app specifics. At a minimum, the 
flags below are supported -- in the case of DS apps, both
positional arguments <inputDir> and <outputDir>; for FS apps
only <outputDir> -- and similarly for <in> <out> directories
where necessary.)

    NAME

       mgz2labels.py 

    SYNOPSIS

        python mgz2labels.py                                         \\
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
                fnndsc/pl-mgz2labels mgz2labels                        \
                /incoming /outgoing

    DESCRIPTION

        `mgz2labels.py` ...

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

# A set containing all of the unique labels
LUT = pickle.load(open('label_LUT', 'rb'))
LABEL_SET = {0}

class Mgz2labels(ChrisApp):
    """
    MGZ label-wise converter
    """
    AUTHORS                 = 'Tingyi Zhang <tingyi97@bu.edu>'
    SELFPATH                = os.path.dirname(os.path.abspath(__file__))
    SELFEXEC                = os.path.basename(__file__)
    EXECSHELL               = 'python3'
    TITLE                   = 'MGZ2LABELS'
    CATEGORY                = ''
    TYPE                    = 'ds'
    DESCRIPTION             = 'MGZ label-wise converter'
    DOCUMENTATION           = 'http://wiki'
    VERSION                 = '0.1'
    ICON                    = ''  # url of an icon image
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

        try:
            os.mkdir(options.outputdir + "/train")
            os.mkdir(options.outputdir + "/masks")

        except OSError:
            print("Output folders already exist")

        print(Gstr_title)

        if not os.path.exists(options.outputdir):
            os.mkdir(options.outputdir)

        # Slice the .mgz file to 256 .png files
        # Preprocess the .png files to create  a giant .npy file for training
        self.convert_to_jpeg(options)
        self.preprocess(options, LABEL_SET)
        print('Finished.')

    """
    Prepare PNG files for training by converting them
    into .npy files
    """
    def preprocess(self, options, labels):
        create_train_data(options, labels)
        
    # convert label ranges from 0-255
    def convert_key(self, dictionary, data):
        for i in range(0, 255):
            for j in range(0, 255):
                data[i][j] = list(dictionary.keys())[list(dictionary.values()).index(data[i][j])]
        return data

    def convert_nifti_to_png(self, new_image, output_name):
        # converting nifti to .png

        # get all the labels present
        labels = np.unique(new_image.astype(np.uint16))
        LABEL_SET.update(labels)

        # Input data is the ground truth
        if "mask" in output_name:
            num_of_labels = len(LUT)
            count = 1
            for label in labels:
                print("Processing labels: {0}/{1}".format(count, num_of_labels), end='\r')
                count += 1
                
                copy_image = np.copy(new_image)
            
                # Marking one label
                copy_image[copy_image != label] = 0
                copy_image[copy_image == label] = 255
            
                self.write_to_file(copy_image, output_name + '/label-' + "{:0>5}".format(str(label)))
            print('Processing labels done.')

            print("Processing the whole mask...", end='\r')
            for label in labels:
                new_image[new_image == label] = LUT[label]
            self.write_to_file(new_image, output_name + '/whole')
            print("Processing the whole mask done.")
            return

        # Input data is the train data
        self.write_to_file(new_image, output_name)

    def write_to_file(self, new_image, output_name):
        outputfile = output_name
        inputfile = 'input'
        ask_rotate_num = 90
        ask_rotate = 'n'
        total_slices = new_image.shape[2]

        if not os.path.exists(outputfile):
            os.makedirs(outputfile)

        slice_counter = 0
        # iterate through slices
        for current_slice in range(0, total_slices):
            # alternate slices
            if (slice_counter % 1) == 0:
                # rotate or no rotate
                if ask_rotate.lower() == 'y':
                    if ask_rotate_num == 90 or ask_rotate_num == 180 or ask_rotate_num == 270:
                        if ask_rotate_num == 90:
                            data = np.rot90(new_image[:, :, current_slice])
                        elif ask_rotate_num == 180:
                            data = np.rot90(np.rot90(new_image[:, :, current_slice]))
                        elif ask_rotate_num == 270:
                            data = np.rot90(np.rot90(np.rot90(new_image[:, :, current_slice])))
                elif ask_rotate.lower() == 'n':
                    data = new_image[:, :, current_slice]

                # prevents lossy conversion
                data = data.astype(np.uint16)

                # alternate slices and save as png
                if (slice_counter % 1) == 0:
                    image_name = output_name + "_" + "{:0>3}".format(str(current_slice + 1)) + ".png"
                    imageio.imwrite(image_name, data.astype(np.uint16))

                    # move images to folder
                    src = image_name
                    shutil.copy(src, outputfile)
                    os.remove(src)
                    slice_counter += 1

    def convert_to_jpeg(self, options):
        path = options.inputdir
        dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
        for i in tqdm(dirs):
            # converting mgz to numpy
            img = nib.load(options.inputdir + "/" + i + "/brain.mgz")
            img1 = nib.load(options.inputdir + "/" + i + "/aparc.a2009s+aseg.mgz")
            X_numpy = img.get_fdata()
            y_numpy = img1.get_fdata()

            print('=' * 30)
            print('Processing subject: ' + i)
            # converting nifti to png
            print('Creating train images...', end='\r')
            self.convert_nifti_to_png(X_numpy, options.outputdir + "/train/" + i)
            print('Creating train images done.')

            print('Creating mask images...')
            self.convert_nifti_to_png(y_numpy, options.outputdir + "/masks/" + i)
            print('Processing subject: ' + i + ' done.')
            print('=' * 30)

    def show_man_page(self):
        """
        Print the app's man page.
        """
        print(Gstr_synopsis)


if __name__ == "__main__":
    chris_app = Mgz2labels()
    chris_app.launch()
