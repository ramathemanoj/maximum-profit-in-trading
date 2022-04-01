list_a = [10, 1, 2, 3, 4, 9]

n = len(list_a)
num_list = []
for i in range(n):
    row = []
    for j in range(i, n):
        row.append(list_a[j] - list_a[i])
    num_list.append(max(row))
print(max(num_list))
