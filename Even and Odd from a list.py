even_odd_list = [2, 5, 78, 93, 3, 15, 34, 7, 8, 5, 1, 9]

even = []   # a list for even numbers

odd = []    # a list for odd numbers

for num in even_odd_list:   # for each number in the original list,
    if num % 2 == 0:        # if dividing the number by 2 gives a remainder of 0,
        even.append(num)    # add the number to the list named even using Python's list append() method
    else:
        odd.append(num)     # otherwise, append it to the list named odd

# This empty list will now contain the populated even and odd lists
separated = []

separated.append(even)  # append the list named even to separated

separated.append(odd)   # append the list named odd to separated

# prints out the contents of both lists and not just the variable names
print(separated)
