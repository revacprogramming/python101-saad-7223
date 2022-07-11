# Regular Expressions
# https://www.py4e.com/lessons/regex
'''import re

hand = open("dataset/regex12.txt")
x=list()
for line in hand:
    y = re.findall('[0-9]+',line)
    x = x+y

sum=0
for k in x:
    sum = sum + int(k)
print(sum)
'''
import re
fname = input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print("File not found!")
    quit()
numlist = []
for line in fhand:
    num_in_line = re.findall('[0-9]+', line)
    if len(num_in_line) < 1 : continue
    for num in num_in_line:
        numlist.append(int(num))
print(sum(numlist))

