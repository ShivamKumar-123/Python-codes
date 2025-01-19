fruit_name = input("Enter fruit name : ");
fruit_color = input("Enter fruit color: ");

if fruit_name == "Banana":
    if fruit_color=="Green":
        print("Unripe \n");
    elif fruit_color=="Yellow":
        print("Ripe \n");
    else:
        print("Overripe \n");

else:
    print("do not have any information about this till now \n");