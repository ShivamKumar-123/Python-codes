with open("file handling/myfile5.txt",'r') as f:
    print(type(f))
    #Move to the byte in the file
    f.seek(10)
    #read the next 5 bytes
    print(f.tell())
    data = f.read(5)
    print(data)