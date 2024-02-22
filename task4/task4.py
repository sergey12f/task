import sys
import re
print(sys.argv[1])
with open(sys.argv[1],'r') as file:
    nums = list(file)

for i in range(len(nums)):
    nums[i] = int(re.sub("[^0-9]", "", nums[i]))
print(nums)
m = sorted(nums)[len(nums) // 2]
count = 0
for id, i in enumerate(nums):
    while i != m:
        if i < m:
            i += 1
            count += 1
        elif i > m:
             i -= 1
             count += 1
        else:
            nums[id] = i
print(count)