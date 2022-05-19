from copy import deepcopy


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

        self.__statistics = None

    def run(self, verbose=True):
        """
        to do

        :return:
        """

        if verbose:
            print("Running analytics")

        statistics = [[[]]]

        for count in range(self.__count_min, self.__count_max):
            for frequency in range(self.__frequency_min, self.__frequency_max):
                for strength in range(self.__strength_min // self.__strength_step,
                                      self.__strength_max // self.__strength_step):
                    if verbose:
                        print(".", end="")
                    strength_cancer = strength * self.__strength_step
                    strength_normal = strength_cancer * self.__strength_modifier
                    run_ = deepcopy(self.__run_)
                    run_.chemo(self.__start, count, frequency, strength_cancer, strength_normal)
                    statistics[-1][-1].append(run_.get_final())
                statistics[-1].append([])
            statistics.append([])

        print("")
        self.__statistics = statistics
        return self
