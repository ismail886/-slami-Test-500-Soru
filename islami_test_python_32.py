import tkinter as tk
from tkinter import messagebox
import os, sys

def play_correct():                     # dogru ses cevabı
    if sys.platform.startswith("win"):  # windows ise
        import winsound                 # windows modülü
        winsound.Beep(1000, 200)        # frekens ve süre
    else:
        os.system("printf '\\a'")       # diger sistemlerde terminalde ses çalar

def play_wrong():                       # yanlış ses cevabı
    if sys.platform.startswith("win"):  # widows ise
        import winsound                 # windows modülü
        winsound.Beep(400, 300)         # frekans ve süre
    else:
        os.system("printf '\\a\\a'")    # diğer sistemlerde terminalde iki kez ses çalar

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
    {"q": "6. İlk vahiy hangi sure ile başlamıştır?",
     "a": ["Fatiha", "Alak", "Bakara", "Yasin"], "c": 1},
    {"q": "7. Zekât kimlere verilir?",
     "a": ["Zenginlere", "Fakirlere", "Devlete", "Akrabaya"], "c": 1},
    {"q": "8. Peygamberimiz hangi şehirde doğmuştur?",
     "a": ["Medine", "Mekke", "Taif", "Kudüs"], "c": 1},
    {"q": "9. Kur’an’da adı geçen tek kadın kimdir?",
     "a": ["Hz. Havva", "Hz. Meryem", "Hz. Asiye", "Hz. Sare"], "c": 1},
    {"q": "10. Namazın farzlarından biri hangisidir?",
     "a": ["Tesbih", "Niyet", "Salavat", "Dua"], "c": 1},
]

root = tk.Tk()
root.title("Sesli İslami Test")
root.geometry("800x520")

current = 0
score = 0
selected = tk.IntVar(value=-1)

label = tk.Label(root, text="", font=("Segoe UI", 16),
                 wraplength=720, justify="left")
label.pack(pady=20)

buttons = []
for i in range(4):
    rb = tk.Radiobutton(root, text="", variable=selected,
                        value=i, font=("Segoe UI", 13))
    rb.pack(anchor="w", padx=100, pady=3)
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
        messagebox.showwarning("Uyarı", "Lütfen bir seçenek seç")
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
        messagebox.showinfo(
            "Test Bitti 🎉",
            f"Sonuç:\n{score} / {len(questions)} doğru"
        )
        root.destroy()

tk.Button(
    root, text="İleri ▶", command=next_q,
    font=("Segoe UI", 13, "bold"),
    bg="#1976d2", fg="white", padx=20, pady=8
).pack(pady=20)

load()
root.mainloop()




# 1.ci soru.... İslam’ın şartları kaç tanedir?

# bu test 10 soru vardır ve dogru ve yanlışlarda farklı sesler çalmaktadır ...



#  pycharm community de altta solda terminale tıkla .... açılan pencereye alttaki kodu yapıştır ....

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_32.py


#  & "E:/İslami Test Soruları/.venv/Scripts/python.exe" islami_test_python_32.py   Pardusda

# python3 "/home/ismail/Documents/Python/gtk-dersi/data/İslami Test/Soruları/islami_test_python_32.py" pardusda

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_32.py  windows da

#  C'deki Klasörü güncellemek için üst solda 4 çizgiye tıkla altta şu yazana tıkla ... Reload all from Disk

