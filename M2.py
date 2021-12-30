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




