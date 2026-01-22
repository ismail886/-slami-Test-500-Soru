# Kaldırılabilir (kullanılmıyor):

# import tkinter as tk

# from tkinter import ttk, messagebox

#  sorular...01.....10 soru..ilk denemedir bu..

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

print("\nISLAMI BILGILER TESTI 10 SORU TERMİNALDEN")
print("-" * 30)

for i, soru in enumerate(sorular, start=1):
    print(f"\n{i}. {soru['soru']}")
    for secenek in soru["secenekler"]:
        print(secenek)

    while True:
        cevap = input("Cevabınız (A/B/C/D): ").upper()
        if cevap in ["A", "B", "C", "D"]:
            break
        print("Lütfen A, B, C veya D giriniz.")

    if cevap == soru["cevap"]:
        print("✓ Doğru!")
        dogru += 1
    else:
        print(f"✗ Yanlış! Doğru cevap: {soru['cevap']}")

print("\n" + "=" * 30)
print("TEST SONUCU")
print("=" * 30)
print(f"Doğru Sayısı : {dogru}")
print(f"Yanlış Sayısı: {len(sorular) - dogru}")
print(f"Başarı Oranı : %{(dogru/len(sorular))*100:.1f}")
print(f"Puan         : {dogru * 10} / 100")



#  1.ci soru... İslam’ın beş şartından biri aşağıdakilerden hangisidir?

# 10 soru terminalden çalışıyor....

# yukarıda terminalden New Terminal Window a tıklayıp açın....

# terminale bu kadu yapıştırın ve entere basın...


#  pycharm community de altta solda terminale tıkla .... açılan pencereye alttaki kodu yapıştır ....

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_0.py


# python3 "/home/ismail/Documents/Python/gtk-dersi/data/İslami Test Soruları/islami_test_python_0.py"   pardusda


# & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_0.py  windows da
