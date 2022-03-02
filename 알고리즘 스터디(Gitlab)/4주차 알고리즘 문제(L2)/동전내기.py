c = list(str(input()))

zero = 0
one = 0

for i in range(len(c)-1):
    if c[i] == "0":
        if c[i+1] != "0":
            zero += 1
        else:
            pass
    else:
        if c[i+1] != "1":
            one += 1
        else:
            pass

print(min(zero, one))
