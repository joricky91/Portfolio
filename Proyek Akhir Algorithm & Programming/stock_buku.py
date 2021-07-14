def main():
    import function as f

    file_buku = f.openFile('Data Buku.txt')
    data_buku = []
    data_stock = []
    data_available = []

    for i in range(len(file_buku)):
        field = file_buku[i].split(',')
        data_buku.append(field[0])
        data_stock.append(field[1])
        data_available.append(int(field[1])-int(field[2]))

    for i in range(len(file_buku)):
        for j in range(i+1, len(file_buku)):
            if data_available[i] < data_available[j]:
                temp_judul = data_buku[i]
                data_buku[i] = data_buku[j]
                data_buku[j] = temp_judul

                temp_stock = data_stock[i]
                data_stock[i] = data_stock[j]
                data_stock[j] = temp_stock

                temp_avail = data_available[i]
                data_available[i] = data_available[j]
                data_available[j] = temp_avail

    print('-'*45)
    print('DATA STOCK BUKU'.center(46))
    print('-'*45)
    print('{0:^20} {1:1} {2:^8} {3:1} {4:9}'.format(
        'JUDUL', '|', 'STOCK', '|', 'AVAILABLE'))
    print('-'*45)
    for i in range(len(file_buku)):
        print('{0:^20} {1:1} {2:^8} {3:1} {4:^7} {5:1}'.format(
            data_buku[i], '|', data_stock[i], '|', data_available[i], '|'))
    print('-'*45)


main()
