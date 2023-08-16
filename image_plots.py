


import numpy as np
import matplotlib.pyplot as plt



# check your screen dpi
# https://www.infobyip.com/detectmonitordpi.php
screen_dpi = 96


#
# no frame, no white border
# should be exact size as input, with one pixel per pixel preserved
# > at least without titles, w/ title might be different shape
def show_img(img, title = ''):

    size = (img.shape[0]/screen_dpi, img.shape[1]/screen_dpi)
    fig = plt.figure(figsize = size, dpi = screen_dpi, frameon = False)

    plt.imshow(img)

    if title:
        plt.title(title)
    plt.axis('off')
    plt.tight_layout()

    plt.show()

    return


#
# see https://stackoverflow.com/a/56900830 for colorbar size
def show_img_gray(img, title = '', cmap = 'viridis'):

    size = (img.shape[0]/screen_dpi, img.shape[1]/screen_dpi)
    fig = plt.figure(figsize = size, dpi = screen_dpi)
    ax = plt.axes()

    imshow_ref = ax.imshow(img, cmap = cmap)

    if title:
        plt.title(title)
    plt.axis('off')
    cax = fig.add_axes([ax.get_position().x1+0.01,ax.get_position().y0,0.02,ax.get_position().height])
    plt.colorbar(imshow_ref, cax = cax)

    plt.show()

    return