

import numpy as np
import matplotlib.pyplot as plt




# Sort of "Channel-ize" variables into an image
# goes from (n_vars, image_height, image_width)
# to (image_height, image_width, n_vars)
# in keras terms, switch from 'channels first' to 'channels last'
def cursed_channel_swap(var_img_list, n_var = 2, img_h = 500, img_w = 500):
    
    var_img_list = np.array(var_img_list) # np in case of python list
    #  v needed bc following fortran format trick works only on lists v
    var_img_list = var_img_list.reshape((n_var, img_h*img_w)) # flatten each image per variable
    var_img_list = var_img_list.ravel('F') # prioritises vars/columns
    var_img_list = var_img_list.reshape((img_h, img_w, n_var)) # rebuild
    
    return var_img_list




# demo 


img = np.random.randint(0, 2, (3, 10, 10))
test = cursed_channel_swap(img, 3, 10, 10)

print('img shape', img.shape)
print('test shape', test.shape)
plt.imshow(test*255)
plt.show()




