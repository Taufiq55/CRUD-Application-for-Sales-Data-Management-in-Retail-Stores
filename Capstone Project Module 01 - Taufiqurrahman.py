from tabulate import tabulate


# Data penjualan dalam bentuk dictionary dalam list
data_barang = [{'id':1201,'nama':'Oreo',                 'kategori':'Makanan Dan Minuman',        'harga':10000,  'stock':100,    'jumlah_terjual':75,  'metode_pembayaran':'QR Code'},
               {'id':2101,'nama':'Rinso',                'kategori':'Rumah Tangga Dan Kebersihan','harga':25000,  'stock':200,    'jumlah_terjual':150, 'metode_pembayaran':'Tunai'},
               {'id':3301,'nama':'Vitacimin',            'kategori':'Kesehatan Dan Kecantikan',   'harga':2000,   'stock':300,    'jumlah_terjual':200, 'metode_pembayaran':'Debit'},
               {'id':1101,'nama':'Coca Cola',            'kategori':'Makanan Dan Minuman',        'harga':7000,   'stock':500,    'jumlah_terjual':450, 'metode_pembayaran':'Tunai'},
               {'id':2401,'nama':'Superpell',            'kategori':'Rumah Tangga Dan Kebersihan','harga':15000,  'stock':100,    'jumlah_terjual':60,  'metode_pembayaran':'Kartu Kredit'},
               {'id':3201,'nama':'Pasta Gigi Pepsodent', 'kategori':'Kesehatan Dan Kecantikan',   'harga':30000,  'stock':250,    'jumlah_terjual':125, 'metode_pembayaran':'QR Code'},
               {'id':1202,'nama':'Sari Roti',            'kategori':'Makanan Dan Minuman',        'harga':12000,  'stock':400,    'jumlah_terjual':300, 'metode_pembayaran':'QR Code'},
               {'id':2301,'nama':'Wipol',                'kategori':'Rumah Tangga Dan Kebersihan','harga':20000,  'stock':150,    'jumlah_terjual':50,  'metode_pembayaran':'Debit'},
               {'id':3401,'nama':'Vaseline',             'kategori':'Kesehatan Dan Kecantikan',   'harga':50000,  'stock':200,    'jumlah_terjual':80,  'metode_pembayaran':'Kartu Kredit'}] 

# Keranjang belanja
cart = []

#Function utama dari program
def main():             
    while True:                                                                                    # Infinite Loop
        menu()                                                                                     # Menampilkan menu utama
        pilihan_menu = input('Masukkan Pilihan Menu yang ingin dijalankan (1-6): ')                # Meminta user memasukkan input
        if pilihan_menu.isdigit() == True:                                                         # Memeriksa apakah input berupa angka
            pilihan_menu = int(pilihan_menu)                                                       # Casting string menjadi Integer
            if pilihan_menu == 1:
                read()
            elif pilihan_menu == 2:
                update()
            elif pilihan_menu == 3:
                delete()
            elif pilihan_menu == 4:
                create()
            elif pilihan_menu == 5:       
                sell()
            elif pilihan_menu == 6:
                if konfirmasi('Apakah Anda Ingin Menutup Aplikasi?') == True:                                                       # Memanggil function konfirmasi Jika function konfirmasi bernilai True
                    print('\nProgram Ditutup')
                    break                                                                                                           # Keluar dari while loop
                else:
                    print('\nPenutupan Aplikasi Dibatalkan.')                                                                       # Jika function konfirmasi tidak bernilai True
            else:
                print(f'\nPilihan menu {pilihan_menu} tidak tersedia.\nMohon pilih menu yang tersedia (1-6).')                      # Jika User memilih menu yang tidak tersedia
        else:
            print('\nInput tidak valid.\nMohon masukkan pilihan menu yang tersedia yang berupa bilangan bulat (1-6).\n')            # Jika input tidak berupa angka

# Function untuk menampilkan menu utama
def menu():
    print('\n   Selamat Datang di Sistem Manajemen Kasir dan Penjualan HypoMart!\n')
    print('''    ================ Menu Utama ================ 
    |    1. Menampilkan Daftar Penjualan       |
    |    2. Mengupdate Daftar Penjualan        |
    |    3. Menghapus Daftar Penjualan         |
    |    4. Menambahkan Daftar Penjualan       |
    |    5. Penjualan Barang                   |
    |    6. Exit Program                       |
    ============================================\n''')
       
# Function untuk meminta konfirmasi dari user
def konfirmasi(pertanyaan):
    while True:
        checker = (input(f'\n{pertanyaan} (y/n) ')).lower()                         # Merubah bentuk input menjadi lowercase(Untuk meng-handle input uppercase maupun lowercase)
        if checker == 'y':
            return True                                                             # Mengembalikan nilai True kepada function pemanggil, yaitu function konfirmasi                                                      
        elif checker == 'n':
            return False                                                            # Mengembalikan nilai False kepada function pemanggil, yaitu function konfirmasi
        else:
            print('\nMohon masukkan pilihan yang sesuai (y/n).')                    # Jika user meng-input selain 'y' atau 'n'

# Function untuk menampilkan Sub menu read
def read():
    while True:                                                                                     
        print('''        
    ############################### List Menu ################################ 
    |    1. Menampilkan Seluruh Daftar Penjualan                             |
    |    2. Menampilkan Daftar Penjualan Berdasarkan ID                      |
    |    3. Menampilkan Daftar Penjualan Berdasarkan Kategori                |
    |    4. Menampilkan Daftar Penjualan Berdasarkan Metode Pembayaran       |
    |    5. Menampilkan Daftar Penjualan Berdasarkan Total Penjualan         |
    |    6. Kembali ke Menu Utama                                            |
    ##########################################################################\n''')
        pilihan_read = input('Masukkan Pilihan Menu yang ingin dijalankan (1-6): ')                 # Meminta user memasukkan input                   
        if pilihan_read.isdigit() == True:                                                          # Memeriksa apakah input berupa angka                                                                                                                 
            pilihan_read = int(pilihan_read)                                                        # Casting string menjadi Integer
            if pilihan_read == 1:
                if len(data_barang) > 0:                                                            # Jika jumlah item pada list data_barang lebih dari 0 akan menjalankan function table_full
                    table_full()
                else:
                    print('\nData Penjualan tidak tersedia.')                                       # Jika jumlah item pada list data_barang lebih kecil sama dengan 0 akan menampilkan notifikasi
            elif pilihan_read == 2:
                if len(data_barang) > 0:
                    table_id()
                else:
                    print('\nData Penjualan tidak tersedia.')
            elif pilihan_read == 3:
                if len(data_barang) > 0:
                    table_kategori()
                else:
                    print('\nData Penjualan tidak tersedia.')
            elif pilihan_read == 4:
                if len(data_barang) > 0:
                    table_metode_pembayaran()
                else:
                    print('\nData Penjualan tidak tersedia.')
            elif pilihan_read == 5:
                if len(data_barang) > 0:
                    table_filter()
                else:
                    print('\nData Penjualan tidak tersedia.')
            elif pilihan_read == 6:
                break                                                                                                               # Keluar dari while loop
            else:
                print(f'\nPilihan menu {pilihan_read} tidak tersedia.\nMohon masukkan pilihan menu yang tersedia (1-6).')           # Jika User memilih menu yang tidak tersedia
        else:
            print('\nInput tidak valid.\nMohon Masukkan Pilihan Menu Yang Berupa Bilangan Bulat (1-6).\n')                          # Jika input tidak berupa angka

# Tabel yang menampilkan seluruh data penjualan dalam list data_barang      
def table_full():
    tabel = []
    print('\n=============================================================== Daftar Barang ===============================================================\n') 
    for i in range(len(data_barang)):                   # Untuk melakukan iterasi tiap i, Untuk menambahkan item ke dalam list kosong tabel menggunakan .append
        tabel.append([data_barang[i]['id'],data_barang[i]['nama'],data_barang[i]['kategori'],data_barang[i]['stock'],data_barang[i]['jumlah_terjual'],data_barang[i]['harga'],(data_barang[i]['jumlah_terjual']*data_barang[i]['harga']),data_barang[i]['metode_pembayaran']])
    print(tabulate(tabel, headers = ['ID','Nama','Kategori','Stock','Jumlah_Terjual','Harga','Total_Penjualan','Metode_Pembayaran'],tablefmt='double_outline',numalign='right',stralign='left'))
    
# Tabel yang menampilkan 1 data penjualan, dengan index yang akan dimasukkan kedalam parameter 'angka'
def table(angka):
    print('')
    tabel = []
    tabel.append([data_barang[angka]['id'],data_barang[angka]['nama'],data_barang[angka]['kategori'],data_barang[angka]['stock'],data_barang[angka]['jumlah_terjual'],data_barang[angka]['harga'],(data_barang[angka]['jumlah_terjual']*data_barang[angka]['harga']),data_barang[angka]['metode_pembayaran']])
    print(tabulate(tabel, headers = ['ID','Nama','Kategori','Stock','Jumlah_Terjual','Harga','Total_Penjualan','Metode_Pembayaran'],tablefmt='double_outline',numalign='right',stralign='left'))

# Tabel yang menampilkan data dengan nama kolom dan isi kolom tertentu
def isi_table(kolom,isi):
    tabel_read = []
    for i in range(len(data_barang)):                                       # Untuk menambahkan item ke dalam list kosong tabel, jika memenuhi kondisi
        if data_barang[i][kolom] == isi:
            tabel_read.append([data_barang[i]['id'],data_barang[i]['nama'],data_barang[i]['kategori'],data_barang[i]['stock'],data_barang[i]['jumlah_terjual'],data_barang[i]['harga'],(data_barang[i]['jumlah_terjual']*data_barang[i]['harga']),data_barang[i]['metode_pembayaran']]) 
    print(tabulate(tabel_read, headers = ['ID','Nama','Kategori','Stock','Jumlah_Terjual','Harga','Total_Penjualan','Metode_Pembayaran'],tablefmt='double_outline',numalign='right',stralign='left'))

# Tabel yang menampilkan data dengan total penjualan yang lebih dari parameter 'acuan'
def isi_table_besar(acuan):                         
    tabel_filter1 = []
    for i in range(len(data_barang)):                                 # Untuk menambahkan item ke dalam list kosong tabel_filter1, dimana total penjualannya lebih dari 'acuan'
        if (data_barang[i]['jumlah_terjual']*data_barang[i]['harga']) > acuan:
            tabel_filter1.append([data_barang[i]['id'],data_barang[i]['nama'],data_barang[i]['kategori'],data_barang[i]['stock'],data_barang[i]['jumlah_terjual'],data_barang[i]['harga'],(data_barang[i]['jumlah_terjual']*data_barang[i]['harga']),data_barang[i]['metode_pembayaran']]) 
    n = len(tabel_filter1)              # jumlah item pada list tabel_filter1
    if n > 0:                           # jika jumlah item pada list tabel_filter1 lebih dari 0
        print(f'\nBerikut Data Penjualan Yang Total Penjualannya Melebihi {acuan} :')
        print(tabulate(tabel_filter1, headers = ['ID','Nama','Kategori','Stock','Jumlah_Terjual','Harga','Total_Penjualan','Metode_Pembayaran'],tablefmt='double_outline',numalign='right',stralign='left'))
    else:                               # jika jumlah item pada list tabel_filter1 tidak lebih dari 0
        print(f'\nTidak Ditemukan Data Penjualan Dengan Total Penjualan Lebih Besar Dari {acuan}.')

# Tabel yang menampilkan data dengan total penjualan yang kurang dari parameter 'acuan'
def isi_table_kecil(acuan):                        
    tabel_filter2 = []
    for i in range(len(data_barang)):               # Untuk menambahkan item ke dalam list kosong tabel_filter2, dimana total penjualannya kurang dari 'acuan'
        if (data_barang[i]['jumlah_terjual']*data_barang[i]['harga']) < acuan:
            tabel_filter2.append([data_barang[i]['id'],data_barang[i]['nama'],data_barang[i]['kategori'],data_barang[i]['stock'],data_barang[i]['jumlah_terjual'],data_barang[i]['harga'],(data_barang[i]['jumlah_terjual']*data_barang[i]['harga']),data_barang[i]['metode_pembayaran']]) 
    n = len(tabel_filter2)                          # jumlah item pada list tabel_filter2
    if n > 0:                                       # jika jumlah item pada list tabel_filter2 lebih dari 0
        print(f'\nBerikut Data Penjualan Yang Total Penjualannya Dibawah {acuan} :')
        print(tabulate(tabel_filter2, headers = ['ID','Nama','Kategori','Stock','Jumlah_Terjual','Harga','Total_Penjualan','Metode_Pembayaran'],tablefmt='double_outline',numalign='right',stralign='left'))
    else:                                           # jika jumlah item pada list tabel_filter2 tidak lebih dari 0
        print(f'\nTidak Ditemukan Data Penjualan Dengan Total Penjualan Lebih Kecil Dari {acuan}.')

# Function untuk menampilkan tabel berdasarkan kategori   
def table_kategori():
    while True:                                                             
        print('Pilihan Kategori:\n   1. Makanan Dan Minuman.\n   2. Rumah Tangga Dan Kebersihan.\n   3. Kesehatan Dan Kecantikan.')
        pilihan_table = input('\nMasukkan Pilihan Kategori Yang Anda Inginkan (1-3): ')         
        if pilihan_table.isdigit() == True:                                                 # Untuk memeriksa apakah input berupa angka
            pilihan_table = int(pilihan_table)                              
            if pilihan_table == 1:
                isi_table('kategori','Makanan Dan Minuman')
                break                                                                       
            elif pilihan_table == 2:
                isi_table('kategori','Rumah Tangga Dan Kebersihan')
                break                                                                       
            elif pilihan_table == 3:
                isi_table('kategori','Kesehatan Dan Kecantikan')
                break                                                                       
            else:
                print('\nMohon Masukkan Pilihan Kategori Yang Tersedia.')                   # Jika User memilih menu yang tidak tersedia
        else:
            print('\nMohon masukkan pilihan yang berupa bilangan bulat (1-3).')             # Jika input tidak berupa angka

# Function untuk menampilkan tabel berdasarkan metode pembayaran              
def table_metode_pembayaran():
    while True:                                                                     
        print('Pilihan Metode Pembayaran:\n   1. Tunai.\n   2. QR Code.\n   3. Debit.\n   4. Kartu Kredit.')
        pilihan_table = input('\nMasukkan Pilihan Metode Pembayaran Yang Anda Inginkan (1-4): ')
        if pilihan_table.isdigit() == True:                                         # Untuk memeriksa apakah input berupa angka
            pilihan_table = int(pilihan_table)                                      
            if pilihan_table == 1:
                isi_table('metode_pembayaran','Tunai')
                break                                                               
            elif pilihan_table == 2:
                isi_table('metode_pembayaran','QR Code')
                break                                                               
            elif pilihan_table == 3:
                isi_table('metode_pembayaran','Debit')
                break                                                               
            elif pilihan_table == 4:
                isi_table('metode_pembayaran','Kartu Kredit')
                break                                                               
            else:
                print('\nMohon Masukkan Pilihan Kategori Yang Tersedia.')           # Jika User memilih menu yang tidak tersedia             
        else:
            print('\nMohon masukkan pilihan yang berupa bilangan bulat (1-4).')     # Jika input tidak berupa angka
        
# Function untuk menampilkan tabel berdasarkan ID
def table_id():
    while True:                                                                 
        pilihan_id = input('\nMasukkan ID penjualan yang anda inginkan : ')
        if pilihan_id.isdigit() == True:                                        # Untuk memeriksa apakah input berupa angka
            pilihan_id = int(pilihan_id)                                        
            if pilihan_id < 1000 or pilihan_id > 9999:                          # jika id input tidak terdiri dari 4 digit
                print('\nMohon masukkan ID yang terdiri dari 4 digit.')
            else:
                break                                                           
        else:
            print('\nMohon masukkan ID yang berupa bilangan bulat yang terdiri dari 4 digit.')      # Jika input tidak berupa angka
    ada = False                                 # Mendefinisikan ada bernilai False
    for i in range(len(data_barang)):
        if pilihan_id == data_barang[i]['id']:  # Memeriksa apakah id input terdapat didalam tabel daftar barang
            ada = True                          # Merubah nilai ada menjadi True
            x = i                               # untuk menyimpan index pada saat menemukan ID yang sama kedalam variable x
            break
    if ada == True:                             # Jika ada bernilai True
        table(x)                                # Menampilkan table yang berisikan data pada index x
    else:                                       # Jika ada tidak bernilai True
        print(f'\nData Penjualan dengan ID {pilihan_id} tidak tersedia.')

# Function untuk menampilkan tabel berdasarkan filter total penjualan
def table_filter():
    while True:                                             
        print('''        
    ================================= List Menu ================================= 
    |    1. Menampilkan Daftar Penjualan Yang Lebih Besar Dari Parameter        |
    |    2. Menampilkan Daftar Penjualan Yang Lebih Kecil Dari Parameter        |
    |    3. Kembali ke Menu Read                                                |
    =============================================================================\n''')   
        while True:
            pilihan_filter = input('Masukkan pilihan menu yang ingin dijalankan (1-3): ')               
            if pilihan_filter.isdigit() == True:                                                        # Untuk memeriksa apakah input berupa angka
                pilihan_filter = int(pilihan_filter)                                                    
                break                                                                                   
            else:
                print('\nInput tidak valid.\nMasukkan input berupa bilangan bulat. (1-3)')              # Jika input tidak berupa angka
        if pilihan_filter == 1:
            while True:
                nilai_filter = input('Masukkan Nilai Parameter : ')                                     
                if nilai_filter.isdigit() == True:                                                      # Untuk memeriksa apakah input berupa angka
                    nilai_filter = int(nilai_filter)                                                    
                    if nilai_filter < 1000:
                        print('Mohon Masukkan Total Penjualan Dengan Benar. (Minimal 1000)')
                    else:
                        break                                                                           
                else:
                    print('\nInput tidak valid.\nMasukkan total penjualan berupa bilangan bulat. (Minimal 1000)')       # Jika input tidak berupa angka
            isi_table_besar(nilai_filter)                                                               # menampilkan tabel dengan data yang total penjualannya lebih dari 'nilai_filter'
        elif pilihan_filter == 2:
            while True:
                nilai_filter = input('Masukkan Nilai Parameter : ')                                     
                if nilai_filter.isdigit() == True:                                                      # Untuk memeriksa apakah input berupa angka
                    nilai_filter = int(nilai_filter)                                                    
                    if nilai_filter < 1000:
                        print('Mohon Masukkan Total Penjualan Dengan Benar. (Minimal 1000)')
                    else:
                        break                                                                           
                else:
                    print('\nInput tidak valid.\nMasukkan total penjualan berupa bilangan bulat. (Minimal 1000)')       # Jika input tidak berupa angka
            isi_table_kecil(nilai_filter)                                                               # menampilkan tabel dengan data yang total penjualannya kecil dari 'nilai_filter'
        elif pilihan_filter == 3:
            print('\nKembali Ke Menu Read.')
            break                                                                                       
        else:
            print('\nMohon masukkan pilihan yang tersedia. (1-3)')                                      # Jika User memilih menu yang tidak tersedia

# Function untuk menampilkan Sub menu update
def update():
    while True:                                                                                                     
        print('''        
    *************** List Menu *************** 
    |    1. Mengupdate Daftar Penjualan     |
    |    2. Memberikan Discount             |
    |    3. Kembali ke Menu Utama           |
    *****************************************\n''')
        pilihan_update = input('Masukkan Pilihan Menu yang ingin dijalankan (1-3): ')                               
        if pilihan_update.isdigit() == True:                                                                        # Untuk memeriksa apakah input berupa angka
            pilihan_update = int(pilihan_update)                                                                    
            if pilihan_update == 1:
                pembaharuan()
            elif pilihan_update == 2:
                discount()         
            elif pilihan_update == 3:
                break                                                                                          
            else : 
                print(f'\nPilihan menu {pilihan_update} tidak tersedia.\nMohon masukkan pilihan menu yang tersedia (1-3).')                                               # Jika User memilih menu yang tidak tersedia
        else:
            print('\nInput tidak valid.\nMohon Masukkan Pilihan Menu Yang Berupa Bilangan Bulat (1-3).\n')          # Jika input tidak berupa angka

# Function untuk mengupdate data yang sudah ada     
def pembaharuan():
    while True:
        id_update = input('\nMasukkkan ID Penjualan yang ingin anda perbaharui : ')
        if id_update.isdigit() == True:                                         # Untuk memeriksa apakah input berupa angka
            id_update = int(id_update)
            if id_update < 1000 or id_update > 9999:                            # jika id input tidak terdiri dari 4 digit
                print('\nMohon masukkan ID sebanyak 4 digit')
            elif id_update < 0:                                                 # Jika id input lebih kecil dari 0
                print('\nMohon masukkan ID yang berupa bilangan bulat positif yang terdiri dari 4 digit.')
            else:
                break
        else:
            print('\nMohon Masukkan ID yang berupa bilangan bulat dengan 4 digit.')
    ada = False
    for i in range(len(data_barang)):
        if id_update == data_barang[i]['id']:               # Memeriksa apakah id input terdapat didalam tabel daftar barang
            ada = True
            x = i                                           # untuk menyimpan index pada saat menemukan ID yang sama kedalam variable x
            break
    if ada == False:
        print(f'\nData Penjualan dengan ID {id_update} tidak tersedia.')
    else:
        table(x)                                            # Menampilkan table yang berisikan data pada index x 
        if konfirmasi('Apakah Anda Ingin Memperbaharui Data Penjualan Diatas?') == True:   # Jika function konfirmasi bernilai True
            while True:
                print('''Pilihan Update:\n   1. Stock\n   2. Jumlah Terjual\n   3. Harga''')
                nama_kolom = input('\nMasukkan pilihan kolom yang ingin anda perbaharui nilainya (1-3): ')
                if nama_kolom.isdigit() == True:
                    nama_kolom = int(nama_kolom)
                    if nama_kolom not in range(1,4):                    # Jika input berupa angka selain 1, 2, dan 3
                        print('\nMohon masukkan pilihan update yang tersedia.')
                    else:
                        break
                else:
                    print('\nMohon masukkan pilihan dengan bilangan bulat.')
            if nama_kolom == 1:
                while True:
                    stock_baru = input('\nMasukkan stock baru : ')
                    if stock_baru.isdigit() == True:
                        stock_baru = int(stock_baru)
                        if stock_baru < 0:
                            print('\nMohon masukkan stock yang berupa bilangan bulat yang tidak negatif.')
                        else:
                            if konfirmasi('Apakah Anda Ingin Menyimpan Pembaharuan?') == True:
                                data_barang[x]['stock'] = stock_baru                                # Mengganti nilai stock, menjadi nilai stock yang di input
                                print(f'\nStock pada ID Penjualan {id_update} telah diupdate.')
                            else:
                                print('\nMembatalkan Pembaharuan Pada Stock.')
                            break 
                    else:
                        print('Masukkan stock yang berupa bilangan bulat.')
                    
            elif nama_kolom == 2:
                while True:
                    jumlah_terjual_baru = input('\nMasukkan jumlah terjual baru : ')
                    if jumlah_terjual_baru.isdigit() == True:
                        jumlah_terjual_baru = int(jumlah_terjual_baru)
                        if jumlah_terjual_baru < 0:
                            print('\nMohon masukkan jumlah terjual dengan benar yang tidak bernilai negatif.')
                        else:
                            if konfirmasi('Apakah Anda Ingin Menyimpan Pembaharuan?') == True:
                                data_barang[x]['jumlah_terjual'] = jumlah_terjual_baru              # Mengganti nilai jumlah terjual, menjadi nilai jumlah terjual yang di input
                                print(f'\nJumlah Terjual pada ID Penjualan {id_update} telah diupdate.')
                            else:
                                print('\nMembatalkan Pembaharuan Pada Jumlah Terjual.')     
                            break
                    else:
                        print('\nMasukkan jumlah terjual yang berupa bilangan bulat.')
                    
            elif nama_kolom == 3:
                while True:
                    harga_baru = input('\nMasukkan harga baru : ')
                    if harga_baru.isdigit() == True:
                        harga_baru = int(harga_baru)
                        if harga_baru < 1000:
                            print('\nMohon masukkan harga dengan benar, minimal 1000')
                        else:
                            if konfirmasi('Apakah Anda Ingin Menyimpan Pembaharuan?') == True:
                                data_barang[x]['harga'] = harga_baru                                 # Mengganti nilai harga, menjadi nilai harga yang di input
                                print(f'\nHarga pada ID Penjualan {id_update} telah diupdate.')  
                            else:
                                print('\nMembatalkan Pembaharuan')   
                            break 
                    else:
                        print('\nMasukkan harga berupa yang bilangan bulat.')  
        else:
            print('\nMembatalkan Pembaharuan Daftar Penjualan...')                  # Jika function konfirmasi tidak bernilai True

# Funciton untuk mengupdate data harga pada data penjualan dengan menggunakan discount
def discount():
    while True:
        print('\nMenu discount : \n   1. Memberikan discount terhadap semua barang.\n   2. Memberikan discount untuk satu barang.\n   3. Memberikan discount untuk barang-barang dengan kategori yang sama.')
        pilihan_disc = input('\nMasukkan pilihan menu discount :')
        if pilihan_disc.isdigit() == True:
            pilihan_disc = int(pilihan_disc)
            if pilihan_disc not in range(1,4):
                print('\nMohon masukkan pilihan menu discount yang tersedia (1-3).')
            break
        else:
            print('\nInput tidak valid.\nMohon masukkan pilihan menu discount yang berupa bilangan bulat (1-3).')
    while True:
        potongan = input('\nMasukkan jumlah discount yang akan diberikan (tanpa %) : ')
        if potongan.isdigit() == True:
            potongan = int(potongan)
            if potongan not in range(100):
                print('\nMohon masukkan jumlah discount dengan benar (0-100).')
            else:
                potongan = (100 - potongan)/100 
                if pilihan_disc == 1:
                    discount_all(potongan)
                elif pilihan_disc == 2:
                    discount_nama(potongan)
                elif pilihan_disc == 3:
                    discount_kategori(potongan)
                break
        else:
            print('\nInput tidak valid.\nMohon masukkan jumlah discount yang berupa bilangan bulat (1-100).')

# Function untuk memberikan discount pada seluruh barang yang ada
def discount_all(value):
    if konfirmasi(f'Apakah anda ingin memberikan discount sebesar {int(100-(value*100))}% untuk seluruh harga barang?') == True:
        for i in range(len(data_barang)):
            data_barang[i]['harga'] = int(round(data_barang[i]['harga'] * value))
        print('\nSeluruh harga barang telah diberi discount.')
    else:
        print('Pemberian discount dibatalkan.')

# Function untuk memberikan discount pada seluruh barang dengan kategori tertentu
def discount_kategori(value):
    while True:
        print('\nPilihan Kategori:\n   1. Makanan Dan Minuman.\n   2. Rumah Tangga Dan Kebersihan.\n   3. Kesehatan Dan Kecantikan.')
        kategori = input('\nMasukkan pilihan kategori yang ingin anda berikan discount (1-3): ')
        if kategori.isdigit() == True:
            kategori = int(kategori)
            if kategori == 1:
                kategori = 'Makanan Dan Minuman'
                break
            elif kategori == 2:
                kategori = 'Rumah Tangga Dan Kebersihan'
                break
            elif kategori == 3:
                kategori = 'Kesehatan Dan Kecantikan'
                break
            else:
                print('\nMohon masukkan pilihan kategori yang tersedia (1-3).')
        else:
            print('\nInput tidak valid.\nMohon masukkan pilihan kategori yang berupa bilangan bulat (1-3).')
    if konfirmasi(f'Apakah anda ingin memberikan discount sebesar{int(100-(value*100))}% untuk harga barang-barang yang berkategori {kategori}?') == True:
        for i in range(len(data_barang)):
            if data_barang[i]['kategori'] == kategori:
                data_barang[i]['harga'] = int(round(data_barang[i]['harga'] * value))
        print(f'\nHarga barang dengan kategori "{kategori}" telah diberi discount.')
    else:
        print('Pemberian discount dibatalkan.')

# Function untuk memberikan discount pada 1 barang
def discount_nama(value):
    nama = input('\nMasukkan nama barang yang ingin anda berikan discount :').title()
    if konfirmasi(f'Apakah anda ingin memberikan discount sebesar {int(100-(value*100))}% untuk harga barang {nama}?') == True:
        ada = False
        for i in range(len(data_barang)):
            if data_barang[i]['nama'] == nama:
                data_barang[i]['harga'] = int(round(data_barang[i]['harga'] * value))
                ada = True
        if ada == False:
            print(f'\n{nama} tidak tersedia.')
        else:
            print(f'\nHarga {nama} telah diberi discount')
    else:
        print('Pemberian discount dibatalkan.')
        
# Function untuk menampilkan Sub menu delete
def delete():
    while True:
        print('''        
    ----------------- List Menu ----------------- 
    |    1. Menghapus Daftar Penjualan          |
    |    2. Menghapus Semua Daftar Penjualan    |
    |    3. Kembali ke Menu Utama               |
    ---------------------------------------------\n''')
        pilihan_delete = input('Masukkan Pilihan Menu yang ingin dijalankan (1-3): ')
        if pilihan_delete.isdigit() == True:                                                                    # Untuk memeriksa apakah input berupa angka
            pilihan_delete = int(pilihan_delete)
            if pilihan_delete == 1:
                penghapusan()
            elif pilihan_delete == 2:
                hapus_semua()
            elif pilihan_delete == 3:
                break
            else : 
                print(f'\nPilihan menu {pilihan_delete} tidak tersedia.\nMohon masukkan pilihan menu yang tersedia (1-3).')                                           # Jika User memilih menu yang tidak tersedia
        else:
            print('\nInput tidak valid.\nMohon Masukkan Pilihan Menu Yang Berupa Bilangan Bulat (1-3).\n')      # Jika input tidak berupa angka
    
# Function untuk menghapus data pada data penjualan
def penghapusan():
    while True:
        id_delete = input('Masukkkan ID Penjualan yang ingin anda hapus : ')
        if id_delete.isdigit() == True:                             # Untuk memeriksa apakah input berupa angka
            id_delete = int(id_delete)
            if id_delete < 1000 or id_delete > 9999:                # jika id input tidak terdiri dari 4 digit
                print('\nMohon masukkan ID sebanyak 4 digit')
            else:
                break
        else:
            print('\nMohon Masukkan ID yang berupa bilangan bulat.\n')
    ada = False
    for i in range(len(data_barang)):
        if id_delete == data_barang[i]['id']:           # Memeriksa apakah id input terdapat didalam tabel daftar barang
            ada = True
            x = i                                       # untuk menyimpan index kedalam variable x pada saat menemukan ID yang sama
            break
    if ada == False:
        print(f'\nData Penjualan dengan ID {id_delete} tidak tersedia.')
    else:
        table(x)                                        # Menampilkan table yang berisikan data pada index x
        if konfirmasi('Apakah Anda Ingin Menghapus Data Tersebut?') == True:
            del data_barang[x]                          # Untuk menghapus item pada list data_barang pada index x
            print(f'\nData Penjualan dengan ID {id_delete} telah berhasil di hapus.')
        else:
            print('\nMembatalkan Penghapusan Daftar Penjualan...')

# Function untuk menghapus seluruh data yang ada pada data penjualan
def hapus_semua():
    if len(data_barang) > 0:
        if konfirmasi('Apakah Anda Ingin Menghapus Seluruh Data Penjualan Yang Ada?') == True:          # Jika function konfirmasi bernilai True
            for i in range(len(data_barang)):                                                           # Untuk melakukan iterasi sebanyak jumlah item pada list data_barang
                data_barang.pop()                                                                       # Untuk menghapus item pada list data_barang pada index terakhir
            print('\nData penjualan telah berhasil dihapus.')
        else:
            print('\nMembatalkan Penghapusan Daftar Penjualan...')
    else:
        print('\nData Penjualan tidak tersedia.')

# Function untuk menampilkan Sub menu create
def create():
    while True:
        print('''        
    ++++++++++++++++ List Menu ++++++++++++++++ 
    |    1. Menambahkan Daftar Penjualan      |
    |    2. Kembali ke Menu Utama             |
    +++++++++++++++++++++++++++++++++++++++++++\n''')
        pilihan_create = input('Masukkan Pilihan Menu yang ingin dijalankan (1-2): ')
        if pilihan_create.isdigit() == True:                                                                    # Untuk memeriksa apakah input berupa angka
            pilihan_create = int(pilihan_create)
            if pilihan_create == 1:
                if penambahan() == False:                         # Jika function penambahan bernilai False, maka akan menjalankan continue
                    continue                                      # Melewati blok code berikutnya
            elif pilihan_create == 2:
                break
            else:
                print(f'\nPilihan menu {pilihan_create} tidak tersedia.\nMohon masukkan pilihan menu yang tersedia (1-2).')                                             # Jika User memilih menu yang tidak tersedia
        else:
            print('\nInput tidak valid.\nMohon Masukkan Pilihan Menu Yang Berupa Bilangan Bulat (1-2).\n')      # Jika input tidak berupa angka

# Function untuk menambahkan data baru kedalam data penjualan
def penambahan():
    print('\nDigit pertama ID melambangkan kategori, dimana 1 adalah Makanan Dan Minuman, 2 adalah Rumah Tangga Dan Kebersihan, 3 adalah Kesehatan Dan Kecantikan.\nDigit kedua ID melambangkan metode pembayaran, dimana 1 adalah Tunai, 2 adalah QR Code, 3 adalah Debit, 4 adalah Kartu Kredit.\nDigit ketiga dan keempat ID melambangkan nomor nama barang yang memiliki kategori dan metode pembayaran yang sama, yang dimulai dengan 01. ')
    while True:
        new_id = input('\nMasukkan ID Penjualan yang ingin ditambahkan : ')
        if new_id.isdigit() == True:                             # Memeriksa apakah input berupa angka
            new_id = int(new_id)
            if new_id < 1101:
                if new_id < 1000:
                    print('\nMohon masukkan ID dengan 4 digit')
                else:
                    print('\nMohon masukkan ID dengan benar')
            elif new_id > 1399 and new_id < 2101:
                print('\nMohon masukkan ID dengan benar')
            elif new_id > 2399 and new_id < 3101:
                print('\nMohon masukkan ID dengan benar')
            elif new_id == 1200 or new_id == 1300 or new_id == 2200 or new_id == 2300 or new_id == 3200 or new_id == 3300:
                print('\nMohon masukkan ID dengan benar')
            elif new_id > 3399:
                if new_id > 9999:
                    print('\nMohon masukkan ID dengan 4 digit')
                else:
                    print('\nMohon masukkan ID dengan benar')
            else:                                                                            # Jika id input telah terdiri dari 4 digit dan memenuhi kriteria id
                break
        else:
            print('\nMohon Masukkan ID berupa bilangan bulat positif yang terdiri dari 3 digit.')
    ada = False
    for i in range(len(data_barang)):
        if new_id == data_barang[i]['id']:                          # Memeriksa apakah id input terdapat didalam tabel daftar barang
            ada = True                 
            break
    if ada == True:
        print(f'\nData Penjualan dengan ID {new_id} sudah ada.')
        return False                                                # Jika ada bernilai False, maka akan mengembalikan nilai False kepada pemanggil, yaitu function penambahan
    new_name = input('Masukkan nama barang yang ingin ditambahkan : ').title()   #.title digunakan untuk merubah huruf pertama ditiap kata menjadi huruf kapital dan di ikuti dengan huruf kecil
    if new_id//1000 == 1:                                                       # floor division, untuk mencari hasil bagi yang dibulatkan kebawah
        new_kategori = 'Makanan Dan Minuman'
    elif new_id//1000 == 2:
        new_kategori = 'Rumah Tangga Dan Kebersihan'
    elif new_id//1000 == 3:
        new_kategori = 'Kesehatan Dan Kecantikan'
    while True:
        new_stock = input('Masukkkan stock barang yang ingin ditambahkan : ')
        if new_stock.isdigit() == True:
            new_stock = int(new_stock)
            if new_stock < 0:
                print('\nMohon masukkan stock yang berupa bilangan bulat yang tidak negatif.')
            else:
                break
        else:
            print('\nMohon masukkan stock yang berupa bilangan bulat.')
    while True:
        new_price = input('Masukkan harga barang yang ingin ditambahkan : ')
        if new_price.isdigit() == True:
            new_price = int(new_price)
            if new_price < 1000:
                print('\nMohon masukkan harga dengan benar, minimal 1000')
            else:
                break
        else:
            print('\nMohon masukkan harga yang berupa bilangan bulat positif.')
    while True:
        new_sold = input('Masukkan jumlah barang yang telah terjual : ')
        if new_sold.isdigit() == True:
            new_sold = int(new_sold)
            if new_sold < 0:
                print('\nMohon masukkan jumlah terjual dengan benar yang tidak bernilai negatif.')
            else:
                break
        else:
            print('\nMohon masukkan jumlah terjual yang berupa bilangan bulat.')

    if (new_id%1000)//100 == 1:                                             # Modulus, untuk mencari sisa pembagian, dan sisa pembagian itu akan di floor division dengan 100
        new_metode = 'Tunai'
    elif (new_id%1000)//100 == 2:
        new_metode = 'QR Code'
    elif (new_id%1000)//100 == 3:
        new_metode = 'Debit'
    elif (new_id%1000)//100 == 4:
        new_metode = 'Kartu Kredit'
    print('')
    tabel = []
    tabel.append([new_id,new_name,new_kategori,new_stock,new_sold,new_price,(new_sold*new_price),new_metode])
    print(tabulate(tabel, headers = ['ID','Nama','Kategori','Stock','Jumlah_Terjual','Harga','Total_Penjualan','Metode_Pembayaran'],tablefmt='double_outline',numalign='right',stralign='left'))
    if konfirmasi('Apakah Anda Ingin Menambahkan Data diatas Kedalam Aplikasi?') == True:
        data_barang.append({'id':new_id,'nama':new_name,'kategori':new_kategori,'harga':new_price,'stock':new_stock,'jumlah_terjual':new_sold,'metode_pembayaran':new_metode})
        print(f'\nData Penjualan dengan ID {new_id} telah berhasil ditambahkan.')
    else:
        print('\nMembatalkan Penambahan Daftar Penjualan...')

# Function untuk menampilkan Sub menu penjualan
def sell():
    while True:
        print('''        
    >>>>>>>>>>>>>> List Menu <<<<<<<<<<<<<< 
    |      1. Penjualan Barang            |
    |      2. Kembali ke Menu Utama       |
    >>>>>>>>>>>>>>>>>>>-<<<<<<<<<<<<<<<<<<<\n''')
        pilihan_sell = input('Masukkan Pilihan Menu yang ingin dijalankan (1-2): ')
        if pilihan_sell.isdigit() == True:                                                                      # Untuk memeriksa apakah input berupa angka
            pilihan_sell = int(pilihan_sell)
            if pilihan_sell == 1:
                if len(data_barang) > 0:                                                                        # Jika jumlah item pada list data_barang lebih dari 0 akan menjalankan function penjualan
                    penjualan()
                else:
                    print('\nTidak dapat melakukan penjualan, dikarenakan Data Barang tidak tersedia.')         # Jika jumlah item pada list data_barang lebih kecil sama dengan 0 akan menampilkan notifikasi
            elif pilihan_sell == 2:
                break
            else : 
                print(f'\nPilihan menu {pilihan_sell} tidak tersedia.\nMohon masukkan pilihan menu yang tersedia (1-2).')                                           # Jika User memilih menu yang tidak tersedia 
        else:
            print('\nInput tidak valid.\nMohon Masukkan Pilihan Menu Yang Berupa Bilangan Bulat (1-2).\n')      # Jika input tidak berupa angka

# Function untuk melakukan kegiatan penjualan barang
def penjualan():
    while True:
        while True:
            loop_breaker = False                                                            # Mendefinisikan loop_breaker bernilai False
            nama_jual = input('\nMasukkkan nama barang yang terjual : ').title()            # .title digunakan untuk merubah huruf pertama ditiap kata menjadi huruf kapital dan di ikuti dengan huruf kecil
            ada = False
            for i in range(len(data_barang)):
                if nama_jual == data_barang[i]['nama']:                                     # Memeriksa apakah nama barang yang di input terdapat didalam daftar barang
                    ada = True
                    x = i
                    break
            if ada == False:
                print(f'\n{nama_jual} tidak tersedia.')
                if konfirmasi('Apakah ada barang lain yang terjual?') == False:
                    if len(cart) == 0:
                        print('\nKembali Ke Sub Menu Penjualan.')
                    loop_breaker = True                                                     # Merubah nilai loop_breaker menjadi bernilai True
                    break
            else:
                if data_barang[x]['stock'] == 0:
                    print(f'\nStock {nama_jual} habis.')
                    if konfirmasi('Apakah ada barang lain yang terjual?') == False:
                        if len(cart) == 0:
                            print('\nKembali Ke Sub Menu Penjualan.')
                        loop_breaker = True 
                        break
                else:
                    break
        if loop_breaker == True:                                                            # Jika loop_breaker bernilai True, maka akan dilakukan break pada outer while loop 
            break
        while True:
            loop_breaker = False                                                            # Mendefinisikan loop_breaker bernilai False
            jumlah_terjual = input(f'Masukkan jumlah {nama_jual} yang terjual : ')
            if jumlah_terjual.isdigit() == True:
                jumlah_terjual = int(jumlah_terjual)
                if jumlah_terjual < 0:
                    print('Mohon masukkan jumlah terjual dengan benar, tidak bernilai negatif.')
                elif jumlah_terjual > data_barang[x]['stock']:
                    print(f'Pembelian melebihi stock yang tersedia, stock {nama_jual} tersedia sebanyak {data_barang[x]["stock"]}')
                    if konfirmasi(f'Apakah Customer Tetap Ingin Membeli {nama_jual}?') == False:
                        if konfirmasi('Apakah ada barang lain yang terjual?') == False:
                            if len(cart) == 0:
                                print('\nKembali Ke Sub Menu Penjualan.')
                            loop_breaker = True                                             # Merubah nilai loop_breaker menjadi bernilai True
                        break    
                else:
                    break
            else:
                print('\nMohon masukkan jumlah terjual dengan bilangan bulat.')
        if loop_breaker == True:                                                            # Jika loop_breaker bernilai True, maka akan dilakukan break pada outer while loop
            break
        harga_jual = data_barang[x]['harga']
        total_harga = jumlah_terjual*harga_jual
        cart.append([nama_jual,jumlah_terjual,harga_jual,total_harga])                      # Menambahkan item kedalam list cart, dengan menggunakan .append
        print('Cart :')
        table = []
        for i in range(len(cart)):
            table.append([cart[i][0],cart[i][1],cart[i][2]])
        print(tabulate(table, headers = ['Nama','Quantity','Harga'],tablefmt='double_outline',numalign='right',stralign='left'))                # Untuk menampilkan tabel cart dengan bantuan tabulate

        if konfirmasi('Apakah Ada Barang Lain yang terjual?') == False:
            break
            
    if len(cart) > 0:                                  # Jika list cart tidak berupa list kosong, maka akan di jalankan blok code didalamnya
        print('Cart :')
        table = []
        for i in range(len(cart)):
            table.append([cart[i][0],cart[i][1],cart[i][2],cart[i][3]])
        print(tabulate(table, headers = ['Nama','Quantity','Harga','Total_Harga'],tablefmt='double_outline',numalign='right',stralign='left'))      # Untuk menampilkan tabel cart dengan bantuan tabulate
        if konfirmasi('Apakah Customer Ingin Melanjutkan Pembayaran?') == True:
            while True:
                print('Pilihan Metode Pembayaran:\n   1. Tunai.\n   2. QR Code.\n   3. Debit.\n   4. Kartu Kredit.')
                metode_pembayaran = input('\nMasukkan metode pembayaran (1-4) : ')
                if metode_pembayaran.isdigit() == False:
                    print('\nInput tidak valid.\nMohon masukkan bilangan bulat. (1-4)')
                else:
                    metode_pembayaran = int(metode_pembayaran)
                    if metode_pembayaran not in range(1,5):
                        print('\nMohon masukkan pilihan metode pembayaran yang tersedia. (1-4)')
                    break
            if metode_pembayaran != 1:                       # Jika metode pembayaran bukan tunai, maka pembayaran diterima, karena jumlah pembayaran akan sama dengan total harga
                print('\nPembayaran Telah Diterima.')
                
            else:                                           # Jika metode pembayaran menggunakan tunai
                jumlah_total_harga = 0
                for i in range(len(cart)):
                    jumlah_total_harga += cart[i][3]
                while True:
                    print(f'Jumlah yang harus dibayar oleh customer sebesar : {jumlah_total_harga}')
                    bayar = input('Masukkan Total Pembayaran : ')
                    if bayar.isdigit() == True:
                        bayar = int(bayar)
                        if bayar < jumlah_total_harga:
                            print(f'Pembayaran tidak diterima, pembayaran kurang sebesar Rp{jumlah_total_harga-bayar}.')
                        elif bayar > jumlah_total_harga:
                            print(f'\nPembayaran Telah Diterima, Dengan Kembali sebesar Rp{bayar-jumlah_total_harga}.')
                            break
                        else:
                            print('\nPembayaran Telah Diterima.')
                            break
                    else:
                        print('Mohon Masukkan Pembayaran yang berupa bilangan bulat.')
            if metode_pembayaran == 1:                  # Mengubah kembali metode_pembayaran dari interger, menjadi string
                metode_pembayaran = 'Tunai'
            elif metode_pembayaran == 2:
                metode_pembayaran = 'QR Code'
            elif metode_pembayaran == 3:
                metode_pembayaran = 'Debit'
            elif metode_pembayaran == 4:
                metode_pembayaran = 'Kartu Kredit'
            for j in range(len(cart)):                  # Untuk melakukan iterasi pada tiap item pada list cart
                nama_jual = cart[j][0]
                jumlah_terjual = cart[j][1]
                harga_jual = cart[j][2]
                for i in range(len(data_barang)):
                    if data_barang[i]['nama'] == nama_jual:             # Memeriksa bila terdapat nama barang yang sama pada tabel daftar barang dengan nama barang yang terjual
                        data_barang[i]['stock'] -= jumlah_terjual       # stock barang pada tabel daftar barang akan dikurangi dengan jumlah barang yang terjual
                        stock_jual = data_barang[i]['stock']            # stock barang yang terjual, sama dengan hasil pengurangan stock barang pada daftar barang
                        kategori_jual = data_barang[i]['kategori']      # kategori barang, sama dengan kategori barang yang bernama sama
                ada = False
                for i in range(len(data_barang)):
                    if data_barang[i]['nama'] == nama_jual and data_barang[i]['metode_pembayaran'] == metode_pembayaran:            # Memeriksa apakah nama barang yang sama juga memiliki metode pembayaran yang sama
                        data_barang[i]['jumlah_terjual'] += jumlah_terjual                                                          # bila nama dan metode pembayarannya sama, maka jumlah barang yang telah terjual akan ditambahkan dengan jumlah barang yang terjual
                        ada = True
                        break
                if ada == False:
                    id_jual = 1                                                         # Generate id, id dimulai dengan bernilai 1
                    if kategori_jual == 'Makanan Dan Minuman':                          # jika kategorinya adalah makanan dan minuman, maka id akan ditambahkan dengan 1000, yang artinya digit pertama id adalah 1                          
                        id_jual += 1000
                    elif kategori_jual == 'Rumah Tangga Dan Kebersihan':
                        id_jual += 2000
                    elif kategori_jual == 'Kesehatan Dan Kecantikan':
                        id_jual += 3000
                    if metode_pembayaran == 'Tunai':                                    # jika metode pembayarannya adalah tunai, maka id akan ditambahkan dengan 100, yang artinya digit kedua id adalah 1
                        id_jual += 100
                    elif metode_pembayaran == 'QR Code':
                        id_jual += 200
                    elif metode_pembayaran == 'Debit':
                        id_jual += 300
                    elif metode_pembayaran == 'Kartu Kredit':
                        id_jual += 400
                    while True:                                          
                        ada = False
                        for i in range(len(data_barang)):                # untuk memeriksa apakah id jual sama dengan id yang sudah ada dalam data penjualan
                            if id_jual == data_barang[i]['id']:
                                ada = True     
                                break
                        if ada == True:
                            id_jual += 1                                 # untuk menambah kan ID jual dengan 1 jika id sudah ada didalam data penjualan
                        else:    
                            break
                    data_barang.append({'id':id_jual,'nama':nama_jual,'kategori':kategori_jual,'harga':harga_jual,'stock':stock_jual,'jumlah_terjual':jumlah_terjual,'metode_pembayaran':metode_pembayaran})  
            cart.clear()                # Untuk mengembalikan cart menjadi list kosong, setelah pembayaran diterima, agar dapat digunakan untuk transaksi berikutnya
        else:
            print('\nCustomer Membatalkan Pembayaran.')
            cart.clear()                # Untuk mengembalikan cart menjadi list kosong, setelah pembatalan pembayaran, agar dapat digunakan untuk transaksi berikutnya



# Memulai aplikasi
if __name__=="__main__":
    main()

