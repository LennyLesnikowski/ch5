# infile = open("./infile.txt", "r")
# names=[line.rstrip() for line in infile ]

# # infile.close()

# # def main():
# #     displayWithForloop(fileName)
# #     print()
# #     displayWithList(fileName)
    
# # def displayWithForloop(fileName):
# #     infile=openFile (fileName, "r")
# #     for line in infile:
# #         print(line,end="")
# #     infile.close()

# # def displayWithList(fileName):
# #     infile=openFile (fileName, "r")
# #     items =[line.rstrip() for line in infile]
# #     print ("items:", items)
# #     infile.close()

# def main():
#     saveToOutFile("./outFile.txt")

# def openFile(fileName, mode):
#     return open(fileName, mode)


# outFile = openFile("./outFile", "w")

# def saveToOutFile(fileName):
#     for name in names:
#         data=[]
#         if "Doe" not in name:
#             print ("Name to be persisted ", name)
#             outFile.writeline(name + "\n")
#         else:
#             print("Name to be excluded ", name)
#             outFile.writeline(data)
#     outFile.close()

a_list= []

a_set = {}

a_list.append("A")

a_set.add("A")
a_set.add("A")
a_set.add("A")
a_set.add("B")
a_set.add("C")

print (a_set)
