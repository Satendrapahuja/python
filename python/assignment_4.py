number = 0
i = 100
num =0
while number <= i:
    user = input('enter the numbers if u enter q it ll stop and print the number and average :- ')
    if (user != 'q'):
        num = num + int(user)
        i = i + 1
    else:

        print('you enter q')
        break


avg = num / i
print('The user entered the value is :-%d', i)
print('average is :- %d', avg)








