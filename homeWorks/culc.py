class Culculator:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def __add__(self):
        return self.n1 + self.n2

    def __sub__(self):
        return  self.n1 - self.n2

    def __mul__(self):
        return self.n1 * self.n2

    def __truediv__(self):
        return  self.n1 / self.n2
