#? 4. Check whether two strings are anagrams — Ignore spaces and case; don't use sorting.
# ! GOOD QUESTION !!!

#* Two strings are called anagrams when they contain exactly the same characters,
#* with exactly the same frequency(occurance of latter in word), but possibly in a different order.

# example : String 1	String 2	Result
#          listen	    silent	   True
#          hello	    world	  False

# ! important concept 


str1 = input("Enter your word: ")
str2 = input("Enter your second word: ")

# # * Convert both strings to lowercase and remove spaces
# # * replace(" ", "") replaces every space with an empty string
str1 = str1.lower().replace(" ", "")
str2 = str2.lower().replace(" ", "")

# # * Initially assume both strings are anagrams
is_anagram = True

# # ! Anagrams must have equal lengths
if len(str1) != len(str2):
    is_anagram = False

else:
#     # * Traverse every character in the first string
    for char in str1:

#         # * count(char) returns the frequency of that character
#         # ! If even one frequency differs, they are not anagrams
        if str1.count(char) != str2.count(char):
            is_anagram = False

#             # ! Stop checking once a mismatch is found
            break

 # * Print the final result after checking all characters
if is_anagram:
    print("The given words are anagrams")
else:
    print("The given words are not anagrams")


#* str1.count(char) here char is equal for both like 
#* str1 = "sb" and str2 = "bd" the condition checks like -> 
#* if str1.count(s) != str2.count(s)

