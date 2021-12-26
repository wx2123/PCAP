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

