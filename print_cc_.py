# i=1
# while i<=1:
#     print("c"*3)
    
#     j=4
#     while j>=1:
#         print("c")
#         j=j+1
#         k=1
#     while k<=1:
#         print("c"*3)
#         k=k+1
#     i=i+1
    



i=1
while i<=6:
    j=1
    while j<=5:
        if i==1 or j==1 or i==4 or j==5:
            print ('*',end=' ')
        else:
            print ('',end='')
        j=j+1
    print ()
    i=i+1
      
