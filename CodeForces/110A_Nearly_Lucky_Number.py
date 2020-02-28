import math

n = int(input())
count= int(0)

while n!=0:
    # print("N: ",n)
    if n%10 == 4 or n%10 == 7:
        # print("N%10: ",n%10)
        count+=1
        # print("COUNT: ",count)
    n = (math.floor(n//10))
    # print("N/10: ",n)

if count == 4 or count == 7:
    print("YES")
else:
    print("NO")
# print("Final Count:",count)