



import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


# #####
# Plot a boxplot-like plot with percentile values for a few features and/or models
# to compare them.
# Works on receiving the percentile values directly, and not the raw list of observations


list_of_feature_names = ['feature/model 1', 'feature/model 2']

# the relevant percentile values pre-computed for each feature
plot_stats_dict = {'feature/model 1': {}}

fig, ax = plt.subplots(figsize = (10, 6))
for i, feature_name in enumerate(list_of_feature_names):
    stat_dict = plot_stats_dict[feature_name]
    key_suffix = "th_prct_test_precision"
    plt.plot([i - 0.5, i], [stat_dict["50"+key_suffix], stat_dict["50"+key_suffix]], label = 'median' if i==0 else "", color = 'blue')
    # Bottom Left, width, height
    # 50%
    rect_coords = [[i - 0.5, stat_dict["25"+key_suffix]], 0.5, stat_dict["75"+key_suffix] - stat_dict["25"+key_suffix]]
    rect = mpatches.Rectangle(rect_coords[0], rect_coords[1], rect_coords[2],
                              edgecolor = None, facecolor = "green", alpha = 0.5, label = "center 50% of vals" if i==0 else "")
    ax.add_patch(rect)
    # 75%
    rect_coords = [[i - 0.4, stat_dict["12.5"+key_suffix]], 0.4, stat_dict["25"+key_suffix] - stat_dict["12.5"+key_suffix]]
    rect = mpatches.Rectangle(rect_coords[0], rect_coords[1], rect_coords[2],
                              edgecolor = None, facecolor = "orange", alpha = 0.5, label = "center 75% of vals" if i==0 else "")
    ax.add_patch(rect)
    rect_coords = [[i - 0.4, stat_dict["75"+key_suffix]], 0.4, stat_dict["87.5"+key_suffix] - stat_dict["75"+key_suffix]]
    rect = mpatches.Rectangle(rect_coords[0], rect_coords[1], rect_coords[2],
                              edgecolor = None, facecolor = "orange", alpha = 0.5)
    ax.add_patch(rect)
    # 90%
    rect_coords = [[i - 0.3, stat_dict["5"+key_suffix]], 0.3, stat_dict["12.5"+key_suffix] - stat_dict["5"+key_suffix]]
    rect = mpatches.Rectangle(rect_coords[0], rect_coords[1], rect_coords[2],
                              edgecolor = None, facecolor = "red", alpha = 0.5, label = "center 90% of vals" if i==0 else "")
    ax.add_patch(rect)
    rect_coords = [[i - 0.3, stat_dict["87.5"+key_suffix]], 0.3, stat_dict["95"+key_suffix] - stat_dict["87.5"+key_suffix]]
    rect = mpatches.Rectangle(rect_coords[0], rect_coords[1], rect_coords[2],
                              edgecolor = None, facecolor = "red", alpha = 0.5)
    ax.add_patch(rect)
    # 95%
    rect_coords = [[i - 0.2, stat_dict["2.5"+key_suffix]], 0.2, stat_dict["5"+key_suffix] - stat_dict["2.5"+key_suffix]]
    rect = mpatches.Rectangle(rect_coords[0], rect_coords[1], rect_coords[2],
                              edgecolor = None, facecolor = "black", alpha = 0.5, label = "center 95% of vals" if i==0 else "")
    ax.add_patch(rect)
    rect_coords = [[i - 0.2, stat_dict["95"+key_suffix]], 0.2, stat_dict["97.5"+key_suffix] - stat_dict["95"+key_suffix]]
    rect = mpatches.Rectangle(rect_coords[0], rect_coords[1], rect_coords[2],
                              edgecolor = None, facecolor = "black", alpha = 0.5)
    ax.add_patch(rect)
plt.title("Precision of selected features\ncompared in a boxplot-like plot")
plt.xticks(range(len(list_of_feature_names)), list_of_feature_names, rotation = 45)
plt.legend(loc = "best")
plt.show()





