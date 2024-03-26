a = [2,3,2,4,5,6,2,5,3,2]
# dup = a[0]
max_count = 0
max_rep_element = None

for i in a:
    if a.count(i) > 1:
        print("Duplicate Elements=",i,"Repeated times=",a.count(i))

    if a.count(i) > max_count:
        max_count = a.count(i)
        max_rep_element = i
print("Max Repeated Element=", max_rep_element, "Repeated times=", max_count)

