'''
URL shortener in Python
Author: Rehxnnq
'''

import pyshorteners as sh

url = input('Enter Url Here :: ')

s = sh.Shortener()
x = (s.tinyurl.short(url))

print('New url :: ' , x)
