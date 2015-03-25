###########
class bcolors:
  OKGREEN = '\033[92m'
  HEADER = '\033[95m'
  UNDERLINE = '\033[4m'
running = True
while running:
    print '\033[1;31m-------------------- \033[1;m'
    print '\033[1;31mNhap phep tinh Em oi \033[1;m'
    print "1.Cong"
    print "2.Tru"
    print "3.Nhan"
    print "4.Chia"
    print "5.Fibonacci"
    print "6.Thoat chuong trinh"
    choice = raw_input('Chon (1-6): ')
# Thuc hien phep tinh
    if choice == "1":
             num1 = float(raw_input('Moi Ban nhap so thu 1: '))
             num2 = float(raw_input('Moi Ban nhap so thu 2: '))
             print '\033[1;31m-------------------- \033[1;m'
             print '\033[1;32mTong= \033[1;m',num1+num2
    elif choice == "2":
             num1 = float(raw_input('Moi Ban nhap so thu 1: '))
             num2 = float(raw_input('Moi Ban nhap so thu 2: '))
             print '\033[1;31m-------------------- \033[1;m'
             print '\033[1;32mHieu= \033[1;m', num1-num2
    elif choice == "3":
             num1 = float(raw_input('Moi Ban nhap so thu 1: '))
             num2 = float(raw_input('Moi Ban nhap so thu 2: '))
             print '\033[1;31m-------------------- \033[1;m'
             print '\033[1;32mTich= \033[1;m', num1*num2
    elif choice == "4":
             num1 = float(raw_input('Moi Ban nhap so thu 1: '))
             num2 = float(raw_input('Moi Ban nhap so thu 2: '))
             while num2 == 0:
                     num2 = float(raw_input('Nhap lai:'))
             print '\033[1;31m-------------------- \033[1;m'
             print '\033[1;32mThuong= \033[1;m', num1/num2
#Tinh Fibonacci			 
    elif choice == "5":
             x = int(raw_input('Tinh F(n), Moi ban nhap x: '))
             num1=0
             num2=1
             i=1
             f=0
             if x==0 or x==1:
                     y=x
             else:
               while i<x:
                     y=num1+num2
                     num1=num2
                     num2=y
                     i=i+1
             print '\033[1;31m-------------------- \033[1;m'
             print 'F('+str(x)+')= ', y
# Thoat chuong trinh			 
    elif choice == "6":
         running = False

