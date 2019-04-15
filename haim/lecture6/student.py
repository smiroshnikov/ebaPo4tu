class Rectangle:
    pass


class Student:
    def __init__(self, id, lastName, avg, money):
        self.id = id
        self.lastName = lastName
        self.avg = avg
        self.money = money

    def give_money(self):
        if self.money - 1 > 1:
            return ("Student has no loan d")
