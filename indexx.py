while True:
    print("BASİT HESAP MAKİNESİ")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    print("5. Çıkış")

    islem = input("İşlem seçiniz: ")

    if islem == "5":
        print("Program kapatıldı.")
        break

    elif islem == "1":
        sayi1 = float(input("Birinci sayıyı giriniz: "))
        sayi2 = float(input("İkinci sayıyı giriniz: "))

        sonuc = sayi1 + sayi2
        print("Sonuç:", sayi1, "+", sayi2, "=", sonuc)

    elif islem == "2":
        sayi1 = float(input("Birinci sayıyı giriniz: "))
        sayi2 = float(input("İkinci sayıyı giriniz: "))

        sonuc = sayi1 - sayi2
        print("Sonuç:", sayi1, "-", sayi2, "=", sonuc)

    elif islem == "3":
        sayi1 = int(input("Birinci sayıyı giriniz: "))
        sayi2 = int(input("İkinci sayıyı giriniz: "))

        sonuc = sayi1 * sayi2
        print("Sonuç:", sayi1, "*", sayi2, "=", sonuc)

    elif islem == "4":
        sayi1 = float(input("Birinci sayıyı giriniz: "))
        sayi2 = float(input("İkinci sayıyı giriniz: "))

        if sayi2 == 0:
            print("Sıfıra bölme yapılamaz.")
        else:
            sonuc = sayi1 / sayi2
            print("Sonuç:", sayi1, "/", sayi2, "=", sonuc)

    else:
        print("Hatalı seçim yaptınız.")