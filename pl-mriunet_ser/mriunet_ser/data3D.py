from __future__ import print_function

import os
import glob
import numpy as np

from skimage.io import imread

data_path = 'in'

image_rows = int(256)
image_cols = int(256)
image_depth = 16


def load_train_data(options):
    """
    param: user input arguments
    return: `imgs_train` A numpy file, `imgs_mask_train_list` A list contains all labels' .npy file
    """
    imgs_train = np.load(os.path.join(options.inputdir, 'imgs_train.npy'))
    input_dir = os.listdir(options.inputdir)
    imgs_mask_train_list = [npy for npy in input_dir if npy.endswith('.npy') and npy != 'imgs_train.npy']
    return imgs_train, imgs_mask_train_list


def create_test_data(options):
    test_data_path = options.inputdir + '/test/'
    dirs = [test_data for test_data in os.listdir(test_data_path) if os.path.isdir(test_data_path + test_data)]
    print(dirs)
    total = int(len(dirs)) * 18
    print('TOTAL: ', total)

    imgs = np.ndarray((total, image_depth, image_rows, image_cols), dtype=np.uint8)

    i = 0
    j = 0
    print('-' * 30)
    print('Creating test images...')
    print('-' * 30)
    for dirr in sorted(os.listdir(test_data_path)):
        dirr = os.path.join(test_data_path, dirr)
        if not os.path.isdir(dirr):
            continue
        images = sorted(os.listdir(dirr))
        count = total
        for image_name in images:
            if not image_name.endswith('.png'):
                continue
            img = imread(os.path.join(dirr, image_name), as_gray=True)
            img = img.astype(np.uint8)
            img = np.array([img])

            if i < 17:
                imgs[i][j] = img

                j += 1

                if j % (image_depth - 1) == 0:
                    imgs[i][0] = img

                if j % image_depth == 0:
                    imgs[i][1] = img
                    j = 2
                    i += 1
                    if (i % 100) == 0:
                        print('Done: {0}/{1} test 3d images'.format(i, count))
    print('Loading done.')
    imgs = preprocess(imgs)
    np.save(options.inputdir + '/imgs_test.npy', imgs)
    print('Saving to .npy files done.')


def load_test_data(options):
    imgs_test = np.load(options.inputdir + '/imgs_test.npy')
    print('Size: ', imgs_test.shape)
    return imgs_test


def preprocess(imgs):
    imgs = np.expand_dims(imgs, axis=4)
    print(' ---------------- preprocessed -----------------')
    return imgs


def preprocess_squeeze(imgs):
    imgs = np.squeeze(imgs, axis=4)
    print(' ---------------- preprocessed squeezed -----------------')
    return imgs


if __name__ == '__main__':
    create_train_data()
    create_test_data()
