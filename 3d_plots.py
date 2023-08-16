

import numpy as np

import matplotlib.pyplot as plt
import matplotlib.cm as cm


# Probably taken from matplotlib's doc or stackoverflow

# ---- 3D BAR PLOT ----

# Replace by whatever 2d image you have
heatmap = np.random.randn(500, 500)

Z = heatmap[200:250, 200:250]


# Color Map if wanted, optional-----------------------
test_cmap = cm.get_cmap('RdBu_r')
min_height, max_height = np.min(Z), np.max(Z)
color_list = [test_cmap((k - min_height)/(max_height - min_height)) for k in Z.ravel()]

# The good shit--------------------------------------
fig, ax = plt.subplots(figsize = (15, 15), subplot_kw={"projection": "3d"})
X = np.arange(0, 50)
Y = np.arange(0, 50)
X, Y = np.meshgrid(X, Y)
surf = ax.bar3d(X.ravel(), Y.ravel(), 0, 1, 1, Z.ravel(), shade = True, color = color_list)
plt.show()




# ---- 3D SURFACE PLOT ----

# Replace by whatever 2d heatmap
Z = heatmap[200:220, 200:220]

# The good shit ----------------------------------
fig, ax = plt.subplots(figsize = (15, 15), subplot_kw={"projection": "3d"})
X = np.arange(0, 20)
Y = np.arange(0, 20)
X, Y = np.meshgrid(X, Y)
surf = ax.plot_surface(X, Y, Z, cmap = 'RdBu_r', linewidth = 0, antialiased = False)
plt.show()