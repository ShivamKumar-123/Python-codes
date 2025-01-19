num = int(input("Enter a number to print the table : "));
'''
for i in range(1,11):
    if i!=5:
        print(num,"x",i,"=",num*i);
'''
for i in range(1,11):
    if i==5:
        continue;
    print(num,"x",i,"=",num*i);
