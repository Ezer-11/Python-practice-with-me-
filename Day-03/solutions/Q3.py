#? 3. Move all zeros to the end — Preserve the relative order of non-zero elements.
# ! GOOD PROBLEM !!!
#  example : a = [0, 5, 0, 3, 8, 0, 2]

# !common mistake !!!

# a = [0, 5, 0, 3, 8, 0, 2]
# for i in range(len(a)):
#     if a[i] == 0:
#         a.remove(a[i])
#         a.append(0)  
# print(a)

#! When you remove an element:
#* - The list becomes shorter.
#* - The indexes of the remaining elements shift.
#* - But range(len(a)) was calculated using the original length.

a = list(map(int,input("enter your number :\n").split()))
result = []
zero_count = 0
for i in range(len(a)):
    if a[i] != 0:
        result.append(a[i])
    else: 
        zero_count +=1  
for i in range(zero_count):
    result.append(0)

print(result)



