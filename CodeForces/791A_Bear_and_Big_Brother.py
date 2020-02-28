import math

x,y = map(float, (input().split()))

r = ( math.log(y/x) / math.log(1.5) ) + 1
r = int(math.floor(r))

print(r)
