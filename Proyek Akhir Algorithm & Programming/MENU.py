condition = True
while condition == True:

    print("-" * 40)
    print('{0:^40}'.format("L O G I N"))
    print("-" * 40)
    username = input("Username: ")
    password = input("Password: ")
    if username == "admin" and password == "123":
        print("-" * 40)
        print('{0:^40}'.format("M A I N - M E N U"))
        print("-" * 40)
        print("1. Pinjam Buku ")
        print("2. Kembalikan Buku ")
        print("3. Cek Denda Buku ")
        print("4. Tambah Buku ")
        print("5. Exit ")
        print("-" * 40)
        jawaban = input("Pick your choice: ")
        if jawaban == "1":
            print("-" * 40)
            print('{0:^40}'.format("P I N J A M - B U K U"))
            print("-" * 40)
            import PinjamBuku as pinjamBuku

            pinjamBuku.main()
        elif jawaban == "2":
            print("-" * 40)
            print('{0:^40}'.format("P E N G E M B A L I A N"))
            print("-" * 40)
            import KembaliBuku as kembaliBuku
            kembaliBuku.main()

        elif jawaban == "3":
            print("-" * 40)
            print('{0:^40}'.format("C E K - D E N D A"))
            print("-" * 40)
            import cek_denda as cekDenda
            cekDenda.main()

        elif jawaban == "4":
            print("-" * 40)
            print('{0:^40}'.format("T A M B A H - B U K U "))
            print("-" * 40)
            import AddBook as addBook
            addBook.main()
            
        else:
            print("BYE - BYE")
            condition = False

    else:
        print("WRONG USERNAME OR PASSWORD")


