#? Q1. FACTORIAL OF A NUMBER
#* Take a non-negative integer n and calculate its factorial using a loop.

#* Factorial means multiplying all positive integers from 1 to n.
#* By definition, 0! = 1.

#* Input:
#* 5

#* Output:
#* 120


a = int(input("enter your number : "))
product = 1
for i in range(1,a+1):
    product*=i
print(product)  