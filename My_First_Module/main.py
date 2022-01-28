# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 22:35:06 2022

@author: xuewu
"""

from module import suml, prodl

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))

import sys

for p in sys.path:
    print(p)

