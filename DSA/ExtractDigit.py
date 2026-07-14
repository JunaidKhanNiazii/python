n = 5873
number = []
while n != 0:
    R = n % 10
    number.append(R)
    n = n // 10
print(number)