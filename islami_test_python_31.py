import tkinter as tk
from tkinter import messagebox
import os, sys

def play_correct():
    if sys.platform.startswith("win"):
        import winsound
        winsound.Beep(1000, 200)
    else:
        os.system("printf '\\a'")

def play_wrong():
    if sys.platform.startswith("win"):
        import winsound
        winsound.Beep(400, 300)
    else:
        os.system("printf '\\a\\a'")

questions = [
    {"q": "1. İslam’ın şartları kaç tanedir?",
     "a": ["3", "4", "5", "6"], "c": 2},
    {"q": "2. Kur’an-ı Kerim kaç sureden oluşur?",
     "a": ["112", "113", "114", "115"], "c": 2},
    {"q": "3. Namaz günde kaç vakittir?",
     "a": ["3", "4", "5", "6"], "c": 2},
    {"q": "4. Oruç hangi ayda tutulur?",
     "a": ["Şaban", "Recep", "Ramazan", "Muharrem"], "c": 2},
    {"q": "5. Müslümanların kıblesi neresidir?",
     "a": ["Kudüs", "Medine", "Kâbe", "Aksa"], "c": 2},
]

root = tk.Tk()
root.title("Sesli İslami Test")
root.geometry("800x500")

current = 0
score = 0
selected = tk.IntVar(value=-1)

label = tk.Label(root, text="", font=("Segoe UI", 16), wraplength=700)
label.pack(pady=20)

buttons = []
for i in range(4):
    rb = tk.Radiobutton(root, text="", variable=selected, value=i,
                        font=("Segoe UI", 13))
    rb.pack(anchor="w", padx=100)
    buttons.append(rb)

def load():
    selected.set(-1)
    q = questions[current]
    label.config(text=q["q"])
    for i in range(4):
        buttons[i].config(text=q["a"][i])

def next_q():
    global current, score

    if selected.get() == -1:
        messagebox.showwarning("Uyarı", "Bir seçenek seçmelisin")
        return

    if selected.get() == questions[current]["c"]:
        score += 1
        play_correct()
    else:
        play_wrong()

    current += 1

    if current < len(questions):
        load()
    else:
        messagebox.showinfo("Bitti",
            f"Test tamamlandı\nDoğru: {score}/{len(questions)}")
        root.destroy()

tk.Button(root, text="İleri ▶", command=next_q,
          font=("Segoe UI", 12, "bold")).pack(pady=20)

load()
root.mainloop()



# 1.ci soru.... İslam’ın şartları kaç tanedir?

# bu test 5 soru vardır ve bib sesi ile dogru ve yanlışları bildirmektedir...


#  pycharm community de altta solda terminale tıkla .... açılan pencereye alttaki kodu yapıştır ....

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_31.py

# python3 "/home/ismail/Documents/Python/gtk-dersi/data/İslami Test/Soruları/islami_test_python_31.py" pardusda

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_31.py windows da

#  C'deki Klasörü güncellemek için üst solda 4 çizgiye tıkla altta şu yazana tıkla ... Reload all from Disk




