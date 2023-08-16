
import numpy as np


# ###########
# Calibrate a threshold on a decision function or just any value list
# to maximize an F Beta objective function



#
# receives a sub df of shape (feature, label) into numpy array
# array needs to be ordered going down by the feature column
# calibrates threshold on continuous vals array
# one shot model -> eval
# can be used for model -> train perf, not test perf
def calibrate_threshold(arr, feature_name, beta_weights = [5, 1]):

  tracker_keys = ["f_beta", "threshold", "precision", "recall"]
  store_vals = {key: [] for key in tracker_keys}
  compromise_vals = {key: 0 for key in tracker_keys} # stats of the optimal cut

  for i in range(len(arr)):
    threshold = arr[i][0]
    precision = np.sum(arr[:i+1, 1]) / (i+1)
    recall = np.sum(arr[:i+1, 1]) / np.sum(arr[:, 1])
    if recall == 0 and precision == 0:
      f_beta = 0
    else:
      beta = beta_weights[1]/beta_weights[0]
      f_beta = (1 + beta*beta) * (precision * recall) / (beta*beta * precision + recall)

    store_vals["f_beta"].append(f_beta)
    store_vals["threshold"].append(threshold)
    store_vals["precision"].append(precision)
    store_vals["recall"].append(recall)

    if f_beta > compromise_vals["f_beta"]:
      compromise_vals["f_beta"] = f_beta
      compromise_vals["threshold"] = threshold
      compromise_vals["precision"] = precision
      compromise_vals["recall"] = recall
  #
  return_dict = {"lists": store_vals} # all options i.e PR Curve numbers
  return_dict.update({key: compromise_vals[key] for key in tracker_keys})

  return return_dict