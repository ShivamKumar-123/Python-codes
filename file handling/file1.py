# f = open("file handling/myfile.txt", "w")
# print(f.read())
# f.write("Shivam is a good boy")
# f.close()

#writing inside qa file

# f = open("file handling/myfile2.txt","w")
# f.write("Hey how are you")
# f.close()

# f = open("file handling/myfile2.txt","a")
# f.write("Hey how are you \n")
# f.close()

with open("file handling/myfile2.txt",'a') as f:
    f.write("Hey i am inside the with")