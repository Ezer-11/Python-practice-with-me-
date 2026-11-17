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

#*learning python reads the code from top to bottom if the one condition satisfies it will stop.