#? 2. Count descending adjacent pairs — Count elements greater than their immediate next element.
# example: a = [9, 5, 7, 3, 2, 8]

# Compare neighboring elements, one pair at a time:
# Pair	Condition	Count
# 9, 5	9 > 5 True	1
# 5, 7	5 > 7 False	1
# 7, 3	7 > 3 True	2
# 3, 2	3 > 2 True	3
# 2, 8	2 > 8 False	3


a = [72,23 ,34, 78 ,90 ,89]
count = 0

for i in range(len(a)-1):
    if a[i]>a[i+1]:
        count+=1

print(count)

# *simple as me !!! ha ha ha...

