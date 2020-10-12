list_1 = [14, 7, 17, 83, 63, 42, 19]
value = 10
print("list is :" + str(list_1))
count = len([i for i in list_1 if i > value])
print("the numbers greater thn 10 is :-" + str(count))
