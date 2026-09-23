import os

siswa = {}

nis = ''
while True:
    nis = input('NIS: ')
    if len(nis) < 10 or len(nis) > 10 or not(nis.isnumeric()):
        input('Nomor NIS maximum 10 characters in numbers\nPress Enter to try again...')
        os.system('clear')
    else:
        break
nama = input('Nama: ')
alamat = input('Alamat: ')
kontak = input('Nomor kontak: ')

siswa[nis] = {'nama':nama,'alamat':alamat,'kontak':kontak}

print(siswa)