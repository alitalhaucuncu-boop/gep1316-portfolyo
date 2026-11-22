# GEP1316 Kodlama Okuryazarlığı - Ödev 2: İlk Python Programım
# Öğrenci: Ali Taha Üçüncü

# Hesaplama için içinde bulunduğumuz yılı sabit bir değişkende saklıyoruz
mevcut_yil = 2026

# Kullanıcıdan adını metin (string) olarak alıyor ve başındaki/sonundaki fazla boşlukları temizliyoruz
ad = input("Adınız nedir? ").strip()

# Eğer kullanıcı adını boş bıraktıysa varsayılan bir hitap atıyoruz
if ad == "":
    # Boş giriş yapıldığında programın garip görünmemesi için genel hitap kullanıyoruz
    ad = "Değerli Kullanıcı"

# Kullanıcıdan doğum yılını metin (string) olarak istiyoruz
dogum_yili_metin = input("Doğum yılınız nedir? (Örn: 2006): ").strip()

# --- KENDİ EKLEDİĞİM DEĞİŞİKLİK: Hatalı metin, gelecek yıl ve mantıksız yıl doğrulaması ---
# Sayı yerine harf girilirse programın çökmemesi için try-except bloğu başlatıyoruz
try:
    # Kullanıcının metin olarak girdiği doğum yılını tam sayıya (int) dönüştürüyoruz
    dogum_yili = int(dogum_yili_metin)

    # Girilen doğum yılı bulunduğumuz yıldan (2026) büyükse kullanıcıya uyarı veriyoruz
    if dogum_yili > mevcut_yil:
        # Gelecek yıl girildiğinde ekrana açıklayıcı bir hata mesajı yazdırıyoruz
        print(f"Uyarı: {dogum_yili} gelecekte bir yıl! Lütfen {mevcut_yil} veya daha önceki bir doğum yılı giriniz.")
    # Girilen doğum yılı gerçekçi olmayacak kadar eskiyse (1900'den küçükse) uyarı veriyoruz
    elif dogum_yili < 1900:
        # Geçersiz eski tarih için ekrana uyarı mesajı yazdırıyoruz
        print("Uyarı: Lütfen 1900 ile 2026 arasında geçerli bir doğum yılı giriniz.")
    # Girilen yıl geçerli aralıktaysa yaş hesaplama ve kişiye özel karşılama adımına geçiyoruz
    else:
        # Mevcut yıldan doğum yılını çıkararak kullanıcının yaşını hesaplıyoruz
        yas = mevcut_yil - dogum_yili
        # Kullanıcının adını ve hesaplanan yaşını içeren kişiye özel karşılama mesajını yazdırıyoruz
        print(f"\nMerhaba {ad}! {mevcut_yil} yılı itibarıyla {yas} yaşındasın.")
        # Karşılama mesajının devamında derse ve kodlama yolculuğuna yönelik kısa bir not ekliyoruz
        print("GEP1316 Kodlama Okuryazarlığı deposuna hoş geldin, başarılar dilerim!")

# Kullanıcı sayı yerine harf veya sembol girdiyse oluşacak ValueError hatasını yakalıyoruz
except ValueError:
    # Programın çökmesini engelleyip kullanıcıya ne yapması gerektiğini söylüyoruz
    print("Hata: Doğum yılı kısmına yalnızca tam sayı (örneğin 2006) girmelisiniz!") 
