

import numpy as np
import matplotlib.pyplot as plt

# automatic grid plot
# take in data that has a dynamic number of channels
# and automatically plots them in a square-ish grid
def plot_example(x_to_plot, n_var_x):
        
    n_rows = int(np.sqrt(n_var_x+1)) # +1 for the bam
    n_cols = int((n_var_x+1)/n_rows) + 1 # first +1 for bam, second needed for math
    fig, axes = plt.subplots(n_rows, n_cols)
    
    fig.suptitle("figure title")
    
    if n_var_x > 2:
        for i in range(len(axes)):
            for j in range(len(axes[i])):
                axes[i][j].axis('off')
    
    i = 1
    for var_i in range(n_var_x):
        ax = axes[i%n_rows][i//n_rows]
        ax.imshow(x_to_plot[:, :, var_i])
        ax.set_title("title")
        i += 1
    
    return