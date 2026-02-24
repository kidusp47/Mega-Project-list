import math
n = int(input("Please enter a number: "))


for i in range(n+1):
    Fibonacci_value = round(((((1 + math.sqrt(5))/2)**i) - (((1 - math.sqrt(5))/2)**i))/math.sqrt(5))
    print(Fibonacci_value)