print(dir("hello"))

print(help("hi".capitalize))

print("i like to go to school".capitalize())
print("IS THIS SUPPOSED TO WORK?".capitalize())
print("hello".center(40, "*"))
print("gmail.com".find("john"))
s = "i see a cat who likes to cat while i cat on a cat"
# find all occurences
poz = 0
while True:
    poz = s.find("cat", poz)
    if poz == -1:
        break
    print("found cat on position", poz)
    poz += 1

# lower
s = " I SEE A LOT OF THINGS!"
print(s.lower())


# replace - replaces x with y
s = " i see a cat who likes to eat a rat. what a nice cat"
print(s.replace("c", "r"))
print(s.replace("cat", "lion"))

# split
s = "i like to go shopping"
print(s.split())

# title
s = "i like mountains"
print(s.title())

# upper
s = "i see a lot of things"
print(s.upper().capitalize())