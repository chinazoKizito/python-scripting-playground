# Advanced Python
# Object Oriented Programming
class PartyAnimal:
    x = 0

    def party(self):
        self.x = self.x + 1
        print("so far", self.x)


an = PartyAnimal()

an.party()
an.party()
an.party()
an.party()

# Using dir() to find the capabilities of our newly create class
print("Type:", type(an))
print("Dir:", dir(an))

class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('black', 11)
cat2 = Cat('white', 9)
cat3 = Cat('brown', 5)
cat4 = Cat('Kitty', 34)


# 2 Create a function that finds the oldest cat
def oldest(*args):
    names_ages = []
    for item in args:
        names_ages.append((item.age, item.name))
    names_ages.sort(reverse=True)
    return f"The oldest cat is {names_ages[0][1]}, it is {names_ages[0][0]} years old"


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #
print(oldest(cat1, cat2, cat3, cat4))


## @ClassMethod and @StaticMethod
class PlayerCharacter:
    type = "Warrior"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def shout(self):
        return f'My name is {self.name}, I am {self.age} years old'

    @classmethod
    def add_things(cls, num1, num2):
        # Returns an instance of PlayerCharacter with numerical parameters as age
        return cls("Okoro", num1 + num2)

    @staticmethod
    def multiply_things(num1, num2):
        return num1 * num2


# Dunder methods
# more on this can be found in the python documentation for how to use dunder methods
class Toy:
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {"name": "Yoyo", "has_pets": False}

    def __str__(self):
        return f"{self.color}"

    def __len__(self):
        return 5

    def __getitem__(self, item):
        return self.my_dict[item]

    def __call__(self):
        return "Yesss??"


# Inheritance and multiple inheritance
class User:
    def sign_in(self):
        print("signed in successfully")


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"{self.name}, attacking with a power of {self.power}")


class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def check_arrows(self):
        print(f"num of arrows remaining: {self.arrows}")


# Multople Inheritance
class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)


# functional programming lambda funtions
from functools import reduce

li = [1, 2, 3, 4, 5, 6]
print(list(map(lambda item: item * 2, li)))

print(list(filter(lambda item: item % 2 != 0, li)))

print(reduce(lambda acc, item: acc + item, li))

# lamda for list sorting
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
a.sort(key=lambda x: x[1])
print(a)

# List Comprehension
my_list = [w for w in "Hello"]
my_list2 = [num for num in range(0, 100)]
my_list3 = [num ** 2 for num in range(0, 100)]
my_list4 = [num ** 2 for num in range(0, 100) if num % 2 == 0]

# set comprehension
my_set = {w for w in "Hello"}
my_set2 = {num for num in range(0, 100)}
my_set3 = {num ** 2 for num in range(0, 100)}
my_set4 = {num ** 2 for num in range(0, 100) if num % 2 == 0}
# list and set comprehension to solve get duplicates in a list
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = list({i for i in some_list if some_list.count(i) >= 2})

# Dictionary comprehension
simple_dict = {'a': 1, 'b': 2}
my_dict = {k: v ** 2 for k, v in simple_dict.items()}
# create a new dictionary only if number is even
my_dict2 = {k: v ** 2 for k, v in simple_dict.items() if v % 2 == 0}
# new dict with num as key and square(num) as value
my_dict3 = {v: v ** 2 for v in [1, 2, 3]}
print(my_dict3)


# Decorators
# Decorator Pattern
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print("***********")
        func(*args, **kwargs)
        print('***********')

    return wrap_func


@my_decorator
def say_bye(x, y, z, l):
    print(f"Bye friendy {x}, {y}, {z} and {l}")


@my_decorator
def hello(greeting, emoji=':('):
    print(greeting, emoji)


hello('hiiiiii')
say_bye('Chibuzor', "amaka", "amara", "friends")

from time import time


# Performance function to measure the time it takes to run a function
def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        results = fn(*args, **kwargs)
        t2 = time()
        print(f"time taken {t2 - t1}s")
        return results

    return wrapper


# perfromance decorator use case
@performance
def long_time():
    for i in range(10000000):
        i * 5


long_time()

# Create an @authenticated decorator that only allows the function to run if user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True  # changing this will either run or not run the message_friends function.
}


def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]['valid']:
            return fn(*args, **kwargs)

    return wrapper


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)

# Error handling in python
while True:
    try:
        age = int(input("What is your age? "))
        a = 10 / age
        print(f"10/age = {a}")
    except ValueError:
        print("please enter a number")
    except ZeroDivisionError:
        print("please enter age greater than zero")
    else:
        print('Thank you')
        break
    finally:
        print("Okay I'm finally done")


def divide(num1, num2):
    try:
        return num1 / num2
    except TypeError as err:
        print(f"{err}")
    except (TypeError, ZeroDivisionError) as err:
        print(err)


print(divide(2, 0))


# Standard way of creating a generator function using range and yield keyword
def generator_function(num):
    for i in range(num):
        yield i


g = generator_function(100)
next(g)
next(g)
print(next(g))


# For loop under the hood
def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator) * 2)
        except StopIteration:
            break


special_for([1, 2, 3])


# Range function under the hood
class MyGen:
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration


gen = MyGen(0, 100)

for i in gen:
    print(i)

# Implementing Fibonacci numbers with a generator
def fibonacci(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        temp = a
        a = b
        b = temp + b

for item in fibonacci(20):
    print(item)

# Implementing Fibonacci numbers with a list
def fib(num):
    a = 0
    b = 1
    result = []
    for i in range(num):
        result.append(a)
        temp = a
        a = b
        b = temp + b
    return result

print(fib(20))
