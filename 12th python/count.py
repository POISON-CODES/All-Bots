def main():

       string = input('Enter the string')
       org_str = string
       string = string.replace(' ', '')

       integers = 0
       alphabets = 0
       special_chars = 0

       for i in range(len(string)):
              if string[i].isdigit():
                     integers += 1
              elif string[i].isalpha():
                     alphabets += 1
              else:
                     special_chars += 1

       print(f'{alphabets} alphabets, {integers} numbers, {special_chars} special characters.')

if __name__ == '__main__':
       main()