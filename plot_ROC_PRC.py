


import matplotlib.pyplot as plt


from sklearn.metrics import roc_curve, roc_auc_score
from sklearn.metrics import precision_recall_curve, auc
from sklearn.metrics import precision_recall_fscore_support



# Plot ROC Curve, PRC clean and get the AuCs


#
def plot_roc_prc(prediction_probas, labels, show_plots = False, plot_title = ''):

    # Calculate values for ROC
    fpr, tpr, _ = roc_curve(labels, prediction_probas)
    roc_auc = roc_auc_score(labels, prediction_probas)

    # Calculate values for PRC
    precision, recall, _ = precision_recall_curve(labels, prediction_probas)
    prc_auc = auc(recall, precision)

    if show_plots:
      # Graph for ROC
      plt.figure(figsize=(12, 6))

      plt.subplot(1, 2, 1)
      plt.plot(fpr, tpr, color='darkorange', label='ROC curve (area = %0.2f)' % roc_auc)
      plt.plot([0, 1], [0, 1], color='navy', linestyle='--')
      plt.xlim([0.0, 1.0])
      plt.ylim([0.0, 1.05])
      plt.xlabel('False Positive Rate')
      plt.ylabel('True Positive Rate')
      plt.title(plot_title + '\n' + 'ROC Curve')
      plt.legend(loc="best")

      # Graph for PRC
      plt.subplot(1, 2, 2)
      plt.plot(recall, precision, color='blue', label='PRC curve (area = %0.2f)' % prc_auc)
      plt.xlim([0.0, 1.0])
      plt.ylim([0.0, 1.05])
      plt.xlabel('Recall')
      plt.ylabel('Precision')
      plt.title(plot_title + "\n" + 'Precision Recall Curve')
      plt.legend(loc="best")

      plt.show()
    #

    return roc_auc, prc_auc