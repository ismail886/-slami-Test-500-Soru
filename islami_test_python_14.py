import tkinter as tk
from tkinter import ttk, messagebox
import sys
import time
import random

# ------------------81----90----------------
questions = [
    {
        "question": "Allah'ın güzel isimlerine genel olarak ne ad verilir?",
        "options": ["Esma-i Hüsna", "Kelam-ı Kibar", "El-Emin", "Sıfât-ı Zatiye"],
        "answer": "Esma-i Hüsna"
    },
    {
        "question": "Aşağıdakilerden hangisi suyun olmadığı yerde yapılan temizliktir?",
        "options": ["Gusül", "Teyemmüm", "Taharet", "Mesh"],
        "answer": "Teyemmüm"
    },
    {
        "question": "Peygamberimiz kaç yaşında peygamber olmuştur?",
        "options": ["25", "33", "40", "63"],
        "answer": "40"
    },
    {
        "question": "Kur'an-ı Kerim'in ilk suresi hangisidir?",
        "options": ["Bakara", "İhlas", "Fatiha", "Nas"],
        "answer": "Fatiha"
    },
    {
        "question": "İslam'da ilk ezanı okuyan sahabe kimdir?",
        "options": ["Hz. Ali", "Hz. Ömer", "Bilal-i Habeşi", "Hz. Ebubekir"],
        "answer": "Bilal-i Habeşi"
    },
    {
        "question": "Allah'ın her şeyi görmesi sıfatına ne denir?",
        "options": ["İlim", "Semi", "Basar", "Kudret"],
        "answer": "Basar"
    },
    {
        "question": "Kur'an-ı Kerim kaç cüzdür?",
        "options": ["20", "25", "30", "40"],
        "answer": "30"
    },
    {
        "question": "Haccın farzlarından biri hangisidir?",
        "options": ["Say", "Tavaf", "Vakfe", "Hepsi"],
        "answer": "Hepsi"
    },
    {
        "question": "İslam'ın beş şartından hangisi zenginlere farzdır?",
        "options": ["Namaz", "Oruç", "Zekat", "Kelime-i Şehadet"],
        "answer": "Zekat"
    },
    {
        "question": "Allah'ın her şeyi bilmesi sıfatı hangisidir?",
        "options": ["Kudret", "İlim", "Tekvin", "Basar"],
        "answer": "İlim"
    }
]

test_questions = random.sample(questions, 10)

# ------------------ TKINTER ------------------
root = tk.Tk()
root.title("İslami Bilgi Testi")
root.geometry("700x500")
root.configure(bg="#1e293b")

score = 0
q_index = 0
selected = tk.StringVar()

# ------------------ SES ------------------
def play_applause():
    try:
        if sys.platform == 'win32':
            import winsound
            winsound.PlaySound("applause.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
        else:
            print('\a', end='', flush=True)
    except:
        pass

# ------------------ HAVAİ FİŞEK ------------------
canvas = tk.Canvas(root, width=700, height=200, bg="#0f172a", highlightthickness=0)
canvas.pack()

def fireworks(step=0):
    if step > 20:
        return
    canvas.delete("all")
    for _ in range(20):
        x = random.randint(100, 600)
        y = random.randint(50, 150)
        r = step * 3
        color = random.choice(["#38bdf8", "#22c55e", "#facc15", "#f97316"])
        canvas.create_oval(x-r, y-r, x+r, y+r, fill=color, outline="")
    root.after(100, fireworks, step + 1)

# ------------------ UI ------------------
question_label = tk.Label(
    root, text="", wraplength=650, font=("Segoe UI", 14, "bold"),
    fg="white", bg="#1e293b"
)
question_label.pack(pady=20)

options_frame = tk.Frame(root, bg="#1e293b")
options_frame.pack()

radio_buttons = []
for _ in range(4):
    rb = tk.Radiobutton(
        options_frame, text="", variable=selected, value="",
        font=("Segoe UI", 12),
        fg="white", bg="#1e293b", selectcolor="#334155",
        activebackground="#1e293b"
    )
    rb.pack(anchor="w", pady=5)
    radio_buttons.append(rb)

# ------------------ FONKSİYONLAR ------------------
def load_question():
    selected.set("")
    q = test_questions[q_index]
    question_label.config(text=f"{q_index + 1}. {q['question']}")
    for i, option in enumerate(q["options"]):
        radio_buttons[i].config(text=option, value=option)

def next_question():
    global q_index, score
    if selected.get() == "":
        messagebox.showwarning("Uyarı", "Lütfen bir seçenek seçin")
        return

    if selected.get() == test_questions[q_index]["answer"]:
        score += 10

    q_index += 1
    if q_index < len(test_questions):
        load_question()
    else:
        finish_test()

def finish_test():
    for widget in root.winfo_children():
        widget.destroy()

    result = "GEÇTİ 🎉" if score >= 70 else "KALDI ❌"

    tk.Label(
        root, text=f"Puan: {score}\nDurum: {result}",
        font=("Segoe UI", 20, "bold"),
        fg="#22c55e" if score >= 70 else "#ef4444",
        bg="#1e293b"
    ).pack(pady=40)

    if score >= 70:
        play_applause()
        c = tk.Canvas(root, width=700, height=250, bg="#0f172a", highlightthickness=0)
        c.pack()
        globals()["canvas"] = c
        fireworks()

# ------------------ BUTON ------------------
btn = tk.Button(
    root, text="İLERİ ➡",
    font=("Segoe UI", 12, "bold"),
    bg="#22c55e", fg="black",
    command=next_question
)
btn.pack(pady=20)

load_question()
root.mainloop()




#  1.ci soru... Allah'ın güzel isimlerine genel olarak ne ad verilir?

#  sorular 81.....90 arası 10 soru...tkinter modundadır...Baloncuk gösterisi vardır...

#  terminale bu kadu yapıştırın ve entere basın...

#  bu test butonludur ...üstte static kod resmi var..böyle görüntüleniyor ...


#  pycharm community de altta solda terminale tıkla .... açılan pencereye alttaki kodu yapıştır ....

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_14.py



# python3 "/home/ismail/Documents/Python/gtk-dersi/data/İslami Test/Soruları/islami_test_python_14.py" pardusda

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_14.py  windows da


#  C'deki Klasörü güncellemek için üst solda 4 çizgiye tıkla altta şu yazana tıkla ... Reload all from Disk

