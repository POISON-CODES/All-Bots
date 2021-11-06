list = [10, 20, 30, 40, 50]

second_last = list[len(list) - 2]
last = list[len(list) - 1]

list[len(list) - 2] = last
list[len(list) - 1] = second_last

final_list = []

j = 1
length = len(list)
for i in range(length):
       index = length - j
       final_list.append(list[index])
       j += 1

print(final_list)

