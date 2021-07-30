

for i in range(28):
    temp = list(input().split())
    name = temp[0]
    location = " ".join(item for item in temp[1:])
    print(f'"{temp[0]}" : "{location}",')