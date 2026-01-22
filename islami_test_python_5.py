import tkinter as tk
from tkinter import ttk, messagebox

#  sorular 11.....20 arası 10 soru.tkinter modundadır...

sorular = [
    {
        "soru": "Teyemmüm abdesti ne ile alınır?",
        "secenekler": ["Su", "Kağıt", "Toprak", "Kumaş"],
        "cevap": 2
    },
    {
        "soru": "Haccın farzlarından biri olan ve Kabe'nin etrafında 7 kez dönmeye ne denir?",
        "secenekler": ["Say", "İhram", "Vakfe", "Tavaf"],
        "cevap": 3
    },
    {
        "soru": "Zekat verebilmek için sahip olunması gereken asgari zenginlik ölçüsüne ne denir?",
        "secenekler": ["Nisap", "Miktar", "Öşür", "Fitre"],
        "cevap": 0
    },
    {
        "soru": "Peygamberimiz hangi şehirde doğmuştur?",
        "secenekler": ["Medine", "Kudüs", "Mekke", "Taif"],
        "cevap": 2
    },
    {
        "soru": "Peygamberimize ilk vahiy nerede gelmiştir?",
        "secenekler": ["Sevr Mağarası", "Hira Mağarası", "Mescid-i Nebevi", "Kabe"],
        "cevap": 1
    },
    {
        "soru": "Müslümanların ilk hicret ettiği yer neresidir?",
        "secenekler": ["Habeşistan", "Medine", "Mısır", "Bağdat"],
        "cevap": 0
    },
    {
        "soru": "Peygamberimizin Medine'ye hicret ederken yanındaki yol arkadaşı kimdir?",
        "secenekler": ["Hz. Ömer", "Hz. Ali", "Hz. Ebubekir", "Hz. Osman"],
        "cevap": 2
    },
    {
        "soru": "Müslümanlar ile Mekkeli müşrikler arasındaki ilk büyük savaş hangisidir?",
        "secenekler": ["Uhud", "Hendek", "Bedir", "Hayber"],
        "cevap": 2
    },
    {
        "soru": "Peygamberimizin vefat ettiği şehir hangisidir?",
        "secenekler": ["Mekke", "Cidde", "Şam", "Medine"],
        "cevap": 3
    },
    {
        "soru": "Kur'an-ı Kerim'de kaç cüz vardır?",
        "secenekler": ["20", "30", "40", "114"],
        "cevap": 1
    }
]

# ---------------- DEĞİŞKENLER ----------------
soru_index = 0
dogru = 0

# ---------------- PENCERE ----------------
root = tk.Tk()
root.title("İslami Temel Bilgiler Testi – 2")
root.geometry("650x480")
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
    text="📘 İSLAMİ TEMEL BİLGİLER TESTİ (11–20)",
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
        text=f"{soru_index + 11}. {sorular[soru_index]['soru']}"
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





#  1.ci soru... Teyemmüm abdesti ne ile alınır?

#  sorular 11.....20 arası 10 soru.tkinter modundadır...

#  terminale bu kadu yapıştırın ve entere basın...

#  bu test butonludur ...üstte static kod resmi var..böyle görüntüleniyor ...


#  pycharm community de altta solda terminale tıkla .... açılan pencereye alttaki kodu yapıştır ....

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_5.py



# python3 "/home/ismail/Documents/Python/gtk-dersi/data/İslami Test/Soruları/islami_test_python_5.py" pardusda

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_5.py  windows da
