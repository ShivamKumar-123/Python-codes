with open("file handling/myfile3.txt") as f:
    line = f.readline()
    print(line.split("*"))
    print(line.split("*")[0])