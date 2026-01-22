import random

# Test 1: Temel Bilgiler Testi (10 soru) - ✅ DÜZELTİLDİ
test1_sorular = [
    {
        "soru": "İslam'ın beş şartından biri olan ve zengin Müslümanların yılda bir kez mallarının belirli bir kısmını ihtiyaç sahiplerine vermesi anlamına gelen ibadet hangisidir?",
        "secenekler": ["A) Zekat", "B) Sadaka", "C) Hac", "D) Fitre"],
        "dogru": "A"
    },
    {
        "soru": "Kur'an-ı Kerim'in en uzun suresi aşağıdakilerden hangisidir?",
        "secenekler": ["A) Al-i İmran", "B) Bakara", "C) Nisa", "D) Maide"],
        "dogru": "B"
    },
    {
        "soru": "İmanın şartlarından biri olan 'Kaza ve Kadere İman', aşağıdakilerden hangisini kapsar?",
        "secenekler": [
            "A) Sadece geçmişte yaşanan olayları",
            "B) Allah'ın her şeyi bir ölçüye göre takdir etmesi ve zamanı gelince gerçekleşmesi",
            "C) Sadece insanların kendi özgür iradesiyle yaptığı seçimleri",
            "D) Doğa olaylarının tesadüfen meydana gelmesini"
        ],
        "dogru": "B"
    },
    {
        "soru": "Peygamber Efendimiz (s.a.v.)'in gece vakti Mescid-i Haram'dan Mescid-i Aksa'ya götürülmesine ne ad verilir?",
        "secenekler": ["A) Hicret", "B) Miraç", "C) İsra", "D) Vahiy"],
        "dogru": "C"
    },
    {
        "soru": "Aşağıdakilerden hangisi abdestin farzlarından biri değildir?",
        "secenekler": ["A) Yüzü yıkamak", "B) Ağza ve burna su vermek", "C) Elleri dirseklerle beraber yıkamak", "D) Başın dörtte birini meshetmek"],
        "dogru": "B"
    },
    {
        "soru": "Kur'an-ı Kerim hangi halife döneminde kitap (mushaf) haline getirilmiştir?",
        "secenekler": ["A) Hz. Ebubekir", "B) Hz. Ömer", "C) Hz. Osman", "D) Hz. Ali"],
        "dogru": "A"
    },
    {
        "soru": "İslam dininde 'Ef'al-i Mükellefin' içinde yer alan ve yapılması kesin olarak yasaklanan fiillere ne denir?",
        "secenekler": ["A) Mekruh", "B) Haram", "C) Mübah", "D) Vacip"],
        "dogru": "B"
    },
    {
        "soru": "Aşağıdakilerden hangisi Peygamber Efendimiz (s.a.v.)'in çocuklarından biri değildir?",
        "secenekler": ["A) Hz. Fatıma", "B) Hz. Kasım", "C) Hz. Ayşe", "D) Hz. İbrahim"],
        "dogru": "C"
    },
    {
        "soru": "Kıblenin Kudüs'teki Mescid-i Aksa'dan Mekke'deki Kabe'ye çevrildiği olay ne zaman gerçekleşmiştir?",
        "secenekler": [
            "A) Hicretten 5 yıl önce",
            "B) Hicretten yaklaşık 1,5 yıl sonra",
            "C) Mekke'nin Fethinden hemen sonra",
            "D) Veda Haccı sırasında"
        ],
        "dogru": "B"
    },
    {
        "soru": "Allah'ın her şeyi görmesi sıfatına ne ad verilir?",
        "secenekler": ["A) İlim", "B) Semi", "C) Basar", "D) Kudret"],
        "dogru": "C"
    }
]

# Test 2: 50 Soruluk İslami Bilgi Testi - ✅ TAM LİSTE
test2_sorular = [
    {"soru": "Allah'ın var ve bir olmasına ne ad verilir?", "secenekler": ["A) Tevhid", "B) Nübüvvet", "C) Ahiret", "D) Haşir"], "dogru": "A"},
    {"soru": "İmanın şartlarından biri olmayan?", "secenekler": ["A) Meleklere inanmak", "B) Namaz kılmak", "C) Peygamberlere inanmak", "D) Kitaplara inanmak"], "dogru": "B"},
    {"soru": "Zebur hangi peygambere?", "secenekler": ["A) Hz. Musa", "B) Hz. İsa", "C) Hz. Davud", "D) Hz. İbrahim"], "dogru": "C"},
    {"soru": "Öldükten sonra dirilme?", "secenekler": ["A) Mizan", "B) Berzah", "C) Haşir", "D) Kıyamet"], "dogru": "C"},
    {"soru": "Vahiy melek?", "secenekler": ["A) Mikail", "B) Azrail", "C) İsrafil", "D) Cebrail"], "dogru": "D"},
    {"soru": "Namaz baş tekbiri?", "secenekler": ["A) İftitah Tekbiri", "B) Kıyam", "C) Ka'de-i Ahire", "D) Secde"], "dogru": "A"},
    {"soru": "Günde kaç vakit namaz?", "secenekler": ["A) 3", "B) 5", "C) 7", "D) 2"], "dogru": "B"},
    {"soru": "Rükudan sonra?", "secenekler": ["A) Kıraat", "B) Secde", "C) Teşehhüd", "D) Selam"], "dogru": "B"},
    {"soru": "Cemaat zorunlu namaz?", "secenekler": ["A) Teravih", "B) Bayram", "C) Cuma", "D) Vitir"], "dogru": "C"},
    {"soru": "Oruç fidye?", "secenekler": ["A) Zekat", "B) Sadaka", "C) Fidye", "D) Fitre"], "dogru": "C"},
    {"soru": "Teyemmüm?", "secenekler": ["A) Su", "B) Kağıt", "C) Toprak", "D) Kumaş"], "dogru": "C"},
    {"soru": "Kabe tavaf?", "secenekler": ["A) Say", "B) İhram", "C) Vakfe", "D) Tavaf"], "dogru": "D"},
    {"soru": "Zekat nisap?", "secenekler": ["A) Nisap", "B) Miktar", "C) Öşür", "D) Fitre"], "dogru": "A"},
    {"soru": "Peygamber doğumu?", "secenekler": ["A) Medine", "B) Kudüs", "C) Mekke", "D) Taif"], "dogru": "C"},
    {"soru": "İlk vahiy?", "secenekler": ["A) Sevr", "B) Hira Mağarası", "C) Mescid-i Nebevi", "D) Kabe"], "dogru": "B"},
    {"soru": "İlk hicret?", "secenekler": ["A) Habeşistan", "B) Medine", "C) Mısır", "D) Bağdat"], "dogru": "A"},
    {"soru": "Hicret arkadaşı?", "secenekler": ["A) Hz. Ömer", "B) Hz. Ali", "C) Hz. Ebubekir", "D) Hz. Osman"], "dogru": "C"},
    {"soru": "İlk savaş?", "secenekler": ["A) Uhud", "B) Hendek", "C) Bedir", "D) Hayber"], "dogru": "C"},
    {"soru": "Vefat yeri?", "secenekler": ["A) Mekke", "B) Cidde", "C) Şam", "D) Medine"], "dogru": "D"},
    {"soru": "Kur'an cüz sayısı?", "secenekler": ["A) 20", "B) 30", "C) 40", "D) 114"], "dogru": "B"},
    {"soru": "İlk sure?", "secenekler": ["A) Bakara", "B) İhlas", "C) Fatiha", "D) Nas"], "dogru": "C"},
    {"soru": "En kısa sure?", "secenekler": ["A) Kevser", "B) Fil", "C) Maun", "D) Kureyş"], "dogru": "A"},
    {"soru": "Besmelesiz sure?", "secenekler": ["A) Yasin", "B) Tevbe", "C) Rahman", "D) Mülk"], "dogru": "B"},
    {"soru": "Kur'an süresi?", "secenekler": ["A) 10", "B) 23", "C) 40", "D) 63"], "dogru": "B"},
    {"soru": "Ezberleyen?", "secenekler": ["A) Müezzin", "B) İmam", "C) Hafız", "D) Alim"], "dogru": "C"},
    {"soru": "Rızık melek?", "secenekler": ["A) Cebrail", "B) Mikail", "C) Azrail", "D) İsrafil"], "dogru": "B"},
    {"soru": "İşitme sıfatı?", "secenekler": ["A) İlim", "B) Semi", "C) Basar", "D) Kudret"], "dogru": "B"},
    {"soru": "Peygamber zekası?", "secenekler": ["A) Sıdk", "B) Emanet", "C) Fetanet", "D) Tebliğ"], "dogru": "C"},
    {"soru": "20 sayfa?", "secenekler": ["A) Sure", "B) Ayet", "C) Cüz", "D) Hizb"], "dogru": "C"},
    {"soru": "Kabe oğlu?", "secenekler": ["A) Hz. İshak", "B) Hz. İsmail", "C) Hz. Yakup", "D) Hz. Yusuf"], "dogru": "B"},
    {"soru": "Zenginlere farz?", "secenekler": ["A) Namaz", "B) Oruç", "C) Şehadet", "D) Zekat"], "dogru": "D"},
    {"soru": "Sabah rekat?", "secenekler": ["A) 2", "B) 4", "C) 6", "D) 10"], "dogru": "B"},
    {"soru": "Kabir yeri?", "secenekler": ["A) Makam-ı İbrahim", "B) Ravza-i Mutahhara", "C) Altınoluk", "D) Hacerü'l Esved"], "dogru": "B"},
    {"soru": "Ramazan namazı?", "secenekler": ["A) Teheccüd", "B) İşrak", "C) Teravih", "D) Evvabin"], "dogru": "C"},
    {"soru": "Ölüm melek?", "secenekler": ["A) Azrail", "B) Mikail", "C) Münker", "D) Nekir"], "dogru": "A"},
    {"soru": "Dede adı?", "secenekler": ["A) Ebu Talip", "B) Abdülmuttalib", "C) Abdullah", "D) Hamza"], "dogru": "B"},
    {"soru": "İlk müezzin?", "secenekler": ["A) Hz. Ebubekir", "B) Hz. Ali", "C) Bilal-i Habeşi", "D) Zeyd bin Sabit"], "dogru": "C"},
    {"soru": "Göç edenler?", "secenekler": ["A) Ensar", "B) Muhacir", "C) Mürted", "D) Münafık"], "dogru": "B"},
    {"soru": "Yardım edenler?", "secenekler": ["A) Ensar", "B) Muhacir", "C) Tabiun", "D) Sahabe"], "dogru": "A"},
    {"soru": "Kur'an kalbi?", "secenekler": ["A) Bakara", "B) Yasin", "C) Mülk", "D) Fetih"], "dogru": "B"},
    {"soru": "Çocuk olmayan?", "secenekler": ["A) Zeynep", "B) Ümmü Gülsüm", "C) Safiye", "D) Rukiye"], "dogru": "C"},
    {"soru": "Bayram sadakası?", "secenekler": ["A) Fidye", "B) Fitre", "C) Öşür", "D) Haraç"], "dogru": "B"},
    {"soru": "Kabe şehri?", "secenekler": ["A) Medine", "B) Cidde", "C) Mekke", "D) Riyad"], "dogru": "C"},
    {"soru": "Güç sıfatı?", "secenekler": ["A) İlim", "B) Kudret", "C) İrade", "D) Tekvin"], "dogru": "B"},
    {"soru": "El-Emin?", "secenekler": ["A) Hz. Ebubekir", "B) Hz. Ömer", "C) Hz. Muhammed", "D) Hz. Süleyman"], "dogru": "C"},
    {"soru": "Bismillah?", "secenekler": ["A) Allah en büy", "B) Rahman Rahim Allah adıyla", "C) Hamd Allah'adır", "D) Allah birdir"], "dogru": "B"},
    {"soru": "Müslüman hakkı?", "secenekler": ["A) Selamını almak", "B) Malını almak", "C) Sırrını ifşa", "D) Eleştirmek"], "dogru": "A"},
    {"soru": "İlk eş?", "secenekler": ["A) Hz. Ayşe", "B) Hz. Hafsa", "C) Hz. Hatice", "D) Hz. Sevde"], "dogru": "C"},
    {"soru": "Terazi?", "secenekler": ["A) Sırat", "B) Mizan", "C) Mahşer", "D) Berzah"], "dogru": "B"},
    {"soru": "Temel kaynak?", "secenekler": ["A) Hadis", "B) İlmihal", "C) Kur'an", "D) Fıkıh"], "dogru": "C"}
]

def test_goster(sorular, test_adi="İslami Bilgi Testi"):
    print(f"\n{'='*60}")
    print(f"{test_adi} - {len(sorular)} SORU")
    print(f"{'='*60}\n")
    
    dogru_sayisi = 0
    for i, soru in enumerate(sorular, 1):
        print(f"SORU {i}: {soru['soru']}")
        for secenek in soru['secenekler']:
            print(f"  {secenek}")
        
        while True:
            cevap = input(f"\nCevabınızı girin (A/B/C/D): ").upper().strip()
            if cevap in ['A', 'B', 'C', 'D']:
                break
            print("Lütfen A, B, C veya D girin!")
        
        if cevap == soru['dogru']:
            print("✅ DOĞRU!")
            dogru_sayisi += 1
        else:
            print(f"❌ YANLIŞ! Doğru cevap: {soru['dogru']}")
        print("-" * 40)
    
    yuzde = (dogru_sayisi / len(sorular)) * 100
    print(f"\n{'SONUÇ':^60}")
    print(f"{'='*60}")
    print(f"Doğru: {dogru_sayisi}/{len(sorular)} (%{yuzde:.1f})")
    
    if yuzde >= 90:
        print("🎉 MÜKEMMEL!")
    elif yuzde >= 70:
        print("👍 İYİ!")
    else:
        print("📚 ÇALIŞ!")
    print(f"{'='*60}\n")

def rastgele_test(sorular, soru_sayisi=None):
    if soru_sayisi:
        secilen = random.sample(sorular, min(soru_sayisi, len(sorular)))
    else:
        secilen = sorular.copy()
    test_goster(secilen, f"Rastgele - {len(secilen)} Soru")

def main():
    tum_sorular = test1_sorular + test2_sorular
    while True:
        print("\n📚 İSLAMİ TEST MENÜSÜ")
        print("1. Temel (10 soru)")
        print("2. Tam (50 soru)") 
        print("3. Rastgele 20")
        print("4. Rastgele 10")
        print("5. Çıkış")
        
        secim = input("\nSeçim (1-5): ").strip()
        
        if secim == "1":
            test_goster(test1_sorular, "TEMEL BİLGİLER")
        elif secim == "2":
            test_goster(test2_sorular, "50 SORU TAM TEST")
        elif secim == "3":
            rastgele_test(tum_sorular, 20)
        elif secim == "4":
            rastgele_test(tum_sorular, 10)
        elif secim == "5":
            print("Allah'a emanet! 🕌")
            break
        else:
            print("Geçersiz!")

if __name__ == "__main__":
    main()





#  güzel çalışıyor......test etmedim......

# 1.ci soru...İslam'ın beş şartından biri olan ve zengin Müslümanların yılda bir kez mallarının,

# belirli bir kısmını ihtiyaç sahiplerine vermesi anlamına gelen ibadet hangisidir? 


#  sorular 01.....100 arası 100 soru...tkinter modundadır...

#  terminale bu kodu yapıştırın ve entere basın...

#  bu test butonludur ...üstte static kod resmi var..böyle görüntüleniyor ...


#  pycharm community de altta solda terminale tıkla .... açılan pencereye alttaki kodu yapıştır ....

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_39.py


#  & "E:/İslami Test Soruları/.venv/Scripts/python.exe" islami_test_python_39.py   Pardusda

# python3 "/home/ismail/Documents/Python/gtk-dersi/data/İslami Test/Soruları/islami_test_python_39.py" pardusda

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_39.py     windows da

# 01 DEN 100 E KADAR İLERLEYEN SORULAR VAR...SONUNDA BAŞARI DURUMU VE SERTİFİKA ALMA VAR ...

# SES YOK..ANİMASYON YOK.....

# SONUNA KADAR İLERLEDİM mükemmel çalışiıyor... sertifika isim yazmalı çıkıyor... başarı puanı gösteriyor...

#  C'deki Klasörü güncellemek için üst solda 4 çizgiye tıkla altta şu yazana tıkla ... Reload all from Disk

