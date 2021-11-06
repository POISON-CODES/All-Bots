tuple = (1, 0, -2, -3, 4, -5, 6, 7, 8, -9, 10, -11, 0, 254, 12, -23, 0)

positive = 0
negative = 0
zero = 0
for a in tuple:
       if a > 0:
              positive += 1
       elif a < 0:
              negative += 1
       elif a == 0:
              zero += 1


print(f'{positive}positive numbers, {negative} negative numbers and {zero} zeros')