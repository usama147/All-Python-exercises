Cars = [56, 78, 34, 21, 56, 34, 125, 45, 89, 75, 12, 56]
print("Smallest number is", min(Cars))  # Displays the smallest number from the list
print("Largest number is", max(Cars))  # Displays the largest number from the list
total = sum(Cars)
print("The sum of all the numbers are", total)  # Displays the sum of all the numbers.
Cars = list(dict.fromkeys(Cars))  # remove duplicate numbers
print(Cars)  # Prints list without duplicate numbers.

