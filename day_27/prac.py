# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
#
#
# print(add(3, 5, 4, 6))


def calculate(**kwargs):
    for key, value in kwargs.items():
        print(key)
        print(value)


calculate(add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")  # same as self.make = kw["make"]
        self.model = kw.get("model")
        self.colour = kw.get("colour")


my_car = Car(make="Nissan", model="GT-R", colour="Red")
print(my_car.colour)
