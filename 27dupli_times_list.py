a = [2,3,2,4,5,6,2,5,3,2]
# dup = a[0]

for i in a:
    if a.count(i) > 1:
        print("Duplicate Elements=",i,"Repeated Elements=",a.count(i))
