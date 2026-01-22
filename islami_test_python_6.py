import tkinter as tk
from tkinter import ttk, messagebox

# ---------------- SORULAR (21–30) ----------------
sorular = [
    {
        "soru": "Kur'an-ı Kerim'in ilk suresi hangisidir?",
        "secenekler": ["Bakara", "İhlas", "Fatiha", "Nas"],
        "cevap": 2
    },
    {
        "soru": "Kur'an-ı Kerim'in en kısa suresi hangisidir?",
        "secenekler": ["Kevser", "Fil", "Maun", "Kureyş"],
        "cevap": 0
    },
    {
        "soru": "Hangi surenin başında Besmele bulunmaz?",
        "secenekler": ["Yasin", "Tevbe", "Rahman", "Mülk"],
        "cevap": 1
    },
    {
        "soru": "Kur'an-ı Kerim yaklaşık kaç yılda tamamlanmıştır?",
        "secenekler": ["10", "23", "40", "63"],
        "cevap": 1
    },
    {
        "soru": "Kur'an-ı Kerim'i ezberleyen kişiye ne ad verilir?",
        "secenekler": ["Müezzin", "İmam", "Hafız", "Alim"],
        "cevap": 2
    },
    {
        "soru": "Doğa olaylarını ve rızıkları yönetmekle görevli melek hangisidir?",
        "secenekler": ["Cebrail", "Mikail", "Azrail", "İsrafil"],
        "cevap": 1
    },
    {
        "soru": "Allah'ın her şeyi işitmesi sıfatına ne ad verilir?",
        "secenekler": ["İlim", "Semi", "Basar", "Kudret"],
        "cevap": 1
    },
    {
        "soru": "Peygamberlerin akıllı ve zeki olmaları sıfatına ne denir?",
        "secenekler": ["Sıdk", "Emanet", "Fetanet", "Tebliğ"],
        "cevap": 2
    },
    {
        "soru": "Kur'an-ı Kerim'in her 20 sayfalık bölümüne ne ad verilir?",
        "secenekler": ["Sure", "Ayet", "Cüz", "Hizb"],
        "cevap": 2
    },
    {
        "soru": "Kabe'yi Hz. İbrahim ile birlikte inşa eden oğlu kimdir?",
        "secenekler": ["Hz. İshak", "Hz. İsmail", "Hz. Yakup", "Hz. Yusuf"],
        "cevap": 1
    }
]

# ---------------- DEĞİŞKENLER ----------------
soru_index = 0
dogru = 0

# ---------------- PENCERE ----------------
root = tk.Tk()
root.title("İslami Temel Bilgiler Testi – 3")
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
    text="📘 İSLAMİ TEMEL BİLGİLER TESTİ (21–30)",
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
        text=f"{soru_index + 21}. {sorular[soru_index]['soru']}"
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




#  1.ci soru... Kur'an-ı Kerim'in ilk suresi hangisidir?

#  sorular 21.....30 arası 10 soru...tkinter modundadır...

#  terminale bu kadu yapıştırın ve entere basın...

#  bu test butonludur ...üstte static kod resmi var..böyle görüntüleniyor ...


#  pycharm community de altta solda terminale tıkla .... açılan pencereye alttaki kodu yapıştır ....

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_6.py



# python3 "/home/ismail/Documents/Python/gtk-dersi/data/İslami Test/Soruları/islami_test_python_6.py" pardusda

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_6.py  windows da


