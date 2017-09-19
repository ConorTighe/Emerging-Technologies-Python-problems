# Factorial - Problem 4

def factorial(num):
   sum = 0
   for n in range(1,num):
        num = num * n

   values = list(str(num))
   for v in values:
       sum += int(v)
   print "Factorial: ", num, "Sum: ", sum
   return;

factorial(10)
