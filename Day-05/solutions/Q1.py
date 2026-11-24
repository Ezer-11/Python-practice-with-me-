# def count_uppercase(s):
#     count = 0
#     for char in s:
#         if char.isupper():
#             count += 1

#     return count

# def count_digit(s):
#     count =0
#     for char in s:
#       if char.isdigit():
#           count+=1
#     return count 

# def count_lowercase(s):
#     count =0
#     for char in s:
#       if char.islower():
#           count+=1
#     return count 

# def count_special(s):
#     count =0
#     for char in s:
#       if not char.isalnum():
#           if char == " ":
#               continue
#           else:
#            count+=1
#     return count 


# s = input("enter your word: ")
# special = count_special(s)
# digit = count_digit(s)
# lowercase =count_lowercase(s)
# uppercase = count_uppercase(s)

# print(special,digit,lowercase,uppercase)

# *more effective single pass function

def count_char(s):

    # Initialize four counters
    uppercase = 0
    lowercase = 0
    digit = 0
    special = 0

    # Traverse the string only once
    for char in s:

        # Ignore spaces
        if char == " ":
            continue

        elif char.isupper():
            uppercase += 1

        elif char.islower():
            lowercase += 1

        elif char.isdigit():
            digit += 1

        else:
            special += 1

    # Return multiple values as a tuple
    return uppercase, lowercase, digit, special


s = input("Enter your word: ")

# Store the returned tuple
store = count_char(s)

print(store)

            