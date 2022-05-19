import tkinter as tk
import cells


class Run:
    DEF_SCALE = 644

    def __init__(self, count, size, prob_death_normal, prob_death_cancer,
                 prob_spread_alive, prob_spread_death, prob_growth):
        """
        to do

        :param count:
        :param size:
        :param probabilities:
        """
        self.__count = count
        self.__size = size
        self.__prob_death_normal = prob_death_normal
        self.__prob_death_cancer = prob_death_cancer
        self.__prob_spread_alive = prob_spread_alive
        self.__prob_spread_death = prob_spread_death
        self.__prob_growth = prob_growth
        self.__cells = cells.Cells(size).add_cancer((size // 2, size // 2))
        self.__stats = None

    def chemo(self, start, count, frequency, strength_cancer, strength_normal):
        """
        to do

        :param start:
        :param frequency:
        :param count
        :param strength_cancer:
        :param strength_normal:

        :return:
        """
        stats = []
        for step in range(self.__count):
            self.__decide_step(step, start, count, frequency, strength_cancer, strength_normal)
            stats.append(self.__cells.get_statistics())
        self.__stats = stats

    def chemo_graphics(self, start, count, frequency, strength_cancer, strength_normal, scale=(DEF_SCALE, DEF_SCALE)):
        """
        to do

        :param start:
        :param frequency:
        :param count
        :param strength_cancer:
        :param strength_normal:
        :param scale:

        :return:
        """
        stats = []
        window = tk.Tk()
        img = self.__cells.get_image(scale)
        canvas = tk.Canvas(window, height=scale[0], width=scale[1])
        canvas.pack()
        img_container = canvas.create_image(0, 0, image=img, anchor=tk.NW)
        canvas.pack()
        for step in range(self.__count):
            self.__decide_step(step, start, count, frequency, strength_cancer, strength_normal)
            img = self.__cells.get_image(scale)
            canvas.itemconfig(img_container, image=img)
            window.update()
            stats.append(self.__cells.get_statistics())
        window.mainloop()
        self.__stats = stats

    def get_statistics(self):
        """
        to do

        :return:
        """
        return self.__stats

    def get_final(self):
        """
        to do

        :return:
        """
        return self.__stats[-1]

    def __decide_step(self, step, start, count, frequency, strength_cancer, strength_normal):
        """
        to do

        :param step:
        :param start:
        :param frequency:
        :param strength_cancer:
        :param strength_normal:

        :return:
        """
        if step % frequency == start % frequency \
                and count >= (step - start) // frequency \
                and step >= start:
            self.__cells = self.__cells.step(strength_normal,
                                             strength_cancer,
                                             self.__prob_spread_alive,
                                             self.__prob_spread_death,
                                             self.__prob_growth)
        else:
            self.__cells = self.__cells.step(self.__prob_death_normal,
                                             self.__prob_death_cancer,
                                             self.__prob_spread_alive,
                                             self.__prob_spread_death,
                                             self.__prob_growth)
