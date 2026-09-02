from collections import Counter
s = input()
freq = Counter(s)
for ch,freq_ in freq.items():
    print(ch,freq_)

ch , freq_ = freq.most_common(1)[0]   
print(f"Most Frequent: {ch} {freq_}")