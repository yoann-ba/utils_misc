




#%% IMPORTS


import numpy as np # data manipulation



import matplotlib.pyplot as plt # plot


# machine learning model
from sklearn.ensemble import RandomForestRegressor



# code to make a confusion matrix for regressors by binning values
# done quick, probably better to re start from scratch with simple np functions



x = np.random.randn(500, 4)
y = np.random.randint(3, 9, 500)/10


x_train, x_test = x[:400], x[400:]
y_train, y_test = y[:400], y[400:]

reg = RandomForestRegressor()
reg.fit(x_train, y_train)

score = reg.score(x_test, y_test)
print('score', score)

# computes a confusion matrix for a regressor, by binning
# in j : true i predicted as j
def regression_confusion(reg, bins, x_test, y_test):
    
    digit_bool = np.digitize(y_test, bins)
    print(digit_bool)
    confusion_matrix = np.zeros((len(bins), len(bins)))
    for i in range(1, len(bins)+1):
        if len(x_test[digit_bool == i]) > 0:
            preds = reg.predict(x_test[digit_bool == i])
            print('p', preds)
            preds = np.digitize((preds*10).round(), bins)
            print(bins[preds -1])
            for bin_pred in preds:
                confusion_matrix[i-1][bin_pred-1] += 1
    
    # might want to /sum the matrix, or to remove the diagonal afterwards to get just errors
    return confusion_matrix

n_bins = 6
y_test = y_test * 10
print(y_test)
bins = np.linspace(np.min(y_test), np.max(y_test), n_bins)
print(bins)
confusion_matrix = regression_confusion(reg, bins, x_test, y_test)
print(confusion_matrix)
plt.imshow(confusion_matrix, cmap = 'gray')

# bin_means = [y_test[digit_bool == i].mean() for i in range(1, len(bins)+1)]












































