def countdown(start):
    count = start + 1
    while count > 0:
        yield count
        count -= 1


counter = countdown(5)
for i in counter:
    print(i)
