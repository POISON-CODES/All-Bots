import csv

with open('employees.csv', 'r') as file:
       reader = csv.reader(file)

       final_list = []

       next(reader)

       for name, salary, department in reader: 
              if int(salary) > 13000:
                     list = []
                     list.append(name)
                     list.append(salary)
                     list.append(department)

                     final_list.append(list)

       if final_list:
              for name, salary, department in final_list:
                     print(f"{name}, {salary}, {department}")

       else:
              print('No employees have salary over 13000')