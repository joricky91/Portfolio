def edit_buku():
    import function as f

    def check_buku(judul, list):
        if judul in list:
            return True
        else:
            return False

    file_buku = f.openFile('Data Buku.txt')
    data_buku = []
    data_stock = []
    data_dipinjam = []
    for i in range(len(file_buku)):
        field = file_buku[i].split(',')
        data_buku.append(field[0])
        data_stock.append(field[1])
        data_dipinjam.append(field[2])

    check_status = False
    while check_status == False:
        temp_judul = input('Masukan buku yang ingin diedit (0 to menu): ')
        ### Terminate ###
        if temp_judul == '0':
            return False

        check_status = check_buku(temp_judul, data_buku)
        if check_status == False:
            print('--- Buku yang anda cari tidak ditemukan ---')
            return False

    if check_status == True:
        index_buku = data_buku.index(temp_judul)
        new_judul = input('Masukkan judul baru : ')
        new_stock = input('Masukkan stock baru : ')
        new_borrow = input('Masukkan jumlah buku yang sedang dipinjam : ')

        data_buku[index_buku] = new_judul
        data_stock[index_buku] = new_stock
        data_dipinjam[index_buku] = new_borrow

        write = []
        for i in range(len(data_buku)):
            text = [data_buku[i], data_stock[i], data_dipinjam[i]]
            write.append(text)

        f.writeFile2(write, 3, 'Data Buku.txt')

        print('--- Buku telah berhasil diedit ! ---')


def delete_book():

    def check_buku(judul, list):
        if judul in list:
            return True
        else:
            return False

    import function as f
    file_buku = f.openFile('Data Buku.txt')
    data_buku = []
    data_stock = []
    data_dipinjam = []
    for i in range(len(file_buku)):
        field = file_buku[i].split(',')
        data_buku.append(field[0])
        data_stock.append(field[1])
        data_dipinjam.append(field[2])

    check_status = False
    while check_status == False:
        temp_judul = input('Masukan buku yang ingin dihapus (0 to menu): ')
        ### Terminate ###
        if temp_judul == '0':
            return False

        check_status = check_buku(temp_judul, data_buku)
        if check_status == False:
            print('--- Buku yang anda cari tidak ditemukan ---')
            return False

    if check_status == True:
        index_buku = data_buku.index(temp_judul)

        print('-'*40)
        print('{0:15} {1:1} {2:18}'.format('Buku', ':', temp_judul))
        print('{0:15} {1:1} {2:18}'.format(
            'Stock', ':', data_stock[index_buku]))
        if int(data_dipinjam[index_buku]) > 0:
            print('{0:15} {1:1} {2:18}'.format(
                'Sedang dipinjam', ':', data_dipinjam[index_buku]))
        print('-'*40)

        sure = ''
        while sure != 'Y' or sure != 'N':
            sure = input(
                'Apakah anda yakin untuk menghapus buku ini ? (Y/N) : ').upper()
            if sure == 'Y':
                data_buku.remove(data_buku[index_buku])
                data_dipinjam.remove(data_dipinjam[index_buku])
                data_stock.remove(data_stock[index_buku])

                write = []
                for i in range(len(data_buku)):
                    text = [data_buku[i], data_stock[i], data_dipinjam[i]]
                    write.append(text)

                f.writeFile2(write, 3, 'Data Buku.txt')
                print('--- Buku telah berhasil dihapus ! ---')

                break

            if sure == 'N':
                return False
            else:
                print('-- Invalid input --')
