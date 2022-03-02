N = int(input())

result = []

cubes = [250, 40, 10]

if N % 10 != 0:
    print(-1)
else:
    for cube in cubes:
        result.append(N // cube)
        N = N % cube
    print(*result[::-1])


