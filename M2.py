# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 12:10:44 2021

@author: xuewu
"""
# 2.2.1.1 The nature of strings in Python

# Example 1
word = 'by'
print(len(word))


# Example 2
empty = ''
print(len(empty))


# Example 3
i_am = 'I\'m'
print(len(i_am))

# 2.2.1.2 The nature of strings in Python

multiline = '''Line #1
Line #2'''

print(len(multiline))


multiline = """Line #1
Line #2"""
print(len(multiline))


# 2.2.1.3 The nature of strings in Python
str1 = 'a'
str2 = 'b'

print(str1 + str2)
print(str2 + str1)
print(5 * 'a')
print('b' * 4)


# 2.2.1.4 The nature of strings in Python

# Demonstrating the ord() function.

char_1 = '牛'
char_2 = ' '  # space

print(ord(char_1))
print(ord(char_2))

# 2.2.1.5 The nature of strings in Python

# Demonstrating the chr() function.

print(chr(97))
print(chr(945))

# 2.2.1.6 The nature of strings in Python

# Indexing strings.

the_string = 'silly walks'

for ix in range(len(the_string)):
    print(the_string[ix], end=' ')

print()

# # Iterating through a string.

the_string = 'silly walks'

for character in the_string:
    print(character, end=' ')

print()


# 2.2.1.7 The nature of strings in Python

# Slices

alpha = "abdefg"

print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])

# 2.2.1.8 The nature of strings in Python

alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" in alphabet)
print("F" in alphabet)
print("1" in alphabet)
print("ghi" in alphabet)
print("Xyz" in alphabet)


alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" not in alphabet)
print("F" not in alphabet)
print("1" not in alphabet)
print("ghi" not in alphabet)
print("Xyz" not in alphabet)

# 2.2.1.11 The nature of strings in Python

# Demonstrating min() - Example 1:
print(min("aAbByYzZ"))


# Demonstrating min() - Examples 2 & 3:
t = 'The Knights Who Say "Ni!"'
print('[' + min(t) + ']')

t = [0, 1, 2]
print(min(t))

# # 2.2.1.11 The nature of strings in Python
# Demonstrating max() - Example 1:
print(max("aAbByYzZ"))


# Demonstrating max() - Examples 2 & 3:
t = 'The Knights Who Say "Ni!"'
print('[' + max(t) + ']')

t = [0, 1, 2]
print(max(t))

# # 2.2.1.13 The nature of strings in Python
# Demonstrating the index() method:
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))



# 2.3.1.1 String methods

print("Alpha".capitalize())
print('ALPHA'.capitalize())
print(' Alpha'.capitalize())
print('123'.capitalize())
print("αβγδ".capitalize())


# 2.3.1.2 String methods
# Demonstrating the center() method:
print('[' + 'alpha'.center(10) + ']')

print('[' + 'Beta'.center(2) + ']')
print('[' + 'Beta'.center(4) + ']')
print('[' + 'Beta'.center(6) + ']')

print('[' + 'gamma'.center(20, '*') + ']')


# 2.3.1.3 String methods
t = "zeta"
print(t.endswith("a"))
print(t.endswith("A"))
print(t.endswith("et"))
print(t.endswith("eta"))

# 2.3.1.4 String methods
# Demonstrating the find() method:
print("Eta".find("ta"))
print("Eta".find("mma"))


t = 'theta'
print(t.find('eta'))
print(t.find('et'))
print(t.find('the'))
print(t.find('ha'))

print('kappa'.find('a', 2))


print('kappa'.find('a', 1, 4))
print('kappa'.find('a', 2, 4))


# 2.3.1.5 String methods

t = 'Six lambdas'
print(t.isalnum())

t = 'ΑβΓδ'
print(t.isalnum())

t = '20E1'
print(t.isalnum())

t = '新年快乐！'
print(t.isalnum())

# 2.3.1.6 String methods
# Example 1: Demonstrating the isapha() method:
print("Moooo".isalpha())
print('Mu40'.isalpha())

# Example 2: Demonstrating the isdigit() method:
print('2018'.isdigit())
print("Year2019".isdigit())


# 2.3.1.7 String methods
# Example 1: Demonstrating the islower() method:
print("Moooo".islower())
print('moooo'.islower())

# Example 2: Demonstrating the isspace() method:
print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())

# Example 3: Demonstrating the isupper() method:
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())


# 2.3.1.10 String methods
print("pythoninstitute.org".lstrip(".org"))


# 2.3.1.11 String methods

# Demonstrating the replace() method:
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))

print("This is it!".replace("is", "are", 1))
print("This is it!".replace("is", "are", 2))

# 2.5.1.4 Four simple programs

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


# 2.5.1.6 LAB: Improving the Caesar cipher
checkText = False
while checkText != True:
    text = input("Enter your message: ")
    if text != '':
        checkText = True
        
checkShift = False
shiftNumber = list(range(1,26))
while checkShift != True:
    try:
        shift = int(input("Enter your shift number(1~25): "))
        if shift in shiftNumber:
            checkShift = True
    except:
        print("Please Enter number between 1 and 25!!")
        continue      

cipher = ''
for char in text:
    if not char.isalpha():
        cipher += char
    if char.islower():
        code = ord(char) + shift
        if code > ord('z'):
            code = ord('a') + (code - ord('z') - 1)
        cipher += chr(code)
        
    if char.isupper():
        code = ord(char) + shift
        if code > ord('Z'):
            code = ord('A') + (code -ord('Z') - 1)
        cipher += chr(code)

print(cipher)


# 2.7.1.4 The anatomy of exceptions
def bad_fun(n):
    try:
        return 1 / n
    except ArithmeticError:
        print("Arithmetic Problem!")
    return None

bad_fun(0)

print("THE END.")

# 
def bad_fun(n):
    return 1 / n

try:
    bad_fun(0)
except ArithmeticError:
    print("What happened? An exception was raised!")

print("THE END.")

# 2.7.1.5 The anatomy of exceptions | raise
def bad_fun(n):
    raise ZeroDivisionError

try:
    bad_fun(0)
except ArithmeticError:
    print("What happened? An error?")

print("THE END.")

# 2.7.1.8 SECTION SUMMARY

def foo(x):
    assert x
    return 1/x


try:
    print(foo(0))
except ZeroDivisionError:
    print("zero")
except:
    print("some")


# 2.8.1.1 Useful exceptions
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

# 2.8.1.2 Useful exceptions

# This code cannot be terminated
# by pressing Ctrl-C.

from time import sleep

seconds = 0

while True:
    try:
        print(seconds)
        seconds += 1
        sleep(1)
    except KeyboardInterrupt:
        print("Don't do that!")


# 2.8.1.3 Useful exceptions

# One of these imports will fail - which one?
try:
    import math
    import time
    import abracadabra

except:
    print('One of your imports has failed.')

# How to abuse the dictionary
# and how to deal with it?
dictionary = { 'a': 'b', 
               'b': 'c', 
               'c': 'd' }
ch = 'a'
try:
    while True:
        ch = dictionary[ch]
        print(ch)
except KeyError:
    print('No such key:', ch)
    
    
print(ord('c') - ord('a'))
print(float('1,3'))

print("Mike" > "Mikey")

x = '\''
print(len(x))
