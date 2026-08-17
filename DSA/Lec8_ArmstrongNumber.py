n = 153
original = n
new = 0
# count = 0

# # while n!= 0:
# #     count +=1
# #     n = n // 10

count = len( str(n))


n = original

while n!= 0:
    R = n % 10
    R = R ** count 
    new +=R
    n = n // 10
print(new)


# Time complexity = O(N)
# space complexity in o(1)