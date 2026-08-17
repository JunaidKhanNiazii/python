s = "azyxyyzaaa"

q = ["d", "a", "y", "x"]

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

for ch in q:
    print(ch, freq.get(ch, 0))