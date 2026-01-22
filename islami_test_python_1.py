# İslami Bilgiler İnteraktif Test (Başarı Durumu)

#  sorular 01.....10 arası 10 soru. başka formattadır...

sorular = [
    {
        "soru": "İslam’ın beş şartından biri aşağıdakilerden hangisidir?",
        "secenekler": ["A) Zekât", "B) Oruç", "C) Hicret", "D) Cihat"],
        "cevap": "B"
    },
    {
        "soru": "Kur’an-ı Kerim hangi ayda indirilmeye başlanmıştır?",
        "secenekler": ["A) Muharrem", "B) Recep", "C) Ramazan", "D) Şaban"],
        "cevap": "C"
    },
    {
        "soru": "Hz. Muhammed (s.a.v.)’e ilk vahiy hangi melek aracılığıyla gelmiştir?",
        "secenekler": ["A) Azrail", "B) Mikail", "C) İsrafil", "D) Cebrail"],
        "cevap": "D"
    },
    {
        "soru": "Günde kaç vakit namaz farzdır?",
        "secenekler": ["A) 3", "B) 4", "C) 5", "D) 6"],
        "cevap": "C"
    },
    {
        "soru": "Aşağıdakilerden hangisi İslam’ın şartlarından biri değildir?",
        "secenekler": ["A) Namaz", "B) Oruç", "C) Hac", "D) Kurban kesmek"],
        "cevap": "D"
    },
    {
        "soru": "Kur’an-ı Kerim kaç sureden oluşur?",
        "secenekler": ["A) 110", "B) 112", "C) 114", "D) 116"],
        "cevap": "C"
    },
    {
        "soru": "İman neyi ifade eder?",
        "secenekler": [
            "A) İbadet etmek",
            "B) Allah’a ve iman esaslarına gönülden inanmak",
            "C) İyi insan olmak",
            "D) Günah işlememek"
        ],
        "cevap": "B"
    },
    {
        "soru": "Zekât kimlere verilir?",
        "secenekler": [
            "A) Sadece akrabalara",
            "B) Zenginlere",
            "C) Fakir ve ihtiyaç sahiplerine",
            "D) Herkese"
        ],
        "cevap": "C"
    },
    {
        "soru": "Hz. Muhammed (s.a.v.) hangi şehirde doğmuştur?",
        "secenekler": ["A) Medine", "B) Kudüs", "C) Mekke", "D) Taif"],
        "cevap": "C"
    },
    {
        "soru": "Aşağıdakilerden hangisi haramdır?",
        "secenekler": [
            "A) Sadaka vermek",
            "B) Yalan söylemek",
            "C) Selam vermek",
            "D) İlim öğrenmek"
        ],
        "cevap": "B"
    }
]

dogru = 0

print("\n📘 İSLAMİ BİLGİLER TESTİ")
print("-" * 35)

for i, soru in enumerate(sorular, start=1):
    print(f"\n{i}. {soru['soru']}")
    for secenek in soru["secenekler"]:
        print(secenek)

    while True:
        cevap = input("Cevabınız (A/B/C/D): ").upper()
        if cevap in ["A", "B", "C", "D"]:
            break
        print("❗ Lütfen A, B, C veya D giriniz.")

    if cevap == soru["cevap"]:
        print("✅ Doğru!")
        dogru += 1
    else:
        print(f"❌ Yanlış! Doğru cevap: {soru['cevap']}")

puan = dogru * 10

print("\n📊 TEST SONUCU")
print("-" * 35)
print(f"Doğru Sayısı : {dogru}")
print(f"Yanlış Sayısı: {len(sorular) - dogru}")
print(f"Puan        : {puan} / 100")

# Başarı durumu
if puan >= 70:
    print("🎉 BAŞARI DURUMU: GEÇTİ")
else:
    print("❌ BAŞARI DURUMU: KALDI")



#  1.ci soru... İslam’ın beş şartından biri aşağıdakilerden hangisidir?

#  sorular 01.....10 arası 10 soru. başka formattadır...

#  yukarıda terminalden New Terminal Window a tıklayıp açın....

#  terminale bu kadu yapıştırın ve entere basın...


#  pycharm community de altta solda terminale tıkla .... açılan pencereye alttaki kodu yapıştır ....

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_1.py



#  python3 "/home/ismail/Documents/Python/gtk-dersi/data/İslami Test/Soruları/islami_test_python_1.py" pardusda

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_1.py  windowsda



'''
- - - -  - - - çıktı bu şekilde olmalıdır - - - - - - -

ISLAMI BILGILER TESTI
------------------------------

1. İslam’ın beş şartından biri aşağıdakilerden hangisidir?
A) Zekât
B) Oruç
C) Hicret
D) Cihat
Cevabınız (A/B/C/D): 

'''

'''
📊 TEST SONUCU
-----------------------------------
Doğru Sayısı : 10
Yanlış Sayısı: 0
Puan        : 100 / 100
🎉 BAŞARI DURUMU: GEÇTİ
(.venv) PS E:\İslami Test Soruları> 

'''

