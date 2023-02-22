i=int(input("enter the number"))
orge=i
sum=0
while i>0:
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10
if orge==sum:
    print("it is an armstrong")
else:
    print("it is not an armstrong")