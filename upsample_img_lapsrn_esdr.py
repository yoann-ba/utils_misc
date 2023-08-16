
import numpy as np
import matplotlib.pyplot as plt

import cv2
from cv2 import dnn_superres


#################################################################
#
# THIS CV2 NEEDS TO CALL opencv-contrib-python NOT opencv-python
#
# if confused about different opencv packages and modules opencv-python, opencv-contrib-python: 
# https://pypi.org/project/opencv-python/ read the part Installation > 3.
# https://stackoverflow.com/a/62460856 same explanation
# "pip uninstall package —yes"
#################################################################


#%% Paths, Model


# Upsample with a model, then finishes to (output_shape), then saves in output_folder
def upsample_img(img_name, model, output_shape, scaling_value, output_folder):
    
    img = cv2.imread(img_name, -1)
    (out_height, out_width) = output_shape
    
    # if img size allows it
    if img.shape[0] > out_height/scaling_value or img.shape[1] > out_width/scaling_value:
        print('warning original size big', 'img_name', img.shape)
    
    img = np.dstack([img, img, img]) # need 3 channels
    img = np.clip(img, -1, 1)
    img = (255*0.5 * (img + 1)).astype(np.uint8)
    
    # Upsampling
    result = model.upsample(img)
    result = result[:, :, 0]
    
    # resize to 500 x 500
    result = cv2.resize(result, (out_height, out_width), interpolation = cv2.INTER_CUBIC)
    
    # save
    cv2.imwrite(output_folder + '/' + 'img_name', result)
    
    return result # return unneeded if we batch process, can be useful for 


# Load model

LapSRN_path = 'LapSRN_x8.pb' # the 8x version weights, can be found in qista aei poc github / model, or my utils

scaling_value = 8

lapsrn = dnn_superres.DnnSuperResImpl_create()
lapsrn.readModel(LapSRN_path)
lapsrn.setModel("lapsrn", scaling_value)

# Image parameters
out_height = 500
out_width = 500

img_folder = 'img_folder'
output_folder = 'output_folder'

img_name = 'img_name.png'

# Run upsampling

result = upsample_img(img_folder + '/' + img_name, lapsrn, (out_height, out_width), scaling_value, output_folder)




# ESDR version

ESDR_path = 'EDSR_x3.pb'

esdr = dnn_superres.DnnSuperResImpl_create()

# Read the desired model
esdr.readModel(ESDR_path)
# Set the desired model and scale to get correct pre- and post-processing
esdr.setModel("edsr", 3)
















