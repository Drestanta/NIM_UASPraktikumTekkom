def pilihan():
    print("=====Selamat datang di XXV=====")
    tanggal = int(input("Masukkan tanggal hari ini:"))
    
    print("==Berikut genre film yang tersedia==")
    print("1. Horror")
    print("2. Action")
    pilih = int(input("Silahkan pilih mau nonton film bergenre apa:"))
    
    if(pilih == 1) :
        print("==Berikut pilihan film Horror yang sedang tayang==")
        print("1. The Devil's Light")
        print("2. Pengabdi Setan")
        exit()
    if(pilih == 2) :
        print("==Berikut pilihan film Action yang sedang tayang==")
        print("1. Black Panther: Wakanda Forever")
        print("2. Avatar: The Way of Water")
        exit()
    if(pilih>=3) :
        print("Pilihan yang anda pilih tidak tersedia di bioskop ini")
        exit()
    
    film = int(input("Silahkan pilih mau nonton film apa:"))
    pesan = int(input("Mau memesan tiket sebanyak:"))

pilihan()