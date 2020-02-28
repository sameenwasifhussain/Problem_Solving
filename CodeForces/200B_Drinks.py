n = int(input())
arra = list(map(float,input().split()))

sum = 0

for nums in arra:
    sum += nums

result = sum / n
print(result)
