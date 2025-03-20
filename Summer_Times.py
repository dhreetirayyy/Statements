number = int(input("Enter Temperature to check (in Farenheit):"))
print("Temp. to be checked", number , "degrees Farenheit")
if (0 <= number <= 68):
    print("Its gonna be cold")
else:
    print("Its gonna be hot")