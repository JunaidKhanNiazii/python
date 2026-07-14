from math import sqrt
n = 15

list = []

for i in range(1,n):
    if n % i ==0:
        list.append(i)
    if i > (n // 2):
        break
list.append(n)
print(list)

# Time complexilty   N / 2 or N 
# space complexity  k

# More optimize way 

n = 36

list = []   # space complexity o(k)

for i in range(1, int(sqrt(n) + 1)): # Time complexity o(Sqrt(N))
    if n % i ==0:
        v = n // i  
        list.append(i)
        if i != v:
            list.append(v)
print(sorted(list)) # Time complexity o(NlogN)

# space complexiy o(k)