print("Assalam-o-Alikum..!  \nHope you are fine...\nWelcome to MHZ Fast Foods...\nHere you can get pizza, fries, burger, sandwiches.")
x=int(input("Press 1 for pizza of Rs.1000, 2 for fries of Rs.30, 3 for burger of Rs.200 And 4 for sandwiches of Rs.70 : "))
if x==1:
    print("You chose pizza")
elif(x==2):
    print("You chose fries")
elif(x==3):
    print("You chose burger")
elif(x==4):
    print("You chose sandwich")
else:
    print("This is not in list")
    exit(0)

n=int(input("Enter the quantity of chosen item : "))
if x==1:
    a=n*1000
    print(f"Your bill is Rs.{a}")
elif(x==2):
    a = n*30
    print(f"Your bill is Rs.{a}")
elif(x==3):
    a=str(n*200)
    print("Your bill is Rs."+a)
elif(x==4):
    a=str(n*70)
    print("Your bill is Rs."+a)

