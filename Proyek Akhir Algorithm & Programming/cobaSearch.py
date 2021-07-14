def main():
    import function as f
    import re
    import time


    data = f.openFile('Data Buku.txt')
    book = []
    for i in range(len(data)):
        field = data[i].split(',')
        book.append(field[0])


    result = []

    search_input = input('Masukan buku yang ingin dicari  (0 to menu): ').lower()
    if search_input == '0':
        return False

    for j in range(len(book)):
        hasil = re.findall(search_input,book[j])
        if hasil:
            result.append(book[j])

    result.sort()

    if len(result) > 0:
        print("Buku yang mungkin anda maksud :")
        for k in range(len(result)):
            print('{0:2}. {1:20}'.format(k+1, result[k]))
        main()
    else:
        print('-- Buku yang anda cari tidak ditemukan --')
        time.sleep(0.5)
        main()

main()