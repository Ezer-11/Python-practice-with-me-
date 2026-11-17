#? 2. Positive, negative and zero counter — Take 10 integers and count positive, negative and zero values.

a = list(map(int,input("enter your numbers\n").split()))
# *list will store all the inputs in -> [] 
# *map will convert all the input into integer 
# *split will seaprate everything

positive = 0
negative = 0
zero = 0

for i in range(len(a)):
  
  if(a[i]>0):
    print("positve")
    positive +=1
  elif(a[i]<0):
    print("negative")
    negative+=1
  else:
    print("zero") 
    zero+=1   

print(positive)
print(negative)
print(zero)

# *in list index starts from zero
# *a[i] to acess the element from the list

# !alternate solution
# !we can acces the element inside list without index 

#  *for num in a:
#  *    if num > 0:
#  *       positive += 1
#  *    elif num < 0:
#  *        negative += 1
#  *   else:
#  *     zero += 1
