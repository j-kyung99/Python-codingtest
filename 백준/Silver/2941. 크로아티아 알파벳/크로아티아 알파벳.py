alpha = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
str = input()

for i in alpha:
    str = str.replace(i, "_")
print(len(str))
