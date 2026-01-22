import tkinter as tk
from tkinter import ttk, messagebox

# ---------------- SORULAR (81–90) ----------------
sorular = [
    {
        "soru": "Peygamberlerin günahsız olmalarına ne denir?",
        "secenekler": ["İsmet", "Emanet", "Tebliğ", "Sıdk"],
        "cevap": 0
    },
    {
        "soru": "Hz. Nuh'un gemisinin oturduğu dağ olarak Kur'an'da geçen yer neresidir?",
        "secenekler": ["Ağrı Dağı", "Cudi Dağı", "Erciyes Dağı", "Uhud Dağı"],
        "cevap": 1
    },
    {
        "soru": "Bir Müslüman öldüğünde ona karşı yapılması gereken son görev nedir?",
        "secenekler": [
            "Helva dağıtmak",
            "Mevlit okutmak",
            "Cenaze namazını kılmak ve defnetmek",
            "Evini ziyaret etmek"
        ],
        "cevap": 2
    },
    {
        "soru": "Namazın vaktinin girdiğini bildirmek için yapılan çağrıya ne denir?",
        "secenekler": ["Kamet", "Selâ", "Ezan", "Zikir"],
        "cevap": 2
    },
    {
        "soru": "Peygamberlerin Allah'tan getirdiği emirlerin her zaman doğru olması sıfatı hangisidir?",
        "secenekler": ["Sıdk", "Fetanet", "İsmet", "Emanet"],
        "cevap": 0
    },
    {
        "soru": "Ramazan ayında Kur'an'ı birinin okuyup diğerlerinin takip etmesine ne ad verilir?",
        "secenekler": ["Hatim", "Mukabele", "Mevlit", "Tilavet"],
        "cevap": 1
    },
    {
        "soru": "\"Lâ ilâhe illallah\" sözü ne anlama gelir?",
        "secenekler": [
            "Allah en büyüktür",
            "Allah'tan başka ilah yoktur",
            "Hamd Allah'adır",
            "Allah bizi korusun"
        ],
        "cevap": 1
    },
    {
        "soru": "İslam'da \"Şehitlerin Efendisi\" olarak anılan Peygamberimizin amcası kimdir?",
        "secenekler": ["Hz. Abbas", "Hz. Hamza", "Ebu Talip", "Hz. Cafer"],
        "cevap": 1
    },
    {
        "soru": "Peygamberimizin hicret sonrası Medine'de inşa ettirdiği mescidin adı nedir?",
        "secenekler": [
            "Mescid-i Aksa",
            "Mescid-i Nebevi",
            "Mescid-i Kıbleteyn",
            "Mescid-i Haram"
        ],
        "cevap": 1
    },
    {
        "soru": "Kurban ibadeti hangi peygamberin sünnetidir?",
        "secenekler": ["Hz. Nuh", "Hz. İbrahim", "Hz. Musa", "Hz. İsa"],
        "cevap": 1
    }
]

# ---------------- DEĞİŞKENLER ----------------
soru_index = 0
dogru = 0

# ---------------- PENCERE ----------------
root = tk.Tk()
root.title("İslami Bilgi Testi (81–90)")
root.geometry("700x520")
root.resizable(False, False)
root.configure(bg="#f1f5f9")

style = ttk.Style()
style.theme_use("clam")

style.configure("Title.TLabel", font=("Segoe UI", 17, "bold"))
style.configure("Question.TLabel", font=("Segoe UI", 11))
style.configure("TRadiobutton", font=("Segoe UI", 10))
style.configure("TButton", font=("Segoe UI", 10), padding=6)

# ---------------- ANA ÇERÇEVE ----------------
frame = ttk.Frame(root, padding=22)
frame.pack(expand=True, fill="both")

lbl_title = ttk.Label(
    frame,
    text="📘 İSLAMİ BİLGİ TESTİ (81–90)",
    style="Title.TLabel"
)
lbl_title.pack(pady=(0, 15))

lbl_soru = ttk.Label(
    frame,
    text="",
    wraplength=650,
    style="Question.TLabel"
)
lbl_soru.pack(pady=12)

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
        text=f"{soru_index + 81}. {sorular[soru_index]['soru']}"
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
btn_sonraki.pack(pady=22)

# ---------------- BAŞLAT ----------------
soruyu_yukle()
root.mainloop()




#  1.ci soru... Peygamberlerin günahsız olmalarına ne denir?

#  sorular 81.....90 arası 10 soru...tkinter modundadır...

#  terminale bu kadu yapıştırın ve entere basın...

#  bu test butonludur ...üstte static kod resmi var..böyle görüntüleniyor ...


#  pycharm community de altta solda terminale tıkla .... açılan pencereye alttaki kodu yapıştır ....

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_12.py


#  & "E:/İslami Test Soruları/.venv/Scripts/python.exe" islami_test_python_12.py   Pardusda

# python3 "/home/ismail/Documents/Python/gtk-dersi/data/İslami Test/Soruları/islami_test_python_12.py" pardusda

#  C'deki Klasörü güncellemek için üst solda 4 çizgiye tıkla altta şu yazana tıkla ... Reload all from Disk



