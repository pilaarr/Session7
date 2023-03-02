a = "abdcefghijklmnop"
print(a[3:6])  # the beginning is included but the end is not (we need to put 6 instead of 5
print(a[13:17], a[-3:], a[13:])  # if you don't put anything after : it goes until the end
print(a[:10])  # from the beginning until the position we put

# step slice
print(a[:10:2])  # you go two by two
print(a[:10:2], a[::3])

# you can use negative start, stop and even step
print(1[10:3:-1])
print(a[::-1])  # reversed string

# check if a string is palindrome:
a = "racecar"
if a == a[::-1]:
    print(a, "is palindrome")
else:
    print("not so much")