def menu():
    print("-" * 40)
    print('{0:^40}'.format("M A I N - M E N U"))
    print("-" * 40)
    print("1. Pinjam Buku ")
    print("2. Kembalikan Buku ")
    print("3. Cek Denda Buku ")
    print("4. Tambah Buku ")
    print("5. Edit/Delete Buku")
    print('6. Search Buku')
    print('7. Stock Buku')
    print("0. Exit ")
    print("-" * 40)


def login():
    print("-" * 40)
    print('{0:^40}'.format("L O G I N"))
    print("-" * 40)
    login = False
    while login == False:
        username = input("Username: ")
        password = input("Password: ")
        if username == "admin" and password == "123":
            login = True
        else:
            print("WRONG USERNAME OR PASSWORD")


def main():
    menu()
    jawaban = -1
    while jawaban < 0 or jawaban > 7:
        jawaban = int(input("Pick your choice: "))
        if jawaban == 1:
            print('-' * 40)
            print('{0:^40}'.format("P I N J A M - B U K U"))
            print('-' * 40)
            import PinjamBuku as pinjam
            pinjam_buku = pinjam.main()
            if pinjam_buku == False:
                main()
            main()

        elif jawaban == 2:
            print('-' * 40)
            print('{0:^40}'.format("P E N G E M B A L I A N"))
            print('-' * 40)
            import KembaliBuku as kembali
            kembali_buku = kembali.main()
            if kembali_buku == False:
                main()
            main()

        elif jawaban == 3:
            print('-' * 40)
            print('{0:^40}'.format("C E K - D E N D A"))
            print('-' * 40)
            import cek_denda as denda
            cekdenda = denda.main()
            if cekdenda == False:
                main()
            main()

        elif jawaban == 4:
            print('-' * 40)
            print('{0:^40}'.format("T A M B A H - B U K U "))
            print('-' * 40)
            import AddBook as add
            add_book = add.main()
            if add_book == False:
                main()

        elif jawaban == 5:
            print('-' * 40)
            print('{0:^40}'.format("E D I T/D E L E T E - B U K U"))
            print('-' * 40)
            print('1. Delete Buku')
            print('2. Edit Buku')
            menu_edit = -1
            while menu_edit < 0 or menu_edit > 2:
                menu_edit = int(input('Pick your choice : '))
                if menu_edit == 1:
                    import DeleteEdit as editdel
                    delete = editdel.delete_book()
                    if delete == False:
                        main()
                    main()
                elif menu_edit == 2:
                    import DeleteEdit as editdel
                    editbuku = editdel.edit_buku()
                    if editbuku == False:
                        main()
                    main()
                else:
                    print('-- Invalid choice --')
        elif jawaban == 6:
            import cobaSearch as search
            print('-' * 40)
            print('{0:^40}'.format("S E A R C H I N G"))
            print('-' * 40)
            searching = search.main()
            if searching == False:
                main()

        elif jawaban == 7:
            import stock_buku as stock
            stock.main()
            main()

        elif jawaban == 0:
            print("BYE - BYE")
            exit()

        else:
            print('-- Invalid choice --')


login()
main()
