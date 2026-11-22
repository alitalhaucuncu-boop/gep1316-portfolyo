# GEP1316 Kodlama Okuryazarlığı - Ödev 3: Python ile Kişisel Hesaplayıcı
# Konu: İşletme - Brüt Kâr Marjı ve KDV Hesaplayıcı
# Öğrenci: Ali Taha Üçüncü

# Başlık bilgisini ekrana yazdırıyoruz
print("=== İŞLETME KÂR MARJI VE KDV HESAPLAYICI ===")

# 1. VERİ TİPİ (str): Kullanıcıdan ürün adını metin olarak alıyoruz
urun_adi = input("Ürün adı: ").strip()

# Sayısal dönüşümlerde harf girilmesine karşı hata yakalama bloğu başlatıyoruz
try:
    # 2. VERİ TİPİ (float): Alış maliyetini input() ile alıp ondalıklı sayıya dönüştürüyoruz
    alis_maliyeti = float(input("Birim alış maliyeti (TL): "))

    # KDV hariç satış fiyatını input() ile alıp ondalıklı sayıya (float) dönüştürüyoruz
    satis_fiyati = float(input("KDV hariç birim satış fiyatı (TL): "))

    # 3. VERİ TİPİ (int): Satış adedini tam sayıya dönüştürüyoruz
    satis_adedi = int(input("Satış adedi: "))

    # KDV oranını tam sayı (int) olarak alıyoruz (ör. 1, 10 veya 20)
    kdv_orani = int(input("KDV oranı (% olarak, örn. 10 veya 20): "))

    # Uç durum kontrolü: Karşılaştırma operatörleri (<, <=) ile sıfır ve negatif değerleri denetliyoruz
    if alis_maliyeti < 0 or satis_fiyati <= 0 or satis_adedi <= 0 or kdv_orani < 0:
        # Sıfıra bölme hatasını (ZeroDivisionError) ve mantıksız girdileri engelliyoruz
        print("\nUyarı: Satış fiyatı ve satış adedi 0'dan büyük; maliyet ve KDV oranı 0 veya pozitif olmalıdır.")
    else:
        # Aritmetik operatörler (-, *, /, +) ile finansal hesaplamaları yapıyoruz
        # Birim başına elde edilen brüt kâr tutarını hesaplıyoruz
        birim_kar = satis_fiyati - alis_maliyeti

        # Satış adedine göre toplam brüt kâr tutarını hesaplıyoruz
        toplam_kar = birim_kar * satis_adedi

        # Brüt kâr marjı formülü: (Birim Kâr / KDV Hariç Satış Fiyatı) * 100
        kar_marji = (birim_kar / satis_fiyati) * 100

        # Birim ürün için eklenecek KDV tutarını hesaplıyoruz
        kdv_tutari = satis_fiyati * (kdv_orani / 100)

        # KDV dahil birim satış fiyatını buluyoruz
        kdv_dahil_birim_fiyat = satis_fiyati + kdv_tutari

        # KDV dahil toplam satış tutarını (ciroyu) hesaplıyoruz
        kdv_dahil_toplam_tutar = kdv_dahil_birim_fiyat * satis_adedi

        # 4. VERİ TİPİ (bool): Karşılaştırma operatörleri (>, >=) ile kârlılık durumunu belirliyoruz
        karli_mi = birim_kar > 0
        hedef_marj_saglandi_mi = kar_marji >= 20.0

        # Biçimli çıktı (f-string) ile tüm sonuçları düzenli şekilde ekrana yazdırıyoruz
        print("\n--- HESAPLAMA SONUÇLARI ---")
        print(f"Ürün Adı                  : {urun_adi}")
        print(f"Birim Brüt Kâr            : {birim_kar:.2f} TL")
        print(f"Toplam Brüt Kâr ({satis_adedi} adet) : {toplam_kar:.2f} TL")
        print(f"Brüt Kâr Marjı            : %{kar_marji:.2f}")
        print(f"KDV Tutarı (%{kdv_orani})          : {kdv_tutari:.2f} TL")
        print(f"KDV Dahil Birim Fiyat     : {kdv_dahil_birim_fiyat:.2f} TL")
        print(f"KDV Dahil Toplam Tutar    : {kdv_dahil_toplam_tutar:.2f} TL")
        print(f"Satış Kârlı mı? (bool)    : {karli_mi}")
        print(f"%20 Hedef Marj Sağlandı mı?: {hedef_marj_saglandi_mi}")

# Sayısal alanlara harf veya geçersiz karakter girilirse kullanıcıyı uyarıyoruz
except ValueError:
    print("\nHata: Maliyet, fiyat, adet ve KDV oranı alanlarına yalnızca sayısal değer giriniz.")
