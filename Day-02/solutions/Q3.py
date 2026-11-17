#? 3. Count vowels in a string — Count English vowels regardless of case.

word = input("Enter a word: ")

count = 0

for character in word:
    if character.lower() in "aeiou":
        count += 1

print(count)

# !One important programming concept to remember:
#* - for i in range(len(a)) → iterates over indexes.
#* - for character in word → iterates directly over characters.
