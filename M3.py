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

# 3.2.1.4 A short journey from procedural to object approach

class Stack:  # Defining the Stack class.
    def __init__(self):  # Defining the constructor function.
        print("Hi!")

stack_object = Stack()  # Instantiating the object.



# 3.2.1.7 A short journey from procedural to object approach
class Stack:
    def __init__(self):
        self.__stack_list = []


    def push(self, val):
        self.__stack_list.append(val)


    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


stack_object = Stack()

stack_object.push(3)
stack_object.push(2)
stack_object.push(1)

print(stack_object.pop())
print(stack_object.pop())
print(stack_object.pop())


# # 3.2.1.8 A short journey from procedural to object approach
class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

stack_object_1 = Stack()
stack_object_2 = Stack()

stack_object_1.push(3)
stack_object_2.push(stack_object_1.pop())

print(stack_object_2.pop())
