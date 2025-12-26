# GUDANG (DATA STOK)

# PROJECT PLANNING
# Goal : Membuat Rencana Program : Preview Data Stok saat ini, Menambahkan stok yang baru datang, 
# dan Mengurangi stok apabila laku dibeli orang,  

# Task : Problem: stok yang tidak update
#        Sektor Bisnis: frozen food
#        Stakeholder: admin
#        Data yang digunakan : 
# ID Produk |Kategori | Produk | Jumlah Stok | Last Update  


#CREATE MENU 
# Goal : Memiliki Tampilan Menu
# Task : Buat tampilan Menu Program 


ListProduct = {

        "ID Product" : ["SN1", "SN2","AY1","AY2","SA1","SA2","IK1","IK2"],
        "Category" : ["Snack","Snack","Ayam","Ayam","Sapi","Sapi","Ikan","Ikan"],
        "Product" : ["Tahu Susu", "Cireng", "Fillet Dada Ayam", "Fillet Paha Ayam", "Daging Sapi Giling","Slice Beef", "Salmon Scrape","Fillet Dori"],
        "Qty Stock" : [10,10,10,10,10,10,10,10],
        "Last Update" : ["17 Des 2025","17 Des 2025","17 Des 2025","17 Des 2025","17 Des 2025","17 Des 2025","17 Des 2025","17 Des 2025"]
}

#CREATE FUNCTIONALITY
# Goal : Fungsionalitas program
# TASK : Fungsi Create, Read, Update, Delete


def Main_Menu():
    MainMenu = ["Stock Opname Bekuu.id",
                " ",
                "List Menu :",
                "1.Display Current Stock", #READ
                "2.Add New Product", #CREATE
                "3.Add Stock for Current Product", #UPDATE
                "4.Reduce Stock for Current Product", #UPDATE
                "5.Delete Product", #DELETE
                "6.Exit Menu",
                " ",
                ]

    for item in MainMenu:
        print(item)

Main_Menu()

MenuInput = int(input("Masukkan angka Menu yang ingin dijalankan : ", ))

def Read_Data():
    print()
    print("Daftar Produk Bekuu.id")
    print()
    # Cetak header
    print(f"|{'ID Product':<10}|{'Category':<20}|{'Product':<20}|{'Qty Stock':<15}|{'Last Update':<20}|")
    print("-" * 80)
    # Cetak List Produk
    for ID, Category, Product, Stock, LastUpdate in zip(ListProduct['ID Product'], ListProduct['Category'], ListProduct['Product'], ListProduct['Qty Stock'], ListProduct['Last Update']):
        print(f"|{ID:<10}|{Category:<20}|{Product:<20}|{Stock:<15}|{LastUpdate:<20}|")
    #Cetak Main Menu
    print()


def BacktoMainMenu() :
    ContinueOrNot = (input("Apakah Anda Mau Kembali Ke Menu Utama - [Ya(Y)/Tidak(T)]: ", ))
    while ContinueOrNot != "T" and ContinueOrNot != "Y":
        print("Mohon Masukkan Input Sesuai Program (Y/T)")
        ContinueOrNot = (input("Apakah Anda Mau Kembali Ke Menu Utama - [Ya(Y)/Tidak(T)]: ", ))
    if ContinueOrNot == "Y":
        Main_Menu()    
    else:
        print("Terimakasih dan Sampai Jumpa!")
    

while True:
    if MenuInput == 1: #display
        Read_Data()
        
        BacktoMainMenu()

        Main_Menu()



    elif MenuInput == 2: #add new product
        Read_Data()

        idProduct= (input('Masukkan ID Produk Baru  :'))
        while idProduct in ListProduct["ID Product"]:
            print("Data yang diinput sudah ada")
            idProduct= (input('Masukkan ID Produk Baru  :'))

        newCategory= (input('Masukkan Kategori Produk Baru  :'))

        newProduct= (input('Masukkan Nama Produk Baru  :'))
        while newProduct in ListProduct["Product"]:
            print("Data yang diinput sudah ada")
            newProduct= (input('Masukkan Nama Produk Baru  :'))
       
        stockNewProduct= (input('Masukkan QTY Produk Baru  :'))
        while stockNewProduct.isalpha() :
            print("Mohon Masukkan Angka Bulat")
            stockNewProduct=(input('Masukkan QTY Produk Baru  :'))
        stockNewProduct_int=int(stockNewProduct)
        dateInput= (input('Masukkan tanggal hari ini (Ex: 17 Des 2025)  :'))

        SaveOrNot = input("Apakah Anda Yakin untuk Menambahkan Produk Baru? - [Ya(Y)/Tidak(T)]:  ")
        while SaveOrNot != "T" and SaveOrNot != "Y":
            print("Mohon Masukkan Input Sesuai Program (Y/T)")
            SaveOrNot = (input("Apakah Anda Yakin untuk Menambahkan Produk Baru? - [Ya(Y)/Tidak(T)]: ", ))
        if SaveOrNot == "T":
            print("Tidak Mensave Data dan Kembali ke Main Menu")
            Main_Menu()
        if SaveOrNot == "Y":
            ListProduct["ID Product"].append(idProduct)
            ListProduct["Category"].append(newCategory)
            ListProduct["Product"].append(newProduct)
            ListProduct["Qty Stock"].append(stockNewProduct_int)
            ListProduct["Last Update"].append(dateInput)
       
            print("Saving Data..")
            print("Data Saved")
            print()
        
            Read_Data()

            print("Produk Berhasil Ditambahkan!")
            print()
            Main_Menu()
        
        MenuInput = int(input("Masukkan angka Menu yang ingin dijalankan : ", ))
    
    elif MenuInput == 3: #add qty product
        Read_Data()
        print()

        IDInput=(input('Masukkan ID Product yang ingin ditambah :')) #contoh misal S1
        
        while IDInput not in ListProduct["ID Product"]:
            print("Tidak ada data Produk dalam index yang dipilih")
            IDInput=(input('Masukkan ID Product yang ingin ditambah :'))
        if IDInput in ListProduct["ID Product"]:
            ListID=ListProduct["ID Product"] #['S1', 'S2', 'A1', 'A2', 'S1', 'S2', 'I1', 'I2'],
            indexIDInput=ListID.index(IDInput) #0,
            ListQty=ListProduct["Qty Stock"] #10,10,10,10,10,10,10,10,10,10,
            QtyInput=(input('Masukkan Qty Product yang ingin ditambah :')) #contoh misal 5
            while QtyInput.isalpha():
                print("Mohon Masukkan Angka Bulat")
                QtyInput=(input('Masukkan Qty Product yang ingin ditambah :'))
            QtyInput_int=int(QtyInput)
            newQty=QtyInput_int+ListProduct["Qty Stock"][indexIDInput]
            ListProduct["Qty Stock"][indexIDInput]=newQty
        else:
            print()    
        
        Read_Data()
        print()    
        print("Qty Produk Berhasil Ditambahkan !")
        
        BacktoMainMenu()
        
        Main_Menu()
        MenuInput = int(input("Masukkan angka Menu yang ingin dijalankan : ", ))

    elif MenuInput == 4: #reduce qty product
        
        Read_Data()

        IDInput=(input('Masukkan ID Product yang ingin dikurangi :')) #contoh misal S1
        
        while IDInput not in ListProduct["ID Product"]:
            print("Tidak ada data Produk dalam index yang dipilih")
            IDInput=(input('Masukkan ID Product yang ingin dikurangi :'))
        if IDInput in ListProduct["ID Product"]:
            ListID=ListProduct["ID Product"] #['S1', 'S2', 'A1', 'A2', 'S1', 'S2', 'I1', 'I2'],
            indexIDInput=ListID.index(IDInput) #0,
            ListQty=ListProduct["Qty Stock"] #10,10,10,10,10,10,10,10,10,10,

            InputQty=(input('Masukkan Qty Product yang ingin dikurangi :')) #contoh misal 5
            while InputQty.isalpha():
                print("Mohon Masukkan Angka Bulat")
                InputQty=(input('Masukkan Qty Product yang ingin dikurangi :'))

            QtyInput=int(InputQty)
            while QtyInput>ListQty[indexIDInput]:
                print(f"Stock Product tinggal {ListQty[indexIDInput]}")
                QtyInput=int(input('Masukkan Qty Product yang ingin dikurangi :'))
            else:
                QtyInput<ListQty[indexIDInput]
                newQty=ListQty[indexIDInput]-QtyInput
                ListQty[indexIDInput]=newQty
                Read_Data()     
                print()
                print("Qty Produk Berhasil Dikurangi!")
        else:
            print()    
        

        BacktoMainMenu()
        
        Main_Menu()
        MenuInput = int(input("Masukkan angka Menu yang ingin dijalankan : ", ))

    elif MenuInput == 5: #delete product
        Read_Data()

        IDInput=(input('Masukkan ID Product yang ingin dihapus :')) #contoh misal S1

        while IDInput not in ListProduct["ID Product"]:
            print("Tidak ada data Produk dalam index yang dipilih")
            IDInput=(input('Masukkan ID Product yang ingin dikurangi :'))
        if IDInput in ListProduct["ID Product"]:
            DeleteOrNot = input("Apakah Anda Yakin untuk Menghapus Produk Tersebut? - [Ya(Y)/Tidak(T)]:  ")
            while DeleteOrNot != "T" and DeleteOrNot != "Y":
                print("Mohon Masukkan Input Sesuai Program (Y/T)")
                DeleteOrNot = input("Apakah Anda Yakin untuk Menghapus Produk Tersebut? - [Ya(Y)/Tidak(T)]:")
            if DeleteOrNot == "T" :
                print("Cancel Mendelete Data dan Kembali ke Main Menu")
                Main_Menu() 
            else :
                ListID=ListProduct["ID Product"] #['S1', 'S2', 'A1', 'A2', 'S1', 'S2', 'I1', 'I2'],
                indexIDInput=ListID.index(IDInput) #0
                del ListProduct["ID Product"][indexIDInput]
                del ListProduct["Category"][indexIDInput]
                del ListProduct["Product"][indexIDInput]
                del ListProduct["Qty Stock"][indexIDInput]
                del ListProduct["Last Update"][indexIDInput]
            
                Read_Data()
                print()    
                print(" Produk Berhasil Dihapus !")
                print()
                
        BacktoMainMenu()

        Main_Menu()
        MenuInput = int(input("Masukkan angka Menu yang ingin dijalankan : ", ))



    elif MenuInput == 6: #exit menu
        print("Terimakasih dan Sampai Jumpa!")
      

    else:
        while MenuInput<=0 or MenuInput>6:
            print("Angka Input anda tidak valid")
            MenuInput = int(input("Masukkan angka Menu yang ingin dijalankan : ", ))
