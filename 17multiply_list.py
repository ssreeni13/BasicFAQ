ls = [1, 2, 3, 4, 5]
temp = 1

# Approach1 - using loop
for i in range(0, len(ls)):
    temp *= ls[i]
print(temp)

# Approach2 - using numpy
import numpy

a = numpy.prod(ls)
print(a)
