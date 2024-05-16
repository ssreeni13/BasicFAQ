def long_consec_seq(nums):
    if not nums:
        return 0
    nums.sort()
    max_length = 1
    current_length = 1
    for i in range(1,len(nums)):
        if nums[i] == nums[i-1] + 1:
            current_length += 1
            max_length = max(max_length, current_length)
        elif nums[i] != nums[i-1] + 1:
            current_length = 1
    return max_length


ls = [100,4,200,1,3,2]
p = long_consec_seq(ls)
print(p)




