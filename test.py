import math

print("I like to be a module.")

import module

print("I like to be a module.")
print(__name__)


if __name__ == "__main__":
    print("I prefer to be a module.")
else:
    print("I like to be a module.")

counter = 0
if __name__ == "__main__":
    print("I prefer to be a module.")
else:
    print("I like to be a module.")
    
import module
print(module.counter)


#!/usr/bin/env python3 

""" module.py - an example of a Python module """

__counter = 0


def suml(the_list):
    global __counter
    __counter += 1
    the_sum = 0
    for element in the_list:
        the_sum += element
    return the_sum


def prodl(the_list):
    global __counter    
    __counter += 1
    prod = 1
    for element in the_list:
        prod *= element
    return prod


if __name__ == "__main__":
    print("I prefer to be a module, but I can do some tests for you.")
    my_list = [i+1 for i in range(5)]
    print(suml(my_list) == 15)
    print(prodl(my_list) == 120)

from module import suml, prodl
zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))

import sys
for p in sys.path:
    print(p)

from sys import path
path.append('..\\modules')
import module
zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module.suml(zeroes))
print(module.prodl(ones))


# main2.py
from sys import path
path.append('..\\packages')
import extra.iota
print(extra.iota.funI())

from sys import path
path.append('..\\packages')

from extra.iota import funI
print(funI())



from sys import path
path.append('..\\packages')

import extra.good.best.sigma
from extra.good.best.tau import funT

print(extra.good.best.sigma.funS())
print(funT())

from sys import path
path.append('..\\packages')
import extra.good.best.sigma as sig
import extra.good.alpha as alp
print(sig.funS())
print(alp.funA())



from sys import path
path.append('..\\packages\\extrapack.zip')

import extra.good.best.sigma as sig
import extra.good.alpha as alp
from extra.iota import funI
from extra.good.beta import funB

print(sig.funS())
print(alp.funA())
print(funI())
print(funB())


import sys
if __name__ == "__main__":
    print "Don't do that!"
    sys.exit()

import sys
# note the double backslashes!
sys.path.append("D:\\Python\\Project\\Modules")

pip help

pip help operation

pip show package_name

pip show pip