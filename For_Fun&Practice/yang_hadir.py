import os

orang = []

while True:
    os.system('clear')
    nama = input('Yang Hadir: ')
    orang.append(nama)
    confirm = input('Confirm list? (y/n): ')
    if confirm == "n":
        break
print("-"*21)
print("|{:^2}|{:^12}|".format("No", "Nama"))
print("-"*21)

for i in range(len(orang)):
    print("|{:^2}|{:^12}|".format(i+1, orang[i]))
    print("-"*21)