import math
no_of_entries = int(input("Enter number of entries:"))
i = 1
num_lists = []
while i <= no_of_entries:
    num_inputs = int(input("Enter a number"))
    num_lists.append(num_inputs)
    geo_mean = (math.prod(num_lists)) ** (1/no_of_entries)
    i += 1
print("The geometric mean is ",geo_mean)
