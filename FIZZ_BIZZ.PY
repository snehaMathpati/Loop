i=1
while i<=50:
    if i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Bizz")
    if i%3==0 and i%5==0:
        print("FizzBizz")
    else:
        print(i)
    i=i+1
