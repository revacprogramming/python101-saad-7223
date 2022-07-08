def get_cs():
    """get string input"""
    s=input("Enter a string : ")
    return s

def cs_to_lot(cs):
    """convert connected string to list of strings"""
    l=cs.split(';');x=[]
    for i in l:
        a=i.split('=')
        x.append(tuple(a))
    return x
    
def main():
    cs = get_cs()

    lot = cs_to_lot(cs)
    print(lot)


if __name__ == '__main__':
    main()
