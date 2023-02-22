countev=0
countod=0
i=1
while i<=7:
    if i%2==0:
        countev=countev+i
    else:
        countod=countod+i
    i=i+1

print("even no.s =",countev)
print("odd no.s =",countod)