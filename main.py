import inspect #Bir fonksiyonun hangi fonksiyon tarafından çağırıldığını öğrenebilmek içinbu modülü kullandım
import sys
sys.path.append("lib") # Bu kod Python'a, proje dizininde yer alan lib klasörünün içindeki modülleri araması gerektiğini belirtir. Bu sayede bu projede kullanmış olduğum bütün modülleri tek bir klasör içerisinde toplamış oldum
import subprocess #Bu modülü, harici bir komut çalıştırabilmek için ve bu programı yeniden başlatabilmek için kullandım.
#Harici bir komut çalıştırmak istememin sebebi, projemde üçüncü taraf bir modül olan "tabulate" modülünü ve prompt_toolkit modülünü, projeyi çalıştıracak olan kişinin sisteminde yüklü değilse sisteme otomatik olarak yükleyebilmek için
#Ama yinede ilgili modülleri (tabulate.py ve prompt_toolkit), projenin yanında lib dizininde veriyorum. Bu modüller lib dizininde durduğu sürece, harici bir komutla kütüphaneyi yüklemeye gerek kalmayacaktır.
# Programı yeniden başlatmak istememin sebebi ise ilgili modüller komut ile yüklendikten sonra programın yeniden başlaması gerekmektedir.
from os import system #Console ekranını temizleyebilmek için bu modülü dahil ettim
import csv #csv formatındaki dosyalar ile işlemler yapabilmek için bu modülü dahil ettim

try:
    from tabulate import tabulate # 2 boyutlu liste içerisindeki verileri yazdırırken, konsol ekranında veriler düzenli bir şekilde görünmesi için için bu modülü dahil ettim.
except ModuleNotFoundError:
    subprocess.check_call(["pip", "install", "tabulate"]) #Eğer modül sistemde yüklü değilse yada proje dizininde yoksa;"pip install tabulate" komutu ile ilgili modülü otomatik olarak yüklenecektir.
    python = sys.executable
    subprocess.call([python] + sys.argv) #Modül yüklendikten sonra programı tekrar başlatıyorum. Bu programın tekrar başlatılması demek kapanıp açılması anlamına gelmiyor.
    exit() #Bu yüzden önceki process deki bu programı kapatıyorum

try:
    from prompt_toolkit import prompt # CSV dosyasının içindeki verileri güncellerken, konsol ekranında kullanıcıdan değer alırken hız ve estetik katması açısından bu modülü kullanmak istedim.
    from prompt_toolkit.completion import WordCompleter # Bu modül, kullanıcı konsol ekranından değer girerken kullanıcıya öneriler sunup tab veya yön tuşları ile otomatik tamamlama yapmaya yarıyor
    from prompt_toolkit.lexers import SimpleLexer # SimpleLexer özelliği ise, kelime tamamlama esnasında kelime önerilirken, önerilen kelimelerin türkçe karakterleride desteklemesini sağlar
except ModuleNotFoundError:
    subprocess.check_call(["pip", "install", "prompt_toolkit"])
    python = sys.executable
    subprocess.call([python] + sys.argv)
    exit()
# Normal şartlarda proje, gereksinim duyduğu modüller ile beraber paketlenip bir setup dosyası haline getirildikten sonra kullanıcıya teslim edilmesi gerekmektedir ve bunun farkındayım. Ancak bu kadar ileriye gitmek istemedim ve böyle bir yaklaşım tercih ettim 

def main(): #Programdaki bütün fonksiyonları main isimli temel fonksiyon üzerinden kontrol ettim
    while(True):
        system('cls')
        print_menu()
        secenek = ''
        try:
            secenek = int(input('Lütfen seçiminizi girin: '))
        except:
            print('Geçersiz giriş. Lütfen bir numara girin...')
        
        if secenek == 1:
           mukellef_listele()
        elif secenek == 2:
            mukellef_ekle()
        elif secenek == 3:
            mukellef_guncelle()
        elif secenek == 4:
            mukellef_sil()
        elif secenek == 5:
            mukellef_ara()
        elif secenek == 6:
            vergi_hesapla()
        elif secenek == 7:
            print('Çıkış yapıldı...')
            exit()
        else:
            print('Yanlış seçenek. Lütfen tekrar deneyin...')

menu_secenekleri = {
    1: 'Mükellef Listele',
    2: 'Mükellef Ekle',
    3: 'Mükellef Güncelle',
    4: 'Mükellef Sil',
    5: 'Mukellef Ara',
    6: 'Vergi Hesapla',
    7: 'Çıkış'
}

def print_menu(submenu = 0):
    if submenu == 0:
        for key in menu_secenekleri.keys():
            print ('[',key,'] -', menu_secenekleri[key])
    elif submenu == 1:
        print("[1] - Detaylı görüntüle")
        print("[2] - Geri")
    elif submenu == 2:
        print("[1] - Bu Mükellefi Güncelle")
        print("[2] - Bu Mükellefi Sil")
        print("[3] - Bu Mükellefin Vergisini Hesapla")
        print("[4] - Çık")

def mukellef_listele():
    system('cls')
    mukellefler = []
    kisisel_bilgiler = []
    sirketler = []
    kontroller = []
    ivd_hesaplari = []
    gelirler_giderler = []
    
    #Tek bir with deyimi ile, bütün csv dosyalarını aynı anda açıp dosyaların içindeki bilgileri okudum
    with open("mukellef.csv") as mukellef, open("kisisel_bilgiler.csv") as kisisel_bilgi, open("sirket.csv") as sirket, open("kontrol.csv") as kontrol, open("ivd.csv") as ivd, open("gelir_gider.csv") as gelirgider:
        mukellef_okuyucu = csv.reader(mukellef, delimiter=";")
        kisisel_bilgi_okuyucu = csv.reader(kisisel_bilgi, delimiter=";")
        sirket_okuyucu = csv.reader(sirket, delimiter=";")
        kontrol_okuyucu = csv.reader(kontrol, delimiter=";")
        ivd_okuyucu = csv.reader(ivd, delimiter=";")
        gelirgider_okuyucu = csv.reader(gelirgider, delimiter=";")

        #CSV dosyalarından okumuş olduğum verileri, listelere aktardım
        for row in mukellef_okuyucu:
            mukellefler.append(row)

        for row in kisisel_bilgi_okuyucu:
            kisisel_bilgiler.append(row)

        for row in sirket_okuyucu:
            sirketler.append(row)

        for row in kontrol_okuyucu:
            kontroller.append(row)

        for row in ivd_okuyucu:
            ivd_hesaplari.append(row)

        for row in gelirgider_okuyucu:
            gelirler_giderler.append(row)

    #Mükellefler listesinin içindeki bütün sütunları yazdırmak istemiyorum. Çünkü istenmeyen sütunlar, mükellefe ait bilgilerin id numarasını oluşturuyor. Bu id numaraları tek başlarına anlamsız veriler.
    # İstenilen sütunları al
    secilen_veriler = [[row[i] for i in [0, 1, 2, 3, 4]] for row in mukellefler]
    # Tabloyu oluştur ve yazdır
    tablo = tabulate(secilen_veriler, headers="firstrow")
    print(tablo)

    print_menu(1)
    secenek = int(input("Lütfen Seçiminizi girin : "))
    if secenek == 1:
        while(True):
            mukellef_id = int(input("Detaylı görüntülemek istediğiniz mükellefin id numarasını girin :"))
            if detayli_mukellef_listele(mukellef_id) == False:
                print("Böyle bir mükellef bulunamadı. Lütfen tekrar deneyin.")
            else:
                break
    else:
        system('cls')

def detayli_mukellef_listele(mukellef_id):
    mukellefler = []
    kisisel_bilgiler = []
    sirketler = []
    kontroller = []
    ivd_hesaplari = []
    gelirler_giderler = []
    
    #Tek bir with deyimi ile, bütün csv dosyalarını aynı anda açıp dosyaların içindeki bilgileri okudum
    with open("mukellef.csv") as mukellef, open("kisisel_bilgiler.csv") as kisisel_bilgi, open("sirket.csv") as sirket, open("kontrol.csv") as kontrol, open("ivd.csv") as ivd, open("gelir_gider.csv") as gelirgider:
        mukellef_okuyucu = csv.reader(mukellef, delimiter=";")
        kisisel_bilgi_okuyucu = csv.reader(kisisel_bilgi, delimiter=";")
        sirket_okuyucu = csv.reader(sirket, delimiter=";")
        kontrol_okuyucu = csv.reader(kontrol, delimiter=";")
        ivd_okuyucu = csv.reader(ivd, delimiter=";")
        gelir_gider_okuyucu = csv.reader(gelirgider, delimiter=";")

        #CSV dosyalarından okumuş olduğum verileri, listelere aktardım
        for row in mukellef_okuyucu:
            mukellefler.append(row)

        for row in kisisel_bilgi_okuyucu:
            kisisel_bilgiler.append(row)

        for row in sirket_okuyucu:
            sirketler.append(row)

        for row in kontrol_okuyucu:
            kontroller.append(row)

        for row in ivd_okuyucu:
            ivd_hesaplari.append(row)

        for row in gelir_gider_okuyucu:
            gelirler_giderler.append(row)
    
    # Filtreleme işlemi
    filtrelenmis_mukellef = [satir for satir in mukellefler if satir[0] == str(mukellef_id)]  #Mükellef id si mukellef_id ye eşit olanı getir

    bulundu = bool(filtrelenmis_mukellef) # Liste doluysa True, boşsa False. Yani kullanıcının parametre olarak bu fonksiyona gönderdiği id değeri csv dosyasında bir değere karşılık gelip gelmediğini kontrol etmiş oluyorum

    if bulundu: #Eğer kullanıcının girdiği ve parametre olarak bu fonksiyona gönderdiği id değerine sahip bir veri varsa
        system('cls')
        print("\nMükellef bilgileri >>>")
        #Seçilen mükellefe ait id leri alıyorum
        mukellef_id = filtrelenmis_mukellef[0][0]
        kisisel_bilgi_id = filtrelenmis_mukellef[0][5]
        sirket_id = filtrelenmis_mukellef[0][6]
        kontrol_id = filtrelenmis_mukellef[0][7]
        ivd_id = filtrelenmis_mukellef[0][8]
        gelir_gider_id = filtrelenmis_mukellef[0][9]

        # Tabloyu oluştur
        secilen_veriler =  [[row[i] for i in [0, 1, 2, 3, 4]] for row in filtrelenmis_mukellef]
        secilen_mukellef = tabulate(secilen_veriler, headers=["id","ad", "soyad", "email","telefon"], tablefmt="outline")
        print(secilen_mukellef)

        print("\nKişisel Bilgiler >>>")
        filtrelenmis_kisisel_bilgi = [satir for satir in kisisel_bilgiler if satir[0] == str(kisisel_bilgi_id)]
        secilen_kisisel_bilgi = tabulate(filtrelenmis_kisisel_bilgi, headers=["id","tckn", "doğum tarihi","mükellef olma tarihi", "terk transfer tarihi","terk transfer nedeni"], tablefmt="outline")
        print(secilen_kisisel_bilgi)

        print("\nŞirket Bilgileri >>>")
        filtrelenmis_sirket_bilgisi = [satir for satir in sirketler if satir[0] == str(sirket_id)]
        secilen_sirket_bilgisi = tabulate(filtrelenmis_sirket_bilgisi, headers=["id","şirket türü", "faaliyet adresi","il", "vergi dairesi", "vergi numarası", "şirket ünvanı", "faaliyet alanı","çalışan sayısı", "işe başlama tarihi"], tablefmt="outline")
        print(secilen_sirket_bilgisi)

        print("\nKontrol >>>")
        filtrelenmis_kontrol_bilgisi = [satir for satir in kontroller if satir[0] == str(kontrol_id)]
        secilen_kontrol_bilgisi = tabulate(filtrelenmis_kontrol_bilgisi, headers=["id","vergi levhası","sözleşme", "yoklama","defterbeyan"],tablefmt="outline")
        print(secilen_kontrol_bilgisi)

        print("\nİVD Hesabı >>>")
        filtrelenmis_ivd_hesap_bilgisi = [satir for satir in ivd_hesaplari if satir[0] == str(ivd_id)]
        secilen_ivd_bilgisi = tabulate(filtrelenmis_ivd_hesap_bilgisi, headers=["id","kullanıcı adı","şifre"],tablefmt="outline")
        print(secilen_ivd_bilgisi)

        print("\nGelir Gider >>>")
        filtrelenmis_gelir_gider_bilgisi = [satir for satir in gelirler_giderler if satir[0] == str(gelir_gider_id)]
        secilen_gelir_gider_bilgisi = tabulate(filtrelenmis_gelir_gider_bilgisi, headers=["id", "gelir", "gider"], tablefmt="outline")
        print(secilen_gelir_gider_bilgisi)

        print_menu(2)
        secim = int(input("Lütfen seçiminizi girin : "))

        if secim == 1:
            mukellef_guncelle(mukellef_id, kisisel_bilgi_id, sirket_id, kontrol_id, ivd_id, gelir_gider_id)
        elif secim == 2:
            mukellef_sil(mukellef_id, kisisel_bilgi_id, sirket_id, kontrol_id, ivd_id, gelir_gider_id)
        elif secim == 3:
            vergi_hesapla(mukellef_id, sirket_id, gelir_gider_id)
        else:
            print_menu()
            mukellef_listele()
    else: 
        return False

def mukellef_ekle():
    # Yeni bir mükellef eklemeden önce, eklenmiş olan önceki mükelleflerin id sine ihtiyacım var. Bu sayede son mükellefin id numarasının bir fazlası kadar yeni ve benzersiz bir id numarası oluşturabilirim.
    # Yeni id'leri kullanıcının insiyatifine bırakmıyorum. Çünkü bu id'ler primary key ve foreign key olduğu için benzersiz olmak zorunda
    mukellef_ids = []
    kisisel_bilgi_ids = []
    sirket_ids = []
    ivd_ids = []
    kontrol_ids = []
    gelir_gider_ids = []

    #Bütün csv dosyalarını tek tek okuyarak, bütün dosyalardaki id bilgilerini, son eki _ids olan listelere ekliyorum
    with open("mukellef.csv", 'r') as mukellef, open("kisisel_bilgiler.csv", 'r') as kisisel_bilgiler, open("sirket.csv", 'r') as sirket, open("ivd.csv", 'r') as ivd ,open("kontrol.csv", 'r') as kontrol, open("gelir_gider.csv", 'r') as gelirgider:
        mukellef_okuyucu = csv.reader(mukellef, delimiter=";")
        kisisel_bilgiler_okuyucu = csv.reader(kisisel_bilgiler, delimiter=";")
        sirket_okuyucu = csv.reader(sirket, delimiter=";")
        ivd_okuycu = csv.reader(ivd, delimiter=";")
        kontrol_okuyucu = csv.reader(kontrol, delimiter=";")
        gelir_gider_okuyucu = csv.reader(gelirgider, delimiter=";")

        for row in mukellef_okuyucu:
            mukellef_ids.append(row[0])  # İlk sütunun değerini listeye ekler

        for row in kisisel_bilgiler_okuyucu:
            kisisel_bilgi_ids.append(row[0])
        
        for row in sirket_okuyucu:
            sirket_ids.append(row[0])

        for row in ivd_okuycu:
            ivd_ids.append(row[0])

        for row in kontrol_okuyucu:
            kontrol_ids.append(row[0])
        
        for row in gelir_gider_okuyucu:
            gelir_gider_ids.append(row[0])

    try:
        son_mukellef_id = mukellef_ids[len(mukellef_ids) - 1] #Son mükellefin id'sini al
        yeni_mukellef_id = int(son_mukellef_id) + 1 #Son mükellefin id'sinin bir fazlası kadar yeni bir id oluştur
    except ValueError: # Eğer hiç mükellef eklenmemişse, sütun ismini (id), değer olarak alıyor ve buda ValueError Hatasına sebebiyet veriyor
        yeni_mukellef_id = 1 #Eğer önce hiç mükellef eklenmemişse, yeni id'yi 1 olarak ayarlıyorum

    try:
        son_kisisel_bilgi_id = kisisel_bilgi_ids[len(kisisel_bilgi_ids) - 1]
        yeni_kisisel_bilgi_id = int(son_kisisel_bilgi_id) + 1
    except ValueError:
        yeni_kisisel_bilgi_id = 1

    try:
        son_sirket_id = sirket_ids[len(sirket_ids) - 1]
        yeni_sirket_id = int(son_sirket_id) + 1
    except ValueError:
        yeni_sirket_id = 1
    
    try:
        son_ivd_id = ivd_ids[len(ivd_ids) - 1]
        yeni_ivd_id = int(son_ivd_id) + 1
    except ValueError:
        yeni_ivd_id = 1

    try:
        son_kontrol_id = kontrol_ids[len(kontrol_ids) - 1]
        yeni_kontrol_id = int(son_kontrol_id) + 1
    except ValueError:
        yeni_kontrol_id = 1
    
    try:
        son_gelir_gider_id = gelir_gider_ids[len(gelir_gider_ids) - 1]
        yeni_gelir_gider_id = int(son_gelir_gider_id) + 1
    except ValueError:
        yeni_gelir_gider_id = 1

    while True:
        # Oluşan yeni id, önceki mükelleflere tanımlanıp tanımlanmadığını kontrol et. Çünkü, CSV dosyalarına manuel olarak müdahale edilmiş olabilir veya mükelleflerin id leri ardışık bir şekilde artmıyor olabilir
        if str(yeni_mukellef_id) not in mukellef_ids: 
            '''Oluşan yeni id, önceki mükelleflere ait değil'''
            break
        else:
            yeni_mukellef_id += 1 # Eğer oluşan yeni mükellefin id'si, kayıtlı olan mükelleflerden birine ait ise, yeni_mukellef_id benzersiz olana kadar 1 arttır

    while True:
        if str(yeni_kisisel_bilgi_id) not in kisisel_bilgi_ids: 
            '''Oluşan yeni id, önceki mükelleflere ait değil'''
            break
        else:
            yeni_kisisel_bilgi_id += 1

    while True:
        if str(yeni_sirket_id) not in sirket_ids: 
            '''Oluşan yeni id, önceki mükelleflere ait değil'''
            break
        else:
            yeni_sirket_id += 1
    
    while True:
        if str(yeni_ivd_id) not in ivd_ids: 
            '''Oluşan yeni id, önceki mükelleflere ait değil'''
            break
        else:
            yeni_ivd_id += 1

    while True:
        if str(yeni_kontrol_id) not in kontrol_ids: 
            '''Oluşan yeni id, önceki mükelleflere ait değil'''
            break
        else:
            yeni_kontrol_id += 1

    while True:
        if str(yeni_gelir_gider_id) not in gelir_gider_ids:
            '''Oluşan yeni id, önceki mükelleflere ait değil'''
            break
        else:
            yeni_gelir_gider_id += 1

    # Kullanıcının gireceği bilgileri saklamak için listelerimi tanımladım
    yeni_mukellef = []
    yeni_kisisel_bilgi = []
    yeni_sirket = []
    yeni_ivd = []
    yeni_kontrol = []
    yeni_gelir_gider = []

    # Kullanıcından bilgileri aldım
    ad = input("Ad : ")
    soyad = input("Soyad : ")
    eposta = input("Eposta : ")
    telefon = input("Telefon : ")

    #Oluşturmuş olduğum benzersiz id yi ve kullanıcıdan alınan verileri listeye ekledim. Bu verilerin belirli bir sırası olduğu için, bu işlemleri insert fonksiyonu ile yapmayı tercih ettim
    yeni_mukellef.insert(0, str(yeni_mukellef_id))
    yeni_mukellef.insert(1, ad)
    yeni_mukellef.insert(2, soyad)
    yeni_mukellef.insert(3, eposta)
    yeni_mukellef.insert(4, telefon)
    yeni_mukellef.insert(5, str(yeni_kisisel_bilgi_id))
    yeni_mukellef.insert(6, str(yeni_sirket_id))
    yeni_mukellef.insert(7, str(yeni_kontrol_id))
    yeni_mukellef.insert(8, str(yeni_ivd_id))
    yeni_mukellef.insert(9, str(yeni_gelir_gider_id))

    tckn = input("T.C. Kimlik No : ")
    dogum_tarihi = input("Doğum Tarihi (GG.AA.YY) : ")
    mukellef_olma_tarihi = input("Mükellef olma tarihi (GG.AA.YY) : ")
    terk_transfer_tarihi = input("Terk/Transfer tarihi (GG:AA.YY) : ")
    terk_transfer_nedeni = input("Terk/Transfer Nedeni? : ")

    yeni_kisisel_bilgi.insert(0, str(yeni_kisisel_bilgi_id))
    yeni_kisisel_bilgi.insert(1, tckn)
    yeni_kisisel_bilgi.insert(2, dogum_tarihi)
    yeni_kisisel_bilgi.insert(3, mukellef_olma_tarihi)
    yeni_kisisel_bilgi.insert(4, terk_transfer_tarihi)
    yeni_kisisel_bilgi.insert(5, terk_transfer_nedeni)

    #Burada şirket türü olarak, konsol ekranında kullanıcıya öneriler göstererek kullanıcıyı doğru yönlendirmeye çalışıyorum
    sirket_turu_tamamlamalari = ["Anonim", "Limited", "Kollektif", "Komandit", "Kooperatif"]  # Tamamlama listesi
    sirket_tamamlayici = WordCompleter(sirket_turu_tamamlamalari, ignore_case=True) #ignore_case=True parametresi, büyük-küçük harf duyarlılığını yok sayar

    sirket_turu = prompt("Şirket türü ('Tab tuşuna basarak seçenekleri görüntüleyin'): ", completer=sirket_tamamlayici, lexer=SimpleLexer()) #lexer=SimpleLexer() parametresi sayesinde kullanıcıya önerilen kelimeler türkçe karakteride destekliyor
    faaliyet_adresi = input("Faaliyet adresi : ")
    il = input("İl : ")
    vergi_dairesi = input("Vergi dairesi : ")
    vergi_numarasi = input("Vergi No : ")
    sirket_unvani = input("Şirket Ünvanı : ")
    faaliyet_alani = input("Faaliyet alanı : ")
    calisan_sayisi = input("Çalışan sayısı : ")
    ise_baslama_tarihi = input("İşe başlama tarihi (GG.AA.YY) : ")

    yeni_sirket.insert(0, str(yeni_sirket_id))
    yeni_sirket.insert(1, sirket_turu)
    yeni_sirket.insert(2, faaliyet_adresi)
    yeni_sirket.insert(3, il)
    yeni_sirket.insert(4, vergi_dairesi)
    yeni_sirket.insert(5, vergi_numarasi)
    yeni_sirket.insert(6, sirket_unvani)
    yeni_sirket.insert(7, faaliyet_alani)
    yeni_sirket.insert(8, calisan_sayisi)
    yeni_sirket.insert(9, ise_baslama_tarihi)

    ivd_username = input("IVD Kullanıcı adı : ")
    ivd_password = input("IVD Şifre : ")

    yeni_ivd.insert(0, str(yeni_ivd_id))
    yeni_ivd.insert(1, ivd_username)
    yeni_ivd.insert(2, ivd_password)

    kontrol_tamamlamalari = ["Var", "Yok"]  # Oto. Tamamlama listesi
    kontrol_tamamlayici = WordCompleter(kontrol_tamamlamalari, ignore_case=True)

    vergi_levhasi = prompt("Vergi levhası var mı? (Var/Yok/Tab):", completer=kontrol_tamamlayici)
    sozlesme = prompt("Sözleşmesi var mı? (Var/Yok/Tab) : ", completer=kontrol_tamamlayici)
    yoklama = prompt("Yoklaması var mı? (Var/Yok/Tab) : ", completer=kontrol_tamamlayici)
    defterbeyan = prompt("Defterbeyan var mı? (Var/Yok/Tab) : ", completer=kontrol_tamamlayici)

    yeni_kontrol.insert(0, str(yeni_kontrol_id))
    yeni_kontrol.insert(1, vergi_levhasi)
    yeni_kontrol.insert(2, sozlesme)
    yeni_kontrol.insert(3, yoklama)
    yeni_kontrol.insert(4, defterbeyan)

    gelir = gider = None
    while True: # Mükellefin vergisini hesaplarken, gelir ve gider değerleri üzerinden hesaplama yapacağım için kullanıcıyı sayı girmeye zorluyorum
        try:
            gelir = int(input("Mükellefin toplam gelirini girin : "))
            break
        except:
            print("Lütfen bir sayı giriniz.")
    while True:
        try:
            gider = int(input("Mükellefin toplam giderini girin : "))
            break
        except:
            print("Lütfen bir sayı giriniz.")
    
    yeni_gelir_gider.insert(0, str(yeni_gelir_gider_id))
    yeni_gelir_gider.insert(1, str(gelir))
    yeni_gelir_gider.insert(2, str(gider))

    #Son olarak listelere eklenen bu verileri, satır satır CSV dosyalarını ekledim
    with open("mukellef.csv", 'a', newline='') as yeni_mukellef_ekle, open("kisisel_bilgiler.csv", 'a', newline='') as yeni_kisisel_bilgi_ekle, open("sirket.csv", 'a', newline='') as yeni_sirket_ekle, open("ivd.csv", 'a', newline='') as yeni_ivd_ekle, open("kontrol.csv", 'a', newline='') as yeni_kontrol_ekle, open("gelir_gider.csv", 'a', newline='') as yeni_gelir_gider_ekle:
        yeni_mukellef_ekle.write(";".join(yeni_mukellef))
        yeni_mukellef_ekle.write("\n") #Boş satır eklememin sebebi, dosya birdahaki sefere tekrar açıldığında yeni eklenecek olan verilerin bu oluşan satıra eklenmesi sağlanacak. Yani ileriye dönük bir işlem gerçekleştirmiş oldum

        yeni_kisisel_bilgi_ekle.write(";".join(yeni_kisisel_bilgi))
        yeni_kisisel_bilgi_ekle.write("\n")

        yeni_sirket_ekle.write(";".join(yeni_sirket))
        yeni_sirket_ekle.write("\n")

        yeni_ivd_ekle.write(";".join(yeni_ivd))
        yeni_ivd_ekle.write("\n")

        yeni_kontrol_ekle.write(";".join(yeni_kontrol))
        yeni_kontrol_ekle.write("\n")

        yeni_gelir_gider_ekle.write(";".join(yeni_gelir_gider))
        yeni_gelir_gider_ekle.write("\n")

    print("Mükellef başarıyla eklendi...")
    input("<- Geri [Enter]\n")
    system('cls')

def mukellef_guncelle(mukellef_id = None, kisisel_bilgi_id = None, sirket_id = None, kontrol_id = None, ivd_id = None, gelir_gider_id = None):
    cagiran_cerceve = inspect.currentframe().f_back #Bu fonksiyonun hangi fonksiyon tarafından çalıştırıldığı bilgisini alıyorum
    cagiran_adi = inspect.getframeinfo(cagiran_cerceve).function #Çünkü farklı fonksiyonlar tarafından çağırılabileceğinden, bu fonksiyon işleyişinde de farklılıklar oluşuyor

    mukellefid = kisiselbilgiid = sirketid = kontrolid = ivdid = gelirgiderid = None
    mukellefler = []

    if cagiran_adi == "main": #Eğer fonksiyon main fonksiyonundan çağırılmışsa, mükellefin id değerinden, diğer bilgilerinin id değerlerine ulaşıyorum
        with open("mukellef.csv") as mukellef:
            mukellef_okuyucu = csv.reader(mukellef, delimiter=";")
            #CSV dosyasından okumuş olduğum veriyi listeye aktardım
            for row in mukellef_okuyucu:
                mukellefler.append(row)

        while True:
            mukellefid = input("Güncellemek istediğiniz mükellefin ID değerini girin : ")

            # Filtreleme işlemi
            filtrelenmis_mukellef = [satir for satir in mukellefler if satir[0] == str(mukellefid)]  #Mükellef id si mukellefid ye eşit olanı getir
            bulundu = bool(filtrelenmis_mukellef) #Eğer liste doluysa True, boşsa False

            if bulundu:
                #Güncellenecek mükellefe ait id değerlerini alıyorum
                kisiselbilgiid = filtrelenmis_mukellef[0][5]
                sirketid = filtrelenmis_mukellef[0][6]
                kontrolid = filtrelenmis_mukellef[0][7]
                ivdid = filtrelenmis_mukellef[0][8]
                gelirgiderid = filtrelenmis_mukellef[0][9]
                break
            else:
                print("Bu ID değerine sahip bir mükellef bulunmamaktadır.")
    else:
        # Eğer bu fonksiyon, main fonksiyonundan farklı bir fonksiyondan çağırılmış ise, id değerleri zaten parametre olarak gönderiliyor
        mukellefid = mukellef_id
        kisiselbilgiid = kisisel_bilgi_id
        sirketid = sirket_id
        kontrolid = kontrol_id
        ivdid = ivd_id
        gelirgiderid = gelir_gider_id

    guncellenen_veri = []

    while True:
        guncelleme_turu = int(input('''
        1- Mükellef Bilgisi
        2- Kişisel Bilgi
        3- Şirket Bilgisi
        4- Kontrol Bilgisi
        5- İVD Hesap Bilgisi
        6- Gelir Gider Bilgisi
        
        Mükellefin hangi bilgisini güncellemek istiyorsunuz : '''))

        if guncelleme_turu == 1:
            with open("mukellef.csv", 'r', encoding="utf-8") as mukellef:
                csv_okuyucu = csv.DictReader(mukellef, delimiter=";")
                alanlar = csv_okuyucu.fieldnames # CSV dosyasınındaki sütunların başlık isimlerini alıp liste haline getirdim
                '''
                    Burada farkettiğim bir sorun; pythonun csv modülünün fieldnames fonksiyonu, büyük Ş harfini decode edemiyor.
                    Bu yüzden csv dosyalarının sütun-başlık isimlerinde büyük Ş harfini kullanamadım
                '''
                sutun_tamamlayici =  WordCompleter(alanlar, ignore_case=True) # Bu başlık isimlerini kullanıcıya öneriyorum
                
                while True:
                    guncellenecek_sutun = prompt("Hangi sütunu güncellemek istiyorsunuz ('Tab' tuşuna basarak seçenekleri görüntüleyin): ", completer=sutun_tamamlayici, lexer=SimpleLexer())
                    if guncellenecek_sutun in alanlar: #Eğer kullanıcının belirttiği sütun ismi csv dosyasındaki sütun ismi ile eşleşiyorsa
                        yeni_deger = input("Yeni değer : ")
                    
                        for satir in csv_okuyucu:
                            if satir["id"] == mukellefid:
                                satir[guncellenecek_sutun] = yeni_deger
                            guncellenen_veri.append(satir)
                        break
                    else:
                        print("Böyle bir sütun ismi yok.")
        
            with open("mukellef.csv", 'w', newline='', encoding="utf-8") as dosya:
                csv_yazici = csv.DictWriter(dosya, fieldnames=alanlar, delimiter=";")
                csv_yazici.writeheader()
                csv_yazici.writerows(guncellenen_veri)
        
            print("Mükellef başarıyla güncellendi!")
            break
        elif guncelleme_turu == 2:
            with open("kisisel_bilgiler.csv", 'r', encoding="utf-8") as kisiselbilgiler:
                csv_okuyucu = csv.DictReader(kisiselbilgiler, delimiter=";")
                alanlar = csv_okuyucu.fieldnames # CSV dosyasınındaki sütunların başlık isimlerini alıp liste haline getirdim
                
                sutun_tamamlayici =  WordCompleter(alanlar, ignore_case=True) # Bu başlık isimlerini kullanıcıya öneriyorum
                
                while True:
                    guncellenecek_sutun = prompt("Hangi sütunu güncellemek istiyorsunuz ('Tab' tuşuna basarak seçenekleri görüntüleyin): ", completer=sutun_tamamlayici, lexer=SimpleLexer())
                    if guncellenecek_sutun in alanlar:
                        yeni_deger = input("Yeni değer : ")
                    
                        for satir in csv_okuyucu:
                            if satir["id"] == kisiselbilgiid:
                                satir[guncellenecek_sutun] = yeni_deger
                            guncellenen_veri.append(satir)
                        break
                    else:
                        print("Böyle bir sütun ismi yok.")
        
            with open("kisisel_bilgiler.csv", 'w', newline='', encoding="utf-8") as dosya:
                csv_yazici = csv.DictWriter(dosya, fieldnames=alanlar, delimiter=";")
                csv_yazici.writeheader()
                csv_yazici.writerows(guncellenen_veri)
        
            print("Mükellef başarıyla güncellendi!")
            break
        elif guncelleme_turu == 3:
            with open("sirket.csv", 'r', encoding="utf-8") as sirketbilgileri:
                csv_okuyucu = csv.DictReader(sirketbilgileri, delimiter=";")
                alanlar = csv_okuyucu.fieldnames # CSV dosyasınındaki sütunların başlık isimlerini alıp liste haline getirdim

                sutun_tamamlayici =  WordCompleter(alanlar, ignore_case=True) # Bu başlık isimlerini kullanıcıya öneriyorum
                while True:
                    guncellenecek_sutun = prompt("Hangi sütunu güncellemek istiyorsunuz ('Tab' tuşuna basarak seçenekleri görüntüleyin): ", completer=sutun_tamamlayici, lexer=SimpleLexer())
                    if guncellenecek_sutun in alanlar:
                        yeni_deger = input("Yeni değer : ")
                    
                        for satir in csv_okuyucu:
                            if satir["id"] == sirketid:
                                satir[guncellenecek_sutun] = yeni_deger
                            guncellenen_veri.append(satir)
                        break
                    else:
                        print("Böyle bir sütun ismi yok.")
        
            with open("sirket.csv", 'w', newline='', encoding="utf-8") as dosya:
                csv_yazici = csv.DictWriter(dosya, fieldnames=alanlar, delimiter=";")
                csv_yazici.writeheader()
                csv_yazici.writerows(guncellenen_veri)
        
            print("Mükellef başarıyla güncellendi!")
            break
        elif guncelleme_turu == 4:
            with open("kontrol.csv", 'r', encoding="utf-8") as kontrolbilgileri:
                csv_okuyucu = csv.DictReader(kontrolbilgileri, delimiter=";")
                alanlar = csv_okuyucu.fieldnames # CSV dosyasınındaki sütunların başlık isimlerini alıp liste haline getirdim

                sutun_tamamlayici =  WordCompleter(alanlar, ignore_case=True) # Bu başlık isimlerini kullanıcıya öneriyorum
                
                while True:
                    guncellenecek_sutun = prompt("Hangi sütunu güncellemek istiyorsunuz ('Tab' tuşuna basarak seçenekleri görüntüleyin): ", completer=sutun_tamamlayici, lexer=SimpleLexer())
                    if guncellenecek_sutun in alanlar:
                        yeni_deger = input("Yeni değer : ")
                    
                        for satir in csv_okuyucu:
                            if satir["id"] == kontrolid:
                                satir[guncellenecek_sutun] = yeni_deger
                            guncellenen_veri.append(satir)
                        break
                    else:
                        print("Böyle bir sütun ismi yok.")
        
            with open("kontrol.csv", 'w', newline='', encoding="utf-8") as dosya:
                csv_yazici = csv.DictWriter(dosya, fieldnames=alanlar, delimiter=";")
                csv_yazici.writeheader()
                csv_yazici.writerows(guncellenen_veri)
        
            print("Mükellef başarıyla güncellendi!")
            break
        elif guncelleme_turu == 5:
            with open("ivd.csv", 'r', encoding="utf-8") as ivdbilgileri:
                csv_okuyucu = csv.DictReader(ivdbilgileri, delimiter=";")
                alanlar = csv_okuyucu.fieldnames # CSV dosyasınındaki sütunların başlık isimlerini alıp liste haline getirdim

                sutun_tamamlayici =  WordCompleter(alanlar, ignore_case=True) # Bu başlık isimlerini kullanıcıya öneriyorum
                
                while True:
                    guncellenecek_sutun = prompt("Hangi sütunu güncellemek istiyorsunuz ('Tab' tuşuna basarak seçenekleri görüntüleyin): ", completer=sutun_tamamlayici, lexer=SimpleLexer())
                    if guncellenecek_sutun in alanlar:
                        yeni_deger = input("Yeni değer : ")
                    
                        for satir in csv_okuyucu:
                            if satir["id"] == ivdid:
                                satir[guncellenecek_sutun] = yeni_deger
                            guncellenen_veri.append(satir)
                        break
                    else:
                        print("Böyle bir sütun ismi yok.")
        
            with open("ivd.csv", 'w', newline='', encoding="utf-8") as dosya:
                csv_yazici = csv.DictWriter(dosya, fieldnames=alanlar, delimiter=";")
                csv_yazici.writeheader()
                csv_yazici.writerows(guncellenen_veri)
        
            print("Mükellef başarıyla güncellendi!")
            break
        elif guncelleme_turu == 6:
            with open("gelir_gider.csv", 'r', encoding="utf-8") as gelirgiderbilgileri:
                csv_okuyucu = csv.DictReader(gelirgiderbilgileri, delimiter=";")
                alanlar = csv_okuyucu.fieldnames # CSV dosyasınındaki sütunların başlık isimlerini alıp liste haline getirdim

                sutun_tamamlayici =  WordCompleter(alanlar, ignore_case=True) # Bu başlık isimlerini kullanıcıya öneriyorum
                
                while True:
                    guncellenecek_sutun = prompt("Hangi sütunu güncellemek istiyorsunuz ('Tab' tuşuna basarak seçenekleri görüntüleyin): ", completer=sutun_tamamlayici, lexer=SimpleLexer())
                    if guncellenecek_sutun in alanlar:
                        while True: #Burada kullanıcıyı sayı girmeye zorluyorum çünkü vergi hesaplaması yaparken gelir ve gider değerlerinin sayı olmasına ihtiyacım var
                            try:
                                yeni_deger = int(input("Yeni değer : "))
                                break
                            except ValueError:
                                print("Lütfen bir sayı giriniz.")

                        for satir in csv_okuyucu:
                            if satir["id"] == gelirgiderid:
                                satir[guncellenecek_sutun] = str(yeni_deger)
                            guncellenen_veri.append(satir)
                        break
                    else:
                        print("Böyle bir sütun ismi yok.")
        
            with open("gelir_gider.csv", 'w', newline='', encoding="utf-8") as dosya:
                csv_yazici = csv.DictWriter(dosya, fieldnames=alanlar, delimiter=";")
                csv_yazici.writeheader()
                csv_yazici.writerows(guncellenen_veri)
        
            print("Mükellef başarıyla güncellendi!")
            break
        else:
            print("Geçersiz seçim.")
    
    input("Devam etmek için Enter'a basın\n")
    detayli_mukellef_listele(mukellefid)

def mukellef_sil(mukellef_id = None, kisisel_bilgi_id = None, sirket_id = None, kontrol_id = None, ivd_id = None, gelir_gider_id = None):
    cagiran_cerceve = inspect.currentframe().f_back #Bu fonksiyonun hangi fonksiyon tarafından çalıştırıldığı bilgisini alıyorum
    cagiran_adi = inspect.getframeinfo(cagiran_cerceve).function #Çünkü farklı fonksiyonlar tarafından çağırılabileceğinden, bu fonksiyon işleyişinde de farklılıklar oluşuyor

    mukellefid = kisiselbilgiid = sirketid = kontrolid = ivdid = gelirgiderid = None
    mukellefler = []
    kisisel_bilgiler = []
    sirketler = []
    kontroller = []
    ivdler = []
    gelirgiderler = []

    with open("mukellef.csv") as mukellef, open("kisisel_bilgiler.csv") as kisiselbilgi, open("sirket.csv") as sirket, open("kontrol.csv") as kontrol, open("ivd.csv") as ivd, open("gelir_gider.csv") as gelirgider:
            mukellef_okuyucu = csv.reader(mukellef, delimiter=";")
            kisiselbilgi_okuyucu = csv.reader(kisiselbilgi, delimiter=";")
            sirket_okuyucu = csv.reader(sirket, delimiter=";")
            kontrol_okuyucu = csv.reader(kontrol, delimiter=";")
            ivd_okuyucu = csv.reader(ivd, delimiter=";")
            gelirgider_okuyucu = csv.reader(gelirgider, delimiter=";")

            #CSV dosyasından okumuş olduğum verileri listelere aktardım
            for row in mukellef_okuyucu:
                mukellefler.append(row)
            for row in kisiselbilgi_okuyucu:
                kisisel_bilgiler.append(row)
            for row in sirket_okuyucu:
                sirketler.append(row)
            for row in kontrol_okuyucu:
                kontroller.append(row)
            for row in ivd_okuyucu:
                ivdler.append(row)
            for row in gelirgider_okuyucu:
                gelirgiderler.append(row)

    if cagiran_adi == "main": #Eğer fonksiyon main fonksiyonundan çağırılmışsa, mükellefin id değerinden, diğer bilgilerinin id değerlerine ulaşıyorum
        while True:
            mukellefid = input("Silmek istediğiniz mükellefin ID değerini girin : ")

            # Filtreleme işlemi
            filtrelenmis_mukellef = [satir for satir in mukellefler if satir[0] == str(mukellefid)]  #Mükellef id si mukellefid ye eşit olanı getir
            bulundu = bool(filtrelenmis_mukellef) #Eğer liste doluysa True, boşsa False

            if bulundu:
                #Silincek mükellefe ait diğer id değerlerini alıyorum
                kisiselbilgiid = filtrelenmis_mukellef[0][5]
                sirketid = filtrelenmis_mukellef[0][6]
                kontrolid = filtrelenmis_mukellef[0][7]
                ivdid = filtrelenmis_mukellef[0][8]
                gelirgiderid = filtrelenmis_mukellef[0][9]
                break
            else:
                print("Bu ID değerine sahip bir mükellef bulunmamaktadır.")
    else:
        # Eğer bu fonksiyon, main fonksiyonundan farklı bir fonksiyondan çağırılmış ise, id değerleri zaten parametre olarak gönderiliyor
        mukellefid = mukellef_id
        kisiselbilgiid = kisisel_bilgi_id
        sirketid = sirket_id
        kontrolid = kontrol_id
        ivdid = ivd_id
        gelirgiderid = gelir_gider_id

    for satir in mukellefler:
        if satir[0] == str(mukellefid): # Mükellefler listesinin içinde, id değeri mukellefid değerine eşit olanı listeden çıkarıyorum
            mukellefler.remove(satir)
    for satir in kisisel_bilgiler:      # Aynı işlemleri, ilgili mükellefe ait bilgilerin saklandığı diğer dosyalardada yapıyorum.
        if satir[0] == str(kisiselbilgiid): # Çünkü dosyalar arasında id değerine göre ilişkisel bir bağlantı var. Yani bir mükellef silindiyse, o mükellefe ait diğer bilgileri de siliyorum
            kisisel_bilgiler.remove(satir)
    for satir in sirketler:
        if satir[0] == str(sirketid):
            sirketler.remove(satir)
    for satir in kontroller:
        if satir[0] == str(kontrolid):
            kontroller.remove(satir)
    for satir in ivdler:
        if satir[0] == str(ivdid):
            ivdler.remove(satir)
    for satir in gelirgiderler:
        if satir[0] == str(gelirgiderid):
            gelirgiderler.remove(satir)
    
    # Son olarak silinmesi istenen mükellef listelerden çıkarıldıktan sonra, listelerin son güncel halini sıfırdan CSV dosyalarına yazıyorum
    with open("mukellef.csv", 'w', newline='') as mukellef_yaz, open("kisisel_bilgiler.csv", 'w', newline='') as kisisel_bilgi_yaz, open("sirket.csv", 'w', newline='') as sirket_yaz, open("kontrol.csv", 'w', newline='') as kontrol_yaz, open("ivd.csv", 'w', newline='') as ivd_yaz, open("gelir_gider.csv", 'w', newline='') as gelir_gider_yaz:
        mukellef_yazici = csv.writer(mukellef_yaz, delimiter=";")
        mukellef_yazici.writerows(mukellefler)

        kisisel_bilgi_yazici = csv.writer(kisisel_bilgi_yaz, delimiter=";")
        kisisel_bilgi_yazici.writerows(kisisel_bilgiler)

        sirket_yazici = csv.writer(sirket_yaz, delimiter=";")
        sirket_yazici.writerows(sirketler)

        kontrol_yazici = csv.writer(kontrol_yaz, delimiter=";")
        kontrol_yazici.writerows(kontroller)

        ivd_yazici = csv.writer(ivd_yaz, delimiter=";")
        ivd_yazici.writerows(ivdler)

        gelir_gider_yazici = csv.writer(gelir_gider_yaz, delimiter=";")
        gelir_gider_yazici.writerows(gelirgiderler)

    print("Mükellef başarıyla silindi!")
    input("Devam etmek için Enter'a basın\n")
    system('cls')

def mukellef_ara():
    aranan_deger = input("Aramak istediğiniz mükellefe ait değer girin (ad/soyad/email/telefon): ")

    bulunan_satirlar = []
    with open("mukellef.csv", 'r') as dosya:
        okuyucu = csv.reader(dosya, delimiter=";")
        for satir in okuyucu:
            for deger in satir:
                if aranan_deger in deger:
                    bulunan_satirlar.append(satir)
                    break

    if len(bulunan_satirlar) > 0:
        secilen_veriler = [[row[i] for i in [0, 1, 2, 3, 4]] for row in bulunan_satirlar] # Csv dosyasındaki bulunan satırı, tüm sütunlarıyla yazdırmıyorum
        print("Arama sonuçları: \n")
        
        tablo = tabulate(secilen_veriler, headers=["id", "ad", "soyad", "email", "telefon"])
        print(tablo, "\n")
        print_menu(1)
        secim = int(input("Seçiminizi girin : "))
        
        if secim == 1:
            mukellefid = input("Detaylı görüntülemek istediğiniz mükellefin id değerini girin : ")
            detayli_mukellef_listele(mukellefid)
        elif secim == 2:
            pass
    else:
        print("Aranan değer bulunamadı.")
        input("Devam etmek için Enter'a basın")
    system('cls')

def vergi_hesapla(mukellef_id = None, sirket_id = None,  gelir_gider_id = None):
    cagiran_cerceve = inspect.currentframe().f_back #Bu fonksiyonun hangi fonksiyon tarafından çalıştırıldığı bilgisini alıyorum
    cagiran_adi = inspect.getframeinfo(cagiran_cerceve).function #Çünkü farklı fonksiyonlar tarafından çağırılabileceğinden, bu fonksiyon işleyişinde de farklılıklar oluşuyor

    mukellefid = sirketid = gelirgiderid = None
    mukellefler = []
    sirketler = []
    gelirgiderler = []

    with open("mukellef.csv") as mukellef, open("sirket.csv") as sirket, open("gelir_gider.csv") as gelirgider:
            mukellef_okuyucu = csv.reader(mukellef, delimiter=";")
            sirket_okuyucu = csv.reader(sirket, delimiter=";")
            gelirgider_okuyucu = csv.reader(gelirgider, delimiter=";")

            #CSV dosyasından okumuş olduğum verileri listelere aktardım
            for row in mukellef_okuyucu:
                mukellefler.append(row)
            for row in sirket_okuyucu:
                sirketler.append(row)
            for row in gelirgider_okuyucu:
                gelirgiderler.append(row)

    if cagiran_adi == "main": #Eğer fonksiyon main fonksiyonundan çağırılmışsa, mükellefin id değerinden, diğer bilgilerinin id değerlerine ulaşıyorum
        while True:
            mukellefid = input("Vergisini hesaplamak istediğiniz mükellefin id değerini girin : ")

            # Filtreleme işlemi
            filtrelenmis_mukellef = [satir for satir in mukellefler if satir[0] == str(mukellefid)]  #Mükellef id si mukellefid ye eşit olanı getir
            bulundu = bool(filtrelenmis_mukellef) #Eğer liste doluysa True, boşsa False

            if bulundu:
                #Vergisi hesaplanacak mükellefe ait diğer id değerlerini alıyorum
                sirketid = filtrelenmis_mukellef[0][6]
                gelirgiderid = filtrelenmis_mukellef[0][9]
                ad = filtrelenmis_mukellef[0][1]
                soyad = filtrelenmis_mukellef[0][2]
                break
            else:
                print("Bu ID değerine sahip bir mükellef bulunmamaktadır.")
    else:
        # Eğer bu fonksiyon, main fonksiyonundan farklı bir fonksiyondan çağırılmış ise, id değerleri zaten parametre olarak gönderiliyor
        mukellefid = mukellef_id
        sirketid = sirket_id
        gelirgiderid = gelir_gider_id
    
    sirket = [satir for satir in sirketler if satir[0] == str(sirketid)]
    calisan_sayisi = int(sirket[0][8])

    gelirgider = [satir for satir in gelirgiderler if satir[0] == str(gelirgiderid)]
    gelir = int(gelirgider[0][1])
    gider = int(gelirgider[0][2])

    vergi = 0
    damga_vergisi = 144.40
    muhtasar_beyanname_vergisi = 230.70
    katma_deger_vergisi = gelir * 0.18
    gecici_vergi = gelir * 0.15

    if calisan_sayisi > 0 or not None: #Eğer iş yerinde çalışan işçi varsa, o iş yeri muhtasar beyanname verigisini ödemekle mükelleftir.
        vergi += muhtasar_beyanname_vergisi
    if gelir > gider: # Eğer işyerinin geliri giderinden yüksekse o işyeri katma değer vergisini ödemekle mükelleftir.
        vergi += katma_deger_vergisi

    vergi += damga_vergisi + gecici_vergi

    if cagiran_adi == "main":
        print("{} {} isimli mükellefin ödemesi gereken toplam vergi tutarı : {} TL".format(ad, soyad, vergi))
        input("Devam etmek için Enter'a basın")
    else:
        print("Mükellefin ödemesi gereken vergi tutarı : {} TL".format(vergi))
        input("Devam etmek için Enter'a basın")
        detayli_mukellef_listele(mukellefid)
    
if __name__=='__main__': #Programın doğrudan çalıştırılıp çalıştırılmadığını anlamak için __name__ özelliğinin değerini kontrol ettim
    main()
