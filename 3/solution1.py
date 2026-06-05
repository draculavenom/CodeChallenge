nums = [3, 2, 8, 5, 6, 7, 4, 9, 10]
target = 18

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            print("index 1: " + str(i) + "; index 2: " + str(j))