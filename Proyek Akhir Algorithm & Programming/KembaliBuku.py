def main():
    from datetime import date
    import function as f

    def check_data(nama, nim, buku):
        if nama in pinjam_nama:
            check_nama = pinjam_nama[::-1]
            check_nim = pinjam_nim[::-1]
            check_buku = pinjam_buku[::-1]
            check_status = pinjam_status[::-1]
            index_check = check_nama.index(nama)
            if check_nim[index_check] == nim and check_buku[index_check] == buku:
                return True
            else:
                return False
        else:
            return False

    def get_date(tgl_kembali, tgl_pinjam):
        day = (tgl_pinjam.split('-'))[2]
        month = (tgl_pinjam.split('-'))[1]
        year = (tgl_pinjam.split('-'))[0]
        difference = tgl_kembali - date(int(year), int(month), int(day))
        hari = difference.days - 7
        return hari

    ## Read & Get Data Peminjam ##
    file_pinjam = open('Data Pinjam.txt', 'r')
    data_pinjam = file_pinjam.read().split('\n')
    file_pinjam.close()
    pinjam_nama = []
    pinjam_buku = []
    pinjam_tgl = []
    pinjam_nim = []
    pinjam_status = []

    for i in range(len(data_pinjam)):
        field = data_pinjam[i].split(',')
        pinjam_nama.append(field[0])
        pinjam_buku.append(field[2])
        pinjam_tgl.append(field[3])
        pinjam_nim.append(field[1])
        pinjam_status.append(field[4])

    status_input = False
    while status_input == False:
        ## Input Peminjam ##
        input_nama = input('Masukan Nama (0 to menu): ')
        ## Terminate ##
        if input_nama == '0':
            return False
        ###############
        input_nim = input('Masukan NIM : ')
        input_buku = input('Masukan Judul Buku : ')

        check_status = check_data(input_nama, input_nim, input_buku)
        if check_status == False:  # Cek jika data yang dimasukkan tidak sesuai ##
            print('--- Data yang dimasukkan tidak sesuai ---')
            return False

        if check_status == True:

            check_status = pinjam_status[::-1]
            check_nama = pinjam_nama[::-1]
            index_check = check_nama.index(input_nama)
            if check_status[index_check] == '1':
                print('--- Anda telah mengembalikan buku ---')
                return False

            status_input = True

            ## Cari tanggal pinjam ##
            check_nama = pinjam_nama[::-1]
            check_tgl = pinjam_tgl[::-1]
            index_tgl = check_nama.index(input_nama)
            tgl_pinjam = check_tgl[index_tgl]
            tgl_kembali = date.today()
            hari = get_date(tgl_kembali, tgl_pinjam)

            if hari < 1:
                denda = 0
            else:
                denda = hari * 500

            ## Format Output ##
            print('-'*40)
            print('{0:20} {1:1} {2:18}'.format('Nama', ':', input_nama))
            print('{0:20} {1:1} {2:18}'.format('NIM', ':', input_nim))
            print('{0:20} {1:1} {2:18}'.format('Buku', ':', input_buku))
            print('{0:20} {1:1} {2:18}'.format(
                'Denda', ':', 'Rp. ' + str(denda)))
            print('-'*40)
            print('PENGEMBALIAN BUKU BERHASIL'.center(40))
            print('-'*40)

        ## Stock pinjam -1 + write to file ##
            data_buku = f.openFile('Data Buku.txt')
            buku_judul = []
            buku_stock = []
            buku_dipinjam = []
            for i in range(len(data_buku)):
                field = data_buku[i].split(',')
                buku_judul.append(field[0])
                buku_stock.append(field[1])
                buku_dipinjam.append(int(field[2]))
            index = buku_judul.index(input_buku)
            buku_dipinjam[index] -= 1

            write_buku = []
            for i in range(len(buku_judul)):
                text_buku = [buku_judul[i],
                             buku_stock[i], str(buku_dipinjam[i])]
                write_buku.append(text_buku)
            f.writeFile2(write_buku, 3, 'Data Buku.txt')

            ## Ubah status pinjam jd '1' + write to file ##
            check_index = pinjam_nim[::-1]
            index_status = check_index.index(input_nim)
            check_status = pinjam_status[::-1]
            check_status[index_status] = '1'
            pinjam_status = check_status[::-1]

            write_pinjam = []
            for i in range(len(pinjam_buku)):
                text_pinjam = [pinjam_nama[i], pinjam_nim[i],
                               pinjam_buku[i], pinjam_tgl[i], pinjam_status[i]]
                write_pinjam.append(text_pinjam)
            f.writeFile2(write_pinjam, 5, 'Data Pinjam.txt')

            ## Record pengembalian ke file ##
            file_kembali = open('Data Pengembalian.txt', 'a')
            text = input_nama + ',' + input_nim + ',' + \
                input_buku + ',' + str(tgl_kembali) + '\n'
            file_kembali.write(text)
            file_kembali.close()


main()
