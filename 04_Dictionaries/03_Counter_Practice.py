from collections import Counter
s = input()
freq = Counter(s)
for ch ,frequency in freq.items():
    print(ch,frequency)
ch,frequency = freq.most_common(1)[0]
print("Most frequent:")
print(ch,frequency)