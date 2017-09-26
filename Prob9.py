
import math

num = int(input('Enter a number to find square root: '))

def newtonSqrt(x):
    sqrt = 0.5 * x
    z = 0.5 * (sqrt + x/ sqrt)
    while z != sqrt:
        sqrt = z
        z = 0.5 * (sqrt + x/ sqrt)
    return sqrt

print("Newtons Squareroot:", newtonSqrt(num))
print("Pythons Squareroot:", math.sqrt(num))

