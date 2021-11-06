def prime(number):
       for num in range(number):
              flag = False
              if num > 1:
                     for i in range(2, num):
                            if (num % i) == 0:
                                   flag = True
                                   break
                     if flag==False:
                            print(num)


def main():
       number = input('Enter the number to find prime numbers till\n')
       prime(int(number))

if __name__ == '__main__':
       main()