numbers = [12,25,7,33,18]
max_val = [numbers[0]]
for i in numbers:
    if max_val[0] < i :
        max_val.pop()
        max_val.append(i)
print(max_val[0])