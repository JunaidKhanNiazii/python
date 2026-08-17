word = "python is easy python is powerful "
words = word.split(" ")
freq = {}

for i in words:
    if i in freq:
        freq[i] +=1
    else:
        freq[i] = 1
print(freq)