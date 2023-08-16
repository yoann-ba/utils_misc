



import numpy as np


# sk learn stuff
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.pipeline import make_pipeline

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis



# ############
# Fit a few basic ML classifiers on a section of a dataframe for a quick overview
# No hyperopt
# Tracks a few metrics (F-Beta with exposed weights, Precision, Recall)
# Repeated SKF
# Calibration of the decision function threshold 
# Registers avg, std, and some percentiles over all runs



# if we want a function to calibrate decision threshold
def calibrate_threshold():
    
    # actual code
    
    return #calibrated threshold


# if we want a separate function to handle evaluation
def evaluate_test():
    
    # actual code
    
    return # some kind of dict of perf stats



#
# takes in a dataframe, precise the X and Y inside, can expose them as params ofc
# models initialised with some default-ish parameters, can change them
# can add a whole hyperopt inside if wanted
def basic_ML_models(df, n_macro_splits = 10, n_micro_splits = 5, beta_weights = [5, 1]):
    
    rskf = RepeatedStratifiedKFold(n_splits = n_micro_splits, n_repeats = n_macro_splits)
    
    high_potential_features = ["feature_1", "feature_2"]
    
    X = df[high_potential_features].to_numpy()
    Y = df["label_column"].to_numpy()
    
    names = [
        "Log Reg",
        "KNN",
        "Linear SVM",
        "RBF SVM",
        "Gaussian Process",
        "Decision Tree",
        "Random Forest",
        "MLP",
        "AdaBoost",
        "Naive Bayes",
        "QDA",
    ]
    classifiers = [
        LogisticRegression(),
        KNeighborsClassifier(5),
        SVC(kernel="linear", C=0.025, probability = True),
        SVC(gamma=2, C=1, probability = True),
        GaussianProcessClassifier(1.0 * RBF(1.0)),
        DecisionTreeClassifier(max_depth=5),
        RandomForestClassifier(max_depth=5),
        MLPClassifier(max_iter = 1000, hidden_layer_sizes = (20, 20, 20)),
        AdaBoostClassifier(),
        GaussianNB(),
        QuadraticDiscriminantAnalysis(),
    ]
    
    tracker_keys = ["f_beta", "precision", "recall"] + ["roc_auc", "prc_auc"]
    # pre build an empty list dict for each classifier
    test_score_lists = {clf_name: {key: [] for key in tracker_keys} for clf_name in names}
    # add their name to their stat info just in case
    [test_score_lists[clf_name].update({"clf_name": clf_name}) for clf_name in names]
    
    for i, (train_index, test_index) in enumerate(rskf.split(X, Y)):
      #print(f"Split {i}/{n_macro_splits*n_micro_splits}")
      train_X, train_Y = X[train_index], Y[train_index]
      test_X, test_Y = X[test_index], Y[test_index]
      
      for (name, clf_obj) in zip(names, classifiers):
        clf = make_pipeline(StandardScaler(), clf_obj) # MinMaxScaler, StandardScaler
        clf.fit(train_X, train_Y)
        # predictions = clf.predict(test_X)
    
        # checked, all models implement predict_proba
        train_probas = clf.predict_proba(train_X)[:, 1]
        
        temp_array = np.dstack((train_probas, train_Y))[0]
        temp_array = temp_array[temp_array[:, 0].argsort()[::-1]] # sort by first column, descending
        train_dict = calibrate_threshold(temp_array, name, beta_weights = beta_weights)
        
        test_probas = clf.predict_proba(test_X)[:, 1]
        test_dict = evaluate_test(test_probas, test_Y, train_dict["threshold"], 
                                  beta_weights = beta_weights)
        
        for key in tracker_keys:
          test_score_lists[name][key].append(test_dict[key])
      # 
    #
    
    # for each classifier, add mean, std and percentiles of each tracked metric
    [test_score_lists[clf_name].update({f"avg_test_{key}": np.nanmean(test_score_lists[clf_name][key]) for key in tracker_keys}) for clf_name in names]
    [test_score_lists[clf_name].update({f"std_test_{key}": np.nanstd(test_score_lists[clf_name][key]) for key in tracker_keys}) for clf_name in names]
    for prct in [2.5, 5, 12.5, 25, 50, 75, 87.5, 95, 97.5]:
      # what a gloriously disgusting yet efficient line, splendid
      [test_score_lists[clf_name].update({f"{prct}th_prct_test_{key}": np.nanpercentile(test_score_lists[clf_name][key], prct) for key in tracker_keys}) for clf_name in names]
    
    return_dict = {
        "n_micro_splits": n_micro_splits,
        "n_macro_splits": n_macro_splits,
        "beta_weights": beta_weights,
        "test_scores": test_score_lists,
    }
    
    print("Train/Test split, model, eval for some classic ML classifiers")
    print("Fit on a selection of features w/ high individual separation")
    print(f"Calibration on an F beta of weights {beta_weights}")
    print(f"{n_macro_splits} repeats of a {n_micro_splits}-fold Stratified CV")
    print(f"{'model name name':20s} | F score@threshold | Precision vs Recall | AuROC & AuPRC")
    print("Format of avg_over_all_splits (±std_over_all_splits)")
    print("--")
    for clf_name in names:
      print_text = f"{clf_name:20s} | "
      print_text += f"{test_score_lists[clf_name]['avg_test_f_beta']:0.2f} (±{test_score_lists[clf_name]['std_test_f_beta']:0.2f}) | "
      print_text += f"{test_score_lists[clf_name]['avg_test_precision']*100:5.2f}% (±{test_score_lists[clf_name]['std_test_precision']*100:5.2f}%) vs "
      print_text += f"{test_score_lists[clf_name]['avg_test_recall']*100:5.2f}% (±{test_score_lists[clf_name]['std_test_recall']*100:5.2f}%) |"
      print_text += f"{test_score_lists[clf_name]['avg_test_roc_auc']*100:5.2f}% (±{test_score_lists[clf_name]['std_test_roc_auc']*100:5.2f}%) &"
      print_text += f"{test_score_lists[clf_name]['avg_test_prc_auc']*100:5.2f}% (±{test_score_lists[clf_name]['std_test_prc_auc']*100:5.2f}%)"
      print(print_text)
    
    # add a percentile print by adapting something like this : 
    
    # if show_percentiles:
    #     print_text = f"{' ':30s} | ["
    #     for prct in [2.5, 5, 12.5, 25, 50, 75, 87.5, 95, 97.5]:
    #       print_text += f"{threshold_stats[str(prct)+'th_prct_test_f_beta']:0.2f} "
    #     print_text += f"] @["
    #     for prct in [2.5, 5, 12.5, 25, 50, 75, 87.5, 95, 97.5]:
    #       print_text += f"{threshold_stats[str(prct)+'th_prct_test_threshold']:5.2f} "
    #     print_text += f"] | ["
    #     for prct in [2.5, 5, 12.5, 25, 50, 75, 87.5, 95, 97.5]:
    #       print_text += f"{threshold_stats[str(prct)+'th_prct_test_precision']*100:5.2f} "
    #     print_text += f"] vs ["
    #     for prct in [2.5, 5, 12.5, 25, 50, 75, 87.5, 95, 97.5]:
    #       print_text += f"{threshold_stats[str(prct)+'th_prct_test_recall']*100:5.2f} "
    #     print_text += "]"
    #     print(print_text)
    
    return return_dict



