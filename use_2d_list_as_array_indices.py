

import numpy as np


# using a list of 2d indices as array indices without bugging out rows/cols


# peak_idx = '2d coord list'
# peaks_boolean = np.zeros_like('matrix from which idx is extracted', dtype = bool)
# peaks_boolean[tuple(peak_idx.T)] = True


# demo

# without
test = np.zeros((5, 5))
ll = np.array([[2, 1], [4, 1]])

test[ll] = 1
print(test)
print('')

# with
test = np.zeros((5, 5))
ll = np.array([[2, 1], [4, 1]])

test[tuple(ll.T)] = 1
print(test)














