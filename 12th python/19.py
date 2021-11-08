import pickle
def write():
       f=open("Student.dat", 'wb')
       while True:
              r=int(input('Enter Roll No..'))
              n = input('Enter Name:')
              record = [r,n]
              pickle.dump(record,f)
              ch=input('Enter more? (Y/N)')
              if ch in "Nn":
                     break
       f.close()

def read():
       f=open("Student.dat","rb")
       try:
              while True:
                     rec =pickle.load(f)
                     print(rec)
       except EOFError:
              f.close()

def update():
       f=open('student.dat', 'rb+')
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

if __name__ == '__main__':
       write()
       read()
       update()
       read()