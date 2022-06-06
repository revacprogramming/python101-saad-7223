# Regular Expressions
# https://www.py4e.com/lessons/regex
import re

hand = open("dataset/mbox-short.txt")
x=list()
for line in hand:
    y = re.findall('[0-9]+',line)
    x = x+y

sum=0
for z in x:
    sum = sum + int(z)
print(sum)
