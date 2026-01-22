import tkinter as tk
from tkinter import ttk, messagebox
import sys
import time

# ------------------ SORULAR 101–110 ------------------

questions = [
    {"q": "101. Peygamberlerin Allah’tan aldıkları emirleri insanlara eksiksiz iletmesine ne denir?",
     "a": ["Emanet", "Tebliğ", "İsmet", "Fetanet"], "c": 1},

    {"q": "102. İslam’da farz olan ilk ibadet hangisidir?",
     "a": ["Oruç", "Zekât", "Namaz", "Hac"], "c": 2},

    {"q": "103. Kur’an-ı Kerim kaç sureden oluşur?",
     "a": ["112", "113", "114", "115"], "c": 2},

    {"q": "104. İslam’ın şartları kaç tanedir?",
     "a": ["4", "5", "6", "7"], "c": 1},

    {"q": "105. Hicret hangi şehirden hangi şehre yapılmıştır?",
     "a": ["Mekke – Taif", "Mekke – Medine", "Medine – Kudüs", "Mekke – Şam"], "c": 1},

    {"q": "106. Peygamberimizin babasının adı nedir?",
     "a": ["Abdullah", "Ebu Talip", "Abbas", "Haris"], "c": 0},

    {"q": "107. Oruç tutmanın farz olduğu ay hangisidir?",
     "a": ["Muharrem", "Şaban", "Ramazan", "Recep"], "c": 2},

    {"q": "108. İslam’da ilk müezzin kimdir?",
     "a": ["Hz. Ali", "Hz. Ömer", "Bilal-i Habeşi", "Ammar"], "c": 2},

    {"q": "109. Kur’an-ı Kerim’in indirilmeye başlandığı gece hangisidir?",
     "a": ["Miraç", "Berat", "Kadir", "Regaip"], "c": 2},

    {"q": "110. Namazda kıyam ne demektir?",
     "a": ["Oturmak", "Secde", "Ayakta durmak", "Rükû"], "c": 2},
]

# ------------------ TKINTER PENCERE ------------------

root = tk.Tk()
root.title("İslami Test (101–110)")
root.geometry("900x600")
root.configure(bg="#e3f2fd")

style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Segoe UI", 12), padding=10)

current = 0
answers = [tk.IntVar(value=-1) for _ in questions]

# ------------------ ANA FRAME ------------------

frame = tk.Frame(root, bg="#e3f2fd")
frame.pack(fill="both", expand=True, padx=30, pady=20)

question_label = tk.Label(
    frame, font=("Segoe UI", 16, "bold"),
    bg="#e3f2fd", wraplength=800, justify="left"
)
question_label.pack(anchor="w", pady=15)

radio_buttons = []
for i in range(4):
    rb = tk.Radiobutton(
        frame, font=("Segoe UI", 13),
        bg="#e3f2fd", anchor="w"
    )
    rb.pack(fill="x", pady=5)
    radio_buttons.append(rb)

# ------------------ FONKSİYONLAR ------------------

def load_question(index):
    question_label.config(text=questions[index]["q"])
    for i, rb in enumerate(radio_buttons):
        rb.config(
            text=questions[index]["a"][i],
            variable=answers[index],
            value=i
        )

def next_q():
    global current
    if current < len(questions) - 1:
        current += 1
        load_question(current)

def prev_q():
    global current
    if current > 0:
        current -= 1
        load_question(current)

def show_result():
    score = 0
    for i, q in enumerate(questions):
        if answers[i].get() == q["c"]:
            score += 1

    if score >= 6:
        play_success_animation()
        messagebox.showinfo("SONUÇ", f"{score}/10 🎉 GEÇTİN")
    else:
        messagebox.showwarning("SONUÇ", f"{score}/10 ❌ KALDIN")

def play_success_animation():
    try:
        if sys.platform == 'win32':
            import winsound
            winsound.PlaySound("applause.wav",
                               winsound.SND_FILENAME | winsound.SND_ASYNC)
        else:
            print('\a', end='', flush=True)
    except:
        pass

    anim = tk.Toplevel(root)
    anim.geometry("400x200")
    anim.configure(bg="#0d47a1")
    tk.Label(
        anim,
        text="🎉 TEBRİKLER 🎉",
        font=("Segoe UI", 22, "bold"),
        fg="white",
        bg="#0d47a1"
    ).pack(expand=True)

    anim.after(2000, anim.destroy)

# ------------------ BUTONLAR ------------------

btn_frame = tk.Frame(root, bg="#e3f2fd")
btn_frame.pack(pady=20)

ttk.Button(btn_frame, text="⏮ Geri", command=prev_q).grid(row=0, column=0, padx=10)
ttk.Button(btn_frame, text="İleri ⏭", command=next_q).grid(row=0, column=1, padx=10)
ttk.Button(btn_frame, text="Testi Bitir", command=show_result).grid(row=0, column=2, padx=10)

# ------------------ BAŞLAT ------------------

load_question(current)
root.mainloop()





#  101.sodan başlıyor... Peygamberlerin Allah’tan aldıkları emirleri insanlara eksiksiz iletmesine ne denir?

#  sorular 121.....130 arası 10 soru...tkinter modundadır...

#  terminale bu kadu yapıştırın ve entere basın...

#  bu test butonludur ...üstte static kod resmi var..böyle görüntüleniyor ...


#  pycharm community de altta solda terminale tıkla .... açılan pencereye alttaki kodu yapıştır ....

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_16.py


# python3 "/home/ismail/Documents/Python/gtk-dersi/data/İslami Test/Soruları/islami_test_python_16.py" pardusda

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_16.py  windows da

#  C'deki Klasörü güncellemek için üst solda 4 çizgiye tıkla altta şu yazana tıkla ... Reload all from Disk



