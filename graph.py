import matplotlib.pyplot as plt


class Graph:
    def __init__(self, statistics):
        self.statistics = statistics

    def plot_all(self):
        plt.clf()
        x = [i + 1 for i in range(len(self.statistics))]
        dead = [i[0] for i in self.statistics]
        alive = [i[1] for i in self.statistics]
        cancer = [i[2] for i in self.statistics]
        plt.plot(x, dead, label="dead")
        plt.plot(x, alive, label="alive")
        plt.plot(x, cancer, label="cancer")
        plt.xlabel('time(cycle)')
        plt.ylabel('amount')
        plt.title("plot of all types")
        plt.legend()

    def plot_dead(self):
        pass
        # to do

    def plot_alive(self):
        pass
        # to do

    def plot_cancerous(self):
        pass
        # to do

    @staticmethod
    def show():
        plt.show()

    @staticmethod
    def save(file):
        plt.savefig(file)
        pass
