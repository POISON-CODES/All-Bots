import math

def main():
       num = input('Enter the number to check')
       num = int(num)
       mod = 0
       sum = 0
       org_num = num
       while num > 0:
              mod = num%10
              sum = sum + (mod*mod*mod)
              num = math.floor(num/10)

       if sum == org_num:
              print(f'{org_num} is armstrong')
       else:
              print(f'{org_num} is not armstrong')

if __name__ == '__main__':
       main()