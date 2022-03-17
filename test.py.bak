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

pip install pygame


import pygame
run = True
width = 400
height = 100
pygame.init()
screen = pygame.display.set_mode((width, height))
font = pygame.font.SysFont(None, 48)
text = font.render("Welcome to pygame", True, (255, 255, 255))
screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2))
pygame.display.flip()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT\
        or event.type == pygame.MOUSEBUTTONUP\
        or event.type == pygame.KEYUP:
            run = False
multiline = 'Line #1
Line #2'
print(len(multiline))


multiline = '''Line #1
Line #2'''
print(len(multiline))

multiline = """Line #1
Line #2"""
print(len(multiline))

# Demonstrating the ord() function.

char_1 = 'a'
char_2 = ' '  # space

print(ord(char_1))
print(ord(char_2))

# Demonstrating the chr() function.
print(chr(97))  # output: a
print(chr(945)) # output: α

# Indexing strings.
the_string = 'silly walks'
for ix in range(len(the_string)):
    print(the_string[ix], end=' ')
print()

# Iterating through a string.
the_string = 'silly walks'
for character in the_string:
    print(character, end=' ')
print()


alphabet = "bcdefghijklmnopqrstuvwxy"
alphabet = "a" + alphabet
alphabet = alphabet + "z"
print(alphabet)


# Demonstrating min() - Example 1:
print(min("aAbByYzZ"))
# Demonstrating min() - Examples 2 & 3:
t = 'The Knights Who Say "Ni!"'
print('[' + min(t) + ']')
t = [0, 1, 2]
print(min(t))

# Demonstrating max() - Example 1:
print(max("aAbByYzZ"))
# Demonstrating max() - Examples 2 & 3:
t = 'The Knights Who Say "Ni!"'
print('[' + max(t) + ']')
t = [0, 1, 2]
print(max(t))

# Demonstrate the index() method:
print("aAbByYzZaA".index("b")) # outputs: 2
print("aAbByYzZaA".index("Z")) # outputs: 7
print("aAbByYzZaA".index("A")) # outputs: 1


# Demonstrating the list() function:
print(list("abcabc"))                # outputs: ['a', 'b', 'c', 'a', 'b', 'c']
#Demonstrating the count() method:
print("abcabc".count("b"))           # outputs: 2
print('abcabc'.count("d"))           # outputs: 0


asterisk = '*'
plus = "+"
decoration = (asterisk + plus) * 4 + asterisk
print(decoration)
outputs *+*+*+*+*.

# Demonstrating the capitalize() method:
print('aBcD'.capitalize()) # output: Abcd

print("Alpha".capitalize()) # Output: Alpha
print('ALPHA'.capitalize()) # Output: Alpha
print(' Alpha'.capitalize())# Output:  alpha
print('123'.capitalize())   # Output: 123
print("αβγδ".capitalize())  # Output: Αβγδ


Output:
Alpha
Alpha
 alpha
123
Αβγδ


# Demonstrating the center() method:
print('[' + 'alpha'.center(10) + ']') # output: [  alpha   ]

print('[' + 'Beta'.center(2) + ']') #output: [Beta]
print('[' + 'Beta'.center(4) + ']') #output: [Beta]
print('[' + 'Beta'.center(6) + ']') #output: [ Beta ]
Output:
[Beta]
[Beta]
[ Beta ]

print('[' + 'gamma'.center(20, '*') + ']')

# Demonstrating the endswith() method:
if "epsilon".endswith("on"):
    print("yes")
else:
    print("no")
    
    
t = "zeta"
print(t.endswith("a"))   #output: True
print(t.endswith("A"))   #output: False
print(t.endswith("et"))  #output: False
print(t.endswith("eta")) #output: True
Output:
True
False
False
True


# Demonstrating the find() method:
print("Eta".find("ta"))    #output: 1
print("Eta".find("mma"))   #output: -1

t = 'theta'
print(t.find('eta')) #output: 2
print(t.find('et'))  #output: 2
print(t.find('the')) #output: 0
print(t.find('ha'))  #output: -1
Output:
2
2
0
-1

print('kappa'.find('a', 2))  #output: 4 


the_text = """A variation of the ordinary lorem ipsum text has been used in 		type setting since the 1960s or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to the Information Age in the 	mid-1980s by the Aldus Corporation, which employed it in graphics and 	word-processing templatesfor its desktop publishing program PageMaker """
fnd = the_text.find('the')
while fnd != -1:
    print(fnd)
    fnd = the_text.find('the', fnd + 1)	
print('kappa'.find('a', 1, 4))  #output: 1 
print('kappa'.find('a', 2, 4))  #output: -1


# Demonstrate isalnum() method:
print('lambda30'.isalnum())  #output: True 
print('lambda'.isalnum())    #output: True
print('30'.isalnum())        #output: True
print('@'.isalnum())         #output: False
print('lambda_30'.isalnum()) #output: False
print(''.isalnum())          #output: False

The example output is:
True
True
True
False
False
False

t = 'Six lambdas'
print(t.isalnum()) #False
t = 'ΑβΓδ'
print(t.isalnum())#True
t = '20E1'
print(t.isalnum())#True

# Example 1: Demonstrating the isapha() method:
print("Moooo".isalpha()) # True
print('Mu40'.isalpha()) # False

# Example 2: Demonstrating the isdigit() method:
print('2018'.isdigit())  # True
print("Year2019".isdigit()) # False

# Example 1: Demonstrating the islower() method:
print("Moooo".islower())  #False
print('moooo'.islower())   #True

# Example 2: Demonstrating the isspace() method:
print(' \n '.isspace()) #True
print(" ".isspace()) #True
print("mooo mooo mooo".isspace()) #False


# Example 3: Demonstrating the isupper() method:
print("Moooo".isupper())  # False
print('moooo'.isupper())   # False
print('MOOOO'.isupper())  # True

# Demonstrating the join() method:
print(",".join(["omicron", "pi", "rho"]))

# Demonstrating the lower() method:
print("SiGmA=60".lower())

# Demonstrating the lstrip() method:
print("[" + " tau ".lstrip() + "]") # [tau ]
output
[tau ]

print("www.cisco.com".lstrip("w."))

print("pythoninstitute.org".lstrip(".org"))  #output:pythoninstitute.org


# Demonstrating the replace() method:
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org")) 
#www.pythoninstitute.org
print("This is it!".replace("is", "are"))  #Thare are it!
print("Apple juice".replace("juice", ""))  #Apple


print("This is it!".replace("is", "are", 1))     # Thare is it!
print("This is it!".replace("is", "are", 2))     #Thare are it!


# Demonstrating the rfind() method:
print("tau tau tau".rfind("ta"))      #8 
print("tau tau tau".rfind("ta", 9))    #-1 
print("tau tau tau".rfind("ta", 3, 9))  #4 

# Demonstrating the rstrip() method:
print("[" + " upsilon ".rstrip() + "]")  # [ upsilon]
print("cisco.com".rstrip(".com"))    # cis

# Demonstrating the split() method:
print("phi       chi\npsi".split())  #['phi', 'chi', 'psi']


# Demonstrating the startswith() method:
print("omega".startswith("meg"))  #False
print("omega".startswith("om"))   #True

# Demonstrating the strip() method:
print("[" + "   aleph   ".strip() + "]")  # [aleph]


# Demonstrating the swapcase() method:
print("I know that I know nothing.".swapcase())
# Output: i KNOW THAT i KNOW NOTHING.

# Demonstrating the title() method:
print("I know that I know nothing. Part 1.".title())
Output: I Know That I Know Nothing. Part 1.

# Demonstrating the upper() method:
print("I know that I know nothing. Part 2.".upper())
#output I KNOW THAT I KNOW NOTHING. PART 2.


greek = ['omega', 'alpha', 'pi', 'gamma']

# Demonstrating the sorted() function:
first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek)
print(first_greek)  # ['omega', 'alpha', 'pi', 'gamma']
print(first_greek_2) # ['alpha', 'gamma', 'omega', 'pi']

# Demonstrating the sort() method:
second_greek = ['omega', 'alpha', 'pi', 'gamma']
print(second_greek)  # ['omega', 'alpha', 'pi', 'gamma']
second_greek.sort()
print(second_greek)   #['alpha', 'gamma', 'omega', 'pi']

itg = 13
flt = 1.3
si = str(itg)
sf = str(flt)
print(si + ' ' + sf) # outputs: 13 1.3

si = '13'
sf = '1.3'
itg = int(si)
flt = float(sf)
print(itg + flt)
# This is what you'll see in the console: 14.3

# Caesar cipher.
text = input("Enter your message: ")
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)


# Caesar cipher - decrypting a message.
cipher = input('Enter your cryptogram: ')
text = ''
for char in cipher:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)
print(text)

# Numbers Processor.
line = input("Enter a line of numbers - separate them with spaces: ")
strings = line.split()
total = 0
try:
    for substr in strings:
        total += float(substr)
    print("The total is:", total)
except:
    print(substr, "is not a number.")


# IBAN Validator.

iban = input("Enter IBAN, please: ")
iban = iban.replace(' ','')

if not iban.isalnum():
    print("You have entered invalid characters.")
elif len(iban) < 15:
    print("IBAN entered is too short.")
elif len(iban) > 31:
    print("IBAN entered is too long.")
else:
    iban = (iban[4:] + iban[0:4]).upper()
    iban2 = ''
    for ch in iban:
        if ch.isdigit():
            iban2 += ch
        else:
            iban2 += str(10 + ord(ch) - ord('A'))
    iban = int(iban2)
    if iban % 97 == 1:
        print("IBAN entered is valid.")
    else:
        print("IBAN entered is invalid.")
        
import math

x = float(input("Enter x: "))
y = math.sqrt(x)

print("The square root of", x, "equals to", y)

value = 1
value /= 0

my_list = []
x = my_list[0]


first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
if second_number != 0:
    print(first_number / second_number)
else:
    print("This operation cannot be done.")
print("THE END.")


first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
try:
    print(first_number / second_number)
except:
    print("This operation cannot be done.")
print("THE END.")


try:
    print("1")
    x = 1 / 0
    print("2")
except:
    print("Oh dear, something went wrong...")
print("3")

try:
    x = int(input("Enter a number: "))
    y = 1 / x
except:
    print("Oh dear, something went wrong...")
print("THE END.")

try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("You cannot divide by zero, sorry.")
except ValueError:
    print("You must enter an integer value.")
except:
    print("Oh dear, something went wrong...")
print("THE END.")

try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except ValueError:
    print("You must enter an integer value.")
except:
    print("Oh dear, something went wrong...")
print("THE END.")


try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except ValueError:
    print("You must enter an integer value.")
print("THE END.")


try:
    print("Let's try to do this")
    print("#"[2])
    print("We succeeded!")
except:
    print("We failed")
print("We're done")


try:
    print("alpha"[1/0])
except ZeroDivisionError:
    print("zero")
except IndexingError:
    print("index")
except:
    print("some")
# Check: zero


try:
    y = 1 / 0
except ZeroDivisionError:
    print("Oooppsss...")
print("THE END.")

try:
    y = 1 / 0
except ArithmeticError:
    print("Oooppsss...")
print("THE END.")


try:
    y = 1 / 0
except ZeroDivisionError:
    print("Zero Division!")
except ArithmeticError:
    print("Arithmetic problem!")
print("THE END.")

try:
    y = 1 / 0
except ArithmeticError:
    print("Arithmetic problem!")
except ZeroDivisionError:
    print("Zero Division!")
print("THE END.")

def bad_fun(n):
    try:
        return 1 / n
    except ArithmeticError:
        print("Arithmetic Problem!")
    return None
bad_fun(0)
print("THE END.")


def bad_fun(n):
    return 1 / n
try:
    bad_fun(0)
except ArithmeticError:
    print("What happened? An exception was raised!")
print("THE END.")


raise exc

def bad_fun(n):
    raise ZeroDivisionError
try:
    bad_fun(0)
except ArithmeticError:
    print("What happened? An error?")
print("THE END.")

raise

def bad_fun(n):
    try:
        return n / 0
    except:
        print("I did it again!")
        raise
try:
    bad_fun(0)
except ArithmeticError:
    print("I see!")
print("THE END.")



assert expression


import math
x = float(input("Enter a number: "))
assert x >= 0.0
x = math.sqrt(x)
print(x)

try:
    print(1/0)
except ZeroDivisionError:
    print("zero")
except ArithmeticError:
    print("arith")
except:
    print("some")
    
    

try:
    print(1/0)
except ArithmeticError:
    print("arith")
except ZeroDivisionError:
    print("zero")
except:
    print("some")


def foo(x):
    assert x
    return 1/x
try:
    print(foo(0))
except ZeroDivisionError:
    print("zero")
except:
    print("some")
    
from math import tan, radians
angle = int(input('Enter integral angle in degrees: '))
# We must be sure that angle != 90 + k * 180
assert angle % 180 != 90
print(tan(radians(angle)))


# The code shows an extravagant way
# of leaving the loop.
the_list = [1, 2, 3, 4, 5]
ix = 0
do_it = True
while do_it:
    try:
        print(the_list[ix])
        ix += 1
    except IndexError:
        do_it = False
print('Done')


# This code cannot be terminated by pressing Ctrl-C.
from time import sleep
seconds = 0
while True:
    try:
        print(seconds)
        seconds += 1
        sleep(1)
    except KeyboardInterrupt:
        print("Don't do that!")
        
        
Code:
# This code causes the MemoryError exception.
# Warning: executing this code may affect your OS.
# Don't run it in production environments!
string = 'x'
try:
    while True:
        string = string + string
        print(len(string))
except MemoryError:
    print('This is not funny!')
    
    
# The code prints subsequent
# values of exp(k), k = 1, 2, 4, 8, 16, ...
from math import exp
ex = 1
try:
    while True:
        print(exp(ex))
        ex *= 2
except OverflowError:
    print('The number is too big.')



# One of these imports will fail - which one?
try:
    import math
    import time
    import abracadabra
except:
    print('One of your imports has failed.')



# How to abuse the dictionary
# and how to deal with it?
dictionary = { 'a': 'b', 'b': 'c', 'c': 'd' }
ch = 'a'
try:
    while True:
        ch = dictionary[ch]
        print(ch)
except KeyError:
    print('No such key:', ch)


class TheSimplestClass:
    pass
    
my_first_object = TheSimplestClass()

class This_Is_A_Class:
     pass

this_is_an_object = This_Is_A_Class()

stack = []

def push(val):
    stack.append(val)
    
    
def pop():
    val = stack[-1]
    del stack[-1]
    return val



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
print(pop())  # outputs:1
print(pop())  # outputs:2
print(pop())  # outputs:3


class Stack:
    def __init__(self):
        print("Hi!")
stack_object = Stack()

class Stack:

class Stack:
    def __init__(self):
        self.stack_list = []
stack_object = Stack()
print(len(stack_object.stack_list))

class Stack:
    def __init__(self):
        self.__stack_list = []
stack_object = Stack()
print(len(stack_object.__stack_list))


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



class Stack:
    def __init__(self):
        self.__stack_list = []
    def push(self, val):
        self.__stack_list.append(val)
    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val
little_stack = Stack()
another_stack = Stack()
funny_stack = Stack()
little_stack.push(1)
another_stack.push(little_stack.pop() + 1)
funny_stack.push(another_stack.pop() - 2)
print(funny_stack.pop())


class AddingStack(Stack):
    pass
    
class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0



def push(self, val):
    self.__sum += val
    Stack.push(self, val)


def pop(self):
    val = Stack.pop(self)
    self.__sum -= val
    return val

def get_sum(self):
    return self.__sum



class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def get_sum(self):
        return self.__sum

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val


stack_object = AddingStack()

for i in range(5):
    stack_object.push(i)
print(stack_object.get_sum())

for i in range(5):
    print(stack_object.pop())



class ExampleClass:
    def __init__(self, val = 1):
        self.first = val

    def set_second(self, val):
        self.second = val


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)

example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.third = 5

print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)


class ExampleClass:
    def __init__(self, val = 1):
        self.__first = val
    def set_second(self, val = 2):
        self.__second = val
example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_2.set_second(3)
example_object_3 = ExampleClass(4)
example_object_3.__third = 5
print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)

print(example_object_1._ExampleClass__first)


class ExampleClass:
    counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.counter += 1
example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)
print(example_object_1.__dict__, example_object_1.counter)
print(example_object_2.__dict__, example_object_2.counter)
print(example_object_3.__dict__, example_object_3.counter)


class ExampleClass:
    __counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.__counter += 1
example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)
print(example_object_1.__dict__, example_object_1._ExampleClass__counter)
print(example_object_2.__dict__, example_object_2._ExampleClass__counter)
print(example_object_3.__dict__, example_object_3._ExampleClass__counter)


class ExampleClass:
    varia = 1
    def __init__(self, val):
        ExampleClass.varia = val
print(ExampleClass.__dict__)
example_object = ExampleClass(2)
print(ExampleClass.__dict__)
print(example_object.__dict__)


class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1

example_object = ExampleClass(1)
print(example_object.a)
print(example_object.b)


class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1
example_object = ExampleClass(1)
print(example_object.a)
try:
    print(example_object.b)
except AttributeError:
    pass
    
    
class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1
example_object = ExampleClass(1)
print(example_object.a)
if hasattr(example_object, 'b'):
    print(example_object.b)
    
class ExampleClass:
    attr = 1
print(hasattr(ExampleClass, 'attr'))  # True
print(hasattr(ExampleClass, 'prop'))  # False

class ExampleClass:
    a = 1
    def __init__(self):
        self.b = 2
example_object = ExampleClass()
print(hasattr(example_object, 'b'))  # True
print(hasattr(example_object, 'a'))  # True
print(hasattr(ExampleClass, 'b'))    # False
print(hasattr(ExampleClass, 'a'))    # True


class Sample:
    gamma = 0 # Class variable.
    def __init__(self):
        self.alpha = 1 # Instance variable.
        self.__delta = 3 # Private instance variable.
obj = Sample()
obj.beta = 2 # Another instance variable (existing only inside the "obj" instance.)
print(obj.__dict__)


class Python:
    population = 1
    victims = 0
    def __init__(self):
        self.length_ft = 3
        self.__venomous = False


class Classy:
    def method(self):
        print("method")
obj = Classy()
obj.method()


class Classy:
    def method(self, par):
        print("method:", par)
obj = Classy()
obj.method(1) #output: 1
obj.method(2) #output: 2
obj.method(3) #output: 3


class Classy:
    varia = 2
    def method(self):
        print(self.varia, self.var)
obj = Classy()
obj.var = 3
obj.method()


class Classy:
    def other(self):
        print("other")
    def method(self):
        print("method")
        self.other()
obj = Classy()
obj.method()


class Classy:
    def __init__(self, value):
        self.var = value
obj_1 = Classy("object")
print(obj_1.var)


class Classy:
    def __init__(self, value = None):
        self.var = value

obj_1 = Classy("object")
obj_2 = Classy()

print(obj_1.var) #output: object
print(obj_2.var) #output: None


class Classy:
    def visible(self):
        print("visible")    
    def __hidden(self):
        print("hidden")
obj = Classy()
obj.visible()
try:
    obj.__hidden()
except:
    print("failed")
obj._Classy__hidden()

class Classy:
    varia = 1
    def __init__(self):
        self.var = 2
    def method(self):
        pass
    def __hidden(self):
        pass
obj = Classy()
print(obj.__dict__)
print(Classy.__dict__)

class Classy:
    pass
print(Classy.__name__)
obj = Classy()
print(type(obj).__name__)

print(obj.__name__)

class Classy:
    pass
print(Classy.__module__)
obj = Classy()
print(obj.__module__)


class SuperOne:
    pass
class SuperTwo:
    pass
class Sub(SuperOne, SuperTwo):
    pass
def printBases(cls):
    print('( ', end='')
    for x in cls.__bases__:
        print(x.__name__, end=' ')
    print(')')
printBases(SuperOne)
printBases(SuperTwo)
printBases(Sub)


class MyClass:
    pass
obj = MyClass()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5
def incIntsI(obj):
    for name in obj.__dict__.keys():
        if name.startswith('i'):
            val = getattr(obj, name)
            if isinstance(val, int):
                setattr(obj, name, val + 1)
print(obj.__dict__)
incIntsI(obj)
print(obj.__dict__)


class Sample:
    def __init__(self):
        self.name = Sample.__name__
    def myself(self):
        print("My name is " + self.name + " living in a " + Sample.__module__)
obj = Sample()
obj.myself()

class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy
sun = Star("Sun", "Milky Way")
print(sun)

class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy
    def __str__(self):
        return self.name + ' in ' + self.galaxy
sun = Star("Sun", "Milky Way")
print(sun)


class Vehicle:
    pass
class LandVehicle(Vehicle):
    pass
class TrackedVehicle(LandVehicle):
    pass

issubclass(ClassOne, ClassTwo)

class Vehicle:
    pass
class LandVehicle(Vehicle):
    pass
class TrackedVehicle(LandVehicle):
    pass
for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
    for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
        print(issubclass(cls1, cls2), end="\t")
    print()
   
isinstance(objectName, ClassName)

class Vehicle:
    pass
class LandVehicle(Vehicle):
    pass
class TrackedVehicle(LandVehicle):
    pass
my_vehicle = Vehicle()
my_land_vehicle = LandVehicle()
my_tracked_vehicle = TrackedVehicle()
for obj in [my_vehicle, my_land_vehicle, my_tracked_vehicle]:
    for cls in [Vehicle, LandVehicle, TrackedVehicle]:
        print(isinstance(obj, cls), end="\t")
    print()
    
    
    
    
class SampleClass:
    def __init__(self, val):
        self.val = val
object_1 = SampleClass(0)
object_2 = SampleClass(2)
object_3 = object_1
object_3.val += 1
print(object_1 is object_2)
print(object_2 is object_3)
print(object_3 is object_1)
print(object_1.val, object_2.val, object_3.val)
string_1 = "Mary had a little "
string_2 = "Mary had a little lamb"
string_1 += "lamb"
print(string_1 == string_2, string_1 is string_2)


class Super:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "My name is " + self.name + "."
class Sub(Super):
    def __init__(self, name):
        Super.__init__(self, name)
obj = Sub("Andy")
print(obj)

class Super:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "My name is " + self.name + "."
class Sub(Super):
    def __init__(self, name):
        super().__init__(name)
obj = Sub("Andy")
print(obj)


# Testing properties: class variables.
class Super:
    supVar = 1
class Sub(Super):
    subVar = 2
obj = Sub()
print(obj.subVar)
print(obj.supVar)

# Testing properties: instance variables.
class Super:
    def __init__(self):
        self.supVar = 11
class Sub(Super):
    def __init__(self):
        super().__init__()
        self.subVar = 12
obj = Sub()
print(obj.subVar)
print(obj.supVar)


class Level1:
    variable_1 = 100
    def __init__(self):
        self.var_1 = 101
    def fun_1(self):
        return 102
class Level2(Level1):
    variable_2 = 200
    def __init__(self):
        super().__init__()
        self.var_2 = 201    
    def fun_2(self):
        return 202
class Level3(Level2):
    variable_3 = 300
    def __init__(self):
        super().__init__()
        self.var_3 = 301
    def fun_3(self):
        return 302
obj = Level3()
print(obj.variable_1, obj.var_1, obj.fun_1()) # 100 101 102
print(obj.variable_2, obj.var_2, obj.fun_2()) # 200 201 202
print(obj.variable_3, obj.var_3, obj.fun_3()) # 300 301 302


class SuperA:
    var_a = 10
    def fun_a(self):
        return 11
class SuperB:
    var_b = 20
    def fun_b(self):
        return 21
class Sub(SuperA, SuperB):
    pass
obj = Sub()
print(obj.var_a, obj.fun_a())
print(obj.var_b, obj.fun_b())

class Level1:
    var = 100
    def fun(self):
        return 101
class Level2(Level1):
    var = 200
    def fun(self):
        return 201
class Level3(Level2):
    pass
obj = Level3()
print(obj.var, obj.fun())


class Left:
    var = "L"
    var_left = "LL"
    def fun(self):
        return "Left"
class Right:
    var = "R"
    var_right = "RR"
    def fun(self):
        return "Right"
class Sub(Left, Right):
    pass
obj = Sub()
print(obj.var, obj.var_left, obj.var_right, obj.fun())

class One:
    def do_it(self):
        print("do_it from One")
    def doanything(self):
        self.do_it()
class Two(One):
    def do_it(self):
        print("do_it from Two")
one = One()
two = Two()
one.doanything()
two.doanything()


import time
class TrackedVehicle:
    def control_track(left, stop):
        pass
    def turn(left):
        control_track(left, True)
        time.sleep(0.25)
        control_track(left, False)
class WheeledVehicle:
    def turn_front_wheels(left, on):
        pass
    def turn(left):
        turn_front_wheels(left, True)
        time.sleep(0.25)
        turn_front_wheels(left, False)

import time
class Vehicle:
    def change_direction(left, on):
        pass
    def turn(left):
        change_direction(left, True)
        time.sleep(0.25)
        change_direction(left, False)
class TrackedVehicle(Vehicle):
    def control_track(left, stop):
        pass
    def change_direction(left, on):
        control_track(left, on)
class WheeledVehicle(Vehicle):
    def turn_front_wheels(left, on):
        pass
    def change_direction(left, on):
        turn_front_wheels(left, on)
        pass


import time
class Tracks:
    def change_direction(self, left, on):
        print("tracks: ", left, on)
class Wheels:
    def change_direction(self, left, on):
        print("wheels: ", left, on)
class Vehicle:
    def __init__(self, controller):
        self.controller = controller
    def turn(self, left):
        self.controller.change_direction(left, True)
        time.sleep(0.25)
        self.controller.change_direction(left, False)
wheeled = Vehicle(Wheels())
tracked = Vehicle(Tracks())
wheeled.turn(True)
tracked.turn(False)


class Top:
    def m_top(self):
        print("top")
class Middle(Top):
    def m_middle(self):
        print("middle")
class Bottom(Middle):
    def m_bottom(self):
        print("bottom")
object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()


class Top:
    def m_top(self):
        print("top")
class Middle(Top):
    def m_middle(self):
        print("middle")
class Bottom(Middle, Top):
    def m_bottom(self):
        print("bottom")
object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()


class Top:
    def m_top(self):
        print("top")
class Middle(Top):
    def m_middle(self):
        print("middle")
class Bottom(Top, Middle):
    def m_bottom(self):
        print("bottom")
object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()

class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(B, C):
    pass
d = D()

class Top:
    def m_top(self):
        print("top")
class Middle_Left(Top):
    def m_middle(self):
        print("middle_left")
class Middle_Right(Top):
    def m_middle(self):
        print("middle_right")
class Bottom(Middle_Left, Middle_Right):
    def m_bottom(self):
        print("bottom")
object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()

class Mouse:
    def __init__(self, name):
        self.my_name = name
    def __str__(self):
        return self.my_name
the_mouse = Mouse('mickey')
print(the_mouse)  # Prints "mickey". 

class Mouse:
    pass
class LabMouse(Mouse):
    pass
print(issubclass(Mouse, LabMouse), issubclass(LabMouse, Mouse))  
# Prints "False True"

class Mouse:
    pass
class LabMouse(Mouse):
    pass
mickey = Mouse()
print(isinstance(mickey, Mouse), isinstance(mickey, LabMouse))  
# Prints "True False".

class Mouse:
    pass
mickey = Mouse()
minnie = Mouse()
cloned_mickey = mickey
print(mickey is minnie, mickey is cloned_mickey)  # Prints "False True".

class Mouse:
    def __str__(self):
        return "Mouse"
class LabMouse(Mouse):
    def __str__(self):
        return "Laboratory " + super().__str__()
doctor_mouse = LabMouse();
print(doctor_mouse)  # Prints "Laboratory Mouse".

class Mouse:
    Population = 0
    def __init__(self, name):
        Mouse.Population += 1
        self.name = name
    def __str__(self):
        return "Hi, my name is " + self.name
class LabMouse(Mouse):
    pass
professor_mouse = LabMouse("Professor Mouser")
print(professor_mouse, Mouse.Population)  
# Prints "Hi, my name is Professor Mouser 1"

class Mouse:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "My name is " + self.name
class AncientMouse(Mouse):
    def __str__(self):
        return "Meum nomen est " + self.name
mus = AncientMouse("Caesar")  
print(mus)  # Prints "Meum nomen est Caesar"


class Dog:
    kennel = 0
    def __init__(self, breed):
        self.breed = breed
        Dog.kennel += 1
    def __str__(self):
        return self.breed + " says: Woof!"
class SheepDog(Dog):
    def __str__(self):
        return super().__str__() + " Don't run away, Little Lamb!"
class GuardDog(Dog):
    def __str__(self):
        return super().__str__() + " Stay where you are, Mister Intruder!"
rocky = SheepDog("Collie")
luna = GuardDog("Dobermann")

def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("Division failed")
        return None
    else:
        print("Everything went fine")
        return n
print(reciprocal(2))
print(reciprocal(0))


def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("Division failed")
        n = None
    else:
        print("Everything went fine")
    finally:
        print("It's time to say goodbye")
        return n
print(reciprocal(2))
print(reciprocal(0))

try:
    i = int("Hello!")
except Exception as e:
    print(e)
    print(e.__str__())



def print_exception_tree(thisclass, nest = 0):
    if nest > 1:
        print("   |" * (nest - 1), end="")
    if nest > 0:
        print("   +---", end="")
    print(thisclass.__name__)
    for subclass in thisclass.__subclasses__():
        print_exception_tree(subclass, nest + 1)
print_exception_tree(BaseException)


def print_args(args):
    lng = len(args)
    if lng == 0:
        print("")
    elif lng == 1:
        print(args[0])
    else:
        print(str(args))
try:
    raise Exception
except Exception as e:
    print(e, e.__str__(), sep=' : ' ,end=' : ')
    print_args(e.args)
try:
    raise Exception("my exception")
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ')
    print_args(e.args)
try:
    raise Exception("my", "exception")
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ')
    print_args(e.args)
    

class PizzaError(Exception):
    def __init__(self, pizza, message):
        Exception.__init__(self, message)
        self.pizza = pizza


class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza, cheese, message):
        PizzaError._init__(self, pizza, message)
        self.cheese = cheese


class PizzaError(Exception):
    def __init__(self, pizza, message):
        Exception.__init__(self, message)
        self.pizza = pizza
class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza, cheese, message):
        PizzaError.__init__(self, pizza, message)
        self.cheese = cheese
def make_pizza(pizza, cheese):
    if pizza not in ['margherita', 'capricciosa', 'calzone']:
        raise PizzaError(pizza, "no such pizza on the menu")
    if cheese > 100:
        raise TooMuchCheeseError(pizza, cheese, "too much cheese")
    print("Pizza ready!")
for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
    try:
        make_pizza(pz, ch)
    except TooMuchCheeseError as tmce:
        print(tmce, ':', tmce.cheese)
    except PizzaError as pe:
        print(pe, ':', pe.pizza)


class PizzaError(Exception):
    def __init__(self, pizza='uknown', message=''):
        Exception.__init__(self, message)
        self.pizza = pizza
class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza='uknown', cheese='>100', message=''):
        PizzaError.__init__(self, pizza, message)
        self.cheese = cheese
def make_pizza(pizza, cheese):
    if pizza not in ['margherita', 'capricciosa', 'calzone']:
        raise PizzaError
    if cheese > 100:
        raise TooMuchCheeseError
    print("Pizza ready!")
for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
    try:
        make_pizza(pz, ch)
    except TooMuchCheeseError as tmce:
        print(tmce, ':', tmce.cheese)
    except PizzaError as pe:
        print(pe, ':', pe.pizza)


try:
    assert __name__ == "__main__"
except:
    print("fail", end=' ')
else:
    print("success", end=' ')
finally:
    print("done")

import math
try:
    print(math.sqrt(9))
except ValueError:
    print("inf")
else:
    print("fine")


import math
try:
    print(math.sqrt(-9))
except ValueError:
    print("inf")
else:
    print("fine")
finally:
    print("the end")

class NewValueError(ValueError):
    def __init__(self, name, color, state):
        self.data = (name, color, state)
try:
    raise NewValueError("Enemy warning", "Red alert", "High readiness")
except NewValueError as nve:
    for arg in nve.args:
        print(arg, end='! ')


for i in range(5):
    print(i)


class Fib:
    def __init__(self, nn):
        print("__init__")
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1
    def __iter__(self):
        print("__iter__")
        return self
    def __next__(self):
        print("__next__")				
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret
for i in Fib(10):
    print(i)


class Fib:
    def __init__(self, nn):
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1
    def __iter__(self):
        print("Fib iter")
        return self
    def __next__(self):
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret
class Class:
    def __init__(self, n):
        self.__iter = Fib(n)
    def __iter__(self):
        print("Class iter")
        return self.__iter;
object = Class(8)
for i in object:
    print(i)


def fun(n):
    for i in range(n):
        return i
        

def fun(n):
    for i in range(n):
        yield i
        
def fun(n):
    for i in range(n):
        yield i
for v in fun(5):
    print(v)


def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2
for v in powers_of_2(8):
    print(v)


def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2
t = list(powers_of_2(3))
print(t)

def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2
for i in range(20):
    if i in powers_of_2(4):
        print(i)

def fibonacci(n):
    p = pp = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n = p + pp
            pp, p = p, n
            yield n
fibs = list(fibonacci(10))
print(fibs)


list_1 = []
for ex in range(6):
    list_1.append(10 ** ex)
list_2 = [10 ** ex for ex in range(6)]
print(list_1)
print(list_2)

the_list = []
for x in range(10):
    the_list.append(1 if x % 2 == 0 else 0)
print(the_list)

the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
print(the_list)


the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
the_generator = (1 if x % 2 == 0 else 0 for x in range(10))
for v in the_list:
    print(v, end=" ")
print()
for v in the_generator:
    print(v, end=" ")
print()


for v in [1 if x % 2 == 0 else 0 for x in range(10)]:
    print(v, end=" ")
print()
for v in (1 if x % 2 == 0 else 0 for x in range(10)):
    print(v, end=" ")
print()


two = lambda: 2
sqr = lambda x: x * x
pwr = lambda x, y: x ** y
for a in range(-2, 3):
    print(sqr(a), end=" ")
    print(pwr(a, two()))


def print_function(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')
def poly(x):
    return 2 * x**2 - 4 * x + 2
print_function([x for x in range(-2, 3)], poly)


def print_function(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')
print_function([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)

list_1 = [x for x in range(5)]
list_2 = list(map(lambda x: 2 ** x, list_1))
print(list_2)
for x in map(lambda x: x * x, list_2):
    print(x, end=' ')
print()


from random import seed, randint
seed()
data = [randint(-10,10) for x in range(5)]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))
print(data)
print(filtered)

def outer(par):
    loc = par
var = 1
outer(var)
print(var)
print(loc)

def outer(par):
    loc = par
    def inner():
        return loc
    return inner
var = 1
fun = outer(var)
print(fun())


def outer(par):
    loc = par
    def inner():
        return loc
    return inner
var = 1
fun = outer(var)
print(fun())


def make_closure(par):
    loc = par
    def power(p):
        return p ** loc
    return power
fsqr = make_closure(2)
fcub = make_closure(3)
for i in range(5):
    print(i, fsqr(i), fcub(i))


for x in (el * 2 for el in range(5)):
    print(x)  #outputs 0 2 4 6 8.
    
def foo(x,f):
    return f(x)
print(foo(9, lambda x: x ** 0.5))  # outputs 3.0.


short_list = ['mython', 'python', 'fell', 'on', 'the', 'floor']
new_list = list(map(lambda s: s.title(), short_list))
print(new_list)


short_list = [1, "Python", -1, "Monty"]
new_list = list(filter(lambda s: isinstance(s, str), short_list))
print(new_list)  # outputs ['Python', 'Monty'].

def tag(tg):
    tg2 = tg
    tg2 = tg[0] + '/' + tg[1:]
    def inner(str):
        return tg + str + tg2
    return inner
b_tag = tag('<b>')
print(b_tag('Monty Python')) # outputs <b>Monty Python</b>


class Vowels:
    def __init__(self):
        self.vow = "aeiouy " # Yes, we know y isn’t always considered a vowel.
        self.pos = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.pos == len(self.vow):
            raise StopIteration
        self.pos += 1
        return self.vow[self.pos - 1]
vowels = Vowels()
for v in vowels:
print(v, end=' ')     # Check: a e i o u y


any_list = [1, 2, 3, 4]
even_list = # Complete the line here.
print(even_list) # Check: list(map(lambda n: n | 1, any_list))

def replace_spaces(replacement='*'):
    def new_replacement(text):
        return text.replace(' ', replacement)
    return new_replacement
stars = replace_spaces()
print(stars("And Now for Something Completely Different"))


# Recommended:
def f(x): return 3*x
# Not recommended:
f = lambda x: 3*x


try:
    stream = open("C:\Users\User\Desktop\file.txt", "rt")
    # Processing goes here.
    stream.close()
except Exception as exc:
    print("Cannot open the file:", exc)


try:
    # Some stream operations.
except IOError as exc:
    print(exc.errno)


import errno
try:
    s = open("c:/users/user/Desktop/file.txt", "rt")
    # Actual processing goes here.
    s.close()
except Exception as exc:
    if exc.errno == errno.ENOENT:
        print("The file doesn't exist.")
    elif exc.errno == errno.EMFILE:
        print("You've opened too many files.")
    else:
        print("The error number is:", exc.errno)


from os import strerror
try:
    s = open("c:/users/user/Desktop/file.txt", "rt")
    # Actual processing goes here.
    s.close()
except Exception as exc:
    print("The file could not be opened:", strerror(exc.errno))


import errno
try:
    stream = open("file", "rb")
    print("exists")
    stream.close()
except IOError as error:
    if error.errno == errno.ENOENT:
        print("absent")
    else:
        print("unknown")


from os import strerror
try:
    cnt = 0
    s = open('text.txt', "rt")
    ch = s.read(1)
    while ch != '':
        print(ch, end='')
        cnt += 1
        ch = s.read(1)
    s.close()
    print("\n\nCharacters in file:", cnt)
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))


from os import strerror
try:
    cnt = 0
    s = open('text.txt', "rt")
    content = s.read()
    for ch in content:
        print(ch, end='')
        cnt += 1
    s.close()
    print("\n\nCharacters in file:", cnt)
except IOError as e:
    print("I/O error occurred: ", strerr(e.errno))


from os import strerror
try:
    ccnt = lcnt = 0
    s = open('text.txt', 'rt')
    line = s.readline()
    while line != '':
        lcnt += 1
        for ch in line:
            print(ch, end='')
            ccnt += 1
        line = s.readline()
    s.close()
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))


s = open("text.txt")
print(s.readlines(20))
print(s.readlines(20))
print(s.readlines(20))
print(s.readlines(20))
s.close()


from os import strerror
try:
    ccnt = lcnt = 0
    s = open('text.txt', 'rt')
    lines = s.readlines(20)
    while len(lines) != 0:
        for line in lines:
            lcnt += 1
            for ch in line:
                print(ch, end='')
                ccnt += 1
        lines = s.readlines(10)
    s.close()
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))


from os import strerror
try:
	ccnt = lcnt = 0
	for line in open('text.txt', 'rt'):
		lcnt += 1
		for ch in line:
			print(ch, end='')
			ccnt += 1
	print("\n\nCharacters in file:", ccnt)
	print("Lines in file:     ", lcnt)
except IOError as e:
	print("I/O error occurred: ", strerror(e.errno))


from os import strerror
try:
	fo = open('newtext.txt', 'wt') # A new file (newtext.txt) is created.
	for i in range(10):
		s = "line #" + str(i+1) + "\n"
		for ch in s:
			fo.write(ch)
	fo.close()
except IOError as e:
	print("I/O error occurred: ", strerror(e.errno))


from os import strerror
try:
    fo = open('newtext.txt', 'wt')
    for i in range(10):
        fo.write("line #" + str(i+1) + "\n")
    fo.close()
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))


import sys
sys.stderr.write("Error message")

from os import strerror
try:
    bf = open('file.bin', 'rb')
    data = bytearray(bf.read())
    bf.close()
    for b in data:
        print(hex(b), end=' ')
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))


try:
    bf = open('file.bin', 'rb')
    data = bytearray(bf.read(5))
    bf.close()
    for b in data:
        print(hex(b), end=' ')
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

for line in open("file", "rt"):
    print(line, end='')



for line in open("file", "rt"):
    for char in line:
        if char.lower() not in "aeiouy ":
            print(char, end='')
            
            
try:
    stream = open("image.png", "rb")
    # Insert a line here.
    stream.close()
except IOError:
    print("failed")
else:
    print("success")
