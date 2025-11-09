test = ["apple","orange","plum","grape","banana"]
a = 0

for i in test:
    print(f"The number of characters in element {a} is {len(i)}.")
    a += 1

a = 0

while a <= 4:
    print(f"The number of characters in element {a} is {len(test[a])}.")
    a += 1
