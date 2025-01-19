with open('file handling/myfile4.txt','w') as f:
    lines = ['line1 ','line 2 \n','line3 \n']
    f.writelines(lines)