
import os
import numpy as np
from matplotlib import pyplot as plt
from skimage.io import imread


def load_images():
    img1 = imread('img')
    img2 = imread('img')
   
    return img1, img2

def create_heatmap(img1, img2):
    
    heat_map = np.zeros([256,256],dtype=np.uint8)
    for i in range(0,255):
        for j in range(0,255):
            heat_map[i][j] = abs(img2[i][j]-img1[i][j])
            
            
    fig= plt.figure(figsize=(14,16))
    plt.imshow(heat_map,cmap='hot')
    plt.show()

if __name__ == '__main__':
    img1, img2 = load_images()
    create_heatmap(img1, img2)