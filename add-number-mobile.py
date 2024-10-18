list1 = [9121234567, 935123456, 9123457885]
list2 = []

for i in list1:
    if str(i)[0] != '0':
        modified_number = ('0' + str(i)[0:])
        list2.append(modified_number)

print(list2)
