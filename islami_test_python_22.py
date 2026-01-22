import tkinter as tk
from tkinter import ttk, messagebox
import sys
import time

# ------------------ SORULAR İMAN VE KUR'AN ------------------

# -------------------181---------------190--------------------

questions = [
    {"q": "1. İmanın şartları kaç tanedir?",
     "a": ["4", "5", "6", "7"], "c": 2},

    {"q": "2. Allah'ın \"el-Alîm\" isminin anlamı nedir?",
     "a": ["Affedici", "Her şeyi bilen", "Güçlü", "Merhametli"], "c": 1},

    {"q": "3. Meleklerin yaratıldığı varlık nedir?",
     "a": ["Ateş", "Toprak", "Su", "Nur"], "c": 3},

    {"q": "4. Ahiret hayatının başlamasına ne denir?",
     "a": ["Haşir", "Kıyamet", "Mizan", "Sırat"], "c": 1},

    {"q": "5. Peygamberlerin doğru sözlü olmalarına ne ad verilir?",
     "a": ["Emanet", "Fetanet", "Sıdk", "Tebliğ"], "c": 2},

    {"q": "6. Kur'an-ı Kerim kaç sureden oluşur?",
     "a": ["112", "113", "114", "115"], "c": 2},

    {"q": "7. İlk indirilen sure hangisidir?",
     "a": ["Fatiha", "Alak", "Nas", "Bakara"], "c": 1},

    {"q": "8. Kur'an-ı Kerim hangi dilde indirilmiştir?",
     "a": ["İbranice", "Arapça", "Süryanice", "Farsça"], "c": 1},

    {"q": "9. En uzun sure hangisidir?",
     "a": ["Nisa", "Âl-i İmran", "Bakara", "En'am"], "c": 2},

    {"q": "10. Kur'an'da adı geçen tek kadın kimdir?",
     "a": ["Hz. Hatice", "Hz. Aişe", "Hz. Meryem", "Hz. Fatıma"], "c": 2},
]

# ------------------ TKINTER PENCERE ------------------

root = tk.Tk()
root.title("İslami Test - İman ve Kur'an")
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




#  1.soru... İmanın şartları kaç tanedir?

#  sorular 181.....190 arası 10 soru...tkinter modundadır...

#  terminale bu kadu yapıştırın ve entere basın...

#  bu test butonludur ...üstte static kod resmi var..böyle görüntüleniyor ...



#  pycharm community de altta solda terminale tıkla .... açılan pencereye alttaki kodu yapıştır ....

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_22.py


# python3 "/home/ismail/Documents/Python/gtk-dersi/data/İslami Test/Soruları/islami_test_python_22.py" pardusda

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_22.py  windows da

#  C'deki Klasörü güncellemek için üst solda 4 çizgiye tıkla altta şu yazana tıkla ... Reload all from Disk


