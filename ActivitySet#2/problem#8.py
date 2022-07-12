class Menu:
    """fill in class definition here"""
    def __init__(self):
      self.d=dict()

    #if self.d == None or self.d={}:
    def __setitem__(self,k,v):
      self.d[k]=v

    def __str__(self):
      s=""
      for k,v in self.d.items():
        s = s + f"{k} : {v} \n"
      return s
    
m = Menu()
m["idly"] = 10
m["vada"] = 20

print(m)
