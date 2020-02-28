n = int(input())

sum = 0
posi = 0

if n%2==0:
    n = n/2
    posi = n/2 * ((2*2) + (n-1)*(2))
    negi = n/2 * ((2*-1) + (n-1)*(-2))
else:
    n = (n-1) / 2
    posi = n/2 * ((2*2) + (n-1)*(2))
    negi = (n+1)/2 * ((2*-1)+(n)*(-2))

sum = int(posi + negi)
print(sum)



