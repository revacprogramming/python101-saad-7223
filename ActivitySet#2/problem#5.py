

def get_cs():
    """get string input"""
    s=input("Enter a string : ")
    return s

def cs_to_dict(cs):
    """convert connect string to a dictionary"""
    l=cs.split(';');x=[];d={};
    for i in l:
        a=i.split('=')
        x.append(a)
    for j in range(0,len(x)):
        d[x[j][0]]=x[j][1]
    return d    

def dict_to_cs(d):
    """convert a dictionary to connect string"""
    l=list(d.items())
    st=""
    for i in range(0,len(l)):
        st=st+l[i][0]+'='+l[i][1]+';'
    return st


def main():
    cs = get_cs()

    d = cs_to_dict(cs) # convert connect string to a dictionary
    print(d)

    cs = dict_to_cs(d)
    print(cs)


if __name__ == '__main__':
    main()
