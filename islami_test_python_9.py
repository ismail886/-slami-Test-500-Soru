import tkinter as tk
from tkinter import ttk, messagebox

# ---------------- SORULAR (51–60) ----------------
sorular = [
    {
        "soru": "Allah'ın her şeyi önceden bilip planlamasına ne denir?",
        "secenekler": ["Kaza", "Kader", "Tevekkül", "İrade"],
        "cevap": 1
    },
    {
        "soru": "Peygamberlerin Allah'tan aldıkları mesajları insanlara eksiksiz bildirmesine ne denir?",
        "secenekler": ["Tebliğ", "Emanet", "Sıdk", "İsmet"],
        "cevap": 0
    },
    {
        "soru": "Aşağıdakilerden hangisi \"Ulu'l-Azm\" peygamberlerden biri değildir?",
        "secenekler": ["Hz. Nuh", "Hz. İbrahim", "Hz. Adem", "Hz. İsa"],
        "cevap": 2
    },
    {
        "soru": "Hz. Muhammed (s.a.v.) kaç yaşında peygamber olmuştur?",
        "secenekler": ["25", "33", "40", "63"],
        "cevap": 2
    },
    {
        "soru": "Namazda Kur'an-ı Kerim okumaya ne ad verilir?",
        "secenekler": ["Kıyam", "Kıraat", "Tekbir", "Tahiyyat"],
        "cevap": 1
    },
    {
        "soru": "Ölen bir Müslümanın ardından kılınan ve rükûsu, secdesi olmayan namaz hangisidir?",
        "secenekler": ["Vitir Namazı", "Cenaze Namazı", "Küsuf Namazı", "İstiska Namazı"],
        "cevap": 1
    },
    {
        "soru": "Kur'an-ı Kerim'in en uzun ayeti olan Müdayene (Borçlanma) ayeti hangi surededir?",
        "secenekler": ["Bakara", "Nisa", "Maide", "Araf"],
        "cevap": 0
    },
    {
        "soru": "İslam'da ilk cuma namazı nerede kılınmıştır?",
        "secenekler": ["Kabe'de", "Mescid-i Nebevi'de", "Ranuna Vadisi'nde", "Kuba Mescidi'nde"],
        "cevap": 2
    },
    {
        "soru": "İslam dinine göre büyük günahlar (Kebair) arasında ilk sırada hangisi yer alır?",
        "secenekler": [
            "Yalan söylemek",
            "Allah'a ortak koşmak (Şirk)",
            "Gıybet etmek",
            "İsraf etmek"
        ],
        "cevap": 1
    },
    {
        "soru": "Hz. Yusuf'un babası olan peygamber kimdir?",
        "secenekler": ["Hz. Yakup", "Hz. İshak", "Hz. Yahya", "Hz. Zekeriya"],
        "cevap": 0
    }
]

# ---------------- DEĞİŞKENLER ----------------
soru_index = 0
dogru = 0

# ---------------- PENCERE ----------------
root = tk.Tk()
root.title("İslami Bilgi Testi (51–60)")
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
    text="📘 İSLAMİ BİLGİ TESTİ (51–60)",
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
        text=f"{soru_index + 51}. {sorular[soru_index]['soru']}"
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





#  1.ci soru...Allah'ın her şeyi önceden bilip planlamasına ne denir?

#  sorular 51.....60 arası 10 soru...tkinter modundadır...

#  terminale bu kadu yapıştırın ve entere basın...

#  bu test butonludur ...üstte static kod resmi var..böyle görüntüleniyor ...


#  pycharm community de altta solda terminale tıkla .... açılan pencereye alttaki kodu yapıştır ....

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_9.py



# python3 "/home/ismail/Documents/Python/gtk-dersi/data/İslami Test/Soruları/islami_test_python_9.py" pardusda

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_9.py windows da

