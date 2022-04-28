
fileName= "./infile.txt"
infile = open(fileName, "r")
print("infile", infile)
names=[line.rstrip() for line in infile ]

infile.close()

def main():
    displayWithForloop(fileName)
    print()
    displayWithList(fileName)
    
def displayWithForloop(fileName):
    infile=openFile (fileName, "r")
    for line in infile:
        print(line,end="")
    infile.close()

def displayWithList(fileName):
    infile=openFile (fileName, "r")
    items =[line.rstrip() for line in infile]
    print ("items:", items)
    infile.close()

def openFile(fileName, mode):
    return open(fileName, mode)

main()