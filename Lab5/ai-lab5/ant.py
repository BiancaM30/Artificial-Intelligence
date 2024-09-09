from random import randint


class Ant:
    def __init__(self, nodes):
        self.visited = [randint(1, nodes)]
        self.distance = 0