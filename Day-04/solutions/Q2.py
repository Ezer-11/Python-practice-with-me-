#? Q2. MULTIPLICATION TABLE

#* Take an integer and print its multiplication table from 1 to 10.

# *Input:
#* Output:
#* 7 x 1 = 7
#* 7 x 2 = 14
#* 7 x 3 = 21...so on till 10

n = int(input("enter your number"))

for i in range(1,11):

   print(f"{n} x {i} = {n*i}" )  #* new thing print f string  