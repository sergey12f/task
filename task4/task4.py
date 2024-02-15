nums = [0,4,0,21] 
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