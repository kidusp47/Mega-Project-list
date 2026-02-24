def fibonacci(n):
    final = ""
    values = []
    for i in range(n+1):
        fibonacci_value = round(((((1 + math.sqrt(5))/2)**i) - (((1 - math.sqrt(5))/2)**i))/math.sqrt(5))
        values.append(fibonacci_value)
        final = ", ".join(map(str, values))

    print(final)

import math
num = int(input("Please enter a number: "))
fibonacci(num)