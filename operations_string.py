s1 = "Hello"
s2 = "world"
print(s1 +""+ s2)
print(s1, "Hello")
print(3*s2)
print((10//2)*s1) #double slashes means integer division
print(s1, len(s1))
print(3*s2, len(3*s2))
for c in s2:
    print(4*c, end="")

new_string = ""
for c in s2:
    new_string += c*4
print(new_string)

# in can be used to check if one string is inside another
print("H" in s1)
print("d" in s2)
print("x" in s1)
print("wor" in s2)