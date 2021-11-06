dict = {
       'kid_1': '30',
       'kid_2': '50',
       'kid_3': '40',
       'kid_4': '100',
       'kid_5': '70',
}

name = input('Enter student name')
if name in dict:
       print(f'{name} got {dict[name]} marks')
else:
       print(f'{name} not there in dictionary')