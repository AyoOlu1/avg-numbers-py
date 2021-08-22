import math
import sys
print("This program calculates the natural logarithm of 1/(1-x)\n")
print("Enter a value of x less than one\n")
while True:
    x = eval(input("Enter a the value of x: "))
    if x >= 0:
        print("Enter a value less than one")
        sys.exit()
    else:
        y = 1 / (1 - x)
        logarithm = math.log(y)
        print("The natural logarithm of 1/(1-x) is", logarithm)
