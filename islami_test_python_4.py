import tkinter as tk
from tkinter import ttk, messagebox

#  sorular 01.....10 arası 10 soru. başka soru  tkinter modundadır.

sorular = [
    {
        "soru": "İslam'ın beş şartından biri olan ve zengin Müslümanların yılda bir kez mallarının belirli bir kısmını ihtiyaç sahiplerine vermesi anlamına gelen ibadet hangisidir?",
        "secenekler": ["Zekat", "Sadaka", "Hac", "Fitre"],
        "cevap": 0
    },
    {
        "soru": "Kur'an-ı Kerim'in en uzun suresi aşağıdakilerden hangisidir?",
        "secenekler": ["Al-i İmran", "Bakara", "Nisa", "Maide"],
        "cevap": 1
    },
    {
        "soru": "İmanın şartlarından biri olan 'Kaza ve Kadere İman', aşağıdakilerden hangisini kapsar?",
        "secenekler": [
            "Sadece geçmişte yaşanan olayları",
            "Allah'ın her şeyi bir ölçüye göre takdir etmesi ve zamanı gelince gerçekleşmesi",
            "Sadece insanların kendi özgür iradesiyle yaptığı seçimleri",
            "Doğa olaylarının tesadüfen meydana gelmesini"
        ],
        "cevap": 1
    },
    {
        "soru": "Peygamber Efendimiz (s.a.v.)'in gece vakti Mescid-i Haram'dan Mescid-i Aksa'ya götürülmesine ne ad verilir?",
        "secenekler": ["Hicret", "Miraç", "İsra", "Vahiy"],
        "cevap": 2
    },
    {
        "soru": "Aşağıdakilerden hangisi abdestin farzlarından biri değildir?",
        "secenekler": [
            "Yüzü yıkamak",
            "Ağza ve burna su vermek",
            "Elleri dirseklerle beraber yıkamak",
            "Başın dörtte birini meshetmek"
        ],
        "cevap": 1
    },
    {
        "soru": "Kur'an-ı Kerim hangi halife döneminde kitap (mushaf) haline getirilmiştir?",
        "secenekler": ["Hz. Ebubekir", "Hz. Ömer", "Hz. Osman", "Hz. Ali"],
        "cevap": 0
    },
    {
        "soru": "İslam dininde 'Ef'al-i Mükellefin' içinde yer alan ve yapılması kesin olarak yasaklanan fiillere ne denir?",
        "secenekler": ["Mekruh", "Haram", "Mübah", "Vacip"],
        "cevap": 1
    },
    {
        "soru": "Aşağıdakilerden hangisi Peygamber Efendimiz (s.a.v.)'in çocuklarından biri değildir?",
        "secenekler": ["Hz. Fatıma", "Hz. Kasım", "Hz. Ayşe", "Hz. İbrahim"],
        "cevap": 2
    },
    {
        "soru": "Kıblenin Kudüs'teki Mescid-i Aksa'dan Mekke'deki Kabe'ye çevrildiği olay ne zaman gerçekleşmiştir?",
        "secenekler": [
            "Hicretten 5 yıl önce",
            "Hicretten yaklaşık 1,5 yıl sonra",
            "Mekke'nin Fethinden hemen sonra",
            "Veda Haccı sırasında"
        ],
        "cevap": 1
    },
    {
        "soru": "Allah'ın her şeyi görmesi sıfatına ne ad verilir?",
        "secenekler": ["İlim", "Semi", "Basar", "Kudret"],
        "cevap": 2
    }
]

# ---------------- DEĞİŞKENLER ----------------
soru_index = 0
dogru = 0

# ---------------- PENCERE ----------------
root = tk.Tk()
root.title("İslami Temel Bilgiler Testi")
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
    text="📘 İSLAMİ TEMEL BİLGİLER TESTİ",
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




#  1.ci soru... İslam'ın beş şartından biri olan ve zengin Müslümanların yılda bir kez 
#  mallarının belirli bir kısmını ihtiyaç sahiplerine vermesi anlamına gelen ibadet hangisidir?

#  sorular 01.....10 arası 10 soru. başka soru  tkinter modundadır.

#  terminale bu kadu yapıştırın ve entere basın...

#  bu test butonludur ...üstte static kod resmi var..böyle görüntüleniyor ...


#  pycharm community de altta solda terminale tıkla .... açılan pencereye alttaki kodu yapıştır ....

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_4.py



# python3 "/home/ismail/Documents/Python/gtk-dersi/data/İslami Test/Soruları/islami_test_python_4.py" pardusda

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_4.py  windows da

