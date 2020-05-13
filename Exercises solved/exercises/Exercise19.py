# Organizing tuples

datas = []
while True:
    data = input()

    if not data:
        break
    
    datas.append(tuple(data.split(',')))

print(sorted(datas))