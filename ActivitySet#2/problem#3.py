

def get_cs():
    """get string input"""
    s=input("Enter a string : ")
    return s

def cs_to_lot(cs):
    """convert connected string to list of strings"""
    l=cs.split()
    return l

def main():
    cs = get_cs()

    lot = cs_to_lot(cs)
    print(lot)


if __name__ == '__main__':
    main()
