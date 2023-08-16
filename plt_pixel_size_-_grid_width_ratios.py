

import matplotlib.pyplot as plt

px = 1/plt.rcParams['figure.dpi']  # pixel in inches

fig, axes = plt.subplots(1, 3, figsize = (900*px, 1800*px), 
                          gridspec_kw = {'width_ratios': [1, 9, 8]})

# axes plot ....


# this makes the three sub figures be plotted in a way that the first
# has a width 1/9th of the 2nd, and 1/8th of the 3rd

