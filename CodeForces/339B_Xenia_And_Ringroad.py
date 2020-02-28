n, m = map(int,(input().split()))
tasks = list(map(int,(input().split())))

current = 1
work_time = 0

for houses in tasks:
    if houses < current:
        work_time += n - current + 1
        current = 1
    work_time += houses - current
    current = houses

print(work_time)
