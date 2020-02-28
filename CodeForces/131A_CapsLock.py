string_in = input()

if len(string_in) == 1:
    if string_in.isupper():
        print(string_in.lower())
    else:
        print(string_in.upper())
elif (ord(string_in[0])>=97 and ord(string_in[0])<=122) and string_in[1:len(string_in)].isupper():
    x = chr(ord(string_in[0])-32)
    print(x + string_in[1:len(string_in)].lower())
elif string_in.isupper():
    print(string_in.lower())
else:
    print(string_in)
