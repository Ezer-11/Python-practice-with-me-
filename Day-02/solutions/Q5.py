# ? 5. Check whether a list is sorted — Check non-decreasing order without sort() or sorted().

a = list(map(int, input("Enter numbers: ").split()))

is_sorted = True

for i in range(len(a) - 1):

    if a[i] > a[i+1]:
        is_sorted = False
        break

if is_sorted:
    print("Sorted")
else:
    print("Not sorted")

#* we assumed that the initial list is sorted and on the basis of that we checked and whenever 
#* this type of question comes like it is sorted or not like you have to give answer 
#* in yes or no go with this approach assume it and then break it
