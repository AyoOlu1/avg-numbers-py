print("This program calculates the average of a set of numbers")
Sum = 0
num = eval(input("Enter the numbers of entries: "))
count = 1
while count <= num:
    value = eval(input("Input num" +  str(count) + ": "))
    Sum += value
    count += 1
    avg = Sum/num
print(avg)
