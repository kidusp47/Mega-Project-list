from decimal import Decimal, getcontext
n = int(input("Enter n: "))
getcontext().prec = n + 5

if n >1000:
    print("The maximum limit of characters is 1000")
    exit()
pi = Decimal(3)
i = 2
sign = 1
while True:
    term = Decimal(4)/ (Decimal(i) * Decimal(i+1 ) * Decimal(i+2))
    if term < Decimal(10) ** (-n):
        break
    pi += sign * term
    sign *= -1
    i += 2
pi_str = str(pi)
print(f"Your pi value to {n} is {pi_str[:n + 2]}")

