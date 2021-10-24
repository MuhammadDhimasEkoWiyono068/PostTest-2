Bio="tidak"
while Bio=="tidak" or Bio=="Tidak":
    print("======================================================")
    print("         Masukkan Biodata Anda Dengan Benar :")
    print()
    biodata=[input("Nama : "),
             input("NIM : "),
             input("Tempat Tanggal Lahir : "),
             input("Umur : "),
             input("Berat Badan(Dalam satuan Kg) : "),
             input("Tinggi Badan(Dalam Satuan Cm) : ")]
    Bio =(input("\nApakah Biodata yang anda isi Sudah Benar? [Ya/Tidak]?"))
    print("")
    print("======================================================")
    print("                  BIODATA MAHASISWA")
    print()
    print("Nama                 :",str(biodata[0]))
    print("NIM                  :",int(biodata[1]))
    print("Tempat Tanggal Lahir :",str(biodata[2]))
    print("Umur                 :",int(biodata[3]),"Tahun")
    print("Berat Badan          :",float(biodata[4]),"Kg")
    print("Tinggi Badan         :",float(biodata[5]),"Cm")
    print()
    print("======================================================")
    Bio =(input("\nApakah Tampilan Biodata Sudah Benar? [Ya/Tidak]?"))
    print("")