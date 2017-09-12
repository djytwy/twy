import random


def bubbleSort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                 nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

number = []
for k in range(10):
    t = random.randint(0, 100)
    number.append(t)
print(number)
bubbleSort(number)
print(number)
