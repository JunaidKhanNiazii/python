#constraint
#1 <= n[i] <= 10
#n can have 10 ^ 8 element
#m can have 10 ^ 8 element 

n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]

dic = {}
dic2 = {}
for i in n:
    dic[i] = dic.get(i, 0)+1



print(dic)

for j in m:
    if j > 10:
        dic2[j] = 0
    else:
        dic2[j] = dic.get(j,0)

print(dic2)


        
