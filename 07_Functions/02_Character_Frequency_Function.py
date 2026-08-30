def character_frequency(s):

    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    return freq


s = input()

freq = character_frequency(s)

for ch, frequency in freq.items():
    print(ch, frequency)