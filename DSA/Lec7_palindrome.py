original = n = 1221
new = 0
while n != 0:
    R = n % 10
    new = new * 10 + R
    # print(new)
    n = n // 10

print (new)
if original ==  new:
    print("Palindrome")
else:
    print("Not a Palindrome")


# Time complexity = N
# Space complexity 2 variable 