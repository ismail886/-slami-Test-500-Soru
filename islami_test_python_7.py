import tkinter as tk
from tkinter import ttk, messagebox

# ---------------- SORULAR (31–40) ----------------
sorular = [
    {
        "soru": "İslam'ın beş şartından hangisi sadece zenginlere farzdır?",
        "secenekler": ["Namaz", "Oruç", "Kelime-i Şehadet", "Zekat"],
        "cevap": 3
    },
    {
        "soru": "Sabah namazı kaç rekattır?",
        "secenekler": ["2", "4", "6", "10"],
        "cevap": 1
    },
    {
        "soru": "Peygamberimizin kabrinin bulunduğu yere ne ad verilir?",
        "secenekler": ["Makam-ı İbrahim", "Ravza-i Mutahhara", "Altınoluk", "Hacerü'l Esved"],
        "cevap": 1
    },
    {
        "soru": "Ramazan ayında yatsı namazından sonra kılınan sünnet namaz hangisidir?",
        "secenekler": ["Teheccüd", "İşrak", "Teravih", "Evvabin"],
        "cevap": 2
    },
    {
        "soru": "Allah'ın emriyle can almakla görevli melek hangisidir?",
        "secenekler": ["Azrail", "Mikail", "Münker", "Nekir"],
        "cevap": 0
    },
    {
        "soru": "Peygamberimizin dedesinin adı nedir?",
        "secenekler": ["Ebu Talip", "Abdülmuttalip", "Abdullah", "Hamza"],
        "cevap": 1
    },
    {
        "soru": "İslam tarihinde ilk ezanı okuyan sahabe kimdir?",
        "secenekler": ["Hz. Ebubekir", "Hz. Ali", "Bilal-i Habeşi", "Zeyd bin Sabit"],
        "cevap": 2
    },
    {
        "soru": "Mekke'den Medine'ye göç eden Müslümanlara ne ad verilir?",
        "secenekler": ["Ensar", "Muhacir", "Mürted", "Münafık"],
        "cevap": 1
    },
    {
        "soru": "Medineli olup Mekkeli Müslümanlara yardım edenlere ne denir?",
        "secenekler": ["Ensar", "Muhacir", "Tabiun", "Sahabe"],
        "cevap": 0
    },
    {
        "soru": "Kur'an'ın 'kalbi' olarak bilinen sure hangisidir?",
        "secenekler": ["Bakara", "Yasin", "Mülk", "Fetih"],
        "cevap": 1
    }
]

# ---------------- DEĞİŞKENLER ----------------
soru_index = 0
dogru = 0

# ---------------- PENCERE ----------------
root = tk.Tk()
root.title("İslami Temel Bilgiler Testi – 4")
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
    text="📘 İSLAMİ TEMEL BİLGİLER TESTİ (31–40)",
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
        text=f"{soru_index + 31}. {sorular[soru_index]['soru']}"
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


#  1.ci soru... İslam'ın beş şartından hangisi sadece zenginlere farzdır?

#  sorular 31.....40 arası 10 soru...tkinter modundadır...

#  terminale bu kadu yapıştırın ve entere basın...

#  bu test butonludur ...üstte static kod resmi var..böyle görüntüleniyor ...


#  pycharm community de altta solda terminale tıkla .... açılan pencereye alttaki kodu yapıştır ....

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_7.py



# python3 "/home/ismail/Documents/Python/gtk-dersi/data/İslami Test/Soruları/islami_test_python_7.py" pardusda

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_7.py  windows da

