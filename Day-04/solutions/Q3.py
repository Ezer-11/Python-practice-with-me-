#?Q3. ROTATE A LIST TO THE RIGHT BY ONE POSITION

#* Take a list of integers and move its last element to the first position.
# *Every other element should shift one position to the right.

#* Input:
#* 5
#* 10 20 30 40 50

#* Output:
#* 50 10 20 30 40
# ! note you need to hardcode first the list  and 
# !then move the last element to first and further solve question

a = [12, 34, 45, 80, 60, 78]

result = []

# * Add the last element first
result.append(a[-1])

# * Append every element except the last one
for i in range(len(a)-1):
    result.append(a[i])

print(result)

 #* try to take an input of num of list from user and solve it.    