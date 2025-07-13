f = open("where.txt")
print(f.readline())
f.close

with open("where.txt", "a") as f:
    f.write("\nadded line")

with open("where.txt") as f:
    print(f.read())