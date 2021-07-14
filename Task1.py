intList = [10.7, -25, 3/8, 49.6, 50, 62, 74, 84, 97, 101]
sum = 0
for num in intList:
    sum = sum + num
average = sum/len(intList)
print("The number of integer in the list is: ", len(intList))
print("The sum of integer in the list is: ", sum)
print("Average of integer in the list is: ", average)