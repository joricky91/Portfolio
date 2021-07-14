def main():
    from datetime import date
    today = date.today()

    def telatkembali(hariini, tanggalpinjam):
        day = (tanggalpinjam.split('-'))[2]
        month = (tanggalpinjam.split('-'))[1]
        year = (tanggalpinjam.split('-'))[0]
        hari = hariini - date(int(year), int(month), int(day))
        delta = hari.days
        return delta

    def denda(days_difference):
        delta = days_difference - 7
        denda = 500 * delta
        print('{0:19} {1:1} {2:18}'.format(
            "Denda anda hari ini adalah", ":", 'Rp'+str(denda)))

    def ceknama(nama, list):
        if nama in list:
            return True
        else:
            return False

    cek = open('Data Pinjam.txt', 'r')
    data = cek.read().split('\n')
    name = []
    book = []
    borrow = []
    status = []

    for i in range(len(data)):
        field = data[i].split(',')
        name.append(field[0])
        book.append(field[2])
        borrow.append(field[3])
        status.append(field[4])

    name_list = name[::-1]
    book_list = book[::-1]
    borrow_list = borrow[::-1]
    status_list = status[::-1]

    inputnama = input("Masukkan nama (0 to menu): ")
    if inputnama == '0':
        return False
    found = ceknama(inputnama, name_list)

    if found == True:
        index = name_list.index(inputnama)
        if status_list[index] == '0':
            if telatkembali(today, borrow[index]) > 7:
                print('-'*40)
                print('{0:19} {1:1} {2:18}'.format("Nama", ":", inputnama))
                print('{0:19} {1:1} {2:18}'.format(
                    "Judul buku", ":", book_list[index]))
                print('{0:19} {1:1} {2:18}'.format(
                    "Tanggal pinjam", ":", borrow_list[index]))
                print('{0:19} {1:1} {2:18}'.format(
                    "Tanggal hari ini", ":", str(today)))
                denda(telatkembali(today, borrow_list[index]))
                print("CATATAN : denda per hari Rp.500,-".center(40))
                print('-'*40)

            if telatkembali(today, borrow[index]) <= 7:
                print('-'*40)
                print('{0:19} {1:1} {2:18}'.format("Nama", ":", inputnama))
                print('{0:19} {1:1} {2:18}'.format(
                    "Judul buku", ":", book_list[index]))
                print('{0:19} {1:1} {2:18}'.format(
                    "Tanggal pinjam", ":", borrow_list[index]))
                print('{0:19} {1:1} {2:18}'.format(
                    "Tanggal hari ini", ":", str(today)))
                print('-'*40)
                print('Anda belum melebihi batas pengembalian'.center(40))
                print('-'*40)
        else:
            print('-- Anda sudah mengembalikan buku --')

    if found == False:
        print("Nama tidak ditemukan.")


main()
