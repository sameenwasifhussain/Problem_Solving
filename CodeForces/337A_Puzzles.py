n,m = map(int , input().split())
puzzles = list(map(int , input().split()))
min_diff = 10000000000000000

puzzles.sort()

for i in range(0,m-n+1):
    diff = puzzles[i+n-1] - puzzles[i]
    if diff<min_diff:
        min_diff = diff

print(min_diff)