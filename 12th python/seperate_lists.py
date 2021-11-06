def sort(main_list):
       positive_list = []
       negative_list = []
       zero_list = []

       for i in main_list:
              if i == 0:
                     zero_list.append(i)

              elif i > 0:
                     positive_list.append(i)

              elif i < 0:
                     negative_list.append(i)

       print(f'positive_list')
       print(positive_list)
       print('negative_list')
       print(negative_list)
       print('zero_list')
       print(zero_list)

def main():
       main_list = [0, 1, 2, 3, 4, -5, 6, 0, -7, 0, 0, 8, 0, 0, 9, -10, 11, 12, 13, 14]

       sort(main_list)

if __name__ == '__main__':
       main()