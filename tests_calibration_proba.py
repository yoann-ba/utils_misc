


#%% imports

import numpy as np
import matplotlib.pyplot as plt


import os


from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

from sklearn.metrics import classification_report

from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.calibration import CalibratedClassifierCV
from sklearn.calibration import calibration_curve


# ##################
# Messed around with proba calibration stuff
# didn't find much interesting





#%% data

data_X, data_Y = load_iris(return_X_y = True)

data_Y = (data_Y == 1).astype(int)




#%% 



models_base = [LogisticRegression(), GaussianNB(), RandomForestClassifier(), SVC(probability = True)]

# TRAIN TEST

sss = StratifiedShuffleSplit(n_splits = 1, test_size = 0.2)

for train_index, test_index in sss.split(data_X, data_Y):
    X_train, Y_train = data_X[train_index], data_Y[train_index]
    X_test, Y_test = data_X[test_index], data_Y[test_index]
#

# TRAIN VAL CV + CALIBRATION

sss = StratifiedShuffleSplit(n_splits = 5, test_size = 0.2)

for train_index, val_index in sss.split(X_train, Y_train):
    print('######## Fold')
    X_t, Y_t = X_train[train_index], Y_train[train_index]
    X_val, Y_val = X_train[val_index], Y_train[val_index]
    
    for model in models_base:
        print(model)
        plt.figure(figsize = (10, 10))
        plt.title(model)
        #
        temp_model = model.fit(X_t, Y_t)
        #//
        print('**')
        print(f'Base Val Score : {temp_model.score(X_test, Y_test):0.2}')
        y_pred = temp_model.predict_proba(X_test)[:, 1]
        prob_true, prob_pred = calibration_curve(Y_test, y_pred, n_bins=10)
        plt.plot(prob_pred, prob_true, marker='.', label = 'base')
        print(classification_report(Y_test, y_pred >= 0.5))
        #\\
        
        temp_calibrated = CalibratedClassifierCV(base_estimator = temp_model, 
                                                 method = 'sigmoid', 
                                                 cv = 'prefit').fit(X_val, Y_val)
        #//
        print('**')
        print(f'Sig Calibrated Val Score : {temp_calibrated.score(X_test, Y_test):0.2}')
        y_pred = temp_calibrated.predict_proba(X_test)[:, 1]
        prob_true, prob_pred = calibration_curve(Y_test, y_pred, n_bins=10)
        plt.plot(prob_pred, prob_true, marker='.', label = 'sig calib')
        print(classification_report(Y_test, y_pred >= 0.5))
        #\\
        
        temp_calibrated = CalibratedClassifierCV(base_estimator = temp_model, 
                                                 method = 'isotonic', 
                                                 cv = 'prefit').fit(X_val, Y_val)
        #//
        print('**')
        print(f'Iso Calibrated Val Score : {temp_calibrated.score(X_test, Y_test):0.2}')
        y_pred = temp_calibrated.predict_proba(X_test)[:, 1]
        prob_true, prob_pred = calibration_curve(Y_test, y_pred, n_bins=10)
        plt.plot(prob_pred, prob_true, marker='.', label = 'iso calib')
        print(classification_report(Y_test, y_pred >= 0.5))
        #\\
        
        print('')
        
        plt.plot([0, 1], [0, 1], linestyle='--')
        plt.legend(loc = 'best')
        plt.show()
    #
#
























































































