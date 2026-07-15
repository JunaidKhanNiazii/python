n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]

freq = [0] * 11    # index 0 unused

for x in n:
    freq[x] += 1

for q in m:
    if 1 <= q <= 10:
        print(q, freq[q])
    else:
        print(q, 0)