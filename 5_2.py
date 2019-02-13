import pandas as pd
from discretize import do_discretize
import importlib
from split import split_dataset
nbc_file = importlib.import_module('5_1')

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
mpl.rcParams['figure.figsize'] = (7,7)

def plot_learning_curves(x_axis_label, y_axis_label, x_axis, y_axis_1, y_axis_2, type):
    plt.plot(x_axis, y_axis_1, marker='*')
    plt.plot(x_axis, y_axis_2, marker='*')
    plt.legend(['Train', 'Test'], loc='best')
    plt.xlabel(x_axis_label)
    plt.ylabel(y_axis_label)
    plt.title(y_axis_label + ' v/s ' + x_axis_label)
    plt.savefig(type,dpi=300)

def main():
    bins = [2, 5, 10, 50, 100, 200]
    train_scores = []
    test_scores = []
    t_frac = 1
    for num_bin in bins:
        do_discretize(num_bin)
        split_dataset(0.2, 47, "dating-binned.csv")
        accuracy_train, accuracy_test = nbc_file.nbc(t_frac)
        train_scores.append(accuracy_train)
        test_scores.append(accuracy_test)

    plot_learning_curves('Number of Bins', 'Accuracy', bins, train_scores, test_scores, "num_bins_to_accuracy_graph")


if __name__ == '__main__':
    main()