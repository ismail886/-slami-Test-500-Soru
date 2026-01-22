import tkinter as tk
from tkinter import messagebox
import platform
import os

def ses_cal(durum):
    try:
        if platform.system() == "Windows":
            import winsound
            if durum == "dogru":
                winsound.MessageBeep(winsound.MB_ICONASTERISK)
            else:
                winsound.MessageBeep(winsound.MB_ICONHAND)
        else:
            if durum == "dogru":
                os.system("paplay dogru.wav >/dev/null 2>&1 &")
            else:
                os.system("paplay yanlis.wav >/dev/null 2>&1 &")
    except Exception:
        pass

# Test soruları (örnek: TEST_1 ve TEST_2)
testler = {
    1: [
           #  01.....10 a kadar sorular
        ("İslam'ın beş şartından biri olan ve zengin Müslümanların yılda bir kez mallarının belirli bir kısmını ihtiyaç sahiplerine vermesi anlamına gelen ibadet hangisidir?",["Zekat", "Sadaka", "Hac", "Fitre"], "A"),
        ("Kur'an-ı Kerim'in en uzun suresi aşağıdakilerden hangisidir?", ["Al-i İmran", "Bakara", "Nisa", "Maide"], "B"),
        ("İmanın şartlarından biri olan 'Kaza ve Kadere İman', aşağıdakilerden hangisini kapsar?",["Sadece geçmişte yaşanan olayları","Allah'ın her şeyi bir ölçüye göre takdir etmesi ve zamanı gelince gerçekleşmesi","Sadece insanların kendi özgür iradesiyle yaptığı seçimleri","Doğa olaylarının tesadüfen meydana gelmesini"], "B"),
        ("Peygamber Efendimiz (s.a.v.)'in gece vakti Mescid-i Haram'dan Mescid-i Aksa'ya götürülmesine ne ad verilir?", ["Hicret", "Miraç", "İsra", "Vahiy"], "C"),
        ("Aşağıdakilerden hangisi abdestin farzlarından biri değildir?", ["Yüzü yıkamak", "Ağza ve burna su vermek", "Elleri dirseklerle beraber yıkamak", "Başın dörtte birini meshetmek"], "B"),
        ("Kur'an-ı Kerim hangi halife döneminde kitap (mushaf) haline getirilmiştir?", ["Hz. Ebubekir", "Hz. Ömer", "Hz. Osman", "Hz. Ali"], "A"),
        ("İslam dininde 'Ef'al-i Mükellefin' içinde yer alan ve yapılması kesin olarak yasaklanan fiillere ne denir?", ["Mekruh", "Haram", "Mübah", "Vacip"], "B"),
        ("Aşağıdakilerden hangisi Peygamber Efendimiz (s.a.v.)'in çocuklarından biri değildir?", ["Hz. Fatıma", "Hz. Kasım", "Hz. Ayşe", "Hz. İbrahim"], "C"),
        ("Kıblenin Kudüs'teki Mescid-i Aksa'dan Mekke'deki Kabe'ye çevrildiği olay ne zaman gerçekleşmiştir?", ["Hicretten 5 yıl önce", "Hicretten yaklaşık 1,5 yıl sonra", "Mekke'nin Fethinden hemen sonra", "Veda Haccı sırasında"], "B"),
        ("Allah'ın her şeyi görmesi sıfatına ne ad verilir?", ["İlim", "Semi", "Basar", "Kudret"], "C"),
    ],
    2: [
             # 11....20 e kadar sorular
        ("Allah'ın var ve bir olmasına ne ad verilir?", ["Tevhid", "Nübüvvet", "Ahiret", "Haşir"], "A"),
        ("İmanın şartlarından biri olmayan?", ["Meleklere inanmak", "Namaz kılmak", "Peygamberlere inanmak", "Kitaplara inanmak"], "B"),
        ("Zebur hangi peygambere indirilmiştir?", ["Hz. Musa", "Hz. İsa", "Hz. Davud", "Hz. İbrahim"], "C"),
        ("Öldükten sonra dirilmeye ne ad verilir?", ["Mizan", "Berzah", "Haşir", "Kıyamet"], "C"),
        ("Vahiy getiren melek?", ["Mikail", "Azrail", "İsrafil", "Cebrail"], "D"),
        ("Namaza başlarken alınan tekbir?", ["İftitah Tekbiri", "Kıyam", "Ka'de-i Ahire", "Secde"], "A"),
        ("Günde kaç vakit namaz farzdır?", ["3", "5", "7", "2"], "B"),
        ("Rükudan sonra alnı yere koymak?", ["Kıraat", "Secde", "Teşehhüd", "Selam"], "B"),
        ("Cemaatle kılınması zorunlu namaz?", ["Teravih", "Bayram", "Cuma", "Vitir"], "C"),
        ("Oruç tutamayanların verdiği bedel?", ["Zekat", "Sadaka", "Fidye", "Fitre"], "C"),
    ],
    3: [
           # 21....30 a kadar sorular ....  BURADA 11 SORU VAR  EKRANDADA ÇÖZÜLÜYOR ...
        ("Kuran'ın ilk suresi?", ["Bakara", "İhlas", "Fatiha", "Nas"], "C"),
        ("En kısa sure?", ["A) Kevser", "B) Fil", "C) Maun", "D) Kureyş"], "A"),
        ("En kısa sure?", ["A) Kevser", "B) Fil", "C) Maun", "D) Kureyş"], "A"),
        ("Besmelesiz sure?", ["A) Yasin", "B) Tevbe", "C) Rahman", "D) Mülk"], "B"),
        ("Kur'an kaç yılda tamamlandı?", ["A) 10", "B) 23", "C) 40", "D) 63"], "B"),
        ("Kur'an ezberleyen?", ["A) Müezzin", "B) İmam", "C) Hafız", "D) Alim"], "C"),
        ("Rızık melek?", ["A) Cebrail", "B) Mikail", "C) Azrail", "D) İsrafil"], "B"),
        ("Allah'ın işitmesi sıfatı?", ["A) İlim", "B) Semi", "C) Basar", "D) Kudret"], "B"),
        ("Peygamberlerin zekası?", ["A) Sıdk", "B) Emanet", "C) Fetanet", "D) Tebliğ"], "C"),
        ("20 sayfalık bölüm?", ["A) Sure", "B) Ayet", "C) Cüz", "D) Hizb"], "C"),
        ("Kabe'yi inşa eden oğul?", ["A) Hz. İshak", "B) Hz. İsmail", "C) Hz. Yakup", "D) Hz. Yusuf"], "B"),
        
    ],
    4: [
          # 31....40 a kadar sorular 
        ("Sadece zenginlere farz?", ["A) Namaz", "B) Oruç", "C) Kelime-i Şehadet", "D) Zekat"], "D"),
        ("Sabah namazı kaç rekat?", ["A) 2", "B) 4", "C) 6", "D) 10"], "B"),
        ("Peygamber kabri?", ["A) Makam-ı İbrahim", "B) Ravza-i Mutahhara", "C) Altınoluk", "D) Hacerü'l Esved"], "B"),
        ("Ramazan sünnet namazı?", ["A) Teheccüd", "B) İşrak", "C) Teravih", "D) Evvabin"], "C"),
        ("Can alan melek?", ["A) Azrail", "B) Mikail", "C) Münker", "D) Nekir"], "A"),
        ("Peygamber dedesi?", ["A) Ebu Talip", "B) Abdülmuttalib", "C) Abdullah", "D) Hamza"], "B"),
        ("İlk ezan okuyan?", ["A) Hz. Ebubekir", "B) Hz. Ali", "C) Bilal-i Habeşi", "D) Zeyd bin Sabit"], "C"),
        ("Mekke'den göç edenler?", ["A) Ensar", "B) Muhacir", "C) Mürted", "D) Münafık"], "B"),
        ("Medineli yardım edenler?", ["A) Ensar", "B) Muhacir", "C) Tabiun", "D) Sahabe"], "A"),
        ("Kur'an kalbi?", ["A) Bakara", "B) Yasin", "C) Mülk", "D) Fetih"], "B"),   
    ],
    5: [
           # 41....50 e kadar sorular
        ("Peygamber çocuğu olmayan?", ["A) Zeynep", "B) Ümmü Gülsüm", "C) Safiye", "D) Rukiye"], "C"),
        ("Ramazan Bayramı sadakası?", ["A) Fidye", "B) Fitre", "C) Öşür", "D) Haraç"], "B"),
        ("Kabe hangi şehirde?", ["A) Medine", "B) Cidde", "C) Mekke", "D) Riyad"], "C"),
        ("Allah'ın gücü sıfatı?", ["A) İlim", "B) Kudret", "C) İrade", "D) Tekvin"], "B"),
        ("El-Emin lakabı?", ["A) Hz. Ebubekir", "B) Hz. Ömer", "C) Hz. Muhammed", "D) Hz. Süleyman"], "C"),
        ("Bismillah anlamı?", ["A) Allah en büyüktür", "B) Rahman Rahim Allah adıyla", "C) Hamd Allah'adır", "D) Allah birdir"], "B"),
        ("Müslüman hakkı?", ["A) Selamını almak", "B) Malını almak", "C) Sırrını ifşa", "D) Eleştirmek"], "A"),
        ("İlk eş?", ["A) Hz. Ayşe", "B) Hz. Hafsa", "C) Hz. Hatice", "D) Hz. Sevde"], "C"),
        ("Ameller terazisi?", ["A) Sırat", "B) Mizan", "C) Mahşer", "D) Berzah"], "B"),
        ("İslam temel kaynağı?", ["A) Hadis kitapları", "B) İlmihal", "C) Kur'an-ı Kerim", "D) Fıkıh kitapları"], "C"),
       
    ],
    6: [
           # 51....60 a kadar sorular
        ("İslam'da kibirli olmak hangi davranıştır?", ["Günah", "Sevap", "Farz", "Sünnet"], "A"),
        ("Peygamberimizin son hutbesine ne ad verilir?", ["Veda Hutbesi", "Miraç Hutbesi", "Cuma Hutbesi", "Tebliğ Hutbesi"], "A"),
        ("Namazda okunan kısa surelere ne denir?", ["Uzun sure", "Mekki sure", "Kısa sure", "Zamm-ı sure"], "D"),
        ("Kur'an'da cennet için kullanılan isim hangisidir?", ["Sırat", "Firdevs", "Araf", "Kevser"], "B"),
        ("İslam'da israf neyi ifade eder?", ["Tasarruf", "Ölçülü olmak", "Gereksiz harcama", "Yardımlaşma"], "C"),
        ("Peygamberimizin kabri hangi mescidin içindedir?", ["Mescid-i Haram", "Mescid-i Aksa", "Mescid-i Nebevi", "Kuba Mescidi"], "C"),
        ("Kur'an'da cehennem için kullanılan isim hangisidir?", ["Kevser", "Sırat", "Cehim", "Firdevs"], "B"),
        ("İslam'da doğru sözlülüğe ne denir?", ["Sıdk", "Emanet", "İsmet", "Fetanet"], "A"),
        ("Peygamberimizin en yakın arkadaşı kimdir?", ["Hz. Ömer", "Hz. Ali", "Hz. Ebubekir", "Hz. Osman"], "C"),
        ("Kur'an'ın korunmasını Allah'ın üstlendiği ayet hangi surededir?", ["Bakara", "Hicr", "Yasin", "Nisa"], "B"),
        
    ],
    7: [
           # 61....70 e kadar sorular
        ("İslam'da misafire ikram etmek ne sayılır?", ["Zorunluluk", "Günah", "Sevap", "İsraf"], "C"),
        ("Peygamberimizin 'güzel ahlak' ile ilgili sözü hangi kavramı anlatır?", ["İbadet", "Ahlak", "Takva", "Sabır"], "C"),
        ("İslam'da helal–haramı belirleyen temel kaynak hangisidir?", ["Hadis", "İcma", "Kıyas", "Kur'an"], "D"),
        ("Kur'an'ın ana konusu nedir?", ["Tarih", "Ahlak", "İnanç", "Hepsi"], "C"),
        ("İslam'da sözünde durmak hangi kavramla ilgilidir?", ["Sabır", "Emanet", "Sıdk", "Takva"], "B"),
        ("Peygamberimizin son peygamber olması ne ile ifade edilir?", ["Risalet", "Nübüvvet", "Hatm-i Nübüvvet", "Tebliğ"], "C"),
        ("İslam'da insanların eşit olduğunu vurgulayan hutbe hangisidir?", ["Cuma Hutbesi", "Veda Hutbesi", "Miraç Hutbesi", "Tebliğ Hutbesi"], "A"),
        ("Peygamberlerin Allah'tan aldıkları emirleri insanlara eksiksiz iletmesine ne denir?", ["Emanet", "Tebliğ", "İsmet", "Fetanet"], "B"),
        ("Namaz kaç rekattır (farz namazların toplamı günlük)?", ["15", "17", "20", "40"], "A"),
        ("İslam'ın beş şartından biri olan şehadet nedir?", ["Tanıklık", "Namaz", "Oruç", "Zekât"], "A"),
        
    ],
    8: [
           # 71....80 e kadar sorular
        ("Kur'an'da kaç peygamberin ismi geçer?", ["23", "25", "27", "30"], "A"),   
        ("Hz. Muhammed'in peygamberliğe başladığı yaş kaçtır?", ["30", "35", "40", "45"], "C"),
        ("İslam'da namaz kılmanın vacip olduğu yaş kaçtır?", ["7", "10", "12", "15"], "C"),
        ("Kur'an'ın ilk mushaf haline getirilmesi hangi halife dönemindedir?", ["Hz. Ebubekir", "Hz. Ömer", "Hz. Osman", "Hz. Ali"], "B"),
        ("Bedir Savaşı hangi yılda olmuştur?", ["1. Hicri yıl", "2. Hicri yıl", "3. Hicri yıl", "5. Hicri yıl"], "B"),
        ("İslam'da sabır hangi kategoriye girer?", ["Farz", "Vacip", "Fazilet", "Sünnet"], "C"),
        ("Peygamberimizin annesi kimdir?", ["Amine", "Halime", "Hatice", "Aişe"], "A"),
        ("İslam'da gusül abdesti hangi durumda alınır?", ["Her namaz öncesi", "Sadece cuma", "Cünüplükten sonra", "Her gün"], "C"),
        ("Mekke'nin fethi hangi yılda gerçekleşmiştir?", ["6. Hicri yıl", "8. Hicri yıl", "10. Hicri yıl", "11. Hicri yıl"], "B"),
        ("İslam'da tevhid ne demektir?", ["Allah'ın birliği", "Namaz", "Oruç", "Hac"], "A"),
    ],
    9: [
           # 81....90 a kadar sorular
         ("Kur'an'ın nazil olduğu ilk mağaranın adı nedir?", ["Sevr", "Hira", "Uhud", "Nur"], "D"),
         ("İslam'da kadınların başını örtmesine ne denir?", ["Tesettür", "Takva", "Edep", "İffet"], "A"),
         ("Peygamberimizin ilk eşi kimdir?", ["Aişe", "Hatice", "Hafsa", "Sevde"], "B"),
         ("İslam'da faiz ne anlama gelir?", ["Haram kazanç", "Helal kazanç", "Ticaret", "Yardım"], "A"),
         ("Kur'an'da en çok geçen peygamber kimdir?", ["Hz. Muhammed", "Hz. İbrahim", "Hz. Musa", "Hz. İsa"], "C"),
         ("İslam'da kurban kesmek hangi ibadetle ilgilidir?", ["Ramazan", "Hac", "Cuma", "Zekât"], "B"),
         ("Namazda kaç defa secde yapılır (bir rekatta)?", ["1", "2", "3", "4"], "B"),
         ("İslam'da temizliğe verilen önem hangi sözle ifade edilir?", ["İmanın yarısı", "İmanın şartı", "İmanın tamamı", "Sünnet"], "A"),
         ("Kur'an'ın en kısa suresi hangisidir?", ["Kevser", "İhlas", "Nas", "Felak"], "A"),
         ("İslam'da namaz kılarken hangi yön önemlidir?", ["Doğu", "Batı", "Kıble", "Kuzey"], "C"),   
        
    ],
    10: [
             # 91....100 e kadar sorular
         ("Peygamberimizin vefat tarihi hangi ayda olmuştur?", ["Muharrem", "Safer", "Rebiulevvel", "Recep"], "C"),     
         ("Kabe etrafında 7 kez dönmek?", ["A) Say", "B) İhram", "C) Vakfe", "D) Tavaf"], "D"),
         ("Zekat için asgari zenginlik?", ["A) Nisap", "B) Miktar", "C) Öşür", "D) Fitre"], "A"),
         ("Peygamberimiz hangi şehirde doğdu?", ["A) Medine", "B) Kudüs", "C) Mekke", "D) Taif"], "C"),
         ("İlk vahiy nerede geldi?", ["A) Sevr Mağarası", "B) Hira Mağarası", "C) Mescid-i Nebevi", "D) Kabe"], "B"),
         ("İlk hicret yeri?", ["A) Habeşistan", "B) Medine", "C) Mısır", "D) Bağdat"], "A"),
         ("Hicret yol arkadaşı?", ["A) Hz. Ömer", "B) Hz. Ali", "C) Hz. Ebubekir", "D) Hz. Osman"], "C"),
         ("İlk büyük savaş?", ["A) Uhud", "B) Hendek", "C) Bedir", "D) Hayber"], "C"),
         ("Peygamberimizin vefat şehri?", ["A) Mekke", "B) Cidde", "C) Şam", "D) Medine"], "D"),
         ("Kur'an'da kaç cüz var?", ["A) 20", "B) 30", "C) 40", "D) 114"], "B"),   
    ]
}   


tamamlanan_testler = set()
aktif_test = 1

root = tk.Tk()
root.title("İslami Test Paneli")
root.geometry("700x600")
root.configure(bg="lightgray")

def test_ac(test_no):
    if test_no > aktif_test:
        messagebox.showwarning(
            "Uyarı",
            "Bu teste geçmek için önceki testi tamamlamalısınız."
        )
        return

    pencere = tk.Toplevel(root)
    pencere.title(f"TEST_{test_no}")
    pencere.geometry("700x500")

    sorular = testler[test_no]
    index = 0
    dogru_sayisi = 0
    cevap = tk.StringVar()

    def sonraki_soru():
        nonlocal index, dogru_sayisi

        if cevap.get() == sorular[index][2]:
            dogru_sayisi += 1
            ses_cal("dogru")
        else:
            ses_cal("yanlis")

        index += 1
        if index < len(sorular):
            soru_goster()
        else:
            pencere.destroy()
            sonuc_goster(test_no, dogru_sayisi)

    def soru_goster():
        soru_label.config(
            text=f"Soru {index + 1}: {sorular[index][0]}"
        )
        cevap.set(None)
        for i, secenek in enumerate(sorular[index][1]):
            radio_btns[i].config(
                text=secenek,
                value=chr(65 + i)
            )

    soru_label = tk.Label(
        pencere,
        text="",
        wraplength=600,
        font=("Arial", 12)
    )
    soru_label.pack(pady=20)

    radio_btns = []
    for i in range(4):
        rb = tk.Radiobutton(
            pencere,
            text="",
            variable=cevap,
            value="",
            font=("Arial", 11)
        )
        rb.pack(anchor="w")
        radio_btns.append(rb)

    onay_btn = tk.Button(
        pencere,
        text="Cevabı Onayla",
        command=sonraki_soru
    )
    onay_btn.pack(pady=20)

    soru_goster()

def sonuc_goster(test_no, dogru_sayisi):
    global aktif_test

    toplam_soru = len(testler[test_no])
    durum = "GEÇTİ ✅" if dogru_sayisi >= 7 else "KALDI ❌"

    messagebox.showinfo(
        "Test Sonucu",
        f"Doğru Sayısı: {dogru_sayisi}/{toplam_soru}\nDurum: {durum}"
    )

    if dogru_sayisi >= 7:
        tamamlanan_testler.add(test_no)
        aktif_test = test_no + 1
        kutular[test_no - 1].config(
            text=f"TEST_{test_no}\n✅",
            bg="lightgreen"
        )

# =========================
# TEST KUTULARI
# =========================

kutular = []

def kutu_olustur(frame, test_no, row, col):
    btn = tk.Button(
        frame,
        text=f"TEST_{test_no}\n10 SORU VARDIR\nBAŞARI DURUMU\n(GEÇTİ-KALDI)",
        bg="yellow",
        fg="black",
        width=20,
        height=5,
        command=lambda: test_ac(test_no)
    )
    btn.grid(row=row, column=col, padx=10, pady=10)
    kutular.append(btn)

main_frame = tk.Frame(root, bg="lightgray")
main_frame.pack(pady=20)

pozisyonlar = (
    [(0, i) for i in range(4)] +
    [(1, i) for i in range(3)] +
    [(2, i) for i in range(3)]
)

for i, (r, c) in enumerate(pozisyonlar):
    kutu_olustur(main_frame, i + 1, r, c)

root.mainloop()



# ekrana tablo geliyor fakat test yapmadım......isim girmeli sertifika eklemeye çalışıyorum olmadı..... 

# 100 soru var... 10 lu tablo görünümlüdür....

# 1.ci soru...İslam'ın beş şartından biri olan ve zengin Müslümanların yılda bir kez mallarının 
# belirli bir kısmını ihtiyaç sahiplerine vermesi anlamına gelen ibadet hangisidir? 


#  sorular 01.....10arası 10KUTU VAR ... 100 soru...tkinter modundadır...

#  terminale bu kodu yapıştırın ve entere basın...

#  bu test butonludur ...üstte static kod resmi var..böyle görüntüleniyor ...


#  pycharm community de altta solda terminale tıkla .... açılan pencereye alttaki kodu yapıştır ....

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_42.py


#  & "E:/İslami Test Soruları/.venv/Scripts/python.exe" islami_test_python_42.py   Pardusda

# python3 "/home/ismail/Documents/Python/gtk-dersi/data/İslami Test/Soruları/islami_test_python_42.py" pardusda

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_42.py     windows da

# dogruya ayrı ses ... yanlışa ayrı ses var ...

# SONUNA KADAR İLERLEDİM mükemmel çalışıyor... başarı puanı gösteriyor...

#  C'deki Klasörü güncellemek için üst solda 4 çizgiye tıkla altta şu yazana tıkla ... Reload all from Disk



'''
 CEVAP ANAHTARI...İKİNCİ denemedir...test çalışıyor...sonunda sertifika ekledim..
 
TEST_1...01-A  2-B   3-B   4-C   5-B   6-A   7-B   8-C   9-B   10-C

TEST_2....1-A   2-B   3-C   4-C   5-D   6-A   7-B   8-B   9-C  10-C   

TEST_3....1-C   2-A   3-A   4-B   5-B  6-C   7-B   8-C   9-C   10-B        11 SORU VAR BURDA

TEST_4....1-D   2-B   3-B   4-C   5-A  6-B   7-C   8-B   9-A   10-B

TEST_5....1-C   2-B   3-C   4-B   5-C   6-B   7-A   8-C   9-B   10-C

TEST_6....1-A   2-A   3-D   4-B   5-C   6-C   7-B   8-A   9-C   10-B

TEST_7....1-C   2-C   3-D   4-C   5-B   6-C   7-A   8-B   9-A   10-A   

TEST_8....1-A   2-C   3-C   4-B   5-B   6-B   7-A   8-C   9-B   10-A

TEST_9....1-D   2-A   8-B   4-A   5-C   6-B   7-B   8-A   9-A   10-C

TEST_10...1-C   2-D   3-A   4-C   5-B   6-A   7-C   8-C   9-D   10-B

'''





