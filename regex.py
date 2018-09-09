import re
s=input("enter email:")
password=input("enter password:")
CHECK=re.search(r"(^[a-zA-Z0-9_.+-]+@gmail|yahoo+\.com+$)",s)
if(CHECK):
    print("valid email")
else:
    print("not valid email")
if re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', password):
    print("match password")
else:
    print("not match password")