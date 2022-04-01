list_a = ["book", "book", "pen", "book", "pen", "pen", "pencil", "pencil", "book", "pen", "pen", "pen"]

dict_a = {} 
for word in list_a:
    if word in dict_a:
        dict_a[word] += 1 
    else:
        dict_a[word] = 1

list_b = list(dict_a.values())
maximum = max(dict_a.values())
index = list_b.index(maximum)

most_repeated_word = dict([list(dict_a.items())[index]])
print(most_repeated_word)
