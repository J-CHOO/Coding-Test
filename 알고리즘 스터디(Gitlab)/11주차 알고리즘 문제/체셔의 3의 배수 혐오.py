#60점..4,5번 case 오답
n = int(input())
nums = list(map(int, input().split()))

temp = []

if len(nums) == 1:
    print(*nums)
elif len(nums) == 2:
    print(-1)
else:
    for i in range(len(nums)-2):
        if (nums[i] + nums[i+1]) % 3 == 0:
            temp.append(nums[i+2])
            temp.append(nums[i+1])
            nums[i+1] = temp[0]
            nums[i+2] = temp[1]
            temp = []
    print(*nums)
