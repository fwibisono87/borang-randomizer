import random

def pembatas(karakter):
    '''Membuat pembatas dari simbol di argumen '''
    return print (karakter*90)

DaftarNama = []
ListPossibleScore = [1, 2, 3, 4, 5]

print ("Nilai Borang B1 Generator")
print ("Made ny FW for ISEKAI")
print ("This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.")
input("Press enter to continue... ")
print ("")

pembatas("%")
Nama1 = input ("Masukkan nama anggota pertama... ")
DaftarNama.append(Nama1)
Nama2 = input ("Masukkan nama anggota kedua... ")
DaftarNama.append(Nama2)
Nama3 = input ("Masukkan nama anggota ketiga... ")
DaftarNama.append(Nama3)
Nama4 = input ("Masukkan nama anggota keempat... ")
DaftarNama.append(Nama4)
Nama5 = input ("Masukkan nama anggota kelima... ")
DaftarNama.append(Nama5)
Nama6 = input ("Masukkan nama anggota keenam... ")
DaftarNama.append(Nama6)
Nama7 = input ("Masukkan nama anggota ketujuh... ")
DaftarNama.append(Nama7)
pembatas("%")

BatasBawah = int(input ("Masukkan nilai terendah yang anda mau berikan... "))
BatasAtas = int(input ("Masukkan nilai tertinggi yang anda mau berikan... "))

if BatasBawah not in ListPossibleScore:
    print ("Input tidak valid. mengunnakan 3 sebagai batas bawah.")
    BatasBawah=3
if BatasAtas <BatasBawah or BatasBawah>5:
    print ("Input tidak valid. menggunakan 5 sebagai batas atas")
    BatasAtas=5

pembatas("%")
pembatas("_")
print ("{:>3} {:<35} {:<10} {:<10} {:<10} {:<10} ". format("No.", "Nama", "Nilai 1", "Nilai 2", "Nilai 3", "Nilai 4"))
pembatas("_")
Number = 1
Sentinel = 0
while (Sentinel==0):
    for name in DaftarNama:
        N1=random.randint(BatasBawah,BatasAtas)
        N2=random.randint(BatasBawah,BatasAtas)
        N3=random.randint(BatasBawah,BatasAtas)
        N4=random.randint(BatasBawah,BatasAtas)
        print ("{:>3} {:<35} {:<10} {:<10} {:<10} {:<10} ". format(Number, name, N1, N2, N3, N4))
        Number+=1
    pembatas("%")
    Checker=input("Tekan enter untuk mengulangi randomization. Masukkan 1 untuk keluar" )
    if Checker.isdigit():
        Checker = int(Checker)
        Sentinel += Checker
    else:
        Number = 1

