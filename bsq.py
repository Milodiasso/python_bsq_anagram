import sys
import math
import copy


class Bsq:
    """ Attributs globals de class """
    un_attribut_global = "global"

    # la méthode constructeur
    def __init__(self, file):
        """ attributs de constructeur """
        open_file = open(file, "r")
        # lignes = open_file.read()

        self.map = []
        self.nb_point_x = {}
        self.nb_point_y = {}
        self.max_suite_x = {}
        self.max_suite_y = {}
        self.max_suite = 0
        self.lines = int(open_file.readline())
        self.read_file = open_file.readlines()
        self.columns = len(self.read_file[1])-1
        self.coordonnees = list()

        for x in range(0, self.lines):
            self.nb_point_y[x] = 0
            self.max_suite_y[x] = 0

        temp_y = [0] * self.lines
        for k, line in enumerate(self.read_file):
            # print(k, line)
            ligne = line[0:-1]
            self.map.append(list())
            self.nb_point_x[k] = 0
            self.max_suite_x[k] = 0
            temp_x = 0
            for key, car in enumerate(ligne):
                self.map[k].append(car)
                if car == '.':
                    self.nb_point_x[k] += 1
                    self.nb_point_y[key] += 1
                    temp_x += 1
                    if temp_x > self.max_suite_x[k]:
                        self.max_suite_x[k] = temp_x
                    temp_y[key] += 1
                    if temp_y[key] > self.max_suite_y[key]:
                        self.max_suite_y[key] += 1
                else:
                    temp_x = 0
                    temp_y[key] = 0

        open_file.close()
        # self.map.pop(0)
        # print(self.map)
        # print(self.nb_point_x)
        # print(self.nb_point_y)
        # print(self.max_suite_x.values())
        # print(self.max_suite_y.values())
        # print(temp_y)
        max_x = self.calc_max_suite(self.max_suite_x)
        max_y = self.calc_max_suite(self.max_suite_y)
        self.max_suite = min(max_x, max_y)
        # print(max_x)
        # print(max_y)
        # print(self.max_suite)

        self.coordonnes_carre()
        print(math.sqrt(len(self.coordonnees)))
        self.placement()

    def calc_max_suite(self, tab_suite):
        max_x = 0
        temp_x = 0
        temp_suite = copy.copy(self.columns)
        temp_inc = 0
        for key, value in tab_suite.items():
            if value > max_x:
                temp_x += 1
                # print(value)
                if temp_x > max_x:
                    max_x = copy.copy(temp_x)
                if temp_suite > value:
                    temp_suite = copy.copy(value)
                if (temp_suite == value):
                    temp_inc += 1
                if temp_suite == temp_x:
                    # print(temp_inc)
                    temp_x = temp_x - temp_inc
                    temp_inc = 0
                    # print('value:', value, '___ temp_suite:', temp_suite)
                    tab_mini = list()
                    for x in range(0, temp_suite-1):
                        tab_mini.append(copy.copy(tab_suite[key-x]))
                    temp_suite = (min(tab_mini))
            else:
                temp_x = 0
                temp_suite = copy.copy(self.columns)
                temp_inc = 0

        return max_x

    def checker(self, x, y, carre):
        for a in range(0, carre):
            for b in range(0, carre):
                if self.map[x+a][y-b] == '.':
                    self.coordonnees.append([x+a, y-b])
                if self.map[x+a][y-b] == 'o':
                    self.coordonnees = list()
                    return False
        return True

    def coordonnes_carre(self):
        carre = copy.copy(self.max_suite)
        if carre == 0:
            return False
        while carre > 0:
            for x, v in enumerate(self.map):
                if self.lines - x >= carre:
                    for y in range(0, self.columns-1):
                        if self.map[x][y] == '.':
                            if self.checker(x, y, carre):
                                return True
            carre -= 1

    def placement(self):
        for value in self.coordonnees:
            self.map[value[0]][value[1]] = 'x'
        for v in self.map:
            print(v)


ins = Bsq(sys.argv[1])
