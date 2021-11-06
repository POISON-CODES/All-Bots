def sum(list:list):
       sum = 0
       for i in range(len(list)):
              sum = sum + list[i]

       print(f'sum is {sum}')
           
def main():
       n = input('Enter "n"')
       n = int(n)

       list = [0, 1]
       for i in range(n-2):
              length = len(list)

              append = list[length-1] + list[length-2]

              list.append(append)

       sum(list)       

if __name__ == '__main__':
       main()