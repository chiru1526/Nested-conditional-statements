a=str(input("Do you have any health condition Y for yes N for no: "))
b=int(input("Enter attendance percentage: "))
if a.upper()=="Y":
    print("You are allowed to write exam")
else:
    if b>75:
        print(("You are allowed to write exam"))
    else:
         print(("You are not allowed to write exam"))
    