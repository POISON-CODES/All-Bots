def main():
       string = input('Enter String')

       for i in range(len(string)):
              if string[i].isupper():
                     string[i] = string[i].lower()

       print(string)


'''OR

def main():
       string = input('Enter String')

       string = string.lower()

       print(string)

'''

if __name__ == '__main__':
       main()