# len gives you the length of the entire string
print(len("Hello"), len("Hello1"))

# you can assign a string to any variable:

a = "123"
b = "abcd"

# + will concatenate the strings
c = a + b
print(c)

c = c + b + c
print(c) # 123abcdabcd123abcd

# * you can only multiply with a positive integer and repeats the string
a = "Banana"
print(a*3)
print(4*a)
print((4/2)*a)  # cannot multiply by a float
print((4//2)*a)  # this works because it is an integer
print(int(10/3)*a)

# string are iterable... we can use for on them
for letter in a:
    print(letter, end=" ! ")
for letter in a:
    print(3*letter, end="")

# while to iterate string backwards
a = "@racecar!"
print("\n\n")
i = len(a) - 1
while i >= 0:  # starts printing letter by letter but starting from the back
    print(a[i])
    i -= 1  # i = i - 1