Metehan Özdeniz - 22100011083

#
# Algoritma ve Programlama - 2 Dersi Final Projesi

# Konu

Bir mali müşavir, sahip olduğu mükelleflerinin bilgilerini bu otomasyon programında tutmaktadır. Ayrıca bu mükelleflerin vergi hesaplama işlemleri de bu programda yapılmaktadır.

# Vergi Hesaplama

## Damga Vergisi

Damga vergisi 144,40 TL olarak belirlenmiştir. Her ay düzenli olarak verilmelidir.

## Muhtasar Beyanname

Muhtasar Beyanname vergisi 230,70 TL olarak belirlenmiştir. Ancak İşyerinde çalışan bir işçi yoksa o işyeri muhtasar beyannameden muaf tutulacaktır.

## Katma Değer Vergisi

İş yerinin toplam gelirinin %18 kadarıdır. Ancak işyerinin geliri, giderinden düşük ise o işyeri katma değer vergisinden muaf tutulacaktır.

## Geçici Vergi

Geçici vergi sabittir ve her ay düzenli olarak verilmelidir. İşyerinin o ayki gelirinin %15 kadarıdır.

# Yapı

Bu otomasyon programı bilgileri csv formatındaki dosyalarda saklamaktadır. Bu csv dosyaları arasında ilişkisel bir bağlantı vardır. Bu dosyalar arasındaki ilişkisel bağlantı Resim 1'deki gibidir.

![](RackMultipart20230524-1-a1cg25_html_f038195229558dc9.png)

_Resim 1 Diagram_

Programdaki bütün fonksiyonlar, main isimli bir temel fonksiyon üzerinden kontrol edilmektedir. Listeleme, ekleme, güncelleme, arama, silme ve vergi hesaplama işlemleri de ayrı ayrı fonksiyonlarda yapılmıştır.

# Gereksinimler

Bu proje Python dili ile yazılmış olup, Python 3.11.2 sürümü kullanılmıştır. Sistemde Python 3.11.2 sürümünün kurulu olması gerekmektedir.

Gerekli modüller proje dizininde bulunan lib klasöründe verilmiştir. Lib klasörüne erişimin kaybedilmesi durumunda konsol ekranında aşağıdaki komutlar çalıştırılarak sisteme ilgili modüller yüklenmelidir.

_pip install tabulate_

_Bu modül (tabulate); csv dosyalarındaki verilerin konsol ekranında kullanıcıya düzenli bir şekilde ve tablo halinde sunulması için kullanılmıştır._

_pip install prompt\_toolkit_

Bu modül (prompt\_toolkit); Kullanıcı konsol ekranında veri girerken, girdiği verileri otomatik olarak tamamlaması ve kullanıcıya öneriler sunulması için kullanılmıştır.
