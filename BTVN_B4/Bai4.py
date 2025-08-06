n = 5
a = ['123', 'hello', 'S45', 'world', '9999']
b = tuple(a)
print("Tuple b:", b)

count = 0
for i in b:
    if i.isdigit():
        count += 1

print("Số phần tử dạng số:", count)