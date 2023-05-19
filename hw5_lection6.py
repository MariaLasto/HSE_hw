dictionary = {}

with open("orders.txt", encoding='utf-8') as f:
    for line in f.readlines():
        key, val = line.split(' ')
        if key in dictionary:
            dictionary[key] += int(val)
        else:
            dictionary[key] = int(val)
print(dictionary)








