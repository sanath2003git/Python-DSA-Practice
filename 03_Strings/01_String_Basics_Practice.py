s = input()
print(len(s))
print(s[0])
print(s[-1])
rev = s[::-1]
print(rev)
count = 0
for ch in s:
    if ch in "aeiou":
        count += 1
print(count)
if s == rev:
    print("PALINDROME")
else:
    print("NOT PALINDROME")