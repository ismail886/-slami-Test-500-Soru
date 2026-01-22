import tkinter as tk
from tkinter import ttk, messagebox

# ----------------61-----70---------------

sorular = [
    {
        "soru": "Allah'ın her an her şeyi yaratmaya devam etmesi sıfatına ne ad verilir?",
        "secenekler": ["Tekvin", "Bekâ", "Kıyam bi-nefsihi", "Vahdaniyet"],
        "cevap": 0
    },
    {
        "soru": "Oruçlu bir kimsenin hataen bir şey yemesi orucu bozar mı?",
        "secenekler": [
            "Evet, kaza gerekir",
            "Evet, kefaret gerekir",
            "Hayır, bozmaz",
            "Sadece namazı bozar"
        ],
        "cevap": 2
    },
    {
        "soru": "Peygamberimizin \"Cennet kadınlarının efendisi\" olarak nitelediği kızı hangisidir?",
        "secenekler": ["Hz. Zeyneb", "Hz. Rukiye", "Hz. Fatıma", "Hz. Ümmü Gülsüm"],
        "cevap": 2
    },
    {
        "soru": "Kur'an-ı Kerim hangi halife döneminde çoğaltılarak önemli merkezlere gönderilmiştir?",
        "secenekler": ["Hz. Ebubekir", "Hz. Ömer", "Hz. Osman", "Hz. Ali"],
        "cevap": 2
    },
    {
        "soru": "Peygamberimizin hicret sırasında saklandığı mağara hangisidir?",
        "secenekler": ["Hira Mağarası", "Sevr Mağarası", "Uhud Mağarası", "Nur Mağarası"],
        "cevap": 1
    },
    {
        "soru": "Müslümanların bir işe karar vermeden önce Allah'tan hayırlısını dilemek için kıldıkları namaz hangisidir?",
        "secenekler": [
            "Şükür Namazı",
            "İstihare Namazı",
            "Hacet Namazı",
            "Tahiyyetü'l-Mescid"
        ],
        "cevap": 1
    },
    {
        "soru": "Aşağıdakilerden hangisi abdestin sünnetlerinden biridir?",
        "secenekler": [
            "Yüzü yıkamak",
            "Başın dörtte birini meshetmek",
            "Elleri dirseklere kadar yıkamak",
            "Misvak kullanmak veya dişleri fırçalamak"
        ],
        "cevap": 3
    },
    {
        "soru": "Firavun'a karşı mucizeleriyle mücadele eden peygamber kimdir?",
        "secenekler": ["Hz. Musa", "Hz. İsa", "Hz. Şuayb", "Hz. Lut"],
        "cevap": 0
    },
    {
        "soru": "Namazların her rekatında okunan zorunlu sure hangisidir?",
        "secenekler": ["İhlas", "Fatiha", "Felak", "Nas"],
        "cevap": 1
    },
    {
        "soru": "Allah yolunda yapılan her türlü maddi ve manevi çabaya ne ad verilir?",
        "secenekler": ["Ticaret", "Cihat", "Siyaset", "Ganimet"],
        "cevap": 1
    }
]

# ---------------- DEĞİŞKENLER ----------------
soru_index = 0
dogru = 0

# ---------------- PENCERE ----------------
root = tk.Tk()
root.title("İslami Bilgi Testi (61–70)")
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
    text="📘 İSLAMİ BİLGİ TESTİ (61–70)",
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
        text=f"{soru_index + 61}. {sorular[soru_index]['soru']}"
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






#  1.ci soru...Allah'ın her an her şeyi yaratmaya devam etmesi sıfatına ne ad verilir?

#  sorular 61.....70 arası 10 soru...tkinter modundadır...

#  terminale bu kadu yapıştırın ve entere basın...

#  bu test butonludur ...üstte static kod resmi var..böyle görüntüleniyor ...


#  pycharm community de altta solda terminale tıkla .... açılan pencereye alttaki kodu yapıştır ....

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_10.py


# python3 "/home/ismail/Documents/Python/gtk-dersi/data/İslami Test/Soruları/islami_test_python_10.py" pardusda

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_10.py  windows da

#  C'deki Klasörü güncellemek için üst solda 4 çizgiye tıkla altta şu yazana tıkla ... Reload all from Disk



