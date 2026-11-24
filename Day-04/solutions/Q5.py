#? Q5. FIND ALL PRIME NUMBERS IN A RANGE
a = int(input("enter your first number of range\n"))
b = int(input("enter your second number of range\n"))
l1 = []

i = 1
j = a

while (i < b+1 and j < b+1 ):

    if b > a :
     if j % i == 0 and j % i == 1 :
    
        l1.append([j])
    else:
       print("please assain a greater number than b")
print(l1)