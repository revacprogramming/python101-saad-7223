# Files

#filename = "dataset/mbox-short.txt"
fname = input("Enter file name: ")
fh = open(fname)
count=0
result=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    index = line.find(':')
    num = float(line[index+1: ])
    count = count+1
    result = result+num
print("Average spam confidence:", result/count) 
