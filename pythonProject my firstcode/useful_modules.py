from collections import Counter, OrderedDict, defaultdict

# Counter is used to count how many times an item appeared in a list/word
li = [1, 2, 3, 4, 5, 6, 7, 7, 8, ]
a = "Obi is a boy"
b = a.strip(" ")
print(Counter(li))
print(Counter(b))

# default dict is used to avoid key errors when calling dictionaries
dictionary = defaultdict(lambda: "None Existent Key", {'a': 1, 'b': 2})
print(dictionary['c'])

# OrderdDict retains the order that you insert into a dictionary strictly
d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1

# not equal because of the order, normal dictionary will not execute to false
print(d==d2)

import datetime
# time object
time = datetime.time(22, 35, 13)
print(time)
# Date object for today
today = datetime.date.today()
print(today)

from array import array

# Array with datatype specification
arr = array('i', [1, 2, 3])
print(arr)

import pdb
#built in debugger

def add(num1, num2):
    pdb.set_trace()
    return num1 + num2

print(add(3, 'kkkk'))


import re
# Regular expressions
string = 'search, search, search for a piece of text'

a = re.search('search', string)

# Index of start and stop for the string
print(a.span())


# Mulitiple searches
pattern = re.compile('search')
# Find all instances of the string
b = pattern.findall(string)
print(b)
# Returns a full match object if string is a full match of another string else None
c = pattern.fullmatch(string)
# Returns the match based on  the beginning of the string

print(c)

# returns part of the string that there was a match
print(a.group())
