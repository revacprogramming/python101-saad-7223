# Functions
def computepay(h, r):
    if(h>40):
        return (h*r+(((h-40)*r*0.5)))
    else:
        return h*r
hrs = input("Enter Hours:")
h=float(hrs)
rate = input("Enter the rate per hour:")
r=float(rate)
p = computepay(h,r)
print("Pay", p)