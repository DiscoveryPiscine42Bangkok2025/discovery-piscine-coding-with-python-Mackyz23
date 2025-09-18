array = [2,8,9,48,8,22,-12,2]
new_array = []
for i in array:
    if i > 5 and i+2 not in new_array:
        new_array.append(i + 2)
print("Original array:", array)
print("New array:", new_array)