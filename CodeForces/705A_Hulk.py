n = int(input())

if n==1:
    print("I hate", end =" ")
else:
    for i in range(1,n+1):
        if i!=1:
            print("that", end=" ")
        if i%2==1:
            print("I hate", end = " ")
        else:
            print("I love", end = " ")

print("it")