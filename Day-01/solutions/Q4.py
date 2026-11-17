#? 4. Second-largest element — Find the second-largest distinct element in a list without using sort().


a = set(map(int, input("Enter your numbers: ").split()))

largest = float("-inf")
second_largest = float("-inf")

for i in range(len(a)):

    if list(a)[i] > largest:
        second_largest = largest
        largest = list(a)[i]

    elif list(a)[i] > second_largest:
        second_largest = list(a)[i]

if second_largest == float("-inf"):
    print("No second-largest distinct number")
else:
    print("Second largest:", second_largest)
    print("Largest:", largest)

 # ! Mistake 1:
# *largest = num
# *second_largest = largest

# *Why wrong?
#* Both variables now contain the same number.
#* Save the old largest FIRST.

# ! Mistake 2:
#* else:
# *    second_largest = num

#* Why wrong?
# *This can overwrite a valid second-largest number.
#* Use elif num > second_largest instead.

# ! Mistake 3:
#* Assuming set elements are sorted.
#* Sets are unordered collections, not sorted lists.

# ? set()
#* Removes duplicate elements from a collection.*
# *Example: {10, 20, 20, 30} becomes {10, 20, 30}
#* Sets do not support indexing.

# ? list()
#* Converts a set into a list.
#* Example: b = list(a)
# *Lists support indexing, such as b[0], b[1].

# ! Important:
#* A set does not guarantee sorted order.
#* Never assume its elements are arranged from smallest to largest.

# ? float("-inf")
#* Represents negative infinity.
#* Useful as an initial value when searching for the largest numbers.
#* Any ordinary integer is greater than negative infinity.
