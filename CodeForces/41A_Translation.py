strng = input()
revstr = input()

milse = True
str_len = len(strng)
rev_len = len(revstr)

if str_len != rev_len:
    print("NO")
else:
    for i in range(0,str_len):
        if strng[i] != revstr[str_len-1-i]:
            milse = False
            break
    if milse:
        print("YES")
    else:
        print("NO")
