import tkinter as tk
from tkinter import ttk, messagebox

#    aynı sorular deneme
sorular = [
    {
        "soru": "İslam’ın beş şartından biri hangisidir?",
        "secenekler": ["Zekât", "Oruç", "Hicret", "Cihat"],
        "cevap": 1
    },
    {
        "soru": "Kur’an-ı Kerim hangi ayda indirilmeye başlanmıştır?",
        "secenekler": ["Muharrem", "Recep", "Ramazan", "Şaban"],
        "cevap": 2
    },
    {
        "soru": "İlk vahiy hangi melek aracılığıyla gelmiştir?",
        "secenekler": ["Azrail", "Mikail", "İsrafil", "Cebrail"],
        "cevap": 3
    },
    {
        "soru": "Günde kaç vakit namaz farzdır?",
        "secenekler": ["3", "4", "5", "6"],
        "cevap": 2
    },
    {
        "soru": "İslam’ın şartlarından biri değildir?",
        "secenekler": ["Namaz", "Oruç", "Hac", "Kurban kesmek"],
        "cevap": 3
    },
    {
        "soru": "Kur’an-ı Kerim kaç sureden oluşur?",
        "secenekler": ["110", "112", "114", "116"],
        "cevap": 2
    },
    {
        "soru": "İman ne demektir?",
        "secenekler": [
            "İbadet etmek",
            "Allah’a ve iman esaslarına inanmak",
            "İyi insan olmak",
            "Günah işlememek"
        ],
        "cevap": 1
    },
    {
        "soru": "Zekât kimlere verilir?",
        "secenekler": [
            "Akrabalara",
            "Zenginlere",
            "Fakir ve ihtiyaç sahiplerine",
            "Herkese"
        ],
        "cevap": 2
    },
    {
        "soru": "Hz. Muhammed (s.a.v.) nerede doğmuştur?",
        "secenekler": ["Medine", "Kudüs", "Mekke", "Taif"],
        "cevap": 2
    },
    {
        "soru": "Hangisi haramdır?",
        "secenekler": [
            "Sadaka vermek",
            "Yalan söylemek",
            "Selam vermek",
            "İlim öğrenmek"
        ],
        "cevap": 1
    }
]

soru_index = 0
dogru = 0

# Pencere
root = tk.Tk()
root.title("İslami Bilgiler Testi")
root.geometry("500x350")
root.resizable(False, False)

# Soru etiketi
lbl_soru = tk.Label(root, text="", wraplength=450, font=("Arial", 12))
lbl_soru.pack(pady=20)

# Seçenekler
secim = tk.IntVar()
radio_buttons = []

for i in range(4):
    rb = tk.Radiobutton(
        root, text="", variable=secim, value=i, font=("Arial", 11)
    )
    rb.pack(anchor="w", padx=50)
    radio_buttons.append(rb)

# Sonraki butonu
def sonraki():
    global soru_index, dogru

    if secim.get() == -1:
        messagebox.showwarning("Uyarı", "Lütfen bir seçenek seçiniz!")
        return

    if secim.get() == sorular[soru_index]["cevap"]:
        dogru += 1

    soru_index += 1
    secim.set(-1)

    if soru_index < len(sorular):
        soruyu_yukle()
    else:
        sonucu_goster()

btn_sonraki = tk.Button(
    root, text="Sonraki", command=sonraki, width=15
)
btn_sonraki.pack(pady=20)

# Soruyu yükleme
def soruyu_yukle():
    lbl_soru.config(
        text=f"{soru_index + 1}. {sorular[soru_index]['soru']}"
    )
    for i, rb in enumerate(radio_buttons):
        rb.config(text=sorular[soru_index]["secenekler"][i])

# Sonuç ekranı
def sonucu_goster():
    puan = dogru * 10
    durum = "GEÇTİ 🎉" if puan >= 70 else "KALDI ❌"

    messagebox.showinfo(
        "Test Sonucu",
        f"Doğru: {dogru}\n"
        f"Yanlış: {len(sorular) - dogru}\n"
        f"Puan: {puan}/100\n\n"
        f"Durum: {durum}"
    )
    root.destroy()

# Başlangıç
secim.set(-1)
soruyu_yukle()
root.mainloop()




#  1.ci soru... İslam’ın beş şartından biri hangisidir?

#  sorular 01.....10...tkinter butonludur.. başarı durumu var...

# yukarıda terminalden New Terminal Window a tıklayıp açın....

# terminale bu kadu yapıştırın ve entere basın...

#  bu test butonludur ...üstte static kod resmi var..böyle görüntüleniyor ...


#  pycharm community de altta solda terminale tıkla .... açılan pencereye alttaki kodu yapıştır ....

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_2.py


# python3 "/home/ismail/Documents/Python/gtk-dersi/data/İslami Test/Soruları/islami_test_python_2.py" pardusda

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_2.py  windows da

