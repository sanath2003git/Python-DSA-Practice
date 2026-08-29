numbers = list(map(int,input().split()))
freq = {}
for num in numbers:
    freq[num] = freq.get(num,0) + 1
for num in freq:
    if freq[num] == 1:
        print(num)
        exit()
print("None")