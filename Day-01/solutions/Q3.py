#? 3. Reverse a number — Reverse an integer mathematically without converting it into a string.

a = int (input("enter your number\n"))
digit = 0
reverse = 0

while (a>0):
    digit = a%10
    reverse = reverse  * 10 + digit
    a = a//10

print(reverse)

# *we used while loop because we don't know when to stop.
#* digit = a%10 gives the last digit (remainder).
#* reverse store the last digit. 
#* a = a//10 removes the last digit.
#! note: trace the code manually in the notebook