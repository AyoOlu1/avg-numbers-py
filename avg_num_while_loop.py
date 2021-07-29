no_of_elements = int(input("Number of elements: "))
count = 1
Sum = 0
while count <= no_of_elements:
    # if user input is < 1, print "enter +ve num"
    elements = eval(input("Enter the each member of the elements: "))
    Sum += elements
    count += 1
average = Sum / no_of_elements
print(average)