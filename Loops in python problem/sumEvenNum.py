num = int(input("Enter the number: "));

sum_even_num = 0;
"""
i = 0;
while i <= num:
    if i%2==0:
        sum_even_num += i;
    i += 1;
"""
for i in range(1,num+1):
     if i%2==0:
        sum_even_num += i;
print("Sum of even number is : ",sum_even_num);