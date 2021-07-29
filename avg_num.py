from typing import Any, Union

Sum = 0
num = eval(input("Enter how many numbers: "))
count = 0
while count < num:
    value = eval(input("input a num: "))
    Sum += value
    count += 1
    avg = Sum/num
print(avg)
