#? 2. Count numbers divisible by 3 but not 5 — Count qualifying integers in a list.

a = list(map(int,input("enter your number\n").split()))
print(a)
count = 0
for num in a :
    if num%3==0 and num %5 != 0:
        count+=1
print(count)        