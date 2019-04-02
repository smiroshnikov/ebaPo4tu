# class MyFirstClass:
#     pass
#
#
# a = MyFirstClass()
# b = MyFirstClass()
#
# print(a)
# print(b)
#
#
# class Point:
#     def reset(self):
#         self.x = 0
#         self.y = 0
#

import math


#
# p1 = Point()
# p2 = Point()
#
# p1.x = 5
# p1.y = 0
# p2.x = -9
# p2.y = 10
# print(f"p1({p1.x} {p1.y}),p2({p2.x}{p2.y})")
# p1.reset()
# print(f"{p1.x},{p1.y}")
#
# p = Point()
# Point.reset(p)
# print(p.x, p.y)


class PointV20:
    """
    Represents a point in 2D space
    """

    def __init__(self, x=0, y=0):
        """
        Initialize new point , if x , y not specified defaults to origin (0,0)
        :param x: x position
        :param y: y y position
        """
        self.move(x, y)
        # self.x = x
        # self.y = y

    def move(self, x, y):
        """
        moves point to required location
        :param x:
        :param y:
        :return:
        """
        self.x = x
        self.y = y

    def reset(self):
        """
        resets back to origin
        :return:
        """
        self.move(0, 0)

    def calculate_distance(self, other_point):
        """
        Calculates a distance , 2nd Point passed as parameter
        :param other_point:
        :return:
        """
        return math.sqrt(
            (self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)


print(help(PointV20))

point1 = PointV20(1, 2)
point2 = PointV20(0, -3)
point1.reset()
point2.move(5, 0)
print(point2.calculate_distance(point1))
assert (point2.calculate_distance(point1) ==
        point1.calculate_distance(point2))
point1.move(3, 4)
print(point1.calculate_distance(point2))
print(point1.calculate_distance(point1))
