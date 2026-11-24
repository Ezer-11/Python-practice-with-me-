# Taking the number of elements
n = int(input("Enter the number of elements: "))

# Taking multiple integers as input and converting them into a list
a = list(map(int, input("Enter your numbers: ").split()))

# Creating an empty dictionary
f = {}

# Traversing the list using indexes
for i in range(len(a)):

    # a[i] gives the actual element at index i
    # We check whether that element already exists as a key in dictionary

    if a[i] in f:

        # If the element already exists,
        # increase its existing frequency by 1
        f[a[i]] += 1

    else:

        # If the element does not exist,
        # create a new key and assign frequency 1
        f[a[i]] = 1

# Printing the final dictionary
print(f)