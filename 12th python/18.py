import pickle
def write():
    f=open("students.dat", 'wb')
    while True:
        r=int(input('Enter Roll No..'))
        n = input('Enter Name:')
        record = [r,n]
        pickle.dump(record,f)
        ch=input('Enter more? (Y/N)')
        if ch in "Nn":
            break
    f.close()
    read()

def read():
        f=open("students.dat","rb")
        try:
                while True:
                        rec =pickle.load(f)
                        print(rec)
        except EOFError:
                f.close()
        main()
def update():
        f=open('students.dat', 'rb+')
        rollno=int(input('Enter Roll no whose marks you want to update:'))
        try:
                while True:
                        pos=f.tell()
                        rec=pickle.load(f)
                        if rec[0] == rollno:
                                un=input('Enter the name:')
                                rec[1]=un
                                f.seek(pos)
                                pickle.dump(rec, f)

        except EOFError:
                f.close()
                
        read()

def search():
        f=open('students.dat', 'rb')
        rn = int(input('Enter Roll number to search:'))
        try:
                while True:
                        z=f.tell()
                        data=pickle.load(f)
                        if data[0] == rn:
                            print(data[1])

                            break
        except EOFError:
                f.close()
        main()

def main():
    letter = input('Enter "w" for writing, "r" for reading, "u" to update, "s" for search.')
    lett = letter[0]
    if lett in "wrus":
        if lett == "w":
            write()
        elif lett == "r":
            read()
        elif lett == "u":
            update()
        elif lett == "s":
            search()

    else:
        print('invalid choice.')

if __name__ == "__main__":
    write()