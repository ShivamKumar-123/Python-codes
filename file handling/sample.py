with open("file handling/sample1.txt",'w') as f:
    f.write("Hello World!")
    p = f.truncate(5)
    print(p)

with open("file handling/sample1.txt",'r') as f:
    print(f.read())