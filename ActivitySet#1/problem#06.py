# Loops & Iterators

largest = None
smallest = None
while True:
    try:  
        num = input("Enter a number: ")
        if num == "done":
            print("Invalid input")
            break
        elif (largest == None or num < largest):
            largest = num
        elif (smallest == None or num < smallest):
            smallest = num
    except:
            print("Invalid input")
print("Maximum is", largest)
print("Minimum is", smallest)