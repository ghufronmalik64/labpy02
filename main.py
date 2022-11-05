print("Nama         :   Ghufron Malik")
print("Kelas        :   TI.22.B2")
print("Mata Kuliah  :   Bahasa Pemrograman")
print('===================================')

A = int(input("Masukkan bilangan A: "))
B = int(input("Masukkan bilangan B: "))
C = int(input("Masukkan bilangan C: "))

if A>B:
    maks = A
else:
    maks = B
if C>A:
    maks = C

print("BILANGAN TERBESAR ADALAH: ",maks)