import tkinter as tk
from tkinter import ttk, messagebox

#  sorular 01.....10 aynı sorularvar... tkinter modundadır.

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

# ---------------- DEĞİŞKENLER ----------------
soru_index = 0
dogru = 0

# ---------------- PENCERE ----------------
root = tk.Tk()
root.title("İslami Bilgiler Testi")
root.geometry("520x420")
root.configure(bg="#f4f6f8")
root.resizable(False, False)

style = ttk.Style()
style.theme_use("clam")

style.configure("TButton", font=("Segoe UI", 10), padding=6)
style.configure("TRadiobutton", font=("Segoe UI", 10))
style.configure("Title.TLabel", font=("Segoe UI", 14, "bold"))
style.configure("Question.TLabel", font=("Segoe UI", 11))

# ---------------- ANA ÇERÇEVE ----------------
frame = ttk.Frame(root, padding=20)
frame.pack(expand=True, fill="both")

# Başlık
lbl_title = ttk.Label(
    frame,
    text="📘 İslami Bilgiler Testi",
    style="Title.TLabel"
)
lbl_title.pack(pady=(0, 15))

# Soru
lbl_soru = ttk.Label(
    frame,
    text="",
    wraplength=460,
    style="Question.TLabel"
)
lbl_soru.pack(pady=10)

# Seçenekler
secim = tk.IntVar(value=-1)
radio_buttons = []

for i in range(4):
    rb = ttk.Radiobutton(
        frame,
        text="",
        variable=secim,
        value=i
    )
    rb.pack(anchor="w", pady=5, padx=20)
    radio_buttons.append(rb)

# ---------------- FONKSİYONLAR ----------------
def soruyu_yukle():
    lbl_soru.config(
        text=f"{soru_index + 1}. {sorular[soru_index]['soru']}"
    )
    for i, rb in enumerate(radio_buttons):
        rb.config(text=sorular[soru_index]["secenekler"][i])

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

# Buton
btn_sonraki = ttk.Button(
    frame,
    text="Sonraki ➜",
    command=sonraki
)
btn_sonraki.pack(pady=20)

# ---------------- BAŞLAT ----------------
soruyu_yukle()
root.mainloop()



#  1.ci soru... İslam’ın beş şartından biri hangisidir?

#  sorular 01.....10 aynı sorularvar... tkinter modundadır.

#  yukarıda terminalden New Terminal Window a tıklayıp açın....

#  terminale bu kadu yapıştırın ve entere basın...

#  bu test butonludur ...üstte static kod resmi var..böyle görüntüleniyor ...


#  pycharm community de altta solda terminale tıkla .... açılan pencereye alttaki kodu yapıştır ....

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_3.py


# python3 "/home/ismail/Documents/Python/gtk-dersi/data/İslami Test/Soruları/islami_test_python_3.py" pardusda

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_3.py  windowsda
