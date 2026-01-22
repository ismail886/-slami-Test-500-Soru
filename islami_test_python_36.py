import tkinter as tk
from tkinter import ttk, messagebox
import sys
from datetime import datetime


# ------------------ 100 SORU (10 TEST) ------------------

all_questions = [
    # TEST 1 (1-10)
    {"q": "1. Allah'ın var ve bir olmasına, ortağı bulunmamasına ne ad verilir?", "a": ["Tevhid", "Nübüvvet", "Ahiret", "Haşir"], "c": 0},
    {"q": "2. Aşağıdakilerden hangisi imanın şartlarından biri değildir?", "a": ["Meleklere inanmak", "Namaz kılmak", "Peygamberlere inanmak", "Kitaplara inanmak"], "c": 1},
    {"q": "3. İlahi kitaplardan Zebur hangi peygambere indirilmiştir?", "a": ["Hz. Musa", "Hz. İsa", "Hz. Davud", "Hz. İbrahim"], "c": 2},
    {"q": "4. Öldükten sonra dirilip Allah'ın huzurunda toplanmaya ne ad verilir?", "a": ["Mizan", "Berzah", "Haşir", "Kıyamet"], "c": 2},
    {"q": "5. Vahiy getirmekle görevli melek hangisidir?", "a": ["Mikail", "Azrail", "İsrafil", "Cebrail"], "c": 3},
    {"q": "6. Namazın içindeki farzlardan olan, namaza başlarken alınan tekbire ne denir?", "a": ["İftitah Tekbiri", "Kıyam", "Ka'de-i Ahire", "Secde"], "c": 0},
    {"q": "7. Günde kaç vakit namaz kılmak farzdır?", "a": ["3", "5", "7", "2"], "c": 1},
    {"q": "8. Namazda rükudan sonra alnı yere koyarak yapılan harekete ne denir?", "a": ["Kıraat", "Secde", "Teşehhüd", "Selam"], "c": 1},
    {"q": "9. Hangi namazın cemaatle kılınması zorunludur?", "a": ["Teravih", "Bayram", "Cuma", "Vitir"], "c": 2},
    {"q": "10. Oruç tutmaya güç yetiremeyen yaşlıların veya iyileşme ümidi olmayan hastaların verdiği maddi bedele ne denir?", "a": ["Zekat", "Sadaka", "Fidye", "Fitre"], "c": 2},
    
    # TEST 2 (11-20)
    {"q": "11. Teyemmüm abdesti ne ile alınır?", "a": ["Su", "Kağıt", "Toprak", "Kumaş"], "c": 2},
    {"q": "12. Haccın farzlarından biri olan ve Kabe'nin etrafında 7 kez dönmeye ne denir?", "a": ["Say", "İhram", "Vakfe", "Tavaf"], "c": 3},
    {"q": "13. Zekat verebilmek için sahip olunması gereken asgari zenginlik ölçüsüne ne denir?", "a": ["Nisap", "Miktar", "Öşür", "Fitre"], "c": 0},
    {"q": "14. Peygamberimiz hangi şehirde doğmuştur?", "a": ["Medine", "Kudüs", "Mekke", "Taif"], "c": 2},
    {"q": "15. Peygamberimize ilk vahiy nerede gelmiştir?", "a": ["Sevr Mağarası", "Hira Mağarası", "Mescid-i Nebevi", "Kabe"], "c": 1},
    {"q": "16. Müslümanların ilk hicret ettiği yer neresidir?", "a": ["Habeşistan", "Medine", "Mısır", "Bağdat"], "c": 0},
    {"q": "17. Peygamberimizin Medine'ye hicret ederken yanındaki yol arkadaşı kimdir?", "a": ["Hz. Ömer", "Hz. Ali", "Hz. Ebubekir", "Hz. Osman"], "c": 2},
    {"q": "18. Müslümanlar ile Mekkeli müşrikler arasındaki ilk büyük savaş hangisidir?", "a": ["Uhud", "Hendek", "Bedir", "Hayber"], "c": 2},
    {"q": "19. Peygamberimizin vefat ettiği şehir hangisidir?", "a": ["Mekke", "Cidde", "Şam", "Medine"], "c": 3},
    {"q": "20. Kur'an-ı Kerim'de kaç cüz vardır?", "a": ["20", "30", "40", "114"], "c": 1},
    
    # TEST 3 (21-30)
    {"q": "21. Kur'an-ı Kerim'in ilk suresi hangisidir?", "a": ["Bakara", "İhlas", "Fatiha", "Nas"], "c": 2},
    {"q": "22. Kur'an-ı Kerim'in en kısa suresi hangisidir?", "a": ["Kevser", "Fil", "Maun", "Kureyş"], "c": 0},
    {"q": "23. Hangi surenin başında Besmele bulunmaz?", "a": ["Yasin", "Tevbe", "Rahman", "Mülk"], "c": 1},
    {"q": "24. Kur'an-ı Kerim yaklaşık kaç yılda tamamlanmıştır?", "a": ["10", "23", "40", "63"], "c": 1},
    {"q": "25. Kur'an-ı Kerim'i ezberleyen kişiye ne ad verilir?", "a": ["Müezzin", "İmam", "Hafız", "Alim"], "c": 2},
    {"q": "26. Doğa olaylarını ve rızıkları yönetmekle görevli melek hangisidir?", "a": ["Cebrail", "Mikail", "Azrail", "İsrafil"], "c": 1},
    {"q": "27. Allah'ın her şeyi işitmesi sıfatına ne ad verilir?", "a": ["İlim", "Semi", "Basar", "Kudret"], "c": 1},
    {"q": "28. Peygamberlerin akıllı ve zeki olmaları sıfatına ne denir?", "a": ["Sıdk", "Emanet", "Fetanet", "Tebliğ"], "c": 2},
    {"q": "29. Kur'an-ı Kerim'in her 20 sayfalık bölümüne ne ad verilir?", "a": ["Sure", "Ayet", "Cüz", "Hizb"], "c": 3},
    {"q": "30. Kabe'yi Hz. İbrahim ile birlikte inşa eden oğlu kimdir?", "a": ["Hz. İshak", "Hz. İsmail", "Hz. Yakup", "Hz. Yusuf"], "c": 1},
    
    # TEST 4 (31-40)
    {"q": "31. İslam'ın beş şartından hangisi sadece zenginlere farzdır?", "a": ["Namaz", "Oruç", "Kelime-i Şehadet", "Zekat"], "c": 3},
    {"q": "32. Sabah namazı kaç rekattır?", "a": ["2", "4", "6", "10"], "c": 0},
    {"q": "33. Peygamberimizin kabrinin bulunduğu yere ne ad verilir?", "a": ["Makam-ı İbrahim", "Ravza-i Mutahhara", "Altınoluk", "Hacerü'l Esved"], "c": 1},
    {"q": "34. Ramazan ayında yatsı namazından sonra kılınan sünnet namaz hangisidir?", "a": ["Teheccüd", "İşrak", "Teravih", "Evvabin"], "c": 2},
    {"q": "35. Allah'ın emriyle can almakla görevli melek hangisidir?", "a": ["Azrail", "Mikail", "Münker", "Nekir"], "c": 0},
    {"q": "36. Peygamberimizin dedesinin adı nedir?", "a": ["Ebu Talip", "Abdülmuttalip", "Abdullah", "Hamza"], "c": 1},
    {"q": "37. İslam tarihinde ilk ezanı okuyan sahabe kimdir?", "a": ["Hz. Ebubekir", "Hz. Ali", "Bilal-i Habeşi", "Zeyd bin Sabit"], "c": 2},
    {"q": "38. Mekke'den Medine'ye göç eden Müslümanlara ne ad verilir?", "a": ["Ensar", "Muhacir", "Mürted", "Münafık"], "c": 1},
    {"q": "39. Medineli olup Mekkeli Müslümanlara yardım edenlere ne denir?", "a": ["Ensar", "Muhacir", "Tabiun", "Sahabe"], "c": 0},
    {"q": "40. Kur'an'ın 'kalbi' olarak bilinen sure hangisidir?", "a": ["Bakara", "Yasin", "Mülk", "Fetih"], "c": 1},
    
    # TEST 5 (41-50)
    {"q": "41. Aşağıdakilerden hangisi Peygamberimizin çocuklarından biri değildir?", "a": ["Zeynep", "Ümmü Gülsüm", "Safiye", "Rukiye"], "c": 2},
    {"q": "42. Ramazan Bayramı'nda verilen vacip olan sadakaya ne denir?", "a": ["Fidye", "Fitre (Fıtır Sadakası)", "Öşür", "Haraç"], "c": 1},
    {"q": "43. Müslümanların kıblesi olan Kabe hangi şehirdedir?", "a": ["Medine", "Cidde", "Mekke", "Riyad"], "c": 2},
    {"q": "44. Allah'ın her şeye gücünün yetmesi sıfatına ne ad verilir?", "a": ["İlim", "Kudret", "İrade", "Tekvin"], "c": 1},
    {"q": "45. 'El-Emin' (Güvenilir) lakabı kime verilmiştir?", "a": ["Hz. Ebubekir", "Hz. Ömer", "Hz. Muhammed (s.a.v)", "Hz. Süleyman"], "c": 2},
    {"q": "46. Her işe başlarken söylediğimiz 'Bismillahirrahmanirrahim'in anlamı nedir?", "a": ["Allah en büyüktür", "Rahman ve Rahim olan Allah'ın adıyla", "Hamd Allah'adır", "Allah birdir"], "c": 1},
    {"q": "47. Bir Müslümanın başka bir Müslüman üzerindeki haklarından biri nedir?", "a": ["Selamını almak", "Malını almak", "Sırrını ifşa etmek", "Onu eleştirmek"], "c": 0},
    {"q": "48. Peygamberimizin ilk eşi kimdir?", "a": ["Hz. Ayşe", "Hz. Hafsa", "Hz. Hatice", "Hz. Sevde"], "c": 2},
    {"q": "49. Amellerin tartılacağı teraziye ne ad verilir?", "a": ["Sırat", "Mizan", "Mahşer", "Berzah"], "c": 1},
    {"q": "50. İslam'ın temel kaynağı nedir?", "a": ["Hadis kitapları", "İlmihal", "Kur'an-ı Kerim", "Fıkıh kitapları"], "c": 2},
    
    # TEST 6 (51-60)
    {"q": "51. Allah'ın her şeyi önceden bilip planlamasına ne denir?", "a": ["Kaza", "Kader", "Tevekkül", "İrade"], "c": 1},
    {"q": "52. Peygamberlerin Allah'tan aldıkları mesajları insanlara eksiksiz bildirmesine ne denir?", "a": ["Tebliğ", "Emanet", "Sıdk", "İsmet"], "c": 0},
    {"q": "53. Aşağıdakilerden hangisi 'Ulu'l-Azm' peygamberlerden biri değildir?", "a": ["Hz. Nuh", "Hz. İbrahim", "Hz. Adem", "Hz. İsa"], "c": 2},
    {"q": "54. Hz. Muhammed (s.a.v.) kaç yaşında peygamber olmuştur?", "a": ["25", "33", "40", "63"], "c": 2},
    {"q": "55. Namazda Kur'an-ı Kerim okumaya ne ad verilir?", "a": ["Kıyam", "Kıraat", "Tekbir", "Tahiyyat"], "c": 1},
    {"q": "56. Ölen bir Müslümanın ardından kılınan ve rükusu, secdesi olmayan namaz hangisidir?", "a": ["Vitir Namazı", "Cenaze Namazı", "Küsuf Namazı", "İstiska Namazı"], "c": 1},
    {"q": "57. Kur'an-ı Kerim'in en uzun ayeti olan 'Müdayene' (Borçlanma) ayeti hangi surededir?", "a": ["Bakara", "Nisa", "Maide", "Araf"], "c": 0},
    {"q": "58. İslam'da ilk cuma namazı nerede kılınmıştır?", "a": ["Kabe'de", "Mescid-i Nebevi'de", "Ranuna Vadisi'nde", "Kuba Mescidi'nde"], "c": 2},
    {"q": "59. İslam dinine göre 'Büyük Günahlar' (Kebair) arasında ilk sırada hangisi yer alır?", "a": ["Yalan söylemek", "Allah'a ortak koşmak (Şirk)", "Gıybet etmek", "İsraf etmek"], "c": 1},
    {"q": "60. Hz. Yusuf'un babası olan peygamber kimdir?", "a": ["Hz. Yakup", "Hz. İshak", "Hz. Yahya", "Hz. Zekeriya"], "c": 0},
    
    # TEST 7 (61-70)
    {"q": "61. Allah'ın her an her şeyi yaratmaya devam etmesi sıfatına ne ad verilir?", "a": ["Tekvin", "Bekâ", "Kıyam bi-nefsihi", "Vahdaniyet"], "c": 0},
    {"q": "62. Oruçlu bir kimsenin hataen bir şey yemesi orucu bozar mı?", "a": ["Evet, kaza gerekir", "Evet, kefaret gerekir", "Hayır, bozmaz", "Sadece namazı bozar"], "c": 2},
    {"q": "63. Peygamberimizin 'Cennet kadınlarının efendisi' olarak nitelediği kızı hangisidir?", "a": ["Hz. Zeyneb", "Hz. Rukiye", "Hz. Fatıma", "Hz. Ümmü Gülsüm"], "c": 2},
    {"q": "64. Kur'an-ı Kerim hangi halife döneminde çoğaltılarak önemli merkezlere gönderilmiştir?", "a": ["Hz. Ebubekir", "Hz. Ömer", "Hz. Osman", "Hz. Ali"], "c": 2},
    {"q": "65. Peygamberimizin hicret sırasında saklandığı mağara hangisidir?", "a": ["Hira Mağarası", "Sevr Mağarası", "Uhud Mağarası", "Nur Mağarası"], "c": 1},
    {"q": "66. Müslümanların bir işe karar vermeden önce Allah'tan hayırlısını dilemek için kıldıkları namaz hangisidir?", "a": ["Şükür Namazı", "İstihare Namazı", "Hacet Namazı", "Tahiyyetü'l-Mescid"], "c": 1},
    {"q": "67. Aşağıdakilerden hangisi abdestin sünnetlerinden biridir?", "a": ["Yüzü yıkamak", "Başın dörtte birini meshetmek", "Elleri dirseklere kadar yıkamak", "Misvak kullanmak veya dişleri fırçalamak"], "c": 3},
    {"q": "68. Firavun'a karşı mucizeleriyle mücadele eden peygamber kimdir?", "a": ["Hz. Musa", "Hz. İsa", "Hz. Şuayb", "Hz. Lut"], "c": 0},
    {"q": "69. Namazların her rekatında okunan zorunlu sure hangisidir?", "a": ["İhlas", "Fatiha", "Felak", "Nas"], "c": 1},
    {"q": "70. Allah yolunda yapılan her türlü maddi ve manevi çabaya ne ad verilir?", "a": ["Ticaret", "Cihat", "Siyaset", "Ganimet"], "c": 1},
    
    # TEST 8 (71-80)
    {"q": "71. Peygamberimizin süt kardeşinin adı nedir?", "a": ["Esma", "Şeyma", "Nesibe", "Sümeyye"], "c": 1},
    {"q": "72. Kur'an-ı Kerim'in ayetlerini açıklayan ve yorumlayan bilim dalına ne denir?", "a": ["Fıkıh", "Hadis", "Tefsir", "Kelam"], "c": 2},
    {"q": "73. Hangi halife 'Adalet' kavramıyla özdeşleşmiştir?", "a": ["Hz. Ebubekir", "Hz. Ömer", "Hz. Osman", "Hz. Ali"], "c": 1},
    {"q": "74. Müslümanların bir yıl boyunca topladıkları paranın zekatını vermeleri için üzerinden ne kadar zaman geçmelidir?", "a": ["6 ay", "1 kameri yıl", "2 yıl", "100 gün"], "c": 1},
    {"q": "75. 'Allahuekber' sözünün anlamı nedir?", "a": ["Allah birdir", "Allah en büyüktür", "Allah affedicidir", "Allah her şeyi bilir"], "c": 1},
    {"q": "76. Bir insanın öldükten sonra amel defterinin kapanmamasını sağlayan kalıcı iyiliklere ne denir?", "a": ["Zekat-ı Mal", "Sadaka-i Cariye", "Fitre", "Öşür"], "c": 1},
    {"q": "77. Hz. İbrahim'in ateşe atıldığı yer olarak bilinen günümüz şehri hangisidir?", "a": ["Konya", "Bursa", "Şanlıurfa", "Hatay"], "c": 2},
    {"q": "78. Kur'an-ı Kerim'de adı geçen tek kadın kimdir?", "a": ["Hz. Havva", "Hz. Meryem", "Hz. Asiye", "Hz. Sare"], "c": 1},
    {"q": "79. Peygamberimizin doğduğu gece kutlanan kandil hangisidir?", "a": ["Regaip Kandili", "Miraç Kandili", "Mevlid Kandili", "Berat Kandili"], "c": 2},
    {"q": "80. İslam hukukunda bir konudaki dini hükmü açıklayan belgeye ne denir?", "a": ["Ferman", "Berat", "Fetva", "İcma"], "c": 2},
    
    # TEST 9 (81-90)
    {"q": "81. Peygamberlerin günahsız olmalarına ne denir?", "a": ["İsmet", "Emanet", "Tebliğ", "Sıdk"], "c": 0},
    {"q": "82. Hz. Nuh'un gemisinin oturduğu dağ olarak Kur'an'da geçen yer neresidir?", "a": ["Ağrı Dağı", "Cudi Dağı", "Erciyes Dağı", "Uhud Dağı"], "c": 1},
    {"q": "83. Bir Müslüman öldüğünde ona karşı yapılması gereken son görev nedir?", "a": ["Helva dağıtmak", "Mevlit okutmak", "Cenaze namazını kılmak ve defnetmek", "Evini ziyaret etmek"], "c": 2},
    {"q": "84. Namazın vaktinin girdiğini bildirmek için yapılan çağrıya ne denir?", "a": ["Kamet", "Selâ", "Ezan", "Zikir"], "c": 2},
    {"q": "85. Peygamberlerin Allah'tan getirdiği emirlerin her zaman doğru olması sıfatı hangisidir?", "a": ["Sıdk", "Fetanet", "İsmet", "Emanet"], "c": 0},
    {"q": "86. Ramazan ayında Kur'an'ı birinin okuyup diğerlerinin takip etmesine ne ad verilir?", "a": ["Hatim", "Mukabele", "Mevlit", "Tilavet"], "c": 1},
    {"q": "87. 'Lâ ilâhe illallah' sözü ne anlama gelir?", "a": ["Allah en büyüktür", "Allah'tan başka ilah yoktur", "Hamd Allah'adır", "Allah bizi korusun"], "c": 1},
    {"q": "88. İslam'da 'Şehitlerin Efendisi' olarak anılan Peygamberimizin amcası kimdir?", "a": ["Hz. Abbas", "Hz. Hamza", "Ebu Talip", "Hz. Cafer"], "c": 1},
    {"q": "89. Peygamberimizin hicret sonrası Medine'de inşa ettirdiği mescidin adı nedir?", "a": ["Mescid-i Aksa", "Mescid-i Nebevi", "Mescid-i Kıbleteyn", "Mescid-i Haram"], "c": 1},
    {"q": "90. Kurban ibadeti hangi peygamberin sünnetidir?", "a": ["Hz. Nuh", "Hz. İbrahim", "Hz. Musa", "Hz. İsa"], "c": 1},
    
    # TEST 10 (91-100)
    {"q": "91. Allah'ın güzel isimlerine genel olarak ne ad verilir?", "a": ["Esma-i Hüsna", "Kelam-ı Kibar", "El-Emin", "Sıfât-ı Zatiye"], "c": 0},
    {"q": "92. Aşağıdakilerden hangisi suyun olmadığı yerde yapılan temizliktir?", "a": ["Gusül", "Teyemmüm", "Taharet", "Mesh"], "c": 1},
    {"q": "93. İslam dininin temel inanç esaslarını inceleyen bilim dalı hangisidir?", "a": ["Fıkıh", "Akaid / Kelam", "Hadis", "Siyer"], "c": 1},
    {"q": "94. 'Zemzem' suyu hangi peygamber zamanında ortaya çıkmıştır?", "a": ["Hz. Adem", "Hz. İsmail", "Hz. Yunus", "Hz. Süleyman"], "c": 1},
    {"q": "95. Mekke'nin fethi hangi yılda gerçekleşmiştir?", "a": ["622", "624", "630", "632"], "c": 2},
    {"q": "96. Müslümanların birbiriyle karşılaştığında söyledikleri ilk söz nedir?", "a": ["Merhaba", "Nasılsın", "Selamun Aleyküm", "Günaydın"], "c": 2},
    {"q": "97. İslam dininde kaç mezhep (hak mezhep) vardır (Amelde)?", "a": ["2", "3", "4", "5"], "c": 2},
    {"q": "98. Peygamberimize 'Kur'an dışında' verilen, onun söz ve davranışlarından oluşan kaynağa ne denir?", "a": ["Sünnet", "İcma", "Kıyas", "İçtihat"], "c": 0},
    {"q": "99. Müslümanların kıblesi olan Kabe'nin yönünü gösteren cami bölümüne ne denir?", "a": ["Minber", "Mihrap", "Vaaz Kürsüsü", "Minare"], "c": 1},
    {"q": "100. Allah'ın her şeyi görmesi, bilmesi ve denetlemesi bilinciyle yaşamaya ne denir?", "a": ["İhsan", "İhlas", "Takva", "Sabır"], "c": 0},
]

# ------------------ SERTİFİKA FONKSİYONU ------------------

def sertifika_goster(ad_soyad, puan):           # sertifika göster fonksiyonu
    """Sertifika penceresi gösterir"""
    win = tk.Toplevel()                          # sertifika penceresi
    win.title("🎓 Başarı Sertifikası")           
    win.geometry("700x500")                      # pencere boyutu
    win.configure(bg="#ffffff")                # pencere arka plan rengi
    
    # Çerçeve
    cerceve = tk.Frame(win, bg="#0d47a1", padx=20, pady=20)         # çerçeve oluşturma
    cerceve.pack(fill="both", expand=True, padx=20, pady=20)          # çerçeve yerleşimi
    
    # İç beyaz alan
    ic_alan = tk.Frame(cerceve, bg="#ffffff", padx=30, pady=30)     # iç alan çerçevesi
    ic_alan.pack(fill="both", expand=True)                            # iç alan çerçevesi
    
    # Başlık
    tk.Label(                                  # etiket oluşturma
        ic_alan,                               # etiket oluşturma
        text="🎓 BAŞARI SERTİFİKASI 🎓",       # başlık metni
        font=("Segoe UI", 24, "bold"),          # başlık stili
        bg="#ffffff",                         # arka plan rengi
        fg="#0d47a1"                          # başlık rengi
    ).pack(pady=20)                             # başlık etiketi
    
    # Altın çizgi
    tk.Frame(ic_alan, bg="#ffd700", height=3).pack(fill="x", padx=50)   # altın çizgi ekleme
    
    # İsim
    tk.Label(                          # etiket oluşturma
        ic_alan,                       # etiket oluşturma
        text=ad_soyad.upper(),         # isim büyük harflerle
        font=("Segoe UI", 20, "bold"), # isim stili
        bg="#ffffff",                # arka plan rengi
        fg="#1976d2"                 # isim rengi
    ).pack(pady=30)                    # isim etiketi
    
    # Açıklama
    tk.Label(                                                 # etiket oluşturma
        ic_alan,                                              # etiket oluşturma
        text="İslami Test Sınavını Başarıyla Tamamlamıştır",   # açıklama metni
        font=("Segoe UI", 14),            # açıklama stili
        bg="#ffffff",                   # arka plan rengi
        fg="#424242"                    # açıklama rengi
    ).pack(pady=10)                       # açıklama etiketi
    
    # Puan
    tk.Label(                              #
        ic_alan,                           # etiket oluşturma
        text=f"📊 Puan: {puan}/100",        
        font=("Segoe UI", 16, "bold"),     # puan stili
        bg="#ffffff",                    # arka plan rengi
        fg="#2e7d32"                     # puan rengi
    ).pack(pady=15)                        # puan etiketi
    
    # Tarih
    tarih = datetime.now().strftime("%d.%m.%Y")      # tarih formatı
    tk.Label(                                        # etiket oluşturma
        ic_alan,                                     # etiket oluşturma
        text=f"📅 Tarih: {tarih}",                  # tarih etiketi
        font=("Segoe UI", 12),                      # tarih stili
        bg="#ffffff",                             # arka plan rengi
        fg="#757575"                              # tarih rengi
    ).pack(pady=10)                                 # tarih etiketi
    
    # Altın çizgi
    tk.Frame(ic_alan, bg="#ffd700", height=3).pack(fill="x", padx=50, pady=20)   # altın çizgi ekleme
    # Kapat butonu
    tk.Button(                         # buton oluşturma
        ic_alan,                        # buton oluşturma
        text="KAPAT",                   # buton metni
        font=("Segoe UI", 12, "bold"),  # buton stili
        bg="#d32f2f",                # buton arka plan rengi
        fg="white",                    # buton yazı rengi
        padx=30,                       # buton genişliği
        pady=10,                       # buton yerleşimi
        command=win.destroy            # pencere kapatma
    ).pack(pady=10)                    # sertifika penceresi

def isim_al_ve_sertifika(puan):        # isim al ve sertifika fonksiyonu
    win = tk.Toplevel()                # isim giriş penceresi
    win.title("İsim Girişi")           # pencere başlıgı
    win.geometry("400x200")            # pencere boyutu
    win.configure(bg="#e3f2fd")      # pencere arka plan rengi
    win.grab_set()                     # 

    tk.Label(                           # etiket oluşturma
        win,                            # etiket oluşturma
        text="Ad Soyad Giriniz",        # etiket metni
        font=("Segoe UI", 14, "bold"),  # etiket stili
        bg="#e3f2fd"                  # etiket arka plan rengi
    ).pack(pady=20)                     # etiket yerleşimi

    entry = tk.Entry(win, font=("Segoe UI", 14), width=25)   # giriş kutusu
    entry.pack(pady=10)               # giriş kutusu yerleşimi
    entry.focus()                     # giriş kutusuna odaklan

    def onayla():                     # onayla fonksiyonu
        ad = entry.get().strip()      # girilen ismi al
        if not ad:                    # boş isim kontrolü
            messagebox.showwarning("Uyarı", "Lütfen isminizi giriniz!")   # boş isim kontrolü
            return                               # boş isim kontrolü
        win.destroy()                            # isim giriş penceresini kapat
        sertifika_goster(ad, puan)               # sertifika gösterme fonksiyonu

    tk.Button(                                 # buton oluşturma
        win,                                   # buton oluşturma
        text="Sertifikayı Göster",             # buton metni
        font=("Segoe UI", 12, "bold"),         # buton stili
        bg="#2196f3",                        # buton arka plan rengi
        fg="white",                            # buton yazı rengi
        padx=20,                               # buton genişliği
        pady=8,                                # buton yerleşimi
        command=onayla                         # onayla fonksiyonu
    ).pack(pady=20)                            # sertifika butonu
    
    # Enter tuşu ile de onaylayabilsin
    entry.bind('<Return>', lambda e: onayla())    # ------ İSLAMİ TEST PENCERESİ --------

# ------------------ TKINTER PENCERE ------------------

root = tk.Tk()                     # ana pancere
root.title("İslami Test (01–100)") # pencere başlıgı
root.geometry("900x600")           # pencere boyutu
root.configure(bg="#e3f2fd")     # pencere arka plan rengi

style = ttk.Style()                # stil ayarları
style.theme_use("clam")            # tema seçimi
style.configure("TButton", font=("Segoe UI", 12), padding=10)  # buton sitili

current = 0                                             #  0-9 
answers = [tk.IntVar(value=-1) for _ in range(100)]      # her soru için cevep değişkeni

# ------------------ ANA FRAME ------------------

frame = tk.Frame(root, bg="#e3f2fd")                  # ana pencere çerçevesi
frame.pack(fill="both", expand=True, padx=30, pady=20)  # çerçeve yerleşimi

question_label = tk.Label(                              # soru metni etiketi
    frame, font=("Segoe UI", 16, "bold"),               # etiket stili
    bg="#e3f2fd", wraplength=800, justify="left"      # etiket yerleşimi
)
question_label.pack(anchor="w", pady=15)                 # etiket yerleşimi

radio_buttons = []                      # radyo butonları listesi
for i in range(4):                      # 4 seçenek için döngü
    rb = tk.Radiobutton(                # radyo buton oluşturma
        frame, font=("Segoe UI", 13),   # buton sitili
        bg="#e3f2fd", anchor="w"      # buton yerleşimi
    )
    rb.pack(fill="x", pady=5)           # buton yerleşimi
    radio_buttons.append(rb)            # butonu listeye ekle

# ------------------ FONKSİYONLAR ------------------

def load_question(index):                                   # soru yükleme fonksiyonu
    question_label.config(text=all_questions[index]["q"])   # soru metnini ayarlama
    for i, rb in enumerate(radio_buttons):                  # seçenek metinlerini ayarlama
        rb.config(                                          # radyo buton metni
            text=all_questions[index]["a"][i],              # seçenek metni
            variable=answers[index],                        # radyo buton değişkeni
            value=i                                         # radyo buton degeri
        )

def next_q():                              # sonraki soru fonksiyonu
    global current                         #current global değişkeni
    if current < len(all_questions) - 1:   # son soruya gelmediyse
        current += 1                       #current artır
        load_question(current)             # sonraki soruyu yükle

def prev_q():                              # önceki soru fonksiyonu
    global current                         # current global değişkeni
    if current > 0:                        # ilk soruda değilse
        current -= 1                       # current azalt
        load_question(current)             # önceki soruyu yükle

def show_result():                         # sonuç gösterme fonksiyonu
    score = 0                              # puan değişkeni
    for i, q in enumerate(all_questions):  # soruları döngüle
        if answers[i].get() == q["c"]:     # dogru cevap kopntrolü
            score += 1                     # puanı artır

    if score >= 60:                                             # geçme durumu
        play_success_animation()                                # başarı animasyonu
        messagebox.showinfo("SONUÇ", f"{score}/100 🎉 GEÇTİN")  # başarı mesajı
        root.after(500, lambda: isim_al_ve_sertifika(score))     # sertifika alma
    else:
        messagebox.showwarning("SONUÇ", f"{score}/100 ❌ KALDIN") # başarısızlık mesajı

def play_success_animation():                                    # başarı animasyonu fonksiyonu
    try:
        if sys.platform == 'win32':
            import winsound
            winsound.PlaySound("applause.wav",                         # alkış sesi
                               winsound.SND_FILENAME | winsound.SND_ASYNC)  # ses dosyası
        else:
            print('\a', end='', flush=True)  # Linux/Mac için sistem bip sesi
    except:                                                        # ses dosyası bulunamama durumu
        pass                                                       # hatayı yok say

    anim = tk.Toplevel(root)          # animasyonpenceresi
    anim.geometry("400x200")          # pencere boyutu
    anim.configure(bg="#0d47a1")    # pencere arka plan rengi
    tk.Label(                         # etiket
        anim,                          # etiket metni
        text="🎉 TEBRİKLER 🎉",        
        font=("Segoe UI", 22, "bold"),  # etiket sitili
        fg="white",                     # etiket metin rengi
        bg="#0d47a1"                  # etiket arka plan rengi 
    ).pack(expand=True)                 # etiket yerleşimi

    anim.after(2000, anim.destroy)      # 2 saniye sonra pencereyi kapat

# ------------------ BUTONLAR ------------------

btn_frame = tk.Frame(root, bg="#e3f2fd")    # buton çerçevesi
btn_frame.pack(pady=20)                       # buton yerleşimi

ttk.Button(btn_frame, text="⏮ Geri", command=prev_q).grid(row=0, column=0, padx=10)          # geri butonu
ttk.Button(btn_frame, text="İleri ⏭", command=next_q).grid(row=0, column=1, padx=10)         # ileri butonu
ttk.Button(btn_frame, text="Testi Bitir", command=show_result).grid(row=0, column=2, padx=10)  # testi bitir butonu

# ------------------ BAŞLAT ------------------

load_question(current)                      # ilk soruyu yükle
root.mainloop()                             # ana döngüyü başlat





# 1.ci soru... Allah'ın var ve bir olmasına, ortağı bulunmamasına ne ad verilir?

#  sorular 01.....100 arası 100 soru...tkinter modundadır...

#  terminale bu kodu yapıştırın ve entere basın...

#  bu test butonludur ...üstte static kod resmi var..böyle görüntüleniyor ...


#  pycharm community de altta solda terminale tıkla .... açılan pencereye alttaki kodu yapıştır ....

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_36.py


#  & "E:/İslami Test Soruları/.venv/Scripts/python.exe" islami_test_python_36.py   Pardusda

# python3 "/home/ismail/Documents/Python/gtk-dersi/data/İslami Test/Soruları/islami_test_python_36.py" pardusda

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_36.py     windows da

# 01 DEN 100 E KADAR İLERLEYEN SORULAR VAR...SONUNDA BAŞARI DURUMU VE SERTİFİKA ALMA VAR ...

# SES YOK..ANİMASYON YOK.....

# SONUNA KADAR İLERLEDİM mükemmel çalışiıyor... sertifika isim yazmalı çıkıyor... başarı puanı gösteriyor...

#  C'deki Klasörü güncellemek için üst solda 4 çizgiye tıkla altta şu yazana tıkla ... Reload all from Disk



'''
   cevap anahtarı 
   
1-A, 2-B, 3-C, 4-C, 5-D, 6-A, 7-B, 8-B, 9-C, 10-C, 11-C, 12-D, 13-A, 14-C, 15-B, 16-A, 17-C, 18-C, 19-D, 20-B,

21-C, 22-A, 23-B, 24-B, 25-C, 26-B, 27-B, 28-C, 29-C, 30-B, 31-D, 32-B (2 sünnet + 2 farz), 33-B, 34-C, 35-A, 

36-B, 37-C, 38-B, 39-A, 40-B, 41-C (Eşi/Halasıdır), 42-B, 43-C, 44-B, 45-C, 46-B, 47-A, 48-C, 49-B, 50-C.

51-B, 52-A, 53-C, 54-C, 55-B, 56-B, 57-A, 58-C, 59-B, 60-A, 61-A, 62-C, 63-C, 64-C, 65-B, 66-B, 67-D, 68-A, 

69-B, 70-B, 71-B, 72-C, 73-B, 74-B, 75-B, 76-B, 77-C, 78-B, 79-C, 80-C, 81-A, 82-B, 83-C, 84-C, 85-A, 86-B, 

87-B, 88-B, 89-B, 90-B, 91-A, 92-B, 93-B, 94-B, 95-C, 96-C, 97-C, 98-A, 99-B, 100-A.


'''
