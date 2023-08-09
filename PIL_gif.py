


#%% imports

import numpy as np
from PIL import Image, ImageSequence


#%% reading and writing gif

path = ""
pil_image = Image.open(path)

pil_frames = [np.array(frame, dtype = np.uint8) for frame in ImageSequence.Iterator(pil_image)]#[1:]
# first was one channel for some reason

gif_processed = [run_algo(frame) for frame in pil_frames]
gif_processed = [Image.fromarray(frame) for frame in gif_processed]

gif_processed[0].save("test.gif", loop=0, duration=100, 
                      save_all=True, append_images=gif_processed[1:], 
                      minimize_size = True)
# loop 0 for infinite loop
# duration in ms per frame


#%% writing np array to gif

gif_frames = np.array()

gif_processed = [Image.fromarray(frame) for frame in gif_frames]

fps = 15
gif_processed[0].save("test.gif", loop=0, duration=int(1000/fps),
                      save_all=True, append_images=gif_processed[1:],
                      minimize_size = True)