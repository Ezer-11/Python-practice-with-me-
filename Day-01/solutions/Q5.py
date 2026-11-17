#? 5. Perfect number — Check whether a number is a perfect number.

#* A perfect number is a number whose sum of all its positive divisors, 
#* excluding itself, equals the number.
#* example : 6  = 1 ,2,3
# *         => 1+2+3 = 6    

n = int(input("enter your number\n"))
sum= 0
for i in range(1, n):
    if n == 0 :  
      print("not defined")

    elif n%i==0:
       sum +=i

if n ==sum:
    print("the number is perfect ")
else:
   print("not a perfect number")