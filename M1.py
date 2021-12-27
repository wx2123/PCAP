# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 15:35:28 2021

@author: xuewu
"""

# 1.1.1.5 Importing a module | math
import math
print(math.sin(math.pi/2))

# 1.1.1.6 Importing a module | math
import math

def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None

pi = 3.14

print(sin(pi/2))
print(math.sin(math.pi/2))

# 1.1.1.7 Importing a module | math
from math import sin, pi
print(sin(pi/2))


# 1.1.1.8 Importing a module | math
pi = 3.14

def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None
print(sin(pi / 2))

from math import sin, pi

print(sin(pi / 2))


import math
for name in dir(math):
    print(name, end="\t")

import math
dir(math)


# 1.2.1.4 Useful modules | math
from math import ceil, floor, trunc

x = 1.4
y = 2.6

print(floor(x), floor(y))
print(floor(-x), floor(-y))
print(ceil(x), ceil(y))
print(ceil(-x), ceil(-y))
print(trunc(x), trunc(y))
print(trunc(-x), trunc(-y))

# 1.2.1.6 Useful modules | random

from random import random, seed

seed(0)

for i in range(5):
    print(random())

# 1.2.1.7 Useful modules | random
from random import randrange, randint

print(randrange(1), end=' ')
print(randrange(0, 1), end=' ')
print(randrange(0, 1, 1), end=' ')
print(randint(0, 1))


# 1.2.1.8 Useful modules | random

from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list))
print(sample(my_list, 5))
print(sample(my_list, 10))

