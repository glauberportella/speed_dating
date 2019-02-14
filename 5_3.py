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
    t_frac_list = [0.01, 0.1, 0.2, 0.5, 0.6, 0.75, 0.9, 1]
    train_scores = []
    test_scores = []
    num_bin=5
    do_discretize(num_bin)
    split_dataset(0.2, 47, "dating-binned.csv")
    for t_frac in t_frac_list:
        print ("Running Naive Bayes Classifier for f:", t_frac)
        accuracy_train, accuracy_test = nbc_file.nbc(t_frac)
        train_scores.append(accuracy_train)
        test_scores.append(accuracy_test)

    plot_learning_curves('Value of f', 'Accuracy', t_frac_list, train_scores, test_scores, "f_to_accuracy_graph")


if __name__ == '__main__':
    main()