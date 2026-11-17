#? 1. Sum elements at even indexes — Calculate the sum of elements at indexes 0, 2, 4, 6...


a = list(map(int,(input("enter your number\n").split())))

sum = 0
for i in range(len(a)):
    if i %2==0:
        sum += a[i]

print(sum)

