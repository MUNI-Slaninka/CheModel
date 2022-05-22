from run import Run
from analytics import Analytics
import graph

from itertools import compress


def run_single(count, size, prob_death_normal, prob_death_cancer, prob_spread_alive, prob_spread_death, prob_growth,
               chemo_start, chemo_count, chemo_frequency, chemo_cancer, chemo_normal, graphics=True, plot=True):
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
        run_.chemo(chemo_start, chemo_count, chemo_frequency, chemo_cancer, chemo_normal)
        statistics = run_.get_statistics()

    if plot:
        graph.plot_2d(statistics, (1, len(statistics)+1), ["dead", "alive", "cancerous"],
                      "time(no steps)", "count of cells", "Single run")
        graph.show()

    return run_.get_final()


def run_multiple(stats_key, legend, runs_count, count, size, prob_death_normal, prob_death_cancer,
                 prob_spread_alive, prob_spread_death, prob_growth, chemo_start, chemo_count_min, chemo_count_max,
                 chemo_frequency_min, chemo_frequency_max, chemo_strength_min, chemo_strength_max,
                 chemo_strength_modifier, chemo_strength_step, plot=True):
    """
    to do

    :param stats_key
    :param legend
    :param runs_count
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

    analytics_.run(runs_count)

    statistics = analytics_.get_stats(stats_key)

    if plot and analytics_.get_dimensions() == 1:
        graph.plot_2d(statistics, next(analytics_.get_ranges()), list(compress(legend, stats_key)),
                      next(analytics_.get_legend()), "count of cells", "Multiple runs")
        graph.show()

    if plot and analytics_.get_dimensions() == 2:
        for key in _solve_single_key(stats_key):
            single_stats = analytics_.get_stats(key)
            rang_iter = analytics_.get_ranges()
            graph.plot_heatmap(single_stats, next(rang_iter), next(rang_iter),
                               analytics_.get_legend(), list(compress(legend, key))[0])
            graph.show()

    return statistics


def _solve_single_key(keys):
    """
    to do

    :param keys:

    :return:
    """
    for i, x in enumerate(keys):
        if x == 1:
            key = [0] * len(keys)
            key[i] = 1
            yield key
