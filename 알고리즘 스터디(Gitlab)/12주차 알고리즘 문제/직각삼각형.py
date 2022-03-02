while True:
    n = list(map(int, input().split()))
    if n[0] == 0:
        break
    max_n = max(n)
    n.remove(max_n)
    if max_n ** 2 == (n[0])**2 + (n[1])**2:
        print("rightangle")
    else:
        print("triangle")
