

import tkinter as tk                          # Tkinter kütüphanesini içe aktar
from tkinter import messagebox, simpledialog  # Tkinter bileşenleri
import datetime                               # Tarih ve saat işlemleri için
import random                                 # Rastgele kod oluşturma için
import string                                 # Karakter dizileri için
import qrcode                                 # QR kod oluşturma kütüphanesi
from PIL import Image, ImageDraw, ImageFont, ImageTk    # Görüntü işleme kütüphanesi

# =================================================
# ÖRNEK TESTLER (Sadece 2 test gösteriyorum, sen 37'ye tamamlayabilirsin)
# =================================================
testler = [
    [
        # TEST 1 (1-10)
        {"q": "İmanın şartları kaç tanedir?", "a": ["4", "5", "6", "7"], "c": 2},
        {"q": "Allah'ın 'el-Alîm' isminin anlamı nedir?", "a": ["Affedici", "Her şeyi bilen", "Güçlü", "Merhametli"], "c": 1},
        {"q": "Meleklerin yaratıldığı varlık nedir?", "a": ["Ateş", "Toprak", "Su", "Nur"], "c": 3},
        {"q": "Ahiret hayatının başlamasına ne denir?", "a": ["Haşir", "Kıyamet", "Mizan", "Sırat"], "c": 1},
        {"q": "Peygamberlerin doğru sözlü olmalarına ne ad verilir?", "a": ["Emanet", "Fetanet", "Sıdk", "Tebliğ"], "c": 2},
        {"q": "Kur'an-ı Kerim kaç sureden oluşur?", "a": ["112", "113", "114", "115"], "c": 2},
        {"q": "İlk indirilen sure hangisidir?", "a": ["Fatiha", "Alak", "Nas", "Bakara"], "c": 1},
        {"q": "Kur'an-ı Kerim hangi dilde indirilmiştir?", "a": ["İbranice", "Arapça", "Süryanice", "Farsça"], "c": 1},
        {"q": "En uzun sure hangisidir?", "a": ["Nisa", "Âl-i İmran", "Bakara", "En'am"], "c": 2},
        {"q": "Kur'an'da adı geçen tek kadın kimdir?", "a": ["Hz. Hatice", "Hz. Aişe", "Hz. Meryem", "Hz. Fatıma"], "c": 2},
    ],
    [
            # TEST 2 (11-20)
        {"q": "Namaz günde kaç vakittir?", "a": ["3", "4", "5", "6"], "c": 2},
        {"q": "Oruç hangi ayda farz kılınmıştır?", "a": ["Recep", "Şaban", "Ramazan", "Muharrem"], "c": 2},
        {"q": "Zekât hangi mallardan verilir?", "a": ["Sadece altın", "Sadece para", "Zenginlikten", "Yoksulluktan"], "c": 2},
        {"q": "Hac ibadeti nerede yapılır?", "a": ["Medine", "Kudüs", "Mekke", "İstanbul"], "c": 2},
        {"q": "Kurban Bayramı kaç gün sürer?", "a": ["1", "2", "3", "4"], "c": 3},
        {"q": "Hz. Muhammed'in doğduğu şehir?", "a": ["Medine", "Mekke", "Taif", "Kudüs"], "c": 1},
        {"q": "İslam'ın beş şartından biri nedir?", "a": ["Zekât", "Sadaka", "İyilik", "Sabır"], "c": 0},
        {"q": "Kıble yönü neresidir?", "a": ["Kudüs", "Mekke", "Medine", "Şam"], "c": 1},
        {"q": "Kur'an'da kaç ayet vardır?", "a": ["6236", "6666", "7000", "6000"], "c": 0},
        {"q": "İslam'da ilk vahiy nerede gelmiştir?", "a": ["Hira", "Arafat", "Mina", "Mescid-i Haram"], "c": 0},
    ],
    [   
        # TEST 3 (31-40)
        {"q": "21. İslam'da haram olan içkiye ne denir?", "a": ["Hamr", "Meyte", "Hınzır", "Kan"], "c": 0},
        {"q": "22. Cuma namazının farz olduğu rekat sayısı kaçtır?", "a": ["2", "3", "4", "6"], "c": 0},
        {"q": "23. Zekat vermek kimlere farzdır?", "a": ["Herkese", "Fakirlere", "Nisap miktarı mala sahip olanlara", "Zenginlere"], "c": 2},
        {"q": "24. İslam'da ilk kıble neresidir?", "a": ["Kabe", "Mescid-i Aksa", "Mescid-i Nebevi", "Mescid-i Haram"], "c": 1},
        {"q": "25. Peygamberimizin doğum yılına ne ad verilir?", "a": ["Hicret Yılı", "Fil Yılı", "Hendek Yılı", "Fetih Yılı"], "c": 1},
        {"q": "26. Namazda okunan en kısa sure hangisidir?", "a": ["İhlas", "Kevser", "Felak", "Nas"], "c": 1},
        {"q": "27. Hac ibadetinin farz olduğu İslami ay hangisidir?", "a": ["Zilkade", "Zilhicce", "Muharrem", "Safer"], "c": 1},
        {"q": "28. Peygamberimize ilk vahiy hangi melek tarafından getirilmiştir?", "a": ["Mikail", "Azrail", "İsrafil", "Cebrail"], "c": 3},
        {"q": "29. İslam'da niyet hangi ibadet için şarttır?", "a": ["Zekât", "Oruç", "Namaz", "Hepsi"], "c": 3},
        {"q": "30. Peygamberimizin doğduğu şehir hangisidir?", "a": ["Medine", "Mekke", "Kudüs", "Taif"], "c": 1},
   ],
   [     
        # TEST 4 (31-40)  
        {"q": "31. Namazda rükûdan sonra doğrulmaya ne denir?", "a": ["Secde", "Kıyam", "Kavme", "Celse"], "c": 2},
        {"q": "32. İslam'da anne-babaya iyi davranmaya ne denir?", "a": ["Takva", "İhsan", "Birr", "Sabır"], "c": 2},
        {"q": "33. Kur'an'da 'Oku' anlamına gelen ilk kelime hangisidir?", "a": ["Elhamdülillah", "İkra", "Kul", "Allah"], "c": 1},
        {"q": "34. Peygamberimizin sütannesi kimdir?", "a": ["Amine", "Halime", "Ümmü Gülsüm", "Safiye"], "c": 1},
        {"q": "35. İslam'da cuma namazı kimlere farzdır?", "a": ["Kadınlara", "Çocuklara", "Erkeklere", "Yolculara"], "c": 2},
        {"q": "36. Kur'an'ın son suresi hangisidir?", "a": ["Felak", "Nas", "İhlas", "Kevser"], "c": 1},
        {"q": "37. 'Allah yolunda mücadele' anlamına gelen kavram hangisidir?", "a": ["Hicret", "Cihat", "Tebliğ", "Sabır"], "c": 1},
        {"q": "38. Namazda iki secde arasında oturmaya ne denir?", "a": ["Kavme", "Kıyam", "Celse", "Rükû"], "c": 2},
        {"q": "39. İslam'da yalan söylememek hangi sıfatla ilgilidir?", "a": ["İsmet", "Sıdk", "Emanet", "Fetanet"], "c": 1},
        {"q": "40. Peygamberimizin en küçük kızı kimdir?", "a": ["Zeynep", "Rukiye", "Ümmü Gülsüm", "Fatıma"], "c": 3},

   ],  
   [  
       # TEST 5 (41-50)
        {"q": "41. Kur'an'da besmele ile başlayan sure hangisidir?", "a": ["Enfal", "Neml", "Tevbe", "Yasin"], "c": 1},
        {"q": "42. Oruçluyken bilerek yemek yemek neyi bozar?", "a": ["Abdest", "Namaz", "Oruç", "Gusül"], "c": 2},
        {"q": "43. İslam'da komşuluk hakkına ne ad verilir?", "a": ["Kul hakkı", "İnsan hakkı", "Adalet", "Merhamet"], "c": 0},
        {"q": "44. Peygamberimize verilen ilk mucize hangisidir?", "a": ["Miraç", "Kur'an", "Ay'ın yarılması", "İsra"], "c": 1},
        {"q": "45. Kur'an'ın indirildiği dağın adı nedir?", "a": ["Uhud", "Nur", "Sevr", "Cudi"], "c": 1},
        {"q": "46. İslam'da sadaka vermek hangi davranışın göstergesidir?", "a": ["Cimrilik", "İbadet", "Yardımlaşma", "Sabır"], "c": 2},
        {"q": "47. Peygamberimizin kabri hangi şehirde bulunmaktadır?", "a": ["Mekke", "Kudüs", "Medine", "Taif"], "c": 2},
        {"q": "48. Kur'an'ın toplanması hangi halife döneminde tamamlanmıştır?", "a": ["Hz. Ali", "Hz. Ömer", "Hz. Osman", "Hz. Ebubekir"], "c": 2},
        {"q": "49. İslam'da içten ve samimi ibadete ne denir?", "a": ["İhsan", "İhlas", "Takva", "Sabır"], "c": 1},
        {"q": "50. Namazdan sonra '33 defa' okunan zikir hangisidir?", "a": ["Elhamdülillah", "Allahu Ekber", "Sübhanallah", "Hepsi"], "c": 3},

    ],   
    [   
      # TEST 6 (51-60)
        {"q": "51. Kur'an'da adı geçen tek sahabe kimdir?", "a": ["Hz. Ali", "Zeyd bin Harise", "Bilal-i Habeşi", "Hz. Ebubekir"], "c": 1},
        {"q": "52. İslam'da yoksula verilen karşılıksız yardıma ne denir?", "a": ["Zekât", "Sadaka", "Fitre", "Hediye"], "c": 1},
        {"q": "53. Fitre hangi ibadetle ilgilidir?", "a": ["Namaz", "Oruç", "Hac", "Zekât"], "c": 1},
        {"q": "54. Peygamberimizin mesleği neydi?", "a": ["Çiftçi", "Demirci", "Tüccar", "Öğretmen"], "c": 2},
        {"q": "55. Kur'an'da 'Rahman' suresi kaç ayetten oluşur?", "a": ["55", "65", "78", "88"], "c": 2},
        {"q": "56. İslam'da affetmek hangi erdemle ilgilidir?", "a": ["Sabır", "Merhamet", "Cesaret", "Takva"], "c": 1},
        {"q": "57. Peygamberimizin vefat ettiği yaş kaçtır?", "a": ["60", "61", "62", "63"], "c": 3},
        {"q": "58. İslam'da helal kazanç neyi temsil eder?", "a": ["Bereket", "Güç", "Ün", "Makam"], "c": 0},
        {"q": "59. Kur'an'da 'anne' anlamında kullanılan kelime hangisidir?", "a": ["Ümm", "Valid", "Ebe", "Anne"], "c": 0},
        {"q": "60. İslam'da kibirli olmak hangi davranıştır?", "a": ["Günah", "Sevap", "Farz", "Sünnet"], "c": 0},

    ],   
    [   
      # TEST 7 (61-70)
        {"q": "61. Peygamberimizin son hutbesine ne ad verilir?", "a": ["Veda Hutbesi", "Miraç Hutbesi", "Cuma Hutbesi", "Tebliğ Hutbesi"], "c": 0},
        {"q": "62. Namazda okunan kısa surelere ne denir?", "a": ["Uzun sure", "Mekki sure", "Kısa sure", "Zamm-ı sure"], "c": 3},
        {"q": "63. Kur'an'da cennet için kullanılan isim hangisidir?", "a": ["Sırat", "Firdevs", "Araf", "Kevser"], "c": 1},
        {"q": "64. İslam'da israf neyi ifade eder?", "a": ["Tasarruf", "Ölçülü olmak", "Gereksiz harcama", "Yardımlaşma"], "c": 2},
        {"q": "65. Peygamberimizin kabri hangi mescidin içindedir?", "a": ["Mescid-i Haram", "Mescid-i Aksa", "Mescid-i Nebevi", "Kuba Mescidi"], "c": 2},
        {"q": "66. Kur'an'da cehennem için kullanılan isim hangisidir?", "a": ["Kevser", "Sırat", "Cehim", "Firdevs"], "c": 2},
        {"q": "67. İslam'da doğru sözlülüğe ne denir?", "a": ["Sıdk", "Emanet", "İsmet", "Fetanet"], "c": 0},
        {"q": "68. Peygamberimizin en yakın arkadaşı kimdir?", "a": ["Hz. Ömer", "Hz. Ali", "Hz. Ebubekir", "Hz. Osman"], "c": 2},
        {"q": "69. Kur'an'ın korunmasını Allah'ın üstlendiği ayet hangi surededir?", "a": ["Bakara", "Hicr", "Yasin", "Nisa"], "c": 1},
        {"q": "70. İslam'da misafire ikram etmek ne sayılır?", "a": ["Zorunluluk", "Günah", "Sevap", "İsraf"], "c": 2},

    ],
    [  
      # TEST 8 (71-80)
        {"q": "71. Peygamberimizin 'güzel ahlak' ile ilgili sözü hangi kavramı anlatır?", "a": ["İbadet", "Ahlak", "Takva", "Sabır"], "c": 1},
        {"q": "72. İslam'da helal haramı belirleyen temel kaynak hangisidir?", "a": ["Hadis", "İcma", "Kıyas", "Kur'an"], "c": 3},
        {"q": "73. Kur'an'ın ana konusu nedir?", "a": ["Tarih", "Ahlak", "İnanç", "Hepsi"], "c": 3},
        {"q": "74. İslam'da sözünde durmak hangi kavramla ilgilidir?", "a": ["Sabır", "Emanet", "Sıdk", "Takva"], "c": 1},
        {"q": "75. Peygamberimizin son peygamber olması ne ile ifade edilir?", "a": ["Risalet", "Nübüvvet", "Hatm-i Nübüvvet", "Tebliğ"], "c": 2},
        {"q": "76. İslam'da insanların eşit olduğunu vurgulayan hutbe hangisidir?", "a": ["Cuma Hutbesi", "Veda Hutbesi", "Miraç Hutbesi", "Tebliğ Hutbesi"], "c": 1},
        {"q": "77. Peygamberlerin Allah'tan aldıkları emirleri insanlara eksiksiz iletmesine ne denir?", "a": ["Emanet", "Tebliğ", "İsmet", "Fetanet"], "c": 1},
        {"q": "78. Namaz kaç rekattır (farz namazların toplamı günlük)?", "a": ["15", "17", "20", "40"], "c": 1},
        {"q": "79. İslam'ın beş şartından biri olan şehadet nedir?", "a": ["Tanıklık", "Namaz", "Oruç", "Zekât"], "c": 0},
        {"q": "80. Kur'an'da kaç peygamberin ismi geçer?", "a": ["23", "25", "27", "30"], "c": 1},

    ],   
    [   
       # TEST 9 (81-90)
        {"q": "81. Hz. Muhammed'in peygamberliğe başladığı yaş kaçtır?", "a": ["30", "35", "40", "45"], "c": 2},
        {"q": "82. İslam'da namaz kılmanın vacip olduğu yaş kaçtır?", "a": ["7", "10", "12", "15"], "c": 3},
        {"q": "83. Kur'an'ın ilk mushaf haline getirilmesi hangi halife dönemindedir?", "a": ["Hz. Ebubekir", "Hz. Ömer", "Hz. Osman", "Hz. Ali"], "c": 0},
        {"q": "84. Bedir Savaşı hangi yılda olmuştur?", "a": ["1. Hicri yıl", "2. Hicri yıl", "3. Hicri yıl", "5. Hicri yıl"], "c": 1},
        {"q": "85. İslam'da sabır hangi kategoriye girer?", "a": ["Farz", "Vacip", "Fazilet", "Sünnet"], "c": 2},
        {"q": "86. Peygamberimizin annesi kimdir?", "a": ["Amine", "Halime", "Hatice", "Aişe"], "c": 0},
        {"q": "87. İslam'da gusül abdesti hangi durumda alınır?", "a": ["Her namaz öncesi", "Sadece cuma", "Cünüplükten sonra", "Her gün"], "c": 2},
        {"q": "88. Mekke'nin fethi hangi yılda gerçekleşmiştir?", "a": ["6. Hicri yıl", "8. Hicri yıl", "10. Hicri yıl", "11. Hicri yıl"], "c": 1},
        {"q": "89. İslam'da tevhid ne demektir?", "a": ["Allah'ın birliği", "Namaz", "Oruç", "Hac"], "c": 0},
        {"q": "90. Kur'an'ın nazil olduğu ilk mağaranın adı nedir?", "a": ["Sevr", "Hira", "Uhud", "Nur"], "c": 1},

    ],       
    [   
      # TEST 10 (111-120)
        {"q": "91. İslam'da kadınların başını örtmesine ne denir?", "a": ["Tesettür", "Takva", "Edep", "İffet"], "c": 0},
        {"q": "92. Peygamberimizin ilk eşi kimdir?", "a": ["Aişe", "Hatice", "Hafsa", "Sevde"], "c": 1},
        {"q": "93. İslam'da faiz ne anlama gelir?", "a": ["Haram kazanç", "Helal kazanç", "Ticaret", "Yardım"], "c": 0},
        {"q": "94. Kur'an'da en çok geçen peygamber kimdir?", "a": ["Hz. Muhammed", "Hz. İbrahim", "Hz. Musa", "Hz. İsa"], "c": 2},
        {"q": "95. İslam'da kurban kesmek hangi ibadetle ilgilidir?", "a": ["Ramazan", "Hac", "Cuma", "Zekât"], "c": 1},
        {"q": "96. Namazda kaç defa secde yapılır (bir rekatta)?", "a": ["1", "2", "3", "4"], "c": 1},
        {"q": "97. İslam'da temizliğe verilen önem hangi sözle ifade edilir?", "a": ["İmanın yarısı", "İmanın şartı", "İmanın tamamı", "Sünnet"], "c": 0},
        {"q": "98. Kur'an'ın en kısa suresi hangisidir?", "a": ["Kevser", "İhlas", "Nas", "Felak"], "c": 0},
        {"q": "99. İslam'da namaz kılarken hangi yön önemlidir?", "a": ["Doğu", "Batı", "Kıble", "Kuzey"], "c": 2},
        {"q": "100. Peygamberimizin vefat tarihi hangi ayda olmuştur?", "a": ["Muharrem", "Safer", "Rebiulevvel", "Recep"], "c": 2},

   ],     
   [ 
       # TEST 11 (111-120) 
        {"q": "101. İslam’ın beş şartından biri aşağıdakilerden hangisidir?", "a": ["Zekâ", "Oruç", "Hicret", "Cihat"], "c": 1},
        {"q": "102. Kur’an-ı Kerim hangi ayda indirilmeye başlanmıştır?", "a": ["Muharrem", "Recep", "Ramazan", "Şaban"], "c": 2},
        {"q": "103. Hz. Muhammed’e (s.a.v.) ilk vahiy hangi melek aracılığıyla gelmiştir?", "a": ["Azrail", "Mikail", "İsrafil", "Cebrail"], "c": 3},
        {"q": "104. Günde kaç vakit namaz farzdır?", "a": ["3", "4", "5", "6"], "c": 2},
        {"q": "105. Aşağıdakilerden hangisi İslam’ın şartlarından biri değildir?", "a": ["Namaz", "Oruç", "Hac", "Kurban kesmek"], "c": 3},
        {"q": "106. Kur’an-ı Kerim kaç sureden oluşur?", "a": ["110", "112", "114", "116"], "c": 2},
        {"q": "107. “İman” kavramı aşağıdakilerden hangisini ifade eder?", "a": ["İbadet etmek", "Allah’a ve esaslara gönülden inanmak", "İyi insan olmak", "Günah işlememek"], "c": 1},
        {"q": "108. Zekât kimlere verilir?", "a": ["Sadece akrabalara", "Zenginlere", "Fakir ve ihtiyaç sahiplerine", "Herkese"], "c": 2},
        {"q": "109. Hz. Muhammed’in (s.a.v.) doğduğu şehir neresidir?", "a": ["Medine", "Kudüs", "Mekke", "Taif"], "c": 2},
        {"q": "110. Aşağıdakilerden hangisi haram kabul edilir?", "a": ["Sadaka vermek", "Yalan söylemek", "Selam vermek", "İlim öğrenmek"], "c": 1},
      
    ],   
    [   
       # TEST 12 (111-120)
        {"q": "111. Allah'ın her şeyi önceden bilip planlamasına ne denir?", "a": ["Kaza","Kader","Tevekkül","İrade"], "c": 1},
        {"q": "112. Peygamberlerin Allah'tan aldıkları mesajları insanlara eksiksiz bildirmesine ne denir?", "a": ["Tebliğ","Emanet","Sıdk","İsmet"], "c": 0},
        {"q": "113. Aşağıdakilerden hangisi 'Ulu'l-Azm' peygamberlerden biri değildir?", "a": ["Hz. Nuh","Hz. İbrahim","Hz. Adem","Hz. İsa"], "c": 2},
        {"q": "114. Hz. Muhammed (s.a.v.) kaç yaşında peygamber olmuştur?", "a": ["25","33","40","63"], "c": 2},
        {"q": "115. Namazda Kur'an-ı Kerim okumaya ne ad verilir?", "a": ["Kıyam","Kıraat","Tekbir","Tahiyyat"], "c": 1},
        {"q": "116. Ölen bir Müslümanın ardından kılınan ve rükusu, secdesi olmayan namaz hangisidir?", "a": ["Vitir Namazı","Cenaze Namazı","Küsuf Namazı","İstiska Namazı"], "c": 1},
        {"q": "117. Kur'an-ı Kerim'in en uzun ayeti olan 'Müdayene' ayeti hangi surededir?", "a": ["Bakara","Nisa","Maide","Araf"], "c": 0},
        {"q": "118. İslam'da ilk cuma namazı nerede kılınmıştır?", "a": ["Kabe","Mescid-i Nebevi","Ranuna Vadisi","Kuba Mescidi"], "c": 2},
        {"q": "119. İslam dinine göre 'Büyük Günahlar' arasında ilk sırada hangisi yer alır?", "a": ["Yalan söylemek","Allah'a ortak koşmak (Şirk)","Gıybet","İsraf"], "c": 1},
        {"q": "120. Hz. Yusuf'un babası olan peygamber kimdir?", "a": ["Hz. Yakup","Hz. İshak","Hz. Yahya","Hz. Zekeriya"], "c": 0},
 
    ],       
    [  
       # TEST 13 (121-130)
        {"q": "121. Allah'ın her an her şeyi yaratmaya devam etmesi sıfatına ne ad verilir?", "a": ["Tekvin","Bekâ","Kıyam bi-nefsihi","Vahdaniyet"], "c": 0},
        {"q": "122. Oruçlu bir kimsenin hataen bir şey yemesi orucu bozar mı?", "a": ["Evet, kaza gerekir","Evet, kefaret gerekir","Hayır, bozmaz","Sadece namazı bozar"], "c": 2},
        {"q": "123. Peygamberimizin 'Cennet kadınlarının efendisi' olarak nitelediği kızı hangisidir?", "a": ["Hz. Zeyneb","Hz. Rukiye","Hz. Fatıma","Hz. Ümmü Gülsüm"], "c": 2},
        {"q": "124. Kur'an-ı Kerim hangi halife döneminde çoğaltılarak önemli merkezlere gönderilmiştir?", "a": ["Hz. Ebubekir","Hz. Ömer","Hz. Osman","Hz. Ali"], "c": 2},
        {"q": "125. Peygamberimizin hicret sırasında saklandığı mağara hangisidir?", "a": ["Hira","Sevr","Uhud","Nur"], "c": 1},
        {"q": "126. Müslümanların bir işe karar vermeden önce Allah'tan hayırlısını dilemek için kıldıkları namaz hangisidir?", "a": ["Şükür","İstihare","Hacet","Tahiyyetü'l-Mescid"], "c": 1},
        {"q": "127. Aşağıdakilerden hangisi abdestin sünnetlerinden biridir?", "a": ["Yüzü yıkamak","Başın dörtte birini meshetmek","Elleri dirseklere kadar yıkamak","Misvak kullanmak veya dişleri fırçalamak"], "c": 3},
        {"q": "128. Firavun'a karşı mucizeleriyle mücadele eden peygamber kimdir?", "a": ["Hz. Musa","Hz. İsa","Hz. Şuayb","Hz. Lut"], "c": 0},
        {"q": "129. Namazların her rekatında okunan zorunlu sure hangisidir?", "a": ["İhlas","Fatiha","Felak","Nas"], "c": 1},
        {"q": "130. Allah yolunda yapılan her türlü maddi ve manevi çabaya ne ad verilir?", "a": ["Ticaret","Cihat","Siyaset","Ganimet"], "c": 1},
  
    ],      
    [   
        # TEST 14 (131-140) 
        {"q": "131. Peygamberimizin süt kardeşinin adı nedir?", "a": ["Esma","Şeyma","Nesibe","Sümeyye"], "c": 1},
        {"q": "132. Kur'an-ı Kerim'in ayetlerini açıklayan ve yorumlayan bilim dalına ne denir?", "a": ["Fıkıh","Hadis","Tefsir","Kelam"], "c": 2},
        {"q": "133. Kur'an-ı Kerim'in ayetlerini açıklayan ve yorumlayan bilim dalına ne denir?", "a": ["Fıkıh","Hadis","Tefsir","Kelam"], "c": 2},
        {"q": "134. Hangi halife 'Adalet' kavramıyla özdeşleşmiştir?", "a": ["Hz. Ebubekir","Hz. Ömer","Hz. Osman","Hz. Ali"], "c": 1},
        {"q": "135. Müslümanların zekat vermeleri için üzerinden ne kadar zaman geçmelidir?", "a": ["6 ay","1 kameri yıl","2 yıl","100 gün"], "c": 1},
        {"q": "136. 'Allahuekber' sözünün anlamı nedir?", "a": ["Allah birdir","Allah en büyüktür","Allah affedicidir","Allah her şeyi bilir"], "c": 1},
        {"q": "137. Kalıcı iyiliklere (cami, çeşme, okul vb.) ne denir?", "a": ["Zekat-ı Mal","Sadaka-i Cariye","Fitre","Öşür"], "c": 1},
        {"q": "138. Hz. İbrahim'in ateşe atıldığı yer olarak bilinen günümüz şehri hangisidir?", "a": ["Konya","Bursa","Şanlıurfa","Hatay"], "c": 2},
        {"q": "139. Kur'an-ı Kerim'de adı geçen tek kadın kimdir?", "a": ["Hz. Havva","Hz. Meryem","Hz. Asiye","Hz. Sare"], "c": 1},
        {"q": "140. Peygamberimizin doğduğu gece kutlanan kandil hangisidir?", "a": ["Regaip","Miraç","Mevlid","Berat"], "c": 2},   
    ],    
    [  
       # TEST 15 (141-150)    
        {"q": "141. İslam hukukunda dini hükmü açıklayan belgeye ne denir?", "a": ["Ferman","Berat","Fetva","İcma"], "c": 2},  
        {"q": "142. Peygamberlerin günahsız olmalarına ne denir?", "a": ["İsmet","Emanet","Tebliğ","Sıdk"], "c": 0},
        {"q": "143. Hz. Nuh'un gemisinin oturduğu dağ olarak Kur'an'da geçen yer neresidir?", "a": ["Ağrı","Cudi","Erciyes","Uhud"], "c": 1},
        {"q": "144. Bir Müslüman öldüğünde yapılması gereken son görev nedir?", "a": ["Helva dağıtmak","Mevlit okutmak","Cenaze namazını kılmak ve defnetmek","Evini ziyaret etmek"], "c": 2},
        {"q": "145. Namazın vaktinin girdiğini bildirmek için yapılan çağrıya ne denir?", "a": ["Kamet","Selâ","Ezan","Zikir"], "c": 2},
        {"q": "146. Peygamberlerin Allah'tan getirdiği emirlerin her zaman doğru olması sıfatı hangisidir?", "a": ["Sıdk","Fetanet","İsmet","Emanet"], "c": 0},
        {"q": "147. Ramazan ayında Kur'an'ı birinin okuyup diğerlerinin takip etmesine ne ad verilir?", "a": ["Hatim","Mukabele","Mevlit","Tilavet"], "c": 1},
        {"q": "148. Ramazan ayında Kur'an'ı birinin okuyup diğerlerinin takip etmesine ne ad verilir?", "a": ["Hatim","Mukabele","Mevlit","Tilavet"], "c": 1},
        {"q": "149. 'Lâ ilâhe illallah' sözü ne anlama gelir?", "a": ["Allah en büyüktür","Allah'tan başka ilah yoktur","Hamd Allah'adır","Allah bizi korusun"], "c": 1},
        {"q": "150. Peygamberimizin hicret sonrası Medine'de inşa ettirdiği mescidin adı nedir?", "a": ["Mescid-i Aksa","Mescid-i Nebevi","Mescid-i Kıbleteyn","Mescid-i Haram"], "c": 1},          
    ],      
    [  
       # TEST 16 (151-160)   
        {"q": "151. Kurban ibadeti hangi peygamberin sünnetidir?", "a": ["Hz. Nuh","Hz. İbrahim","Hz. Musa","Hz. İsa"], "c": 1},
        {"q": "152. İslam'da 'Şehitlerin Efendisi' olarak anılan Peygamberimizin amcası kimdir?", "a": ["Hz. Abbas","Hz. Hamza","Ebu Talip","Hz. Cafer"], "c": 1},
        {"q": "153. Allah'ın güzel isimlerine genel olarak ne ad verilir?", "a": ["Esma-i Hüsna","Kelam-ı Kibar","El-Emin","Sıfât-ı Zatiye"], "c": 0},
        {"q": "154. Aşağıdakilerden hangisi suyun olmadığı yerde yapılan temizliktir?", "a": ["Gusül","Teyemmüm","Taharet","Mesh"], "c": 1},
        {"q": "155. İslam dininin temel inanç esaslarını inceleyen bilim dalı hangisidir?", "a": ["Fıkıh","Akaid / Kelam","Hadis","Siyer"], "c": 1},
        {"q": "156. 'Zemzem' suyu hangi peygamber zamanında ortaya çıkmıştır?", "a": ["Hz. Adem","Hz. İsmail","Hz. Yunus","Hz. Süleyman"], "c": 1},
        {"q": "157. Mekke'nin fethi hangi yılda gerçekleşmiştir?", "a": ["622","624","630","632"], "c": 2},
        {"q": "158. Müslümanların birbiriyle karşılaştığında söyledikleri ilk söz nedir?", "a": ["Merhaba","Nasılsın","Selamun Aleyküm","Günaydın"], "c": 2},
        {"q": "159. İslam dininde kaç mezhep (hak mezhep) vardır (Amelde)?", "a": ["2","3","4","5"], "c": 2},
        {"q": "160. Peygamberimize 'Kur'an dışında' verilen, onun söz ve davranışlarından oluşan kaynağa ne denir?", "a": ["Sünnet","İcma","Kıyas","İçtihat"], "c": 0},
    ],      
    [  
       # TEST 17 (161-170)    
        {"q": "161. Müslümanların kıblesi olan Kabe'nin yönünü gösteren cami bölümüne ne denir?", "a": ["Minber","Mihrap","Vaaz Kürsüsü","Minare"], "c": 1},
        {"q": "162. Allah'ın her şeyi görmesi, bilmesi ve denetlemesi bilinciyle yaşamaya ne denir?", "a": ["İhsan","İhlas","Takva","Sabır"], "c": 0},
        {"q": "163. İslam'ın beş şartından biri olan ve zengin Müslümanların yılda bir kez mallarının belirli bir kısmını ihtiyaç sahiplerine vermesi anlamına gelen ibadet hangisidir?","a":["Zekat","Sadaka","Hac","Fitre"],"c":0},
        {"q": "164. Kur'an-ı Kerim'in en uzun suresi aşağıdakilerden hangisidir?","a":["Al-i İmran","Bakara","Nisa","Maide"],"c":1},
        {"q": "165. İmanın şartlarından biri olan 'Kaza ve Kadere İman', aşağıdakilerden hangisini kapsar?","a":["Sadece geçmişte yaşanan olayları","Allah'ın her şeyi bir ölçüye göre takdir etmesi ve zamanı gelince gerçekleşmesi","Sadece insanların kendi özgür iradesiyle yaptığı seçimleri","Doğa olaylarının tesadüfen meydana gelmesini"],"c":1},
        {"q": "166. Peygamber Efendimiz (s.a.v.)'in gece vakti Mescid-i Haram'dan Mescid-i Aksa'ya götürülmesine ne ad verilir?","a":["Hicret","Miraç","İsra","Vahiy"],"c":2},
        {"q": "167. Aşağıdakilerden hangisi abdestin farzlarından biri değildir?","a":["Yüzü yıkamak","Ağza ve burna su vermek","Elleri dirseklerle beraber yıkamak","Başın dörtte birini meshetmek"],"c":1},
        {"q": "168. Kur'an-ı Kerim hangi halife döneminde kitap (mushaf) haline getirilmiştir?","a":["Hz. Ebubekir","Hz. Ömer","Hz. Osman","Hz. Ali"],"c":0},
        {"q": "169. İslam dininde 'Ef'al-i Mükellefin' içinde yer alan ve yapılması kesin olarak yasaklanan fiillere ne denir?","a":["Mekruh","Haram","Mübah","Vacip"],"c":1},
        {"q": "170. Aşağıdakilerden hangisi Peygamber Efendimiz (s.a.v.)'in çocuklarından biri değildir?","a":["Hz. Fatıma","Hz. Kasım","Hz. Ayşe","Hz. İbrahim"],"c":2},   
    ],   
    [  
       # TEST 18 (171-180)    
        {"q": "171. Kıblenin Kudüs'teki Mescid-i Aksa'dan Mekke'deki Kabe'ye çevrildiği olay ne zaman gerçekleşmiştir?","a":["Hicretten 5 yıl önce","Hicretten yaklaşık 1,5 yıl sonra","Mekke'nin Fethinden hemen sonra","Veda Haccı sırasında"],"c":1},
        {"q": "172. Allah'ın her şeyi görmesi sıfatına ne ad verilir?","a":["İlim","Semi","Basar","Kudret"],"c":2},
        {"q": "173. Allah'ın var ve bir olmasına, ortağı bulunmamasına ne ad verilir?","a":["Tevhid","Nübüvvet","Ahiret","Haşir"],"c":0},
        {"q": "174. Aşağıdakilerden hangisi imanın şartlarından biri değildir?","a":["Meleklere inanmak","Namaz kılmak","Peygamberlere inanmak","Kitaplara inanmak"],"c":1},
        {"q": "175. İlahi kitaplardan Zebur hangi peygambere indirilmiştir?","a":["Hz. Musa","Hz. İsa","Hz. Davud","Hz. İbrahim"],"c":2},
        {"q": "176. Öldükten sonra dirilip Allah’ın huzurunda toplanmaya ne ad verilir?","a":["Mizan","Berzah","Haşir","Kıyamet"],"c":2},
        {"q": "177. Vahiy getirmekle görevli melek hangisidir?","a":["Mikail","Azrail","İsrafil","Cebrail"],"c":3},
        {"q": "178. Namazın içindeki farzlardan olan, namaza başlarken alınan tekbire ne denir?","a":["İftitah Tekbiri","Kıyam","Ka'de-i Ahire","Secde"],"c":0},
        {"q": "179. Günde kaç vakit namaz kılmak farzdır?","a":["3","5","7","2"],"c":1},
        {"q": "180. Namazda rükudan sonra alnı yere koyarak yapılan harekete ne denir?","a":["Kıraat","Secde","Teşehhüd","Selam"],"c":1},  
    ],      
    [
       # TEST 19 (181-190)    
        {"q": "181. Hangi namazın cemaatle kılınması zorunludur?","a":["Teravih","Bayram","Cuma","Vitir"],"c":2},
        {"q": "182. Oruç tutmaya güç yetiremeyen yaşlıların veya iyileşme ümidi olmayan hastaların verdiği maddi bedele ne denir?","a":["Zekat","Sadaka","Fidye","Fitre"],"c":2},
        {"q": "183. Teyemmüm abdesti ne ile alınır?","a":["Su","Kağıt","Toprak","Kumaş"],"c":2},
        {"q": "184. Haccın farzlarından biri olan ve Kabe'nin etrafında 7 kez dönmeye ne denir?","a":["Say","İhram","Vakfe","Tavaf"],"c":3},
        {"q": "185. Zekat verebilmek için sahip olunması gereken asgari zenginlik ölçüsüne ne denir?","a":["Nisap","Miktar","Öşür","Fitre"],"c":0},
        {"q": "186. Peygamberimiz hangi şehirde doğmuştur?","a":["Medine","Kudüs","Mekke","Taif"],"c":2},
        {"q": "187. Peygamberimize ilk vahiy nerede gelmiştir?","a":["Sevr Mağarası","Hira Mağarası","Mescid-i Nebevi","Kabe"],"c":1},
        {"q": "188. Müslümanların ilk hicret ettiği yer neresidir?","a":["Habeşistan","Medine","Mısır","Bağdat"],"c":0},
        {"q": "189. Peygamberimizin Medine'ye hicret ederken yanındaki yol arkadaşı kimdir?","a":["Hz. Ömer","Hz. Ali","Hz. Ebubekir","Hz. Osman"],"c":2},
        {"q": "190. Müslümanlar ile Mekkeli müşrikler arasındaki ilk büyük savaş hangisidir?","a":["Uhud","Hendek","Bedir","Hayber"],"c":2},  
    ],      
    [  
       # TEST 20 (191-200)    
        {"q": "191. Peygamberimizin vefat ettiği şehir hangisidir?","a":["Mekke","Cidde","Şam","Medine"],"c":3},
        {"q": "200. Kur'an-ı Kerim'de kaç cüz vardır?","a":["20","30","40","114"],"c":1},  
        {"q": "201. Kur'an-ı Kerim'in ilk suresi hangisidir?","a":["Bakara","İhlas","Fatiha","Nas"],"c":2},
        {"q": "202. Kur'an-ı Kerim'in en kısa suresi hangisidir?","a":["Kevser","Fil","Maun","Kureyş"],"c":0},
        {"q": "203. Hangi surenin başında Besmele bulunmaz?","a":["Yasin","Tevbe","Rahman","Mülk"],"c":1},
        {"q": "204. Kur'an-ı Kerim yaklaşık kaç yılda tamamlanmıştır?","a":["10","23","40","63"],"c":1},
        {"q": "205. Kur'an-ı Kerim'i ezberleyen kişiye ne ad verilir?","a":["Müezzin","İmam","Hafız","Alim"],"c":2},
        {"q": "206. Doğa olaylarını ve rızıkları yönetmekle görevli melek hangisidir?","a":["Cebrail","Mikail","Azrail","İsrafil"],"c":1},
        {"q": "207. Allah'ın her şeyi işitmesi sıfatına ne ad verilir?","a":["İlim","Semi","Basar","Kudret"],"c":1},
        {"q": "208. Peygamberlerin akıllı ve zeki olmaları sıfatına ne denir?","a":["Sıdk","Emanet","Fetanet","Tebliğ"],"c":2},
        {"q": "209. Kur'an-ı Kerim'in her 20 sayfalık bölümüne ne ad verilir?","a":["Sure","Ayet","Cüz","Hizb"],"c":2},
        {"q": "200. Kabe'yi Hz. İbrahim ile birlikte inşa eden oğlu kimdir?","a":["Hz. İshak","Hz. İsmail","Hz. Yakup","Hz. Yusuf"],"c":1},
    ],      
    [  
       # TEST 21 (201-210)
        {"q": "201. İslam'ın beş şartından hangisi sadece zenginlere farzdır?","a":["Namaz","Oruç","Kelime-i Şehadet","Zekat"],"c":3},
        {"q": "202. Sabah namazı kaç rekattır?","a":["2","4","6","10"],"c":1},
        {"q": "203. Peygamberimizin kabrinin bulunduğu yere ne ad verilir?","a":["Makam-ı İbrahim","Ravza-i Mutahhara","Altınoluk","Hacerü'l Esved"],"c":1},
        {"q": "204. Ramazan ayında yatsı namazından sonra kılınan sünnet namaz hangisidir?","a":["Teheccüd","İşrak","Teravih","Evvabin"],"c":2},
        {"q": "205. Allah'ın emriyle can almakla görevli melek hangisidir?","a":["Azrail","Mikail","Münker","Nekir"],"c":0},
        {"q": "206. Peygamberimizin dedesinin adı nedir?","a":["Ebu Talip","Abdülmuttalip","Abdullah","Hamza"],"c":1},
        {"q": "207. İslam tarihinde ilk ezanı okuyan sahabe kimdir?","a":["Hz. Ebubekir","Hz. Ali","Bilal-i Habeşi","Zeyd bin Sabit"],"c":2},
        {"q": "208. Mekke'den Medine'ye göç eden Müslümanlara ne ad verilir?","a":["Ensar","Muhacir","Mürted","Münafık"],"c":1},
        {"q": "209. Medineli olup Mekkeli Müslümanlara yardım edenlere ne denir?","a":["Ensar","Muhacir","Tabiun","Sahabe"],"c":0},
        {"q": "210. Kur'an'ın 'kalbi' olarak bilinen sure hangisidir?","a":["Bakara","Yasin","Mülk","Fetih"],"c":1}, 
    ],       
    [   
       # TEST 22 (211-220)    
        {"q": "211. Aşağıdakilerden hangisi Peygamberimizin çocuklarından biri değildir?","a":["Zeynep","Ümmü Gülsüm","Safiye","Rukiye"],"c":2},
        {"q": "212. Ramazan Bayramı'nda verilen vacip olan sadakaya ne denir?","a":["Fidye","Fitre (Fıtır Sadakası)","Öşür","Haraç"],"c":1},
        {"q": "213. Müslümanların kıblesi olan Kabe hangi şehirdedir?","a":["Medine","Cidde","Mekke","Riyad"],"c":2},
        {"q": "214. Allah'ın her şeye gücünün yetmesi sıfatına ne ad verilir?","a":["İlim","Kudret","İrade","Tekvin"],"c":1},
        {"q": "215. 'El-Emin' (Güvenilir) lakabı kime verilmiştir?","a":["Hz. Ebubekir","Hz. Ömer","Hz. Muhammed (s.a.v)","Hz. Süleyman"],"c":2},
        {"q": "216. Her işe başlarken söylediğimiz 'Bismillahirrahmanirrahim'in anlamı nedir?","a":["Allah en büyüktür","Rahman ve Rahim olan Allah'ın adıyla.","Hamd Allah'adır","Allah birdir"],"c":1},
        {"q": "217. Bir Müslümanın başka bir Müslüman üzerindeki haklarından biri nedir?","a":["Selamını almak","Malını almak","Sırrını ifşa etmek","Onu eleştirmek"],"c":0},
        {"q": "218. Peygamberimizin ilk eşi kimdir?","a":["Hz. Ayşe","Hz. Hafsa","Hz. Hatice","Hz. Sevde"],"c":2},
        {"q": "219. Amellerin tartılacağı teraziye ne ad verilir?","a":["Sırat","Mizan","Mahşer","Berzah"],"c":1},
        {"q": "220. İslam'ın temel kaynağı nedir?","a":["Hadis kitapları","İlmihal","Kur'an-ı Kerim","Fıkıh kitapları"],"c":2},   
    ],      
    [  
       # TEST 23 (221-230)
        {"q": "231. İslam’da ilk vahiy hangi sure ile başlamıştır?","a":["Alak","Fatiha","Bakara","İhlas"],"c":0},
        {"q": "232. Peygamberimizin hicret ettiği şehir hangisidir?","a":["Mekke","Medine","Taif","Kudüs"],"c":1},
        {"q": "233. İslam’da zekat vermek için gerekli olan zenginlik ölçüsüne ne denir?","a":["Fitre","Nisap","Öşür","Sadaka"],"c":1},
        {"q": "234. Peygamberimizin Uhud Savaşı’nda şehit olan amcası kimdir?","a":["Hz. Abbas","Hz. Hamza","Hz. Cafer","Hz. Talha"],"c":1},
        {"q": "235. Kur’an’da en çok adı geçen peygamber kimdir?","a":["Hz. Musa","Hz. İbrahim","Hz. Muhammed","Hz. Yusuf"],"c":0},
        {"q": "236. İslam’da cuma namazı kaç rekattır (farz)?","a":["2","4","6","8"],"c":0}, 
        {"q": "237. Peygamberimizin doğum yılı hangi isimle bilinir?","a":["Fil yılı","Hicret yılı","Bedir yılı","Veda yılı"],"c":0},
        {"q": "238. İslam’da oruç hangi ayda farz kılınmıştır?","a":["Recep","Şaban","Ramazan","Muharrem"],"c":2},
        {"q": "239. Peygamberimizin sütannesi kimdir?","a":["Halime","Amine","Hatice","Ümmü Gülsüm"],"c":0},
        {"q": "240. Kur’an’da kıssası en uzun anlatılan peygamber kimdir?","a":["Hz. Yusuf","Hz. Musa","Hz. İbrahim","Hz. Nuh"],"c":1},
    ],      
    [  
       # TEST 24 (241-250)
        {"q": "241. İslam’da ilk şehit kadın sahabe kimdir?","a":["Hz. Hatice","Hz. Fatıma","Hz. Sümeyye","Hz. Zeyneb"],"c":2},
        {"q": "242. Peygamberimizin hicret yolunda saklandığı mağara hangisidir?","a":["Hira","Sevr","Nur","Uhud"],"c":1},
        {"q": "243. Kur’an’da adı geçen tek sure kadın ismiyle hangisidir?","a":["Meryem","Zeynep","Hatice","Fatıma"],"c":0},
        {"q": "244. İslam’da bayram namazı kaç rekattır?","a":["2","4","6","8"],"c":0},
        {"q": "245. Peygamberimizin en çok hadis rivayet eden sahabesi kimdir?","a":["Hz. Ebubekir","Hz. Ömer","Hz. Aişe","Ebu Hureyre"],"c":3},
        {"q": "246. Kur’an’da kıble değişimi hangi surede geçmektedir?","a":["Bakara","Nisa","Maide","Tevbe"],"c":0},
        {"q": "247. Peygamberimizin hicret sırasında yanındaki arkadaşı kimdir?","a":["Hz. Ali","Hz. Ebubekir","Hz. Osman","Hz. Ömer"],"c":1},
        {"q": "248. İslam’da ilk mescid hangisidir?","a":["Mescid-i Haram","Mescid-i Nebevi","Kuba Mescidi","Mescid-i Aksa"],"c":2},
        {"q": "249. Kur’an’da geçen 'İkra' emri hangi surede yer alır?","a":["Alak","Bakara","Fatiha","Yasin"],"c":0},
        {"q": "250. Peygamberimizin veda hutbesi hangi yılda yapılmıştır?","a":["630","631","632","633"],"c":2}, 
    ],   
    [  
      # TEST 25(251-260)]    
        {"q": "251. İslam’da ilk şehit erkek sahabe kimdir?","a":["Hz. Ammar","Hz. Musab","Hz. Ali","Hz. Ebubekir"],"c":0},
        {"q": "252. Kur’an’da en kısa ayet hangisidir?","a":["Rahman","Taha","Yasin","Müddessir"],"c":3},
        {"q": "253. Peygamberimizin doğduğu şehir hangisidir?","a":["Medine","Mekke","Taif","Kudüs"],"c":1},
        {"q": "254. İslam’da ilk vahiy hangi mağarada gelmiştir?","a":["Sevr","Hira","Nur","Uhud"],"c":1},
        {"q": "255. Kur’an’da adı geçen tek deniz hangisidir?","a":["Kızıldeniz","Akdeniz","Karadeniz","Nil"],"c":0},
        {"q": "256. Peygamberimizin hicret ettiği yıl hangi takvimin başlangıcıdır?","a":["Miladi","Rumi","Hicri","Celali"],"c":2},
        {"q": "257. İslam’da zekat kimlere verilmez?","a":["Fakirlere","Yolculara","Zenginlere","Borçlulara"],"c":2},
        {"q": "258. Kur’an’da adı geçen tek kadın peygamber var mıdır?","a":["Evet","Hayır","Bilinmiyor","Tartışmalı"],"c":1},
        {"q": "259. Peygamberimizin en küçük oğlu kimdir?","a":["Hz. Kasım","Hz. Abdullah","Hz. İbrahim","Hz. Hasan"],"c":2},
        {"q": "260. İslam’da ilk ezanı okuyan sahabe kimdir?","a":["Hz. Ali","Bilal-i Habeşi","Hz. Ebubekir","Hz. Ömer"],"c":1},   
    ],
    [  
       # TEST 26 (261-270)
        {"q": "261. Kur’an’da en çok tekrar edilen ayet hangi surede geçer?","a":["Rahman","Bakara","Yasin","İhlas"],"c":0},
        {"q": "262. Peygamberimizin hicret sonrası inşa ettiği mescid hangisidir?","a":["Mescid-i Aksa","Mescid-i Nebevi","Mescid-i Kıbleteyn","Kuba Mescidi"],"c":1},
        {"q": "263. İslam’da ilk şehit çocuk kimdir?","a":["Hz. Hüseyin","Hz. Hasan","Hz. Abdullah","Hz. Kasım"],"c":0},
        {"q": "264. Kur’an’da en uzun sure hangisidir?","a":["Bakara","Al-i İmran","Nisa","Maide"],"c":0},
        {"q": "265. Peygamberimizin en çok sevdiği yiyeceklerden biri hangisidir?","a":["Hurmayı","Balı","Sütü","Zeytini"],"c":0},
        {"q": "266. İslam’da ilk vahiy hangi ayda gelmiştir?","a":["Recep","Şaban","Ramazan","Muharrem"],"c":2},
        {"q": "267. Kur’an’da adı geçen tek dağ hangisidir?","a":["Uhud","Cudi","Hira","Sevr"],"c":1},
        {"q": "268. Peygamberimizin en çok hadis rivayet eden eşi kimdir?","a":["Hz. Hatice","Hz. Aişe","Hz. Sevde","Hz. Hafsa"],"c":1},
        {"q": "269. İslam’da ilk bayram namazı nerede kılınmıştır?","a":["Kabe","Mescid-i Nebevi","Ranuna Vadisi","Kuba Mescidi"],"c":2},
        {"q": "270. Kur’an’da adı geçen tek böcek hangisidir?","a":["Arı","Karınca","Çekirge","Kelebek"],"c":1}, 
    ],      
    [  
       # test 27 (271-280)
        {"q": "271. Peygamberimizin en çok sevdiği renk hangisidir?","a":["Yeşil","Beyaz","Siyah","Kırmızı"],"c":1},
        {"q": "272. İslam’da ilk hutbe nerede okunmuştur?","a":["Kuba","Ranuna","Mekke","Medine"],"c":1},
        {"q": "273. Kur’an’da adı geçen tek şehir hangisidir?","a":["Mekke","Medine","Kudüs","Taif"],"c":0},
        {"q": "274. Peygamberimizin en çok sevdiği içecek hangisidir?","a":["Su","Süt","Bal şerbeti","Hurmalı içecek"],"c":1},
        {"q": "275. İslam’da ilk şehit sahabe kimdir?","a":["Hz. Ammar","Hz. Musab","Hz. Ali","Hz. Ebubekir"],"c":1},
        {"q": "276. Kur’an’da adı geçen tek hayvan hangisidir?","a":["Deve","At","Fil","Kuş"],"c":2},
        {"q": "277. Peygamberimizin en çok sevdiği meyve hangisidir?","a":["Hurma","Zeytin","Nar","Üzüm"],"c":0},
        {"q": "278. İslam’da ilk ezan nerede okunmuştur?","a":["Mekke","Medine","Kuba","Taif"],"c":1},
        {"q": "279. Kur’an’da adı geçen tek bitki hangisidir?","a":["Zeytin","Hurmanın","Buğday","Arpa"],"c":0},
        {"q": "280. Peygamberimizin en çok sevdiği hayvan hangisidir?","a":["At","Deve","Köpek","Kedi"],"c":1},
    ],   
    [  
       # test 28 (281-290)
        {"q": "281. İslam’da ilk namaz nerede kılınmıştır?","a":["Kabe","Mescid-i Nebevi","Kuba Mescidi","Ranuna Vadisi"],"c":3},
        {"q": "282. Kur’an’da adı geçen tek kavim hangisidir?","a":["İbrahim","Nuh","Musa","İsa"],"c":1},
        {"q": "283. Peygamberimizin en çok sevdiği meyve hangisidir?","a":["Hurma","Zeytin","Nar","Üzüm"],"c":0},
        {"q": "284. İslam’da ilk ezan nerede okunmuştur?","a":["Mekke","Medine","Kuba","Taif"],"c":1},
        {"q": "285. Kur’an’da adı geçen tek şehir hangisidir?","a":["Mekke","Medine","Kudüs","Taif"],"c":0},
        {"q": "286. Kur’an’da adı geçen tek şehir hangisidir?","a":["Mekke","Medine","Kudüs","Taif"],"c":0},
        {"q": "287. Kur’an’da adı geçen tek şehir hangisidir?","a":["Mekke","Medine","Kudüs","Taif"],"c":0},
        {"q": "288. Kur’an’da adı geçen tek şehir hangisidir?","a":["Mekke","Medine","Kudüs","Taif"],"c":0},
        {"q": "289. Kur’an’da adı geçen tek şehir hangisidir?","a":["Mekke","Medine","Kudüs","Taif"],"c":0},
        {"q": "290. Kur’an’da adı geçen tek şehir hangisidir?","a":["Mekke","Medine","Kudüs","Taif"],"c":0},  
    ],   
    [  
       # test 29 (291-300)    
        {"q": "291. İslam’da ilk namaz nerede kılınmıştır?","a":["Kabe","Mescid-i Nebevi","Kuba Mescidi","Ranuna Vadisi"],"c":3},
        {"q": "292. Kur’an’da adı geçen tek kavim hangisidir?","a":["İbrahim","Nuh","Musa","İsa"],"c":1},
        {"q": "293. Peygamberimizin en çok sevdiği meyve hangisidir?","a":["Hurma","Zeytin","Nar","Üzüm"],"c":0},
        {"q": "294. İslam’da ilk ezan nerede okunmuştur?","a":["Mekke","Medine","Kuba","Taif"],"c":1},
        {"q": "295. Kur’an’da adı geçen tek şehir hangisidir?","a":["Mekke","Medine","Kudüs","Taif"],"c":0},
        {"q": "296. Kur’an’da adı geçen tek şehir hangisidir?","a":["Mekke","Medine","Kudüs","Taif"],"c":0},
        {"q": "297. Kur’an’da adı geçen tek şehir hangisidir?","a":["Mekke","Medine","Kudüs","Taif"],"c":0},
        {"q": "298. Kur’an’da adı geçen tek şehir hangisidir?","a":["Mekke","Medine","Kudüs","Taif"],"c":0},
        {"q": "299. Kur’an’da adı geçen tek şehir hangisidir?","a":["Mekke","Medine","Kudüs","Taif"],"c":0},
        {"q": "300. Kur’an’da adı geçen tek şehir hangisidir?","a":["Mekke","Medine","Kudüs","Taif"],"c":0},
    ],
    [  
       # test 30 (301-310)                       
        {"q":"301. İslam’da ilk vahiy hangi sure ile başlamıştır?","a":["Alak","Fatiha","Bakara","İhlas"],"c":0},
        {"q":"302. Peygamberimizin hicret ettiği şehir hangisidir?","a":["Mekke","Medine","Taif","Kudüs"],"c":1},
        {"q":"303. İslam’da zekat vermek için gerekli olan zenginlik ölçüsüne ne denir?","a":["Fitre","Nisap","Öşür","Sadaka"],"c":1},
        {"q":"304. Peygamberimizin Uhud Savaşı’nda şehit olan amcası kimdir?","a":["Hz. Abbas","Hz. Hamza","Hz. Cafer","Hz. Talha"],"c":1},
        {"q":"305. Kur’an’da en çok adı geçen peygamber kimdir?","a":["Hz. Musa","Hz. İbrahim","Hz. Muhammed","Hz. Yusuf"],"c":0},
        {"q":"306. İslam’da cuma namazı kaç rekattır (farz)?","a":["2","4","6","8"],"c":0},
        {"q":"307. Peygamberimizin doğum yılı hangi isimle bilinir?","a":["Fil yılı","Hicret yılı","Bedir yılı","Veda yılı"],"c":0},
        {"q":"308. İslam’da oruç hangi ayda farz kılınmıştır?","a":["Recep","Şaban","Ramazan","Muharrem"],"c":2},
        {"q":"309. Peygamberimizin sütannesi kimdir?","a":["Halime","Amine","Hatice","Ümmü Gülsüm"],"c":0},
        {"q":"310. Kur’an’da kıssası en uzun anlatılan peygamber kimdir?","a":["Hz. Yusuf","Hz. Musa","Hz. İbrahim","Hz. Nuh"],"c":1},
    ],   
    [  
       # test 31  (311-320)
        {"q":"311. İslam’da ilk şehit kadın sahabe kimdir?","a":["Hz. Hatice","Hz. Fatıma","Hz. Sümeyye","Hz. Zeyneb"],"c":2},
        {"q":"312. Peygamberimizin hicret yolunda saklandığı mağara hangisidir?","a":["Hira","Sevr","Nur","Uhud"],"c":1},
        {"q":"313. Kur’an’da adı geçen tek sure kadın ismiyle hangisidir?","a":["Meryem","Zeynep","Hatice","Fatıma"],"c":0},
        {"q":"314. İslam’da bayram namazı kaç rekattır?","a":["2","4","6","8"],"c":0},
        {"q":"315. Peygamberimizin en çok hadis rivayet eden sahabesi kimdir?","a":["Hz. Ebubekir","Hz. Ömer","Hz. Aişe","Ebu Hureyre"],"c":3},
        {"q":"316. Kur’an’da kıble değişimi hangi surede geçmektedir?","a":["Bakara","Nisa","Maide","Tevbe"],"c":0},
        {"q":"317. Peygamberimizin hicret sırasında yanındaki arkadaşı kimdir?","a":["Hz. Ali","Hz. Ebubekir","Hz. Osman","Hz. Ömer"],"c":1},
        {"q":"318. İslam’da ilk mescid hangisidir?","a":["Mescid-i Haram","Mescid-i Nebevi","Kuba Mescidi","Mescid-i Aksa"],"c":2},
        {"q":"319. Kur’an’da geçen 'İkra' emri hangi surede yer alır?","a":["Alak","Bakara","Fatiha","Yasin"],"c":0},
        {"q":"320. Peygamberimizin veda hutbesi hangi yılda yapılmıştır?","a":["630","631","632","633"],"c":2},
    ], 
    [  
       # test 32 (321-330)
        {"q":"321. İslam’da ilk şehit erkek sahabe kimdir?","a":["Hz. Ammar","Hz. Musab","Hz. Ali","Hz. Ebubekir"],"c":1},
        {"q":"322. Kur’an’da en kısa ayet hangisidir?","a":["Rahman","Taha","Yasin","Müddessir"],"c":3},
        {"q":"323. Peygamberimizin doğduğu şehir hangisidir?","a":["Medine","Mekke","Taif","Kudüs"],"c":1},
        {"q":"324. İslam’da ilk vahiy hangi mağarada gelmiştir?","a":["Sevr","Hira","Nur","Uhud"],"c":1},
        {"q":"325. Kur’an’da adı geçen tek deniz hangisidir?","a":["Kızıldeniz","Akdeniz","Karadeniz","Nil"],"c":0},
        {"q":"326. Peygamberimizin hicret ettiği yıl hangi takvimin başlangıcıdır?","a":["Miladi","Rumi","Hicri","Celali"],"c":2},
        {"q":"327. İslam’da zekat kimlere verilmez?","a":["Fakirlere","Yolculara","Zenginlere","Borçlulara"],"c":2},
        {"q":"328. Kur’an’da adı geçen tek kadın peygamber var mıdır?","a":["Evet","Hayır","Bilinmiyor","Tartışmalı"],"c":1},
        {"q":"329. Peygamberimizin en küçük oğlu kimdir?","a":["Hz. Kasım","Hz. Abdullah","Hz. İbrahim","Hz. Hasan"],"c":2},
        {"q":"330. İslam’da ilk ezanı okuyan sahabe kimdir?","a":["Hz. Ali","Bilal-i Habeşi","Hz. Ebubekir","Hz. Ömer"],"c":1},
    ],
    [  
       # test 33 (331-340)
        {"q":"331. Kur’an’da en çok tekrar edilen ayet hangi surede geçer?","a":["Rahman","Bakara","Yasin","İhlas"],"c":0},
        {"q":"332. Peygamberimizin hicret sonrası inşa ettiği mescid hangisidir?","a":["Mescid-i Aksa","Mescid-i Nebevi","Mescid-i Kıbleteyn","Kuba Mescidi"],"c":1},
        {"q":"333. İslam’da ilk şehit çocuk kimdir?","a":["Hz. Hüseyin","Hz. Hasan","Hz. Abdullah","Hz. Kasım"],"c":0},
        {"q":"334. Kur’an’da en uzun sure hangisidir?","a":["Bakara","Al-i İmran","Nisa","Maide"],"c":0},
        {"q":"335. Peygamberimizin en çok sevdiği yiyeceklerden biri hangisidir?","a":["Hurmayı","Balı","Sütü","Zeytini"],"c":0},
        {"q":"336. İslam’da ilk vahiy hangi ayda gelmiştir?","a":["Recep","Şaban","Ramazan","Muharrem"],"c":2},
        {"q":"337. Kur’an’da adı geçen tek dağ hangisidir?","a":["Uhud","Cudi","Hira","Sevr"],"c":1},
        {"q":"338. Peygamberimizin en çok hadis rivayet eden eşi kimdir?","a":["Hz. Hatice","Hz. Aişe","Hz. Sevde","Hz. Hafsa"],"c":1},
        {"q":"339. İslam’da ilk bayram namazı nerede kılınmıştır?","a":["Kabe","Mescid-i Nebevi","Ranuna Vadisi","Kuba Mescidi"],"c":2},
        {"q":"340. Kur’an’da adı geçen tek böcek hangisidir?","a":["Arı","Karınca","Çekirge","Kelebek"],"c":1},
    ],       
    [  
       # test 34 (341-350)
        {"q":"341. Peygamberimizin en çok sevdiği renk hangisidir?","a":["Yeşil","Beyaz","Siyah","Kırmızı"],"c":1},
        {"q":"342. İslam’da ilk hutbe nerede okunmuştur?","a":["Kuba","Ranuna","Mekke","Medine"],"c":1},
        {"q":"343. Kur’an’da adı geçen tek şehir hangisidir?","a":["Mekke","Medine","Kudüs","Taif"],"c":0},
        {"q":"344. Peygamberimizin en çok sevdiği içecek hangisidir?","a":["Su","Süt","Bal şerbeti","Hurmalı içecek"],"c":1},
        {"q":"345. İslam’da ilk şehit sahabe kimdir?","a":["Hz. Ammar","Hz. Musab","Hz. Ali","Hz. Ebubekir"],"c":1},
        {"q":"346. Kur’an’da adı geçen kavimlerden biri hangisidir?","a":["Âd Kavmi","Nuh Kavmi","Semud Kavmi","Medyan Kavmi"],"c":1},
        {"q":"347. Kur’an’da adı geçen tek hayvan hangisidir?","a":["Deve","At","Fil","Kuş"],"c":2},
        {"q":"348. Peygamberimizin en çok sevdiği meyve hangisidir?","a":["Hurma","Zeytin","Nar","Üzüm"],"c":0},
        {"q":"349. İslam’da ilk ezan nerede okunmuştur?","a":["Mekke","Medine","Kuba","Taif"],"c":1},
        {"q":"350. Kur’an’da adı geçen tek bitki hangisidir?","a":["Zeytin","Hurmanın","Buğday","Arpa"],"c":0},
    ],      
    [  
       # test 35 (351-360)
        {"q":"351. İslam’da ilk namaz nerede kılınmıştır?","a":["Kabe","Mescid-i Nebevi","Kuba Mescidi","Ranuna Vadisi"],"c":0},
        {"q":"352. Kur’an’da adı geçen kavimlerden biri hangisidir?","a":["Âd Kavmi","Nuh Kavmi","Semud Kavmi","Medyan Kavmi"],"c":1},
        {"q":"353. Peygamberimizin en çok sevdiği tatlı hangisidir?","a":["Bal","Hurmalı tatlı","Sütlaç","Şerbet"],"c":0},
        {"q":"354. İslam’da ilk hutbe nerede okunmuştur?","a":["Mekke","Medine","Kuba","Ranuna"],"c":3},
        {"q":"355. Kur’an’da adı geçen şehirlerden biri hangisidir?","a":["Mekke","Medine","Kudüs","Taif"],"c":0},
        {"q":"356. Peygamberimizin en çok sevdiği giysi hangisidir?","a":["Beyaz elbise","Yeşil cübbe","Keten gömlek","Yün hırka"],"c":0},
        {"q":"357. Kur’an’da adı geçen peygamberlerden biri kimdir?","a":["Hz. İdris","Hz. Lokman","Hz. Zülkarneyn","Hz. Harun"],"c":3},
        {"q":"358. Peygamberimizin en çok sevdiği dua hangisidir?","a":["İstiğfar","Salavat","Fatiha","Ayet-el Kürsi"],"c":0},
        {"q":"359. Kur’an’da adı geçen bir kuş hangisidir?","a":["Hüdhüd","Serçe","Güvercin","Kartal"],"c":0},
        {"q":"360. Peygamberimizin en çok sevdiği silah hangisidir?","a":["Kılıç","Mızrak","Ok","Yay"],"c":0},
    ],           
    [  
       # test 36 (361-370)
        {"q":"361. İslam’da ilk namaz kılınan yer neresidir?","a":["Kabe","Mescid-i Nebevi","Kuba Mescidi","Ranuna Vadisi"],"c":0},
        {"q":"362. Kur’an’da adı geçen kavimlerden biri hangisidir?","a":["Âd Kavmi","Nuh Kavmi","Semud Kavmi","Medyan Kavmi"],"c":2},
        {"q":"363. Peygamberimizin en çok sevdiği içecek hangisidir?","a":["Su","Süt","Bal şerbeti","Hurmalı içecek"],"c":1},
        {"q":"364. İslam’da ilk ezan okunan şehir hangisidir?","a":["Mekke","Medine","Kuba","Taif"],"c":1},
        {"q":"365. Kur’an’da adı geçen şehirlerden biri hangisidir?","a":["Mekke","Medine","Kudüs","Taif"],"c":0},
        {"q":"366. Kur’an’da adı geçen peygamberlerden biri kimdir?","a":["Hz. İdris","Hz. Lokman","Hz. Harun","Hz. Zülkarneyn"],"c":2},
        {"q":"367. Peygamberimizin en çok sevdiği yiyeceklerden biri hangisidir?","a":["Hurma","Bal","Süt","Zeytin"],"c":0},
        {"q":"368. Kur’an’da adı geçen bir deniz hangisidir?","a":["Kızıldeniz","Akdeniz","Nil","Fırat"],"c":0},
        {"q":"369. Peygamberimizin en çok sevdiği sahabelerden biri kimdir?","a":["Hz. Ebubekir","Hz. Ali","Hz. Ömer","Hz. Osman"],"c":0},
        {"q":"370. Kur’an’da adı geçen bir dağ hangisidir?","a":["Cudi","Uhud","Hira","Sevr"],"c":0}
    ]
]


# =================================================
# SERTİFİKA OLUŞTURMA
# =================================================
def sertifika_olustur(isim, skor):
    tarih = datetime.datetime.now().strftime("%d.%m.%Y")
    kod = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    qr_data = f"Katılımcı: {isim}\nSkor: {skor}\nKod: {kod}\nTarih: {tarih}"

    qr = qrcode.make(qr_data)
    qr = qr.resize((150, 150))

    img = Image.new("RGB", (800, 600), "white")
    draw = ImageDraw.Draw(img)

    try:
        font_baslik = ImageFont.truetype("arial.ttf", 40)
        font_icerik = ImageFont.truetype("arial.ttf", 24)
    except:
        font_baslik = ImageFont.load_default()
        font_icerik = ImageFont.load_default()

    draw.text((250, 50), "BAŞARI SERTİFİKASI", font=font_baslik, fill="black")
    draw.text((100, 150), f"Katılımcı: {isim}", font=font_icerik, fill="black")
    draw.text((100, 200), "İslami Bilgi Testi'ni başarıyla tamamlamıştır.", font=font_icerik, fill="black")
    draw.text((100, 250), f"Başarı Puanı: {skor}", font=font_icerik, fill="black")
    draw.text((100, 300), f"Sertifika Kodu: {kod}", font=font_icerik, fill="black")
    draw.text((100, 350), f"Tarih: {tarih}", font=font_icerik, fill="black")
    img.paste(qr, (600, 50))
    img.save("sertifika.png")
    return "sertifika.png"

# =================================================
# QUIZ UYGULAMASI
# =================================================
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("İslami Test Sistemi")
        self.current_test = 0
        self.current_question = 0
        self.score = 0

        # Üst frame: test kutuları
        top_frame = tk.Frame(root)
        top_frame.pack(pady=10)

        self.test_buttons = []
        for i in range(len(testler)):
            satir = i // 6
            sutun = i % 6
            btn = tk.Button(top_frame, text=f"Test {i+1}", width=12, height=2, state="disabled")
            btn.grid(row=satir, column=sutun, padx=5, pady=5)
            self.test_buttons.append(btn)

        # Orta frame: soru ve cevaplar
        middle_frame = tk.Frame(root)
        middle_frame.pack(pady=20)

        self.question_label = tk.Label(middle_frame, text="", font=("Arial", 14))
        self.question_label.pack(pady=10)

        self.answer_buttons = []
        for i in range(4):
            btn = tk.Button(middle_frame, text="", width=30, command=lambda i=i: self.check_answer(i))
            btn.pack(pady=5)
            self.answer_buttons.append(btn)

        self.load_question()

    def load_question(self):
        if self.current_question < len(testler[self.current_test]):
            q = testler[self.current_test][self.current_question]
            self.question_label.config(text=q["q"])
            for i, ans in enumerate(q["a"]):
                self.answer_buttons[i].config(text=ans)
        else:
            self.test_buttons[self.current_test].config(bg="green", text=f"Test {self.current_test+1} ✅")
            self.current_test += 1
            self.current_question = 0
            if self.current_test < len(testler):
                self.load_question()
            else:
                self.finish_quiz()

    def check_answer(self, choice):
        q = testler[self.current_test][self.current_question]
        if choice == q["c"]:
            self.score += 1
        self.current_question += 1
        self.load_question()

    def finish_quiz(self):
        isim = simpledialog.askstring("Sertifika", "Lütfen adınızı giriniz:")
        if isim:
            skor = f"{self.score}/{len(testler)*10}"
            dosya = sertifika_olustur(isim, skor)
            img = Image.open(dosya)
            img = img.resize((400, 300))
            img_tk = ImageTk.PhotoImage(img)

            sertifika = tk.Toplevel(self.root)
            sertifika.title("Sertifika")
            tk.Label(sertifika, text=f"Tebrikler {isim}!\nTesti tamamladınız.\nSkor: {skor}", font=("Arial", 14)).pack(pady=20)
            tk.Label(sertifika, image=img_tk).pack()
            sertifika.image = img_tk

# =================================================
# PROGRAM BAŞLATMA
# =================================================
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()



#   kutucuklar beyaz renktedir....  bir sonraki testte renkli yaptım .....

#   mükemmelliğe giden yoldayım .... 36 test 370 soru vardır... full çalışıyor ...harika bir iş çıkardım 

#   python3 "/home/ismail/Documents/Python/gtk-dersi/data/İslami Test/Soruları/islami_test_python_0.py" pardusda ...

   
#   pycharm community de altta solda terminale tıkla .... açılan pencereye alttaki kodu yapıştır ....

#   & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_45.py


#  & "E:/İslami Test Soruları/.venv/Scripts/python.exe" islami_test_python_45.py   Pardusda

# python3 "/home/ismail/Documents/Python/gtk-dersi/data/İslami Test/Soruları/islami_test_python_45.py" pardusda

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_45.py     windows da


# SONUNA KADAR İLERLEDİM mükemmel çalışıyor... başarı puanı gösteriyor...

#  C'deki Klasörü güncellemek için üst solda 4 çizgiye tıkla altta şu yazana tıkla ... Reload all from Disk


# python3 "/home/ismail/Documents/Python/gtk-dersi/data/İslami Test/Soruları/islami_test_python_0.py" pardusda

