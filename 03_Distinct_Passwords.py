seen = set()
strings = ["abcd", "cbad", "bacd"]
for string in strings:

    even = sorted(string[::2])
    odd = sorted(string[1::2])

    signature = (tuple(even), tuple(odd))

    seen.add(signature)

print(len(seen))