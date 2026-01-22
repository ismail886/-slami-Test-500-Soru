import tkinter as tk
from tkinter import ttk
import random

# ------------------91-----100------------------

questions = [
    {"q": "1. Peygamberlerin günahsız olmalarına ne denir?",
     "a": ["İsmet", "Emanet", "Tebliğ", "Sıdk"], "c": 0},
    {"q": "2. Kur’an-ı Kerim hangi dilde indirilmiştir?",
     "a": ["Türkçe", "Arapça", "Farsça", "İbranice"], "c": 1},
    {"q": "3. Namazın farzlarından biri hangisidir?",
     "a": ["Tesbih", "Niyet", "Salavat", "Dua"], "c": 1},
    {"q": "4. İlk vahiy hangi sureyle başlamıştır?",
     "a": ["Fatiha", "Alak", "Bakara", "Yasin"], "c": 1},
    {"q": "5. Oruç hangi ayda tutulur?",
     "a": ["Şaban", "Recep", "Ramazan", "Muharrem"], "c": 2},
    {"q": "6. Peygamberimizin doğduğu şehir hangisidir?",
     "a": ["Medine", "Mekke", "Taif", "Kudüs"], "c": 1},
    {"q": "7. Kur’an’da adı geçen tek kadın kimdir?",
     "a": ["Hz. Havva", "Hz. Meryem", "Hz. Asiye", "Hz. Sare"], "c": 1},
    {"q": "8. Namaz günde kaç vakittir?",
     "a": ["3", "4", "5", "6"], "c": 2},
    {"q": "9. Müslümanların kıblesi neresidir?",
     "a": ["Mescid-i Aksa", "Kudüs", "Kâbe", "Medine"], "c": 2},
    {"q": "10. Zekât kimlere verilir?",
     "a": ["Zenginlere", "Fakirlere", "Devlete", "Akrabaya"], "c": 1},
]

PASS_SCORE = 6

# ------------------ TKINTER ------------------

root = tk.Tk()
root.title("İslami Bilgi Testi")
root.geometry("900x600")
root.configure(bg="#e3f2fd")

style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Segoe UI", 12), padding=10)

current = 0
answers = [tk.IntVar(value=-1) for _ in questions]

frame = tk.Frame(root, bg="#e3f2fd")
frame.pack(fill="both", expand=True, padx=30, pady=20)

question_lbl = tk.Label(
    frame, font=("Segoe UI", 16, "bold"),
    bg="#e3f2fd", wraplength=800, justify="left"
)
question_lbl.pack(anchor="w", pady=10)

radio_buttons = []
for i in range(4):
    rb = tk.Radiobutton(
        frame, font=("Segoe UI", 13),
        bg="#e3f2fd", anchor="w"
    )
    rb.pack(fill="x", pady=5)
    radio_buttons.append(rb)

# ------------------ FONKSİYONLAR ------------------

def load_question(i):
    question_lbl.config(text=questions[i]["q"])
    for idx, rb in enumerate(radio_buttons):
        rb.config(
            text=questions[i]["a"][idx],
            variable=answers[i],
            value=idx
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

def finish_test():
    correct = 0
    for i, q in enumerate(questions):
        if answers[i].get() == q["c"]:
            correct += 1

    frame.destroy()
    show_result(correct)

# ------------------ SONUÇ + ANİMASYON ------------------

def show_result(score):
    result_frame = tk.Frame(root, bg="#e3f2fd")
    result_frame.pack(fill="both", expand=True)

    text = f"Doğru Sayısı: {score} / {len(questions)}"
    result_lbl = tk.Label(
        result_frame, text=text,
        font=("Segoe UI", 20, "bold"),
        bg="#e3f2fd"
    )
    result_lbl.pack(pady=20)

    status = "🎉 GEÇTİ 🎉" if score >= PASS_SCORE else "❌ KALDI ❌"
    color = "green" if score >= PASS_SCORE else "red"

    status_lbl = tk.Label(
        result_frame, text=status,
        font=("Segoe UI", 28, "bold"),
        fg=color, bg="#e3f2fd"
    )
    status_lbl.pack(pady=10)

    if score >= PASS_SCORE:
        fireworks(result_frame)

def fireworks(parent):
    canvas = tk.Canvas(parent, width=900, height=300, bg="#e3f2fd", highlightthickness=0)
    canvas.pack()

    for _ in range(40):
        x = random.randint(50, 850)
        y = random.randint(50, 250)
        r = random.randint(10, 25)
        color = random.choice(["red", "blue", "green", "orange", "purple"])
        canvas.create_oval(x-r, y-r, x+r, y+r, fill=color, outline="")
        parent.after(50)

# ------------------ BUTONLAR ------------------

btn_frame = tk.Frame(root, bg="#e3f2fd")
btn_frame.pack(pady=10)

ttk.Button(btn_frame, text="⏮ Geri", command=prev_q).grid(row=0, column=0, padx=10)
ttk.Button(btn_frame, text="İleri ⏭", command=next_q).grid(row=0, column=1, padx=10)
ttk.Button(btn_frame, text="✔ Testi Bitir", command=finish_test).grid(row=0, column=2, padx=10)

load_question(current)
root.mainloop()





#  1.soru... Peygamberlerin günahsız olmalarına ne denir?

#  sorular 111.....120 arası 10 soru...tkinter modundadır...

#  terminale bu kadu yapıştırın ve entere basın...

#  bu test butonludur ...üstte static kod resmi var..böyle görüntüleniyor ...


#  pycharm community de altta solda terminale tıkla .... açılan pencereye alttaki kodu yapıştır ....

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_15.py


# python3 "/home/ismail/Documents/Python/gtk-dersi/data/İslami Test/Soruları/islami_test_python_15.py" pardusda

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_15.py  windows da

#  C'deki Klasörü güncellemek için üst solda 4 çizgiye tıkla altta şu yazana tıkla ... Reload all from Disk



