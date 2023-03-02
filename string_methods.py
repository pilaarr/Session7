print(dir(""))  # the doble underscore ones are internal ones, we should not use them

help("".capitalize)
print("bogDAN!", "bogDAN!".capitalize())

# lower
print("lower example ABCDEF =", "ABCDEF".lower())

# center
print("James".center(30))

# count
a = "ana-ana-ana-naana"
print(a.count("ana"), a.count("a"))

# find - index of first occurrence unless start is specified
a = "banana, i like bananas"
print(a.find("banana"), a.find("banana", 5), a[5:].find("banana"))  # start from position 5 onwards

# islower, says if all the letters are lower
print("banana".islower(), "Banana".islower())

# split, breaks down by delimiter
a = "I see a cat on a roof"
print(a.split())  # breaks down by space and returns a list
a = "I,like,fish,and,chips!"
print(a.split(","))
print(a.split("fish"))

# join (kinda like the opposite of split)
a = "I see a cat on the roof"
words = a.split()

print(" ".join(words))
print("++".join(words))
print(" freaking ".join(words))