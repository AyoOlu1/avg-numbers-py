import sys
print("This program calculates the geometric and arithmetic mean of a set of "
      "positive numbers\n")
no_of_entries = int(input("How many numbers do you want to input? "))
count = 0
num_list = []
product = 1
while count < no_of_entries:
    num_inputs = eval(input("Enter a  number: "))
    if num_inputs < 0:
        print("Enter a positive number!")
        sys.exit()
    else:
        num_list.append(num_inputs)
        product *= num_inputs
        addition = sum(num_list)
        arith_mean = addition/no_of_entries
        geo_mean = product ** (1/no_of_entries)
        count += 1

print("The arithmetic mean is", arith_mean)
print("The geometric mean is", geo_mean)
