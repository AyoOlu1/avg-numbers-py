import math
no_of_entries = eval(input("Enter number of entries: "))
i = 1
num_lists = []
while i <= no_of_entries:
        num_inputs = int(input("Enter a number: "))
        num_lists.append(num_inputs)
        num_lists_sum = sum(num_lists)
        arithmetic_mean = num_lists_sum / no_of_entries
        i += 1
print("The arithmetic mean is ", arithmetic_mean)