avg=0
i=1
while i<=11:
    n=int(input("enter the number"))
    avg=(avg+n)
    i=i+1
average=avg/11
print("average number=",average)
if average%5==0:
    print("the average weight is multiple by 5")
else:
    print("the average weight is not multiple by 5")

