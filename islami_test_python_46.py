

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
    ],
    [
       # test 37 (soru 361-370)
        {"q":"361. İslam’da ilk namaz kılınan yer neresidir?","a":["Kabe","Mescid-i Nebevi","Kuba Mescidi","Ranuna Vadisi"],"c":2},
        {"q":"362. Kur’an’da adı geçen kavimlerden biri hangisidir?","a":["Âd Kavmi","Nuh Kavmi","Semud Kavmi","Medyan Kavmi"],"c":0},
        {"q":"363. Peygamberimizin en çok sevdiği içecek hangisidir?","a":["Su","Süt","Bal şerbeti","Hurmalı içecek"],"c":1},
        {"q":"364. İslam’da ilk ezan okunan şehir hangisidir?","a":["Mekke","Medine","Kuba","Taif"],"c":1},
        {"q":"365. Kur’an’da adı geçen şehirlerden biri hangisidir?","a":["Mekke","Medine","Kudüs","Taif"],"c":0},
        {"q":"366. Kur’an’da adı geçen peygamberlerden biri kimdir?","a":["Hz. İdris","Hz. Lokman","Hz. Harun","Hz. Zülkarneyn"],"c":2},
        {"q":"367. Peygamberimizin en çok sevdiği yiyeceklerden biri hangisidir?","a":["Hurma","Bal","Süt","Zeytin"],"c":0},
        {"q":"368. Kur’an’da adı geçen bir deniz hangisidir?","a":["Kızıldeniz","Akdeniz","Nil","Fırat"],"c":0},
        {"q":"369. Peygamberimizin en çok sevdiği sahabelerden biri kimdir?","a":["Hz. Ebubekir","Hz. Ali","Hz. Ömer","Hz. Osman"],"c":0},
        {"q":"370. İslam’da ilk hutbe okunan yer neresidir?","a":["Kuba","Ranuna Vadisi","Mescid-i Nebevi","Arafat"],"c":1},
    ],
    [
       # test 38 (soru 371-380)
        {"q":"371. Kur’an’da adı geçen bir nehir hangisidir?","a":["Nil","Fırat","Dicle","Hepsi"],"c":3},
        {"q":"372. Peygamberimizin hicret ettiği şehir hangisidir?","a":["Mekke","Medine","Taif","Kudüs"],"c":1},
        {"q":"373. İslam’da ilk bayram namazı hangi şehirde kılınmıştır?","a":["Mekke","Medine","Kuba","Şam"],"c":1},
        {"q":"374. Kur’an’da adı geçen bir dağ hangisidir?","a":["Uhud","Sevr","Tur","Nur"],"c":2},
        {"q":"375. Peygamberimizin en çok sevdiği yiyeceklerden biri hangisidir?","a":["Hurma","Bal","Süt","Zeytin"],"c":0},
        {"q":"376. Kur’an’da adı geçen bir hayvan hangisidir?","a":["Deve","Köpek","Balık","Hepsi"],"c":3},
        {"q":"377. İslam’da ilk cuma hutbesi nerede okunmuştur?","a":["Kuba","Ranuna Vadisi","Mescid-i Nebevi","Arafat"],"c":1},
        {"q":"378. Kur’an’da adı geçen bir peygamberin babası kimdir?","a":["Hz. Yakup","Hz. İshak","Hz. İbrahim","Hz. Harun"],"c":0},
        {"q":"379. Peygamberimizin en çok sevdiği meyve hangisidir?","a":["Hurma","Üzüm","Nar","Elma"],"c":0},
        {"q":"380. İslam’da ilk bayram kurbanı nerede kesilmiştir?","a":["Mekke","Medine","Kuba","Arafat"],"c":1},
    ],
    [
       # test 39 (soru 381-390) 
        {"q":"381. Kur’an’da adı geçen bir bitki hangisidir?","a":["Zeytin","Buğday","Üzüm","Hepsi"],"c":3},
        {"q":"382. Peygamberimizin hicret yolculuğunda saklandığı mağara hangisidir?","a":["Hira","Sevr","Uhud","Nur"],"c":1},
        {"q":"383. İslam’da ilk bayram namazı hangi yılda kılınmıştır?","a":["1. Hicri yıl","2. Hicri yıl","3. Hicri yıl","5. Hicri yıl"],"c":1},
        {"q":"384. Kur’an’da adı geçen bir kuş hangisidir?","a":["Hüdhüd","Serçe","Güvercin","Kartal"],"c":0},
        {"q":"385. Peygamberimizin en çok sevdiği tatlı hangisidir?","a":["Bal","Hurma","Sütlaç","Üzüm"],"c":0},
        {"q":"386. İslam’da ilk cuma namazı nerede kılınmıştır?","a":["Kuba","Ranuna Vadisi","Mescid-i Nebevi","Arafat"],"c":1},
        {"q":"387. Kur’an’da adı geçen bir peygamberin annesi kimdir?","a":["Hz. Meryem","Hz. Asiye","Hz. Sare","Hz. Havva"],"c":0},
        {"q":"388. Peygamberimizin en çok sevdiği dua hangisidir?","a":["Rabbenâ âtinâ","Fatiha","İhlas","Salavat"],"c":0},
        {"q":"389. İslam’da ilk bayram hutbesi nerede okunmuştur?","a":["Mekke","Medine","Kuba","Arafat"],"c":1},
        {"q":"390. Kur’an’da adı geçen bir deniz hangisidir?","a":["Kızıldeniz","Akdeniz","Karadeniz","Nil"],"c":0},
    ],
    [
       # test 40 (soru 391-400)
        {"q":"391. İslam’da ilk mescid hangisidir?","a":["Mescid-i Haram","Mescid-i Nebevi","Kuba Mescidi","Mescid-i Aksa"],"c":2},
        {"q":"392. Kur’an’da adı geçen bir peygamberin kardeşi kimdir?","a":["Hz. Harun","Hz. İshak","Hz. Yusuf","Hz. Yahya"],"c":0},
        {"q":"393. Peygamberimizin en çok sevdiği dua hangisidir?","a":["Rabbenâ âtinâ","Fatiha","İhlas","Salavat"],"c":0},
        {"q":"394. İslam’da ilk bayram namazı hangi şehirde kılınmıştır?","a":["Mekke","Medine","Kuba","Şam"],"c":1},
        {"q":"395. Kur’an’da adı geçen bir peygamberin annesi kimdir?","a":["Hz. Meryem","Hz. Asiye","Hz. Sare","Hz. Havva"],"c":0},
        {"q":"396. Peygamberimizin en çok sevdiği yiyeceklerden biri hangisidir?","a":["Hurma","Bal","Süt","Zeytin"],"c":0},
        {"q":"397. İslam’da ilk hutbe nerede okunmuştur?","a":["Kuba","Ranuna Vadisi","Mescid-i Nebevi","Arafat"],"c":1},
        {"q":"398. Kur’an’da adı geçen bir dağ hangisidir?","a":["Uhud","Sevr","Tur","Nur"],"c":2},
        {"q":"399. Peygamberimizin en çok sevdiği sahabelerden biri kimdir?","a":["Hz. Ebubekir","Hz. Ali","Hz. Ömer","Hz. Osman"],"c":0},
        {"q":"400. İslam’da ilk hutbe okunan yer neresidir?","a":["Kuba","Ranuna Vadisi","Mescid-i Nebevi","Arafat"],"c":1},
    ],
    [
       # test 41 (soru 401-410)
        {"q":"401. İslam’da ilk bayram namazı hangi yılda kılındı?","a":["1. Hicri yıl","2. Hicri yıl","3. Hicri yıl","5. Hicri yıl"],"c":1},
        {"q":"402. Kur’an’da adı geçen bir peygamberin kardeşi kimdir?","a":["Hz. Harun","Hz. Yusuf","Hz. İshak","Hz. Yahya"],"c":0},
        {"q":"403. Peygamberimizin en çok sevdiği dua hangisidir?","a":["Rabbenâ âtinâ","Fatiha","İhlas","Salavat"],"c":0},
        {"q":"404. İslam’da ilk hutbe nerede okunmuştur?","a":["Kuba","Ranuna Vadisi","Mescid-i Nebevi","Arafat"],"c":1},
        {"q":"405. Kur’an’da adı geçen bir dağ hangisidir?","a":["Uhud","Sevr","Tur","Nur"],"c":2},
        {"q":"406. Peygamberimizin en çok sevdiği sahabelerden biri kimdir?","a":["Hz. Ebubekir","Hz. Ali","Hz. Ömer","Hz. Osman"],"c":0},
        {"q":"407. İslam’da ilk mescid hangisidir?","a":["Mescid-i Haram","Mescid-i Nebevi","Kuba Mescidi","Mescid-i Aksa"],"c":2},
        {"q":"408. Kur’an’da adı geçen bir peygamberin annesi kimdir?","a":["Hz. Meryem","Hz. Asiye","Hz. Sare","Hz. Havva"],"c":0},
        {"q":"409. Peygamberimizin en çok sevdiği yiyeceklerden biri hangisidir?","a":["Hurma","Bal","Süt","Zeytin"],"c":0},
        {"q":"410. İslam’da ilk hutbe okunan yer neresidir?","a":["Kuba","Ranuna Vadisi","Mescid-i Nebevi","Arafat"],"c":1},
    ],
    [
       # test 42 (soru 411-420)
        {"q":"411. Kur’an’da adı geçen bir peygamberin babası kimdir?","a":["Hz. Yakup","Hz. İshak","Hz. İbrahim","Hz. Harun"],"c":0},
        {"q":"412. Peygamberimizin hicret ettiği şehir hangisidir?","a":["Mekke","Medine","Taif","Kudüs"],"c":1},
        {"q":"413. İslam’da ilk bayram kurbanı nerede kesilmiştir?","a":["Mekke","Medine","Kuba","Arafat"],"c":1},
        {"q":"414. Kur’an’da adı geçen bir kuş hangisidir?","a":["Hüdhüd","Serçe","Güvercin","Kartal"],"c":0},
        {"q":"415. Peygamberimizin en çok sevdiği tatlı hangisidir?","a":["Bal","Hurma","Sütlaç","Üzüm"],"c":0},
        {"q":"416. İslam’da ilk cuma namazı nerede kılınmıştır?","a":["Kuba","Ranuna Vadisi","Mescid-i Nebevi","Arafat"],"c":1},
        {"q":"417. Kur’an’da adı geçen bir bitki hangisidir?","a":["Zeytin","Buğday","Üzüm","Hepsi"],"c":3},
        {"q":"418. Peygamberimizin en çok sevdiği dua hangisidir?","a":["Rabbenâ âtinâ","Fatiha","İhlas","Salavat"],"c":0},
        {"q":"419. İslam’da ilk bayram hutbesi nerede okunmuştur?","a":["Mekke","Medine","Kuba","Arafat"],"c":1},
        {"q":"420. Kur’an’da adı geçen bir deniz hangisidir?","a":["Kızıldeniz","Akdeniz","Karadeniz","Nil"],"c":0},
    ],
    [
       # test 43 (soru 421-430)
        {"q":"421. İslam’da ilk mescid hangisidir?","a":["Mescid-i Haram","Mescid-i Nebevi","Kuba Mescidi","Mescid-i Aksa"],"c":2},
        {"q":"422. Kur’an’da adı geçen bir peygamberin kardeşi kimdir?","a":["Hz. Harun","Hz. Yusuf","Hz. İshak","Hz. Yahya"],"c":0},
        {"q":"423. Peygamberimizin en çok sevdiği dua hangisidir?","a":["Rabbenâ âtinâ","Fatiha","İhlas","Salavat"],"c":0},
        {"q":"424. İslam’da ilk hutbe nerede okunmuştur?","a":["Kuba","Ranuna Vadisi","Mescid-i Nebevi","Arafat"],"c":1},
        {"q":"425. Kur’an’da adı geçen bir dağ hangisidir?","a":["Uhud","Sevr","Tur","Nur"],"c":2},
        {"q":"426. Peygamberimizin en çok sevdiği sahabelerden biri kimdir?","a":["Hz. Ebubekir","Hz. Ali","Hz. Ömer","Hz. Osman"],"c":0},
        {"q":"427. İslam’da ilk mescid hangisidir?","a":["Mescid-i Haram","Mescid-i Nebevi","Kuba Mescidi","Mescid-i Aksa"],"c":2},
        {"q":"428. Kur’an’da adı geçen bir peygamberin annesi kimdir?","a":["Hz. Meryem","Hz. Asiye","Hz. Sare","Hz. Havva"],"c":0},
        {"q":"429. Peygamberimizin en çok sevdiği yiyeceklerden biri hangisidir?","a":["Hurma","Bal","Süt","Zeytin"],"c":0},
        {"q":"430. İslam’da ilk hutbe okunan yer neresidir?","a":["Kuba","Ranuna Vadisi","Mescid-i Nebevi","Arafat"],"c":1},
    ],
    [
       # test 44 (soru 431-440)
        {"q":"431. Kur’an’da adı geçen bir peygamberin babası kimdir?","a":["Hz. Yakup","Hz. İshak","Hz. İbrahim","Hz. Harun"],"c":0},
        {"q":"432. Peygamberimizin hicret ettiği şehir hangisidir?","a":["Mekke","Medine","Taif","Kudüs"],"c":1},
        {"q":"433. İslam’da ilk bayram kurbanı nerede kesilmiştir?","a":["Mekke","Medine","Kuba","Arafat"],"c":1},
        {"q":"434. Kur’an’da adı geçen bir kuş hangisidir?","a":["Hüdhüd","Serçe","Güvercin","Kartal"],"c":0},
        {"q":"435. Peygamberimizin en çok sevdiği tatlı hangisidir?","a":["Bal","Hurma","Sütlaç","Üzüm"],"c":0},
        {"q":"436. İslam’da ilk cuma namazı nerede kılınmıştır?","a":["Kuba","Ranuna Vadisi","Mescid-i Nebevi","Arafat"],"c":1},
        {"q":"437. Kur’an’da adı geçen bir bitki hangisidir?","a":["Zeytin","Buğday","Üzüm","Hepsi"],"c":3},
        {"q":"438. Peygamberimizin en çok sevdiği dua hangisidir?","a":["Rabbenâ âtinâ","Fatiha","İhlas","Salavat"],"c":0},
        {"q":"439. İslam’da ilk bayram hutbesi nerede okunmuştur?","a":["Mekke","Medine","Kuba","Arafat"],"c":1},
        {"q":"440. Kur’an’da adı geçen bir deniz hangisidir?","a":["Kızıldeniz","Akdeniz","Karadeniz","Nil"],"c":0},
    ],
    [
       # test 45 (soru 441-450)
        {"q":"441. İslam’da ilk mescid hangisidir?","a":["Mescid-i Haram","Mescid-i Nebevi","Kuba Mescidi","Mescid-i Aksa"],"c":2},
        {"q":"442. Kur’an’da adı geçen bir peygamberin kardeşi kimdir?","a":["Hz. Harun","Hz. Yusuf","Hz. İshak","Hz. Yahya"],"c":0},
        {"q":"443. Peygamberimizin en çok sevdiği dua hangisidir?","a":["Rabbenâ âtinâ","Fatiha","İhlas","Salavat"],"c":0},
        {"q":"444. İslam’da ilk hutbe nerede okunmuştur?","a":["Kuba","Ranuna Vadisi","Mescid-i Nebevi","Arafat"],"c":1},
        {"q":"445. Kur’an’da adı geçen bir dağ hangisidir?","a":["Uhud","Sevr","Tur","Nur"],"c":2},
        {"q":"446. Peygamberimizin en çok sevdiği sahabelerden biri kimdir?","a":["Hz. Ebubekir","Hz. Ali","Hz. Ömer","Hz. Osman"],"c":0},
        {"q":"447. İslam’da ilk bayram kurbanı nerede kesilmiştir?","a":["Mekke","Medine","Kuba","Arafat"],"c":1},
        {"q":"448. Kur’an’da adı geçen bir kuş hangisidir?","a":["Hüdhüd","Serçe","Güvercin","Kartal"],"c":0},
        {"q":"449. Peygamberimizin en çok sevdiği tatlı hangisidir?","a":["Bal","Hurma","Sütlaç","Üzüm"],"c":0},
        {"q":"450. İslam’da ilk cuma namazı nerede kılınmıştır?","a":["Kuba","Ranuna Vadisi","Mescid-i Nebevi","Arafat"],"c":1},
    ],
    [
       # test 46 (soru 451-460)
        {"q":"451. Kur’an’da adı geçen bir bitki hangisidir?","a":["Zeytin","Buğday","Üzüm","Hepsi"],"c":3},
        {"q":"452. Peygamberimizin hicret ettiği şehir hangisidir?","a":["Mekke","Medine","Taif","Kudüs"],"c":1},
        {"q":"453. İslam’da ilk bayram hutbesi nerede okunmuştur?","a":["Mekke","Medine","Kuba","Arafat"],"c":1},
        {"q":"454. Kur’an’da adı geçen bir peygamberin babası kimdir?","a":["Hz. Yakup","Hz. İshak","Hz. İbrahim","Hz. Harun"],"c":0},
        {"q":"455. Peygamberimizin en çok sevdiği yiyeceklerden biri hangisidir?","a":["Hurma","Bal","Süt","Zeytin"],"c":0},
        {"q":"456. İslam’da ilk hutbe okunan yer neresidir?","a":["Kuba","Ranuna Vadisi","Mescid-i Nebevi","Arafat"],"c":1},
        {"q":"457. Kur’an’da adı geçen bir deniz hangisidir?","a":["Kızıldeniz","Akdeniz","Karadeniz","Nil"],"c":0},
        {"q":"458. Peygamberimizin en çok sevdiği sahabelerden biri kimdir?","a":["Hz. Ebubekir","Hz. Ali","Hz. Ömer","Hz. Osman"],"c":0},
        {"q":"459. İslam’da ilk mescid hangisidir?","a":["Mescid-i Haram","Mescid-i Nebevi","Kuba Mescidi","Mescid-i Aksa"],"c":2},
        {"q":"460. Kur’an’da adı geçen bir dağ hangisidir?","a":["Uhud","Sevr","Tur","Nur"],"c":2},
    ],
    [
       # test 47 (soru 461-470)
        {"q":"461. Peygamberimizin hicret yolculuğunda saklandığı mağara hangisidir?","a":["Hira","Sevr","Uhud","Nur"],"c":1},
        {"q":"462. Kur’an’da adı geçen bir kuş hangisidir?","a":["Hüdhüd","Serçe","Güvercin","Kartal"],"c":0},
        {"q":"463. İslam’da ilk bayram namazı hangi şehirde kılınmıştır?","a":["Mekke","Medine","Kuba","Şam"],"c":1},
        {"q":"464. Peygamberimizin en çok sevdiği dua hangisidir?","a":["Rabbenâ âtinâ","Fatiha","İhlas","Salavat"],"c":0},
        {"q":"465. Kur’an’da adı geçen bir peygamberin annesi kimdir?","a":["Hz. Meryem","Hz. Asiye","Hz. Sare","Hz. Havva"],"c":0},
        {"q":"466. İslam’da ilk hutbe nerede okunmuştur?","a":["Kuba","Ranuna Vadisi","Mescid-i Nebevi","Arafat"],"c":1},
        {"q":"467. Kur’an’da adı geçen bir bitki hangisidir?","a":["Zeytin","Buğday","Üzüm","Hepsi"],"c":3},
        {"q":"468. Peygamberimizin en çok sevdiği tatlı hangisidir?","a":["Bal","Hurma","Sütlaç","Üzüm"],"c":0},
        {"q":"469. İslam’da ilk bayram hutbesi nerede okunmuştur?","a":["Mekke","Medine","Kuba","Arafat"],"c":1},
        {"q":"470. Kur’an’da adı geçen bir deniz hangisidir?","a":["Kızıldeniz","Akdeniz","Karadeniz","Nil"],"c":0},
    ],
    [
       # test 48 (soru 471-480)
        {"q":"471. İslam’da ilk mescid hangisidir?","a":["Mescid-i Haram","Mescid-i Nebevi","Kuba Mescidi","Mescid-i Aksa"],"c":2},
        {"q":"472. Kur’an’da adı geçen bir peygamberin kardeşi kimdir?","a":["Hz. Harun","Hz. Yusuf","Hz. İshak","Hz. Yahya"],"c":0},
        {"q":"473. Peygamberimizin en çok sevdiği dua hangisidir?","a":["Rabbenâ âtinâ","Fatiha","İhlas","Salavat"],"c":0},
        {"q":"474. İslam’da ilk hutbe nerede okunmuştur?","a":["Kuba","Ranuna Vadisi","Mescid-i Nebevi","Arafat"],"c":1},
        {"q":"475. Kur’an’da adı geçen bir dağ hangisidir?","a":["Uhud","Sevr","Tur","Nur"],"c":2},
        {"q":"476. Peygamberimizin en çok sevdiği sahabelerden biri kimdir?","a":["Hz. Ebubekir","Hz. Ali","Hz. Ömer","Hz. Osman"],"c":0},
        {"q":"477. İslam’da ilk bayram kurbanı nerede kesilmiştir?","a":["Mekke","Medine","Kuba","Arafat"],"c":1},
        {"q":"478. Kur’an’da adı geçen bir kuş hangisidir?","a":["Hüdhüd","Serçe","Güvercin","Kartal"],"c":0},
        {"q":"479. Peygamberimizin en çok sevdiği tatlı hangisidir?","a":["Bal","Hurma","Sütlaç","Üzüm"],"c":0},
        {"q":"480. İslam’da ilk cuma namazı nerede kılınmıştır?","a":["Kuba","Ranuna Vadisi","Mescid-i Nebevi","Arafat"],"c":1},
    ],
    [
       # test 49 (soru 481-490)
        {"q":"481. Kur’an’da adı geçen bir bitki hangisidir?","a":["Zeytin","Buğday","Üzüm","Hepsi"],"c":3},
        {"q":"482. Peygamberimizin hicret ettiği şehir hangisidir?","a":["Mekke","Medine","Taif","Kudüs"],"c":1},
        {"q":"483. İslam’da ilk bayram hutbesi nerede okunmuştur?","a":["Mekke","Medine","Kuba","Arafat"],"c":1},
        {"q":"484. Kur’an’da adı geçen bir peygamberin babası kimdir?","a":["Hz. Yakup","Hz. İshak","Hz. İbrahim","Hz. Harun"],"c":0},
        {"q":"485. Peygamberimizin en çok sevdiği yiyeceklerden biri hangisidir?","a":["Hurma","Bal","Süt","Zeytin"],"c":0},
        {"q":"486. İslam’da ilk hutbe okunan yer neresidir?","a":["Kuba","Ranuna Vadisi","Mescid-i Nebevi","Arafat"],"c":1},
        {"q":"487. Kur’an’da adı geçen bir deniz hangisidir?","a":["Kızıldeniz","Akdeniz","Karadeniz","Nil"],"c":0},
        {"q":"488. Peygamberimizin en çok sevdiği sahabelerden biri kimdir?","a":["Hz. Ebubekir","Hz. Ali","Hz. Ömer","Hz. Osman"],"c":0},
        {"q":"489. İslam’da ilk mescid hangisidir?","a":["Mescid-i Haram","Mescid-i Nebevi","Kuba Mescidi","Mescid-i Aksa"],"c":2},
        {"q":"490. Kur’an’da adı geçen bir dağ hangisidir?","a":["Uhud","Sevr","Tur","Nur"],"c":2},
    ],
    [
       # test 50 (soru 491-500)
        {"q":"491. Peygamberimizin hicret yolculuğunda saklandığı mağara hangisidir?","a":["Hira","Sevr","Uhud","Nur"],"c":1},
        {"q":"492. Kur’an’da adı geçen bir kuş hangisidir?","a":["Hüdhüd","Serçe","Güvercin","Kartal"],"c":0},
        {"q":"493. İslam’da ilk bayram namazı hangi şehirde kılınmıştır?","a":["Mekke","Medine","Kuba","Şam"],"c":1},
        {"q":"494. Peygamberimizin en çok sevdiği dua hangisidir?","a":["Rabbenâ âtinâ","Fatiha","İhlas","Salavat"],"c":0},
        {"q":"495. Kur’an’da adı geçen bir peygamberin annesi kimdir?","a":["Hz. Meryem","Hz. Asiye","Hz. Sare","Hz. Havva"],"c":0},
        {"q":"496. İslam’da ilk hutbe nerede okunmuştur?","a":["Kuba","Ranuna Vadisi","Mescid-i Nebevi","Arafat"],"c":1},
        {"q":"497. Kur’an’da adı geçen bir bitki hangisidir?","a":["Zeytin","Buğday","Üzüm","Hepsi"],"c":3},
        {"q":"498. Peygamberimizin en çok sevdiği tatlı hangisidir?","a":["Bal","Hurma","Sütlaç","Üzüm"],"c":0},
        {"q":"499. İslam’da ilk bayram hutbesi nerede okunmuştur?","a":["Mekke","Medine","Kuba","Arafat"],"c":1},
        {"q":"500. Kur’an’da adı geçen bir deniz hangisidir?","a":["Kızıldeniz","Akdeniz","Karadeniz","Nil"],"c":0},
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

    draw.text((100, 50), "BAŞARI SERTİFİKASI", font=font_baslik, fill="black")    # başlık yazısı ayarı burdan yap
    draw.text((100, 150), f"Katılımcı: {isim}", font=font_icerik, fill="black")
    draw.text((100, 200), "İslami Bilgi Testi'ni başarıyla tamamlamıştır.", font=font_icerik, fill="black")
    draw.text((100, 250), f"Başarı Puanı: {skor}", font=font_icerik, fill="black")
    draw.text((100, 300), f"Sertifika Kodu: {kod}", font=font_icerik, fill="black")
    draw.text((100, 350), f"Tarih: {tarih}", font=font_icerik, fill="black")
    img.paste(qr, (700, 30))                       # QR kodu nun konumudur ....sağ üst köşe ... buradan değiştir ...
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

        # Üst frame
        top_frame = tk.Frame(root)
        top_frame.pack(pady=10)

        renkler = [
            "#D6DEF8",  # açık mavi         #  kutucukların rengini buradan ayarla
            "#D5F5DA",  # açık yeşil        #  kutucukların rengini buradan ayarla
            "#FCF5CF",  # açık sarı         #  kutucukların rengini buradan ayarla
            "#FAE3D8",  # açık pembe        #  kutucukların rengini buradan ayarla
            "#EFDAEA",  # lavanta           #  kutucukların rengini buradan ayarla
        ]

        self.test_buttons = []
        for i in range(len(testler)):
            satir = i // 6
            sutun = i % 6
            grup_rengi = renkler[i // 10 % len(renkler)]
            btn = tk.Button(top_frame, text=f"Test {i+1}", width=12, height=2,
                            bg=grup_rengi, state="disabled")
            btn.grid(row=satir, column=sutun, padx=5, pady=5)
            self.test_buttons.append(btn)

        # Orta frame
        middle_frame = tk.Frame(root)
        middle_frame.pack(pady=20)

        self.question_label = tk.Label(middle_frame, text="", font=("Arial", 14))
        self.question_label.pack(pady=10)

        self.answer_buttons = []
        for i in range(4):
            btn = tk.Button(middle_frame, text="", width=30,
                            command=lambda i=i: self.check_answer(i))
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
            self.test_buttons[self.current_test].config(bg="green", fg="white",
                                                        text=f"Test {self.current_test+1} ✅")
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
        
'''
..bu bölümü gizledim .... Eger biraz farklı olan alltaki kod çalıssa bunu aktif et ...

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
            tk.Label(sertifika, text=f"Tebrikler {isim}!\nTesti tamamladınız.\nSkor: {skor}",
                     font=("Arial", 14)).pack(pady=20)
            tk.Label(sertifika, image=img_tk).pack()
            sertifika.image = img_tk
            
..alttaki kodu test et .........
          
'''


def finish_quiz(self):
    isim = simpledialog.askstring("Sertifika", "Lütfen adınızı giriniz:")
    if isim:
        # FIX: Toplam soru sayısını dinamik olarak hesapla
        total_questions = sum(len(test) for test in testler)
        skor = f"{self.score}/{total_questions}"
        
        dosya = sertifika_olustur(isim, skor)
        img = Image.open(dosya)
        img = img.resize((400, 300))
        img_tk = ImageTk.PhotoImage(img)

        sertifika = tk.Toplevel(self.root)
        sertifika.title("Sertifika")
        
        # FIX: Daha detaylı bilgi göster
        percentage = (self.score / total_questions) * 100
        tk.Label(sertifika, 
                text=f"Tebrikler {isim}!\nTesti tamamladınız.\nSkor: {skor}\nBaşarı: %{percentage:.1f}",
                font=("Arial", 14)).pack(pady=20)
        tk.Label(sertifika, image=img_tk).pack()
        sertifika.image = img_tk




# =================================================
# PROGRAM BAŞLATMA
# =================================================
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

'''
      ............ cevap anahtarı ...........


001-C, 002-B, 003-D, 004-B, 005-C, 006-C, 007-B, 008-B, 009-C, 010-C,

011-C, 012-C, 013-C, 014-C, 015-D, 016-B, 017-A, 018-B, 019-A, 020-A,

021-A, 022-A, 023-C, 024-B, 025-B, 026-B, 027-B, 028-D, 029-D, 030-B,

031-C, 032-C, 033-B, 034-B, 035-C, 036-B, 037-B, 038-C, 039-B, 040-D,

041-B, 042-C, 043-A, 044-B, 045-B, 046-C, 047-C, 048-C, 049-B, 050-D,

051-B, 052-B, 053-B, 054-C, 055-C, 056-B, 057-D, 058-A, 059-A, 060-A,

061-A, 062-D, 063-B, 064-C, 065-C, 066-C, 067-A, 068-C, 069-B, 070-C,

071-B, 072-D, 073-D, 074-B, 075-C, 076-B, 077-B, 078-B, 079-A, 080-B,

081-C, 082-D, 083-A, 084-B, 085-C, 086-A, 087-C, 088-B, 089-A, 090-B,

091-A, 092-B, 093-A, 094-C, 095-B, 096-B, 097-A, 098-A, 099-C, 100-C,

111-B, 112-A, 113-C, 114-C, 115-B, 116-B, 117-A, 118-C, 119-B, 120-A,

121-A, 122-C, 123-C, 124-C, 125-B, 126-B, 127-D, 128-A, 129-B, 130-B,

131-B, 132-C, 133-C, 134-B, 135-B, 136-B, 137-B, 138-C, 139-B, 140-C,

141-C, 142-A, 143-B, 144-C, 145-C, 146-A, 147-B, 148-B, 149-B, 150-B,

151-B, 152-B, 153-A, 154-B, 155-B, 156-B, 157-C, 158-C, 159-C, 160-A,

161-B, 162-A, 163-A, 164-B, 165-B, 166-C, 167-B, 168-A, 169-B, 170-C,

171-B, 172-C, 173-A, 174-B, 175-C, 176-C, 177-D, 178-A, 179-B, 180-B,

181-C, 182-C, 183-C, 184-D, 185-A, 186-C, 187-B, 188-A, 189-C, 190-C,

191-D, 192-B, 193-C, 194-A, 195-B, 196-B, 197-C, 198-B, 199-C, 200-B,

201-D, 202-B, 203-B, 204-C, 205-A, 206-B, 207-B, 208-B, 209-A, 210-B,

211-C, 212-B, 213-C, 214-B, 215-C, 216-B, 217-A, 218-C, 219-B, 220-C,

221-A, 222-B, 223-B, 224-B, 225-A, 226-A, 227-A, 228-C, 229-A, 230-B,

231-C, 232-B, 233-B, 234-B, 235-A, 236-A, 237-A, 238-C, 239-A, 240-B,

241-C, 242-B, 243-A, 244-A, 245-D, 246-A, 247-B, 248-C, 249-A, 250-C,

251-A, 252-D, 253-B, 254-B, 255-A, 256-C, 257-C, 258-B, 259-C, 260-B,

261-A, 262-B, 263-A, 264-A, 265-A, 266-C, 267-B, 268-B, 269-C, 270-B,

271-B, 272-B, 273-A, 274-B, 275-B, 276-C, 277-A, 278-B, 279-A, 280-B,

281-D, 282-B, 283-A, 284-B, 285-A, 286-A, 287-A, 288-A, 289-A, 290-A,

291-D, 292-B, 293-A, 294-B, 295-A, 296-A, 297-A, 298-A, 299-A, 300-A,

301-A, 302-B, 303-B, 304-B, 305-A, 306-A, 307-A, 308-C, 309-A, 310-B,

311-C, 312-B, 313-A, 314-A, 315-D, 316-A, 317-B, 318-C, 319-A, 320-C,

321-B, 322-D, 323-B, 324-B, 325-A, 326-C, 327-C, 328-B, 329-C, 330-B,

331-A, 332-B, 333-A, 334-A, 335-A, 336-C, 337-B, 338-B, 339-C, 340-B,

341-B, 342-B, 343-A, 344-B, 345-B, 346-B, 347-C, 348-A, 349-B, 350-A,

351-A, 352-B, 353-A, 354-D, 355-A, 356-A, 357-D, 358-A, 359-A, 360-A,

361-A, 362-C, 363-B, 364-B, 365-A, 366-C, 367-A, 368-A, 369-A, 370-A,

371-D, 372-B, 373-B, 374-C, 375-A, 376-D, 377-B, 378-A, 379-A, 380-B,

381-D, 382-B, 383-B, 384-A, 385-A, 386-B, 387-A, 388-A, 389-B, 390-A,

391-C, 392-A, 393-A, 394-B, 395-A, 396-A, 397-B, 398-C, 399-A, 400-B,

401-B, 402-A, 403-A, 404-B, 405-C, 406-A, 407-C, 408-A, 409-A, 410-B,

411-A, 412-B, 413-B, 414-A, 415-A, 416-B, 417-D, 418-A, 419-B, 420-A,

421-C, 422-A, 423-A, 424-B, 425-C, 426-A, 427-C, 428-A, 429-A, 430-B,

431-A, 432-B, 433-B, 434-A, 435-A, 436-B, 437-D, 438-A, 439-B, 440-A,

441-C, 442-A, 443-A, 444-B, 445-C, 446-A, 447-B, 448-A, 449-A, 450-B,

451-D, 452-B, 453-B, 454-A, 455-A, 456-B, 457-A, 458-A, 459-C, 460-C,

461-B, 462-A, 463-B, 464-A, 465-A, 466-B, 467-D, 468-A, 469-B, 470-A,

471-C, 472-A, 473-A, 474-B, 475-C, 476-A, 477-B, 478-A, 479-A, 480-B,

481-D, 482-B, 483-B, 484-A, 485-A, 486-B, 487-A, 488-A, 489-C, 490-C,

491-B, 492-A, 493-B, 494-A, 495-A, 496-B, 497-D, 498-A, 499-B, 500-A


'''


#   kutucuklar  renklidir... 500 soru vardır ...  50 test vardır .....

#   mükemmelliğe giden yoldayım .... 50 test 500 soru vardır... full çalışıyor ...harika bir iş çıkardım 

#   python3 "/home/ismail/Documents/Python/gtk-dersi/data/İslami Test/Soruları/islami_test_python_0.py" pardusda ...

   
#   pycharm community de altta solda terminale tıkla .... açılan pencereye alttaki kodu yapıştır ....

#   & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_46.py


#  & "E:/İslami Test Soruları/.venv/Scripts/python.exe" islami_test_python_46.py   Pardusda

# python3 "/home/ismail/Documents/Python/gtk-dersi/data/İslami Test/Soruları/islami_test_python_46.py" pardusda

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_46.py     windows da


# SONUNA KADAR İLERLEDİM mükemmel çalışıyor... başarı puanı gösteriyor...

#  C'deki Klasörü güncellemek için üst solda 4 çizgiye tıkla altta şu yazana tıkla ... Reload all from Disk


# python3 "/home/ismail/Documents/Python/gtk-dersi/data/İslami Test/Soruları/islami_test_python_0.py" pardusda










