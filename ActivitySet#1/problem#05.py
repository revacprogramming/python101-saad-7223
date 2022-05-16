# Functions


def computepay(h, r):
    return h*r
  
hrs = float(input("Enter hours? "))
rte = float(input("Enter rate per hour? "))

p = computepay(hrs, rte)
print("Pay", p)
'''
OUTPUT:
python ActivitySet#1/problem#05.py
Enter hours? 14
Enter rate per hour? 10
Pay 140.0'''