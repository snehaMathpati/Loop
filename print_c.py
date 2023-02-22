# i=1
# while i<=1:
#     print("@"*4)
#     j=1
#     while j<=2:
#         print("@")
#         j=j+1
#         k=1
#         while k<=1:
#             print("@"*4)
#             k=k+1
#     i=i+1

# i = 0
# while i<5:
#     if i==2:
#         print(i)
#         break
        
#     i= i+1
# else:
#     print(i)

i=0
while i<=5:
    j=0
    while j<=6:
        if i==0 or i==2 or j==0 or j==6:
            print("*",end='')
        print()
        j=j+1
    i=i+1
