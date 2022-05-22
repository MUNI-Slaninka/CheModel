from PIL import Image, ImageTk

import numpy as np


class Cells:

    DEF_PALETTE = [0, 0, 0, 0, 255, 0, 255, 0, 0]

    def __init__(self, size):
        """
        to do

        :param size:
        """
        self.__size = size
        self.__matrix = np.full((size, size), 1, dtype=np.uint8)

    def step(self, prob_death_normal, prob_death_cancer, prob_spread_alive, prob_spread_death, prob_growth):
        """
        to do

        :param prob_death_normal:
        :param prob_death_cancer:
        :param prob_spread_alive:
        :param prob_spread_death:
        :param prob_growth:

        :return:
        """
        for coords, value in np.ndenumerate(self.__matrix):
            if value == 0:
                self.__solve_dead(coords, prob_growth, prob_spread_death)
                continue
            if value == 1:
                self.__solve_alive(coords, prob_death_normal, prob_spread_alive)
                continue
            if value == 2:
                self.__solve_cancer(coords, prob_death_cancer)
                continue

        return self

    def add_cancer(self, row, col):
        """
        to do

        :param row:
        :param col

        :return:
        """
        coordinates = ([(row, col),
                       (row - 1, col),
                       (row + 1, col),
                       (row, col - 1),
                       (row, col + 1)])
        for coord in coordinates:
            self.__matrix[coord] = 2
        return self

    def get_image(self,  scale, palette=None):
        """
        to do

        :param scale:
        :param palette:

        :return:
        """
        if palette is None:
            palette = self.DEF_PALETTE

        image = Image.fromarray(self.__matrix, "P")
        image.putpalette(palette)
        image = image.resize(scale)
        photo = ImageTk.PhotoImage(image=image)

        return photo

    def get_stats(self):
        """
        to do

        :return:
        """
        alive = np.count_nonzero(self.__matrix == 1)
        cancerous = np.count_nonzero(self.__matrix == 2)

        return [self.__size ** 2 - alive - cancerous, alive, cancerous]

    def __solve_dead(self, coords, prob_growth, prob_spread_death):
        """
        to do

        :param coords:
        :param prob_growth:
        :param prob_spread_death:

        :return:
        """
        seed = np.random.random()
        _, alive, cancer = self.__valuate_neighbours(coords[0], coords[1])

        if seed < prob_growth * alive / 4:
            self.__matrix[coords] = 1
        if seed < prob_spread_death * cancer / 4:
            self.__matrix[coords] = 2

    def __solve_alive(self, coords, prob_death_normal, prob_spread_alive):
        """
        to do

        :param coords:
        :param prob_death_normal:
        :param prob_spread_alive:

        :return:
        """
        seed = np.random.random()
        _, _, cancer = self.__valuate_neighbours(coords[0], coords[1])

        if seed < prob_death_normal:
            self.__matrix[coords] = 0
        if seed < prob_spread_alive * cancer / 4:
            self.__matrix[coords] = 2

    def __solve_cancer(self, coords, prob_death_cancer):
        """
        to do

        :param coords:
        :param prob_death_cancer:

        :return:
        """
        seed = np.random.random()

        if seed < prob_death_cancer:
            self.__matrix[coords] = 0

    def __valuate_neighbours(self, row, col):
        """
        to do

        :param row:
        :param col:

        :return:
        """
        coordinates = ([(row - 1, col),
                       (row + 1, col),
                       (row, col - 1),
                       (row, col + 1)])
        neighbours = [self.__matrix[coord] for coord in coordinates
                      if coord[0] < self.__size and coord[1] < self.__size]

        return neighbours.count(0), neighbours.count(1), neighbours.count(2)
