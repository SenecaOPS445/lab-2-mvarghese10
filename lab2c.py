#!/usr/bin/env python3

import sys

#name = 'Jon'
#age = 20

#name = input("Name: ")
#age = input("Age: ")

name = sys.argv[1]
age = sys.argv[2]

print('Hi ' + name + ', you are ' + str(age) + ' years old.')
