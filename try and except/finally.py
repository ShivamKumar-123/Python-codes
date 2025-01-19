'''
try:
    l = [2,3,4,5]
    i = int(input("Enter the index:"))
    print(l[i])
except:
    print("Some error occured")

# finally:
#     print("I am always executed")
print("I am always executed")   # yadi hum finally keyword ka nhi use karte hai to same kaam ye wala part bhi kar raha hai 
# finally ka main work function me aata hai

'''

def exception():
    try:
        l = [1,2,4,5]
        i = int(input("Enter the index : "))
        print(l[i])
        return 1

    except:
        print("Some error occured")
        return 0
    
    # print("I am always executd")

    finally:
        print("I am always executed")


print(exception())

