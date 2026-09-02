from collections import Counter
s = input()
freq =Counter(s)
for ch in s:
    if freq[ch] == 1:
        print(ch)
        break
else:
    print("None")