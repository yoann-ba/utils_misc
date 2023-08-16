


#%% imports

import numpy as np
import matplotlib.pyplot as plt

import plotly.graph_objects as go
from plotly.subplots import make_subplots

import earthpy.spatial as es # for hillshade map

#%% functions

# 2d plot with 1 pixel per value
# can be either a raw imshow or imshow + a hillshade map
def plot_2d(img, title = '', vmin = None, vmax = None, cmap = 'gray',
            size_scaler = 1, mode = 'heightmap'):

  px = 1/plt.rcParams['figure.dpi']  # pixel in inches

  figure_size = (img.shape[0]*px*size_scaler, img.shape[1]*px*size_scaler)
  plt.figure(figsize = figure_size)

  plt.imshow(img, vmin = vmin, vmax = vmax, cmap = cmap)

  if mode == 'hillshade':
    hill = es.hillshade(img*500, azimuth = 30, altitude = 30)
    plt.imshow(hill, cmap = "Greys_r", alpha = 0.5)
  plt.title(title)
  plt.show()

  return


# 3d plot with rotations
# to use in a colab notebook or other similar environment
# (needs some IPython stuff maybe?)
def plot_3d_plotly(img, title = '', size_scaler = 1, height = 1):

  Z = np.copy(img)

  Z[0][0] = 1/height

  figure_size = (img.shape[0]*size_scaler, img.shape[1]*size_scaler)

  fig = go.Figure(data=[go.Surface(z=Z)])

  fig.update_layout(title=title, autosize=False,
                    width=figure_size[0], height=figure_size[1])

  # camera
  fig.update_traces(lighting_fresnel=0, selector=dict(type='surface'))
  fig.update_traces(lighting_specular=0.05, selector=dict(type='surface'))

  # material
  fig.update_traces(colorscale='Greys', selector=dict(type='surface'))
  #fig.update_traces(colorscale=[[0, 'rgb(155,118,83)'], [1, 'rgb(155,118,83)']], selector=dict(type='surface'))
  fig.update_traces(lighting_roughness=0.5, selector=dict(type='surface'))

  # light
  fig.update_traces(lighting_ambient=0.25, selector=dict(type='surface'))
  fig.update_traces(lighting_diffuse=0.8, selector=dict(type='surface'))

  # layout margin
  fig.update_layout(margin_b=1)
  fig.update_layout(margin_l=1)
  fig.update_layout(margin_r=1)
  fig.update_layout(margin_t=1)

  fig.show()

  return