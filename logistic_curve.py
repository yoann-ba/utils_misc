


#%% imports

import numpy as np
import matplotlib.pyplot as plt


#%% 

# an old script to mess with a parametrized logistic curve

X = np.linspace(-5, 5, num = 101)

n_sigma = 3
y_n = 0.9

r = (1/n_sigma) * np.log(y_n/(1-y_n))

Y = 1/(1+np.exp(-r*X))






plt.figure(figsize = (8, 8))

n_sigma = 3
y_n = 0.99
r = (1/n_sigma) * np.log(y_n/(1-y_n))
Y = 1/(1+np.exp(-r*X))
plt.plot(X, Y, label = f'{n_sigma} {y_n}')


n_sigma = 2
y_n = 0.95
r = (1/n_sigma) * np.log(y_n/(1-y_n))
Y = 1/(1+np.exp(-r*X))
plt.plot(X, Y, label = f'{n_sigma} {y_n}')


n_sigma = 3
y_n = 0.95
translate_y = 1

r = (1/n_sigma) * np.log(y_n/(1-y_n))
Y = 1/(1+np.exp(-r*(X-translate_y)))
plt.plot(X, Y, label = f'{n_sigma} {y_n}')


plt.legend(loc = 'best')
plt.show()



#%%




#%%












































































































