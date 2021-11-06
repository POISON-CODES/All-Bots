tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)

odd = 0
even = 0

for a in tuple:
       if a % 2 == 0:
              even += 1
       else:
              odd += 1


print(f'{odd}odd numbers and {even} numbers')