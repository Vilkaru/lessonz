
my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5] # my_lis
i = 0
n = 1
while my_list[i] >= 0:
    if my_list[i] == 0 and len(str(my_list[i])) < len(my_list):
        i = i + n
    elif my_list[i] < 0 and len(str(my_list[i])) < len(my_list):
        break
    else:
        print(my_list[i])
        i = i + n
    













