Menu="ya"
while Menu=="ya" or Menu=="Ya":
    print("==========================")
    print("Program Konversi Mata Uang")
    print("==========================")
    print(">>Menu Pilihan :")
    print("1. IDR - USD")
    print("2. IDR - SGD")
    print("3. IDR - EUR")
    print("4. IDR - JPY")
    print("5. Keluar")
    print("==========================")
    Pilihan=int(input("Masukkan pilihan konversi = "))
    if Pilihan==1:
        print("pilih konversi :")
        print("1.IDR ke USD")
        print("2.USD Ke IDR")
        Pilih=int(input("Pilih konversi = "))
        if Pilih==1:
            a=int(input("Masukkan jumlah IDR = RP "))
            b=float(a/14000)
            print("Nilai IDR Rp", a, "= US$", round(b,1))
            Menu=(input("\nKembali ke menu pilihan? [Ya/Tidak] : "))
            print("")
        elif Pilih==2:
            a=float(input("Masukkan jumlah USD = US$ "))
            b=int(a*14000)
            print("Nilai US$", a, "= Rp", b)
            Menu=(input("\nKembali ke menu pilihan? [Ya/Tidak] : "))
            print("")
        else:
            print("Tidak ada pilihan",Pilih)
            Menu=input("\nKembali ke menu pilihan [Ya/Tidak] : ")
            print("")
    elif Pilihan==2:
        print("pilih konversi :")
        print("1.IDR ke SGD")
        print("2.SGD Ke IDR")
        Pilih=int(input("Pilih konversi = "))
        if Pilih==1:
            a=int(input("Masukkan jumlah IDR = RP "))
            b=float(a/10500)
            print("Nilai IDR Rp", a, "= S$", round(b,1))
            Menu=(input("\nKembali ke menu pilihan? [Ya/Tidak] : "))
            print("")
        elif Pilih==2:
            a=float(input("Masukkan jumlah SGD = S$ "))
            b=int(a*10500)
            print("Nilai SGD S$", a, "= Rp", b)
            Menu=(input("\nKembali ke menu pilihan? [Ya/Tidak] : "))
            print("")
        else:
            print("Tidak ada pilihan",Pilih)
            Menu=input("\nKembali ke menu pilihan [Ya/Tidak] : ")
            print("")
    elif Pilihan==3:
        print("pilih konversi :")
        print("1.IDR ke EUR")
        print("2.EUR Ke IDR")
        Pilih=int(input("Pilih konversi = "))
        if Pilih==1:
            a=int(input("Masukkan jumlah IDR = RP "))
            b=float(a/16500)
            print("Nilai IDR Rp", a, "= €", round(b,1))
            Menu=(input("\nKembali ke menu pilihan? [Ya/Tidak] : "))
            print("")
        elif Pilih==2:
            a=float(input("Masukkan jumlah EUR = € "))
            b=int(a*16500)
            print("Nilai EUR €", a, "= Rp", b)
            Menu=(input("\nKembali ke menu pilihan? [Ya/Tidak] : "))
            print("")
        else:
            print("Tidak ada pilihan",Pilih)
            Menu=input("\nKembali ke menu pilihan [Ya/Tidak] : ")
            print("Terima kasih")
    elif Pilihan==4:
        print("pilih konversi :")
        print("1.IDR ke JPY")
        print("2.JPY Ke IDR")
        Pilih=int(input("Pilih konversi = "))
        if Pilih==1:
            a=int(input("Masukkan jumlah IDR = RP "))
            b=float(a/125)
            print("Nilai IDR Rp", a, "= ¥", round(b,1))
            Menu=(input("\nKembali ke menu pilihan? [Ya/Tidak] : "))
            print("")
        elif Pilih==2:
            a=float(input("Masukkan jumlah JPY = ¥ "))
            b=int(a*125)
            print("Nilai JPY ¥", a, "= Rp", b)
            Menu=(input("\nKembali ke menu pilihan? [Ya/Tidak] : "))
            print("")
        else:
            print("Tidak ada pilihan",Pilih)
            Menu=input("\nKembali ke menu pilihan [Ya/Tidak] : ")
            print("")                                      
    elif Pilihan==5:
        print("Terima kasih")
        break
    else:
        print("Tidak ada pilihan",Pilihan)
        Menu=input("\nKembali ke menu pilihan [Ya/Tidak] : ")
        print("")        