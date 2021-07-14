def main():
    import datetime
    import function as f

    ## Open File Buku ##
    file_buku = open('Data Buku.txt', 'r')
    data = file_buku.read().split('\n')
    file_buku.close()
    buku = []
    stock_total = []
    stock_dipinjam = []
    stock_available = []
    for i in range(len(data)):
        field = data[i].split(',')
        buku.append(field[0])
        stock_total.append(int(field[1]))
        stock_dipinjam.append(int(field[2]))
        stock_available.append(stock_total[i]-stock_dipinjam[i])

    ## Open File Peminjam ##
    file_pinjam = open('Data Pinjam.txt', 'r')
    data_pinjam = file_pinjam.read().split('\n')
    file_pinjam.close()
    nama_peminjam = []
    nim_peminjam = []
    buku_pinjam = []
    tgl_pinjam = []
    status_pinjam = []
    for i in range(len(data_pinjam)):
        field = data_pinjam[i].split(',')
        nama_peminjam.append(field[0])
        nim_peminjam.append(field[1])
        buku_pinjam.append(field[2])
        tgl_pinjam.append(field[3])
        status_pinjam.append(field[4])

    ## Input Data Peminjam ##
    name_input = input("Nama (0 to menu): ")
    if name_input == '0':
        return False
    nim_input = input("Nomor Induk : ")
    if nim_input in nim_peminjam:  # Cek si peminjam udah kembaliin buku ato belum ###
        check_nim = nim_peminjam[::-1]
        index = check_nim.index(nim_input)
        check_status = status_pinjam[::-1]
        # Kalo status nya '0', berarti dia belum kembaliin buku
        if check_status[index] == '0':
            print('-'*63)
            print('Anda telah meminjam buku, mohon kembalikan buku terlebih dahulu')
            print('-' * 63)
            return False

    found = False
    while found == False:  # Cek judul buku nya sesuai sama database ato ga
        book_input = input("Judul Buku : ")
        if book_input not in buku:
            print('-' * 20)
            print("Buku tidak tersedia".center(20))
            print('-' * 20)
            return False

        else:
            index_buku = buku.index(book_input)
            found = True
            stock_dipinjam[index_buku] += 1
    tanggal_input = datetime.date.today()
    lama = tanggal_input + datetime.timedelta(days=7)

    ## Pemastian Pinjam ##
    print('-'*40)
    print('Data Peminjaman'.center(40))
    print('-' * 40)
    print('{0:20} {1:1} {2:18}'.format("Nama", ':', name_input))
    print('{0:20} {1:1} {2:18}'.format("NIM", ':', nim_input))
    print('{0:20} {1:1} {2:18}'.format("Judul Buku", ':', book_input))
    print('{0:20} {1:1} {2:18}'.format(
        "Tanggal Pinjam", ':', str(tanggal_input)))
    print('{0:20} {1:1} {2:18}'.format("Tanggal Kembali", ':', str(lama)))
    print('-' * 40)
    confirmation = ''  # Mastiin datanya bener ato ga
    while confirmation != 'Y' or confirmation != 'N':
        confirmation = input('Make sure the data is right (Y/N) : ').upper()
        if confirmation == 'Y':
            ## Add data to list ##
            nama_peminjam.append(name_input)
            nim_peminjam.append(nim_input)
            tgl_pinjam.append(str(tanggal_input))
            buku_pinjam.append(book_input)
            status_pinjam.append('0')

            ## Write to file ##
            write = []
            for i in range(len(nama_peminjam)):
                text = [nama_peminjam[i], nim_peminjam[i],
                        buku_pinjam[i], tgl_pinjam[i], status_pinjam[i]]
                write.append(text)
            f.writeFile2(write, 5, 'Data Pinjam.txt')

            ## Ubah Jumlah buku dipinjam ##
            write = []
            for i in range(len(buku)):
                text = [buku[i], str(stock_total[i]), str(stock_dipinjam[i])]
                write.append(text)
            f.writeFile2(write, 3, 'Data Buku.txt')
            break

        elif confirmation == 'N':
            return False

        else:
            print('Invalid input')
    print("-- Terima kasih sudah meminjam --")


main()
