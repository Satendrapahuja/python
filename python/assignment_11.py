def intersection(list_1, list_2):
    return list(set(list_1) & set(list_2))
list_1 = [4, 6, 8, 75, 11, 55, 123]
list_2 = [4, 6, 2, 99, 11, 00, 121]
print(intersection(list_1, list_2))
