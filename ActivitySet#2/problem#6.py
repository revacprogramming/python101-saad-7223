class Menu:
    """fill in class definition here"""
    def __init__(self):
        self.d={}

    def add(self,name,price):
        self.d[name]=price

    def show(self):
        s=''
        for i in self.d.items():
            k,v = i
            s=s+f"{k} = {v}\n"
        print(s)    
        
m = Menu()  # Menu is a class
m.add("idly", 10)
m.add("vada", 20)

m.show()
