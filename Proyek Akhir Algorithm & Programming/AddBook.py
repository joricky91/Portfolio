def main():

    import function as f

    def check_book(title, list):
        if title in list:
            return True
        else:
            return False

    data = f.openFile('Data Buku.txt')
    book = []
    stock = []
    borrow = []
    for i in range(len(data)):
        field = data[i].split(',')
        book.append(field[0])
        stock.append(int(field[1]))
        borrow.append(field[2])

    new_book = input('Masukan judul buku (0 to menu): ')

    ## Terminate add book - kembali ke menu ##
    if new_book == '0':
        return False
    #####################################

    new_amount = -1
    while new_amount < 1:
        new_amount = int(input('Masukan jumlah buku : '))
    found = check_book(new_book, book)

    print('-'*40)
    print('Judul : {0:16}'.format(new_book))
    print('Jumlah : {0:16}'.format(str(new_amount)))
    print('-'*40)

    if found == False:  # Buku Baru #
        book.append(new_book)
        stock.append(new_amount)
        borrow.append('0')
        print('--- Buku baru berhasil ditambahkan ---')
    if found == True:  # Buku Ada, Stok nambah #
        index = book.index(new_book)
        stock[index] += new_amount
        print("--- Stok baru berhasil ditambahkan ---")

    write = []
    for j in range(len(book)):
        text = [book[j], str(stock[j]), borrow[j]]
        write.append(text)

    f.writeFile2(write, 3, 'Data Buku.txt')


main()
