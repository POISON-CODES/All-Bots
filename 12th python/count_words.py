def main():
       string = input('Enter String')

       string = string.strip()

       list = []

       word = string.split(' ')

       print(len(word))

if __name__ == '__main__':
       main()