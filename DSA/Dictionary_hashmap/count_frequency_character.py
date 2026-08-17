variable = input("Enter a string: ")
frequency = {}

for i in variable:
    if i in frequency:
        frequency[i] = frequency[i] + 1
    else:
        frequency[i] = 1

print(frequency)