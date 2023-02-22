# i=int(input("enter the number"))
# rev=0
# while i>0:
#     rev=(rev*10)+i%10
#     i=i//10
# print("reverse=",rev)

u=int(input("enter the no : "))
rev=0
while u>0:
    rev=(rev*10)+(u%10)
    u=u//10
print(rev)