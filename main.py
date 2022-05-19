from run import Run
from analytics import Analytics
import graph

COUNT = 128
SIZE = 96

PROB_DEATH_NORMAL = 0.01
PROB_DEATH_CANCER = 0.01
PROB_SPREAD_ALIVE = 0.2
PROB_SPREAD_DEATH = 0.2
PROB_GROWTH = 0.3

CHEMO_START = 24

CHEMO_COUNT = 5
CHEMO_FREQUENCY = 6
CHEMO_CANCER = 0.5
CHEMO_NORMAL = CHEMO_CANCER

CHEMO_COUNT_MIN = 5
CHEMO_COUNT_MAX = CHEMO_COUNT_MIN
CHEMO_FREQUENCY_MIN = 4
CHEMO_FREQUENCY_MAX = 16
CHEMO_STRENGTH_MIN = 0.8
CHEMO_STRENGTH_MAX = CHEMO_STRENGTH_MIN
CHEMO_STRENGTH_MODIFIER = 1
CHEMO_STRENGTH_STEP = 0.1


def run_single(count=COUNT, size=SIZE, prob_death_normal=PROB_DEATH_NORMAL, prob_death_cancer=PROB_DEATH_CANCER,
               prob_spread_alive=PROB_SPREAD_ALIVE, prob_spread_death=PROB_SPREAD_DEATH, prob_growth=PROB_GROWTH,
               chemo_start=CHEMO_START, chemo_count=CHEMO_COUNT, chemo_frequency=CHEMO_FREQUENCY,
               chemo_cancer=CHEMO_CANCER, chemo_normal=CHEMO_NORMAL, graphics=True, plot=True):
    """
    to do

    :param count:
    :param size:
    :param prob_death_normal:
    :param prob_death_cancer:
    :param prob_spread_alive:
    :param prob_spread_death:
    :param prob_growth:
    :param chemo_start:
    :param chemo_frequency:
    :param chemo_count:
    :param chemo_cancer:
    :param chemo_normal:
    :param graphics:
    :param plot:

    :return:
    """

    run_ = Run(count, size, prob_death_normal, prob_death_cancer,
               prob_spread_alive, prob_spread_death, prob_growth)
    if graphics:
        run_.chemo_graphics(chemo_start, chemo_count, chemo_frequency, chemo_cancer, chemo_normal)
        statistics = run_.get_statistics()
    else:
        run_.chemo_graphics(chemo_start, chemo_count, chemo_frequency, chemo_cancer, chemo_normal)
        statistics = run_.get_statistics()

    if plot:
        g = graph.Graph(statistics)
        g.plot_all()
        g.show()

    return run_.get_final()


def run_multiple(count=COUNT, size=SIZE,
                 prob_death_normal=PROB_DEATH_NORMAL, prob_death_cancer=PROB_DEATH_CANCER,
                 prob_spread_alive=PROB_SPREAD_ALIVE, prob_spread_death=PROB_SPREAD_DEATH,
                 prob_growth=PROB_GROWTH,
                 chemo_start=CHEMO_START,
                 chemo_count_min=CHEMO_COUNT_MIN, chemo_count_max=CHEMO_COUNT_MAX,
                 chemo_frequency_min=CHEMO_FREQUENCY_MIN, chemo_frequency_max=CHEMO_FREQUENCY_MAX,
                 chemo_strength_min=CHEMO_STRENGTH_MIN, chemo_strength_max=CHEMO_STRENGTH_MAX,
                 chemo_strength_modifier=CHEMO_STRENGTH_MODIFIER, chemo_strength_step=CHEMO_STRENGTH_STEP, plot=True):
    """
    to do

    :param count:
    :param size:
    :param prob_death_normal:
    :param prob_death_cancer:
    :param prob_spread_alive:
    :param prob_spread_death:
    :param prob_growth:
    :param chemo_start:
    :param chemo_count_min:
    :param chemo_count_max:
    :param chemo_frequency_min:
    :param chemo_frequency_max:
    :param chemo_strength_min:
    :param chemo_strength_max:
    :param chemo_strength_modifier:
    :param chemo_strength_step:
    :param plot:

    :return:
    """

    run_ = Run(count, size, prob_death_normal, prob_death_cancer,
               prob_spread_alive, prob_spread_death, prob_growth)

    analytics_ = Analytics(run_, chemo_start, chemo_count_min, chemo_count_max,
                           chemo_frequency_min, chemo_frequency_max, chemo_strength_min,
                           chemo_strength_max, chemo_strength_modifier, chemo_strength_step)
    if plot:
        g = graph.Graph(statistics)
        g.plot_all()
        g.show()


if __name__ == '__main__':
    run_multiple()
