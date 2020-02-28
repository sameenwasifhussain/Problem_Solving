n = int(input())
count = int(0)

for i in range(0,n):
    a,b = map(int, input().split())
    if b - a >= 2:
        count+=1

print(count)