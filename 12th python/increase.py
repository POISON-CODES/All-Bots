import csv
from os import read

with open('12th python\\employees.csv', 'r') as file:
       reader = csv.reader(file)

       final_list =[]

       next(reader)

       for name, salary, department in reader:
              list = []
              list.append(name)
              list.append(int(salary)+1000)
              list.append(department)

              final_list.append(list)

       for name, salary, department in final_list:
              print(f'{name} {salary} {department}')