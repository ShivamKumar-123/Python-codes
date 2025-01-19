marks = int(input("Enter marks : "));

if marks >= 101:
    print("Please verify  your grade again \n");
    # exit();
    quit();


if marks >= 90:
    print("Grade : A");

elif marks >= 80:
    print("Grade : B");

elif marks >= 70:
    print("Grade : C");

elif marks >= 60:
    print("Grade : D");

else:
    print("Grade: F");

