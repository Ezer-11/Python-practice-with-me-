#? 1. Largest of three numbers — Take three numbers and find the largest using conditional statements.

a = int(input("enter your first number\n"))
b = int(input("enter your second number\n"))
c = int(input("enter your third number\n"))

if(a ==b and b == c):
    print("all are equal")
elif(a>=b and a >=c):
    print(f"{a} is the largest")

elif(b>=c and b> a):
    print(f"{b} is the largest ")

else:
    print(f"{c} is the largest")


#* If if is True → execute the if block and skip the elif and else blocks.

#* If if is False → check the elif condition.

#* if both are False → check else, if present.