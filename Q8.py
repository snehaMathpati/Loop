# i=0
# while i<5:
#     j=0
#     while j<i:
#         if j==1:
#             print("*",end="")
#         else:
#             print(i,end="")
#         j+=1
#     print()
#     i+=1

i=0
while i<5:
    j=0
    while j<i:
        if i%2==0:
            print("C",end="")
        else:
            print(i,end="")
        j+=1
    print()
    i+=1
   