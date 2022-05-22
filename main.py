from start_run import run_single, run_multiple

import params as p

if __name__ == '__main__':
    if p.SINGLE:
        run_single(p.COUNT, p.SIZE, p.PROB_DEATH_NORMAL, p.PROB_DEATH_CANCER, p.PROB_SPREAD_ALIVE,
                   p.PROB_SPREAD_DEATH, p.PROB_GROWTH, p.CHEMO_START, p.CHEMO_COUNT,
                   p.CHEMO_FREQUENCY, p.CHEMO_CANCER, p.CHEMO_NORMAL, graphics=True, plot=True)
    if p.MULTIPLE:
        stats = run_multiple(p.STATS_KEY, p.STATS_KEY_LEGEND, p.RUNS_COUNT, p.COUNT, p.SIZE,
                             p.PROB_DEATH_NORMAL, p.PROB_DEATH_CANCER, p.PROB_SPREAD_ALIVE, p.PROB_SPREAD_DEATH,
                             p.PROB_GROWTH, p.CHEMO_START, p.CHEMO_COUNT_MIN, p.CHEMO_COUNT_MAX,
                             p.CHEMO_FREQUENCY_MIN, p.CHEMO_FREQUENCY_MAX, p.CHEMO_STRENGTH_MIN, p.CHEMO_STRENGTH_MAX,
                             p.CHEMO_STRENGTH_MODIFIER, p.CHEMO_STRENGTH_STEP, plot=True)
