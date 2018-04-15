from random import choice

class RandomWalk():

    def __init__(self, size=5000):
        self.size = size

        self.points = [(0,0)]

    def fill_walk(self):
        while len(self.points) < self.size:
            x_step = choice([1, -1]) * choice([0, 1, 2, 3, 4])
            y_step = choice([1, -1]) * choice([0, 1, 2, 3, 4])

            if x_step == 0 and y_step == 0:
                continue

            point = self.points[-1]
            next_x = point[0] + x_step
            next_y = point[1] + y_step

            self.points.append((next_x, next_y))

    def x_values(self):
        return self.values(0)

    def y_values(self):
        return self.values(1)

    def values(self, index):
        values = []
        for point in self.points:
            values.append(point[index])
        return values;
