from copy import deepcopy
from itertools import compress

import numpy as np


class Analytics:

    def __init__(self, run_, start, count_min, count_max, frequency_min,
                 frequency_max, strength_min, strength_max, strength_modifier, strength_step):
        """
        to do

        :param run_:
        :param start:
        :param count_min:
        :param count_max:
        :param frequency_min:
        :param frequency_max:
        :param strength_min:
        :param strength_max:
        :param strength_modifier:
        :param strength_step:
        """

        self.__run_ = run_
        self.__start = start
        self.__count_min = count_min
        self.__count_max = count_max
        self.__frequency_min = frequency_min
        self.__frequency_max = frequency_max
        self.__strength_min = strength_min
        self.__strength_max = strength_max
        self.__strength_modifier = strength_modifier
        self.__strength_step = strength_step

        self.__strength_count = len(np.arange(self.__strength_min, self.__strength_max + self.__strength_step,
                                              self.__strength_step))
        self.__statistics = None

    def run(self, runs=1, verbose=True):
        """
        to do

        :return:
        """

        if verbose:
            print("Running analytics")

        statistics = [[[]]]

        for count in range(self.__count_min, self.__count_max + 1):
            for frequency in range(self.__frequency_min, self.__frequency_max + 1):
                for strength in np.arange(self.__strength_min, self.__strength_max + self.__strength_step,
                                          self.__strength_step):
                    results = []
                    for _ in range(runs):
                        if verbose:
                            print(".", end="")
                        run_ = deepcopy(self.__run_)
                        run_.chemo(self.__start, count, frequency, strength, strength * self.__strength_modifier)
                        results.append(run_.get_final() + run_.get_avg() + run_.get_min() + run_.get_max())
                    results_avg = [sum([r[i] for r in results]) / len(results) for i in range(len(results[0]))]
                    statistics[-1][-1].append(results_avg)
                statistics[-1].append([])
            statistics.append([])

        print("")
        statistics.pop()
        statistics[-1].pop()
        self.__statistics = statistics

        return self

    def get_stats(self, key=None, full_dim=False):
        """
        to do

        :return:
        """
        statistics = deepcopy(self.__statistics)

        if key:
            _filter_statistics(statistics, key)

        if full_dim:
            return statistics

        squeezed = list(np.squeeze(statistics))
        _to_list_rec(squeezed)

        return squeezed

    def get_dimensions(self):
        """
        to do

        :return:
        """
        dim = 0

        if self.__count_max != self.__count_min:
            dim += 1
        if self.__frequency_max != self.__frequency_min:
            dim += 1
        if self.__strength_count != 1:
            dim += 1

        return dim

    def get_legend(self):
        """
        to do

        :return:
        """
        if self.__count_max != self.__count_min:
            yield "chemotherapy count"
        if self.__frequency_max != self.__frequency_min:
            yield "frequency of chemotherapy"
        if self.__strength_count != 1:
            yield "chemotherapeutics strength"

    def get_ranges(self):
        """
        to do

        :return:
        """
        if self.__count_max != self.__count_min:
            yield self.__count_min, self.__count_max + 1, 1
        if self.__frequency_max != self.__frequency_min:
            yield self.__frequency_min, self.__frequency_max + 1, 1
        if self.__strength_count != 1:
            yield self.__strength_min, self.__strength_max + self.__strength_step, self.__strength_step


def _filter_statistics(statistics,  key):
    """
    to do

    :param statistics:
    :param key:

    :return:
    """
    for ix, x in enumerate(statistics):
        for iy, y in enumerate(x):
            for iz, z in enumerate(y):
                statistics[ix][iy][iz] = list(compress(z, key))


def _to_list_rec(array):
    """
    to do

    :param array:

    :return:
    """
    for index, item in enumerate(array):
        if isinstance(item, np.ndarray):
            array[index] = list(item)
            _to_list_rec(array[index])
