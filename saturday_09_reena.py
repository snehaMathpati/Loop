user=int(input("enter the number"))
if user>10:
    if user%2==0:
        print("enter number is greater than 10,and it is even number =",user)
    elif user%2!=0:
        print("enter number is greater than 10,but it is odd number =",user)
else:
    print("enter number is less than 10") 