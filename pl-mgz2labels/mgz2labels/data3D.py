from __future__ import print_function

import os
import numpy as np
from skimage.io import imread

image_rows = int(256)
image_cols = int(256)
image_depth = 16


def create_train_data(options, labels):
    train_data_path = options.outputdir+"/train/"
    mask_data_path = options.outputdir+'/masks/'
    dirs = os.listdir(train_data_path)
    total = int(len(dirs)*16*2)

    imgs = np.ndarray((total, image_depth, image_rows, image_cols), dtype=np.uint8)
    imgs_mask = np.ndarray((total, image_depth, image_rows, image_cols), dtype=np.uint8)

    imgs_temp = np.ndarray((total, image_depth//2, image_rows, image_cols), dtype=np.uint8)
    imgs_mask_temp = np.ndarray((total, image_depth//2, image_rows, image_cols), dtype=np.uint8)

    i = 0
    print('-'*30)
    print('Creating training images...')
    print('-'*30)
    for dirr in sorted(os.listdir(train_data_path)):
        j = 0
        dirr = train_data_path+"/"+dirr
        if not os.path.isdir(dirr):
            continue
        images = sorted(os.listdir(dirr))
        count = total
        for image_name in images:
            if not image_name.endswith('.png'):
                print('Ignored invalid file: ', image_name)
                continue
            img = imread(os.path.join(dirr, image_name), as_gray=True)
            img = img.astype(np.uint8)
            img = np.array([img])
            imgs_temp[i, j] = img
            j += 1
            if j % (image_depth/2) == 0:
                j = 0
                i += 1
                print('Done: {0}/{1} 3d images'.format(i, count), end='\r')

    for x in range(0, imgs_temp.shape[0]-1):
        imgs[x] = np.append(imgs_temp[x], imgs_temp[x+1], axis=0)

    print('Loading of train data done.')
    imgs = preprocess(imgs)
    np.save(options.outputdir+'/imgs_train.npy', imgs)
    print('Training NPY saved at: ' + options.outputdir + '/imgs_train.npy')

    print('-' * 30)
    print('Creating labeled images...')
    print('-' * 30)

    for label in labels:
        create_mask_data(options, label)
    print('Loading all labels done.')

    # Convert the whole volume to .npy
    print('Processing the whole mask...')
    i = 0
    for dirr in sorted(os.listdir(train_data_path)):
        j = 0
        dirr = mask_data_path + dirr + '/whole'
        if not os.path.exists(dirr):
            return
        images = sorted(file for file in os.listdir(dirr) if file.endswith('.png'))
        count = total
        for mask_name in images:
            img_mask = imread(dirr + '/' + mask_name, as_gray=True)
            img_mask = img_mask.astype(np.uint16)
            img_mask = np.array([img_mask])
            imgs_mask_temp[i, j] = img_mask

            j += 1
            if j % (image_depth / 2) == 0:
                j = 0
                i += 1
                print('Done: {0}/{1} 3d images'.format(i, count), end='\r')

    for x in range(0, imgs_mask_temp.shape[0] - 1):
        imgs_mask[x] = np.append(imgs_mask_temp[x], imgs_mask_temp[x + 1], axis=0)

    imgs_mask = preprocess(imgs_mask)
    np.save(options.outputdir + '/imgs_mask_train.npy', imgs_mask)
    print('Saving to .npy files: done.')


def create_mask_data(options, label):
    train_data_path = options.outputdir+"/train/"
    mask_data_path = options.outputdir+'/masks/'
    dirs = os.listdir(train_data_path)
    total = int(len(dirs)*16*2)

    imgs_mask = np.ndarray((total, image_depth, image_rows, image_cols), dtype=np.uint8)
    imgs_mask_temp = np.ndarray((total, image_depth//2, image_rows, image_cols), dtype=np.uint8)

    i = 0
    print('-' * 30)
    print('Processing label ' + str(label))
    for dirr in sorted(os.listdir(train_data_path)):
        if not os.path.isdir(train_data_path + dirr):
            continue
        j = 0
        dirr = mask_data_path + dirr + '/label-' + "{:0>5}".format(str(label))

        # Label did not exist
        if not os.path.exists(dirr):
            return
        images = sorted(file for file in os.listdir(dirr) if file.endswith('.png'))
        count = total
        for mask_name in images:
            img_mask = imread(dirr + '/' + mask_name, as_gray=True)
            img_mask = img_mask.astype(np.uint16)
            img_mask = np.array([img_mask])
            imgs_mask_temp[i, j] = img_mask

            j += 1
            if j % (image_depth / 2) == 0:
                j = 0
                i += 1
                print('Done: {0}/{1} 3d images'.format(i, count), end='\r')

    for x in range(0, imgs_mask_temp.shape[0] - 1):
        imgs_mask[x] = np.append(imgs_mask_temp[x], imgs_mask_temp[x + 1], axis=0)

    imgs_mask = preprocess(imgs_mask)
    np.save(options.outputdir + '/label-' + "{:0>5}".format(str(label)) + '_mask_train.npy', imgs_mask)
    print('Size of .npy file: ' + str(imgs_mask.shape))
    print('NPY for label ' + "{:0>5}".format(str(label)) + ' saved.')


def preprocess(imgs):
    imgs = np.expand_dims(imgs, axis=4)
    return imgs


def preprocess_squeeze(imgs):
    imgs = np.squeeze(imgs, axis=4)
    return imgs


if __name__ == '__main__':
    create_train_data()
