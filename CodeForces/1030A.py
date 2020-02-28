n = int(input())
diff = list(map(int,input().split()))
hard = False

for i in diff:
    if i == 1:
        hard = True
        break

if hard:
    print("HARD")
else:
    print("EASY")