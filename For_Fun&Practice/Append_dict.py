import os

siswa = {}

while True:
    nis = input('NIS: ')
    nama = input('Nama: ') 
    alamat = input('Alamat: ')
    kontak = input('Nomor kontak: ')

    siswa[nis] = {
        'nama': nama,
        'alamat': alamat,
        'kontak': kontak
    }

    lanjut = input("Tambah siswa lagi? (y/n): ")
    if lanjut.lower() != 'y':
        os.system('clear')
    else:
        break

print("Data semua siswa:")
for nis, info in siswa.items():
    print(f"NIS: {nis}, Nama: {info['nama']}, Alamat: {info['alamat']}, Kontak: {info['kontak']}")