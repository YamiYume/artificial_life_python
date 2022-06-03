from location_tree import RBtree
from numpy import sum as npsum


class PositionManager():

    def __init__(self, population):
        self.xtree = RBtree(0)
        self.ytree = RBtree(1)
        for organism in population:
            self.xtree.insert_organism(organism)
            self.ytree.insert_organism(organism)

    def refresh(self, population):
        self.xtree = RBtree(0)
        self.ytree = RBtree(1)
        for organism in population:
            self.xtree.insert_organism(organism)
            self.ytree.insert_organism(organism)

    def verify_move(self, move):
        column = self.xtree.search_key(move[0], self.xtree.root).value
        row = self.ytree.search_key(move[1], self.ytree.root).value
        return not bool(set(column).intersection(set(row)))

    def get_x_quantities(self, coordinate, population_size):
        quantities = []
        for i in range(coordinate):
            try:
                quantities.append(
                    len(self.xtree.search_key(i, self.xtree.root)))
            except KeyError:
                pass
        return npsum(quantities) / population_size

    def get_y_quantites(self, coordinate, population_size):
        quantities = []
        for i in range(coordinate):
            try:
                quantities.append(
                    len(self.ytree.search_key(i, self.ytree.root)))
            except KeyError:
                pass
        return npsum(quantities) / population_size
