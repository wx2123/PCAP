# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 22:04:05 2022

@author: xuewu
"""


# 3.2.1.2 A short journey from procedural to object approach

stack = []


def push(val):
    stack.append(val)


def pop():
    val = stack[-1]
    del stack[-1]
    return val


push(3)
push(2)
push(1)

print(pop())
print(pop())
print(pop())
