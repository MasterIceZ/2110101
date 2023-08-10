s = input()

if len(s) != 10 or s[0:2] not in ["06", "08", "09"]:
    print("Not a mobile number")
else:
    print("Mobile number")
