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


