password = input("Enter your password to check the strength of password : ");
passLen = len(password);
print(passLen);

if passLen < 6:
    strength = "Weak";
elif passLen >= 6 and passLen <=10:
    strength = "Medium";
else:
    strength = "Strong";

print(strength);