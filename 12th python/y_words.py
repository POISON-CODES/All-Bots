with open('12th python\\story.txt', 'r') as f:
       content = f.read()

       content = content.strip()
       content = content.replace('\n', ' ')
       content = content.replace('.', '')
       content = content.replace('(', '')
       content = content.replace(')', '')
       content = content.replace('-', ' ')

       words = content.split(' ')
       counter = 0
       list = []
       for i in range(len(words) - 1):
              if 'y' in words[i]:
                     if words[i] in list:
                            pass
                     else:
                            list.append(words[i])
                            counter += 1
       print(list)
       print(counter)