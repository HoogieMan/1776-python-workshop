# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 18:27:40 2014

@author: cjhooger
"""

print('hello world')

for char in 'cat':
    print(char)
    
def my_upper(a_str):
    new_str = ''
    for char in a_str:
        x = ord(char)
        if x >= 97 and x <= 122:
            new_x = x - (ord('a') - ord('A'))
        else:
            new_x = x
        new_str = new_str + chr(new_x)
    return new_str