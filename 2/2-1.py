import sys
input = sys.stdin

#Add pre-reading code here

def fix(val):
    return int(val)

def isSafe(nums):
    isInc = nums[0] < nums[1]
    for i in range(len(nums) - 1):
        if abs(nums[i] - nums[i+1]) > 3:
            return False
        if nums[i] == nums[i+1]:
            return False
        if isInc and nums[i] > nums[i+1]:
            return False
        if not isInc and nums[i] < nums[i+1]:
            return False
        
    return True
        

safecount = 0

while True:
    line = input.readline()
    if line == "":
        break

    nums = list(map(fix, line.split(' ')))
    if(isSafe(nums)):
        safecount += 1


print(safecount)