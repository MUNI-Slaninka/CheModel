COUNT = 128
SIZE = 48

PROB_DEATH_NORMAL = 0.01
PROB_DEATH_CANCER = 0.01
PROB_SPREAD_ALIVE = 0.2
PROB_SPREAD_DEATH = 0.2
PROB_GROWTH = 0.2

CHEMO_START = 48

CHEMO_COUNT = 8
CHEMO_FREQUENCY = 4
CHEMO_CANCER = 0.8
CHEMO_NORMAL = 0.65

CHEMO_COUNT_MIN = 5
CHEMO_COUNT_MAX = CHEMO_COUNT_MIN
CHEMO_FREQUENCY_MIN = 4
CHEMO_FREQUENCY_MAX = 6
CHEMO_STRENGTH_MIN = 0.4
CHEMO_STRENGTH_MAX = 0.5
CHEMO_STRENGTH_MODIFIER = 0.8
CHEMO_STRENGTH_STEP = 0.1

STATS_KEY = [False, False, True, False, True, False, False, True, False, False, False, False]
STATS_KEY_LEGEND = ["Dead finish", "Alive finish", "Cancerous finish",
                    "Dead average", "Alive average", "Cancerous average",
                    "Dead min", "Alive min", "Cancerous min",
                    "Dead max", "Alive max", "Cancerous max"]

RUNS_COUNT = 1

SINGLE = False
MULTIPLE = True
