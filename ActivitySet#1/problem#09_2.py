fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0;x=[]
for line in fh:
    if line.startswith("From "):
        l=line.split()
        count+=1
        print(l[1])

print("There were", count, "lines in the file with From as the first word")
