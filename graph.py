import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


def plot_2d(data, range_, labels, x_axis, y_axis, title):
    """
    to do

    :param data:
    :param range_:
    :param labels:
    :param x_axis:
    :param y_axis:
    :param title:

    :return:
    """
    plt.clf()

    plot_data = list(zip(*data))

    for i, label_ in enumerate(labels):
        plt.plot(list(np.arange(range_[0], range_[1], range_[2])), list(plot_data[i]), label=label_)

    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.title(title)
    plt.legend()


def plot_heatmap(data, range_x, range_y, labels, title):
    """
    to do

    :param data:
    :param range_x:
    :param range_y:
    :param labels:
    :param title:

    :return:
    """
    plt.clf()
    pd_data = pd.DataFrame(data, columns=list(np.arange(range_y[0], range_y[1], range_y[2])))
    pd_data.set_index(pd.Index(list(np.arange(range_x[0], range_x[1], range_x[2]))))
    print(pd_data)
    sns.heatmap(pd_data, annot=True)
    plt.xlabel(next(labels))
    plt.ylabel(next(labels))
    plt.title(title)
    plt.legend()


def show():
    """
    to do

    :return:
    """
    plt.show()


def save(file):
    """
    to do

    :param file:

    :return:
    """
    plt.savefig(file)
    pass
