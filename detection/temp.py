

temp = {}

temp2 = input()

for item in temp2.split("\n"):
    key,val = item.split()
    temp[key] = val

print(temp)
