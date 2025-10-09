max_percobaan = 5
percobaan = 0

while percobaan < max_percobaan:
    username = str(input("silakan masukkan username anda: "))
    password = str(input("silakan masukkan password anda: "))
    if (username == "Tya" or username == "Diftya") and password == "042":
        print("Login berhasil")
        break
    else:
        percobaan += 1
        print("Login gagal")
        print("Coba lagi")
    if percobaan == max_percobaan:
        print("Maaf, batas percobaan Anda sudah habis.")
        exit()

sisi_a = int(input("Input panjang sisi A: "))
sisi_b = int(input("Input panjang sisi B: "))
sisi_c = int(input("Input panjang sisi C: "))
if sisi_a + sisi_b <= sisi_c or sisi_a + sisi_c <= sisi_b or sisi_b + sisi_c <= sisi_a:
        print("Bukan Segitiga")
else:
        print("Terdefinisi sebagai segitiga.")
        if sisi_a == sisi_b == sisi_c:
            print("Merupakan segitiga sama sisi.")
        elif sisi_a == sisi_b or sisi_b == sisi_c or sisi_a == sisi_c:
            print("Merupakan segitiga sama kaki.")
        else:
            print("Merupakan segitiga sembarang.")

        pertanyaan_tambahan = input("Apakah anda ingin menghitung luas segitiga ini? (y/n) ")
        if pertanyaan_tambahan == "n" or pertanyaan_tambahan == "N":
            print("Terima kasih telah menggunakan program ini")
            
        elif pertanyaan_tambahan == "y" or pertanyaan_tambahan == "Y":
            alas = float(input("Input panjang alas : "))
            tinggi = float(input("Input tinggi : "))
            luas_segitiga = 0.5 * alas * tinggi
            print("Luas segitiga adalah", luas_segitiga)