import tkinter as tk
from tkinter import ttk, messagebox

# ----------------71----80---------------
sorular = [
    {
        "soru": "Peygamberimizin süt kardeşinin adı nedir?",
        "secenekler": ["Esma", "Şeyma", "Nesibe", "Sümeyye"],
        "cevap": 1
    },
    {
        "soru": "Kur'an-ı Kerim'in ayetlerini açıklayan ve yorumlayan bilim dalına ne denir?",
        "secenekler": ["Fıkıh", "Hadis", "Tefsir", "Kelam"],
        "cevap": 2
    },
    {
        "soru": "Hangi halife \"Adalet\" kavramıyla özdeşleşmiştir?",
        "secenekler": ["Hz. Ebubekir", "Hz. Ömer", "Hz. Osman", "Hz. Ali"],
        "cevap": 1
    },
    {
        "soru": "Müslümanların bir yıl boyunca topladıkları paranın zekatını vermeleri için üzerinden ne kadar zaman geçmelidir?",
        "secenekler": ["6 ay", "1 kameri yıl", "2 yıl", "100 gün"],
        "cevap": 1
    },
    {
        "soru": "\"Allahuekber\" sözünün anlamı nedir?",
        "secenekler": [
            "Allah birdir",
            "Allah en büyüktür",
            "Allah affedicidir",
            "Allah her şeyi bilir"
        ],
        "cevap": 1
    },
    {
        "soru": "Bir insanın öldükten sonra amel defterinin kapanmamasını sağlayan kalıcı iyiliklere ne denir?",
        "secenekler": ["Zekat-ı Mal", "Sadaka-i Cariye", "Fitre", "Öşür"],
        "cevap": 1
    },
    {
        "soru": "Hz. İbrahim'in ateşe atıldığı yer olarak bilinen günümüz şehri hangisidir?",
        "secenekler": ["Konya", "Bursa", "Şanlıurfa", "Hatay"],
        "cevap": 2
    },
    {
        "soru": "Kur'an-ı Kerim'de adı geçen tek kadın kimdir?",
        "secenekler": ["Hz. Havva", "Hz. Meryem", "Hz. Asiye", "Hz. Sare"],
        "cevap": 1
    },
    {
        "soru": "Peygamberimizin doğduğu gece kutlanan kandil hangisidir?",
        "secenekler": ["Regaip Kandili", "Miraç Kandili", "Mevlid Kandili", "Berat Kandili"],
        "cevap": 2
    },
    {
        "soru": "İslam hukukunda bir konudaki dini hükmü açıklayan belgeye ne denir?",
        "secenekler": ["Ferman", "Berat", "Fetva", "İcma"],
        "cevap": 2
    }
]

# ---------------- DEĞİŞKENLER ----------------
soru_index = 0
dogru = 0

# ---------------- PENCERE ----------------
root = tk.Tk()
root.title("İslami Bilgi Testi (71–80)")
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
    text="📘 İSLAMİ BİLGİ TESTİ (71–80)",
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
        text=f"{soru_index + 71}. {sorular[soru_index]['soru']}"
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





#  1.ci soru... Peygamberimizin süt kardeşinin adı nedir?

#  sorular 71.....80 arası 10 soru...tkinter modundadır...

#  terminale bu kadu yapıştırın ve entere basın...

#  bu test butonludur ...üstte static kod resmi var..böyle görüntüleniyor ...



#  pycharm community de altta solda terminale tıkla .... açılan pencereye alttaki kodu yapıştır ....

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_11.py


#  & "E:/İslami Test Soruları/.venv/Scripts/python.exe" islami_test_python_11.py   Pardusda

# python3 "/home/ismail/Documents/Python/gtk-dersi/data/İslami Test/Soruları/islami_test_python_11.py" pardusda

#  C'deki Klasörü güncellemek için üst solda 4 çizgiye tıkla altta şu yazana tıkla ... Reload all from Disk



