hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate per hour:")
r = float(rate)
if(h>40):
    print((h*r+((h-40)*r*0.5)))
else:
    print(r*h)