4#?Find the first non-repeating character — Find the first character appearing exactly once.


a = str(input("enter yout name "))
find = 0
for char in a:
    if a.count(char)==1:

      print(char)
      break

    # *loop iterates for every character in the string 
    #*and a.count(char) counts every character in the string 
    # *like a = "samuel"
    # *first it wil character is s it will check the occurance and then stop if it finds 