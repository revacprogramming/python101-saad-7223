# SET-2 PROBLEM-1
def add(a, b):
    return  a+b #sum of 2 numbers


def main():
    a = int(input("Enter a number : "))  # taking input for variable a
    b = int(input("Enter a number : 5"))  # taking input for variable b
    c = add(a, b)    
    print('sum : ',c)

if __name__ == '__main__':
    main()
