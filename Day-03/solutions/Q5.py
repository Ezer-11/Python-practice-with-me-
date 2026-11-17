#? 5. Find the longest increasing continuous sequence
#* — Find the length of the longest strictly increasing contiguous sequence.

a = list(map(int, input("Enter numbers: ").split()))

# * Start with length 1 because one element is itself a sequence
current_length = 1
max_length = 1

for i in range(len(a) - 1):

    # * Compare adjacent elements
    # ! Strictly increasing means next element > current element
    if a[i] < a[i+1]:

        # * Extend the current increasing sequence
        current_length += 1

        # * Update maximum only when current sequence is longer
        if current_length > max_length:
            max_length = current_length

    else:
        # ! Sequence breaks, so start a new sequence
        current_length = 1

# * max_length stores the longest sequence found
print(max_length)