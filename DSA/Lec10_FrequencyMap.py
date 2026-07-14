nums = [5,6,7,7,1,9,111,1,1,5,1,1]

# method 1
dic = {}

for i in nums:
    if i in dic:
       dic[i] +=1
    else:
        dic[i] = 1

print(dic)

# Hath method

dic2 = {}
for i in nums:
    dic2[i] = dic2.get(i,0) + 1
print(dic2)