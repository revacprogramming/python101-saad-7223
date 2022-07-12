class Menu:
    """fill in class definition here"""
    def __init__(self):
          self.l=list()

    def __add__(self,t):
          self.l.append(t)
          return self
          
    def __str__ (self):
        s =""
        for i in self.l:
            d,q = i
            s = s + f"{d} {q} \n"
        return s
        
m = Menu()
m =m + ("idly", 10) + ("vada", 20)  # Hint: operator overloading special methods (__add__, __sub__, etc.)

print(m)  # should print the menu properly
