with open('12th python\\text.txt', 'r') as f:
       content = f.read()

       content = str(content)
       content = content.strip()
       words = content.split(' ')
       j=0
       for i in range(len(words) - 1):
              i=i-j
              if len(words[i]) > 4:
                     words.pop(i)
                     j=j+1

       print(len(words))