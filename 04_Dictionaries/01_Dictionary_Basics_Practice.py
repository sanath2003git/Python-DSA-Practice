numbers = list(map(int,input().split()))
freq = {}
for num in numbers:
    freq[num] = freq.get(num,0) + 1
print(freq)
for number , frequency in freq.items():
    print(f"{number} -> {frequency}")