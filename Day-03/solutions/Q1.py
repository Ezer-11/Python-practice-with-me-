#? 1. Find an element's index — Find the first occurrence without index() or in.

target = int(input("Enter your number: "))
numbers = [12, 34, 45, 54, 23]

found = False

for i in range(len(numbers)):
    if target == numbers[i]:
        print(i)
        found = True
        break

if not found:
    print(-1)

#* we assumed that we didn't found the number and used boolean  
#* without using boolean >

# target = int(input("Enter your number: "))
# numbers = [12, 34, 45, 54, 23]

# for i in range(len(numbers)):
#     if target == numbers[i]:
#         print(i)
#         break
# else:
#     print(-1)
