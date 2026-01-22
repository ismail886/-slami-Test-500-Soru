import tkinter as tk
from tkinter import ttk, messagebox

# ---------------- SORULAR (41–50) ----------------
sorular = [
    {
        "soru": "Aşağıdakilerden hangisi Peygamberimizin çocuklarından biri değildir?",
        "secenekler": ["Zeynep", "Ümmü Gülsüm", "Safiye", "Rukiye"],
        "cevap": 2
    },
    {
        "soru": "Ramazan Bayramı'nda verilen vacip olan sadakaya ne denir?",
        "secenekler": ["Fidye", "Fitre (Fıtır Sadakası)", "Öşür", "Haraç"],
        "cevap": 1
    },
    {
        "soru": "Müslümanların kıblesi olan Kabe hangi şehirdedir?",
        "secenekler": ["Medine", "Cidde", "Mekke", "Riyad"],
        "cevap": 2
    },
    {
        "soru": "Allah'ın her şeye gücünün yetmesi sıfatına ne ad verilir?",
        "secenekler": ["İlim", "Kudret", "İrade", "Tekvin"],
        "cevap": 1
    },
    {
        "soru": "\"El-Emin\" (Güvenilir) lakabı kime verilmiştir?",
        "secenekler": ["Hz. Ebubekir", "Hz. Ömer", "Hz. Muhammed (s.a.v)", "Hz. Süleyman"],
        "cevap": 2
    },
    {
        "soru": "Her işe başlarken söylediğimiz \"Bismillahirrahmanirrahim\"in anlamı nedir?",
        "secenekler": [
            "Allah en büyüktür",
            "Rahman ve Rahim olan Allah'ın adıyla.",
            "Hamd Allah'adır",
            "Allah birdir"
        ],
        "cevap": 1
    },
    {
        "soru": "Bir Müslümanın başka bir Müslüman üzerindeki haklarından biri nedir?",
        "secenekler": [
            "Selamını almak",
            "Malını almak",
            "Sırrını ifşa etmek",
            "Onu eleştirmek"
        ],
        "cevap": 0
    },
    {
        "soru": "Peygamberimizin ilk eşi kimdir?",
        "secenekler": ["Hz. Ayşe", "Hz. Hafsa", "Hz. Hatice", "Hz. Sevde"],
        "cevap": 2
    },
    {
        "soru": "Amellerin tartılacağı teraziye ne ad verilir?",
        "secenekler": ["Sırat", "Mizan", "Mahşer", "Berzah"],
        "cevap": 1
    },
    {
        "soru": "İslam'ın temel kaynağı nedir?",
        "secenekler": ["Hadis kitapları", "İlmihal", "Kur'an-ı Kerim", "Fıkıh kitapları"],
        "cevap": 2
    }
]

# ---------------- DEĞİŞKENLER ----------------
soru_index = 0
dogru = 0

# ---------------- PENCERE ----------------
root = tk.Tk()
root.title("İslami Temel Bilgiler Testi – 5")
root.geometry("650x500")
root.resizable(False, False)
root.configure(bg="#f3f4f6")

style = ttk.Style()
style.theme_use("clam")

style.configure("Title.TLabel", font=("Segoe UI", 16, "bold"))
style.configure("Question.TLabel", font=("Segoe UI", 11))
style.configure("TRadiobutton", font=("Segoe UI", 10))
style.configure("TButton", font=("Segoe UI", 10), padding=6)

# ---------------- ANA ÇERÇEVE ----------------
frame = ttk.Frame(root, padding=20)
frame.pack(expand=True, fill="both")

lbl_title = ttk.Label(
    frame,
    text="📘 İSLAMİ TEMEL BİLGİLER TESTİ (41–50)",
    style="Title.TLabel"
)
lbl_title.pack(pady=(0, 15))

lbl_soru = ttk.Label(
    frame,
    text="",
    wraplength=600,
    style="Question.TLabel"
)
lbl_soru.pack(pady=10)

secim = tk.IntVar(value=-1)
radio_buttons = []

for i in range(4):
    rb = ttk.Radiobutton(
        frame,
        text="",
        variable=secim,
        value=i
    )
    rb.pack(anchor="w", pady=6, padx=20)
    radio_buttons.append(rb)

# ---------------- FONKSİYONLAR ----------------
def soruyu_yukle():
    lbl_soru.config(
        text=f"{soru_index + 41}. {sorular[soru_index]['soru']}"
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
        f"Başarı Durumu: {durum}"
    )
    root.destroy()

btn_sonraki = ttk.Button(
    frame,
    text="Sonraki ➜",
    command=sonraki
)
btn_sonraki.pack(pady=20)

# ---------------- BAŞLAT ----------------
soruyu_yukle()
root.mainloop()




#  1.soru....Aşağıdakilerden hangisi Peygamberimizin çocuklarından biri değildir?

#  sorular 41.....50 arası 10 soru...tkinter modundadır...

#  terminale bu kadu yapıştırın ve entere basın...

#  bu test butonludur ...üstte static kod resmi var..böyle görüntüleniyor ...


#  pycharm community de altta solda terminale tıkla .... açılan pencereye alttaki kodu yapıştır ....

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_8.py


# python3 "/home/ismail/Documents/Python/gtk-dersi/data/İslami Test/Soruları/islami_test_python_8.py" pardusda

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_8.py  windows da
