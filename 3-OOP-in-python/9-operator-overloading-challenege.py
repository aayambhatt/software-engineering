class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        print("self: ", self.x, self.y)
        print("other: ", other.x, other.y)
        return Vector(0,0)


v1 = Vector(1, 2)   # self.x = 1, self.y = 2
v2 = Vector(3, 4)   # other.x = 3, other.y = 4

v3 = v1 + v2        # this triggers __add__(self=v1, other=v2)
