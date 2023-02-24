#Program ini ditulis oleh
#Nama : Mohammad Hatta
#NPM  : 2006470685

#Mengimpor library yang digunakan
import pandas as pd
import xlsxwriter as xls

#Membuat array kosong yang nantinya akan diisi oleh input data yang dimasukkan pengguna
Nama            =[]   
NPM             =[]
Jenis_Kelamin   =[]
TTL             =[]
Nomor_HP        =[]

# Keadaan awal untuk menjalankan loop fungsi while
Keadaan2=True

#Fungsi while digunakan agar pengguna dapat menambahkan data mahasiswa berikutnya
while Keadaan2==True:

#Pengguna memasukkan data mahasiswa (Nama Mahasiswa, NPM, Jenis Kelamin, TTL, & Nomor HP)
    x1=input('Nama Mahasiswa: ')            
    x2=input('NPM: ')                       
    x3=input('Jenis Kelamin (L/P): ')             
    x4=input('Tempat dan Tanggal Lahir: ')  
    x5=input('Nomor HP: ')                  

#Data mahasiswa yang sudah diinput oleh pengguna akan dimasukkan ke array kosong sebelumnya
    Nama.append(x1)                        
    NPM.append(x2)                         
    Jenis_Kelamin.append(x3)              
    TTL.append(x4)                        
    Nomor_HP.append(x5)                      
    
#Sistem memberikan pilihan kepada pengguna jika ingin menambahkan/menyimpan data yang sudah diisi
    print("Apakah Anda masih ingin menambahkan data mahasiswa berikutnya?")
    Keadaan1=input('Tambahkan/Simpan: ')
    if Keadaan1=='Tambahkan': 
        Keadaan2=True 
        print("Data Anda berhasil ditambahkan, namun belum tersimpan. Untuk menyimpan data Anda perlu menulis Simpan.")
#Fungsi Loop while akan terus berlanjut jika Keadaan2=True, yaitu saat pengguna menginput pilihan "Tambahkan" pada pilihan "Tambahkan/Simpan"
    elif Keadaan1=='Simpan':
        Keadaan2=False
        print("Data Anda telah berhasil disimpan pada direktori file:D://Semester6/AI/Tugas1/Data Mahasiswa.xlsx ")
#Fungsi Loop while akan berhenti jika Keadaan2=False, yaitu saat pengguna menginput pilihan "Simpan" pada pilihan "Tambahkan/Simpan"
    else:
        Keadaan3 = True
        while Keadaan3:
            Keadaan1=input('Tambahkan/Simpan: ')
            if Keadaan1=='Tambahkan': 
                Keadaan2=True
                Keadaan3 = False
                print("Data Anda berhasil ditambahkan, namun belum tersimpan. Untuk menyimpan data Anda perlu menulis Simpan.")
            elif Keadaan1=='Simpan':
                Keadaan2=False
                Keadaan3 = False
                print("Data Anda telah berhasil disimpan pada direktori file:D://Semester6/AI/Tugas1/Data Mahasiswa.xlsx")
            else:
                print("Harap masukkan pilihan yang sesuai, yaitu Tambahkan/Simpan")
                Keadaan3 = True
#Program ini tidak akan berakhir jikan Keadaan2 tidak terpenuhi, yaitu saat pengguna memasukkan pilihan "Tambahkan/Simpan"

#Menyimpan data yang sudah dimasukkan oleh pengguna ke file 'Data Mahasiswa.xlsx'
kerangka_data=pd.DataFrame({'Nama Mahasiswa':Nama,
                            'NPM': NPM, 
                            'Jenis Kelamin': Jenis_Kelamin, 
                            'Tempat dan Tanggal Lahir':TTL , 
                            'Nomor HP': Nomor_HP})
kerangka_data.to_excel("D://Semester6/AI/Tugas/Tugas 1/Data Mahasiswa.xlsx", index = False)