num = input("Enter a number :")
print(f"Multiplication table of {num} is : ")

try:
    for i in range(1,11):
        print(f"{int(num)} X {i} = {int(num)*i}")
# except Exception as e:
#     # print(e)
#     print("Give the correct input")  # yha par kuch bhi print karva sakte hai
except :
    # print(e)
    print("Give the correct input")

print("Some improtant line of code ")
print("End of the code")