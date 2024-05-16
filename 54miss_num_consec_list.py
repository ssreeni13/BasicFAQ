ls = [1,2,3,4,5,6,8]
ex_sum = (ls[-1] * (ls[-1] + 1)) // 2
ac_sum = 0
for i in ls:
    ac_sum += i
miss_num = ex_sum - ac_sum
print(miss_num)