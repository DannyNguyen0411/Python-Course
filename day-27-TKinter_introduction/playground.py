# Many Positional arguments "args"
def add(*args):
    print(args[2])
    result = sum(args)
    return result

def add_two(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(1, 2, 3, 6, 100, 100))

# Many Keywords arguments "kwargs"
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan", color="Rainbow")
print(my_car.color)