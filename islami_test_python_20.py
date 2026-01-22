import tkinter as tk
from tkinter import ttk, messagebox
import sys
import time

# ------------------ SORULAR 161–170 ------------------

questions = [
    {"q": "161. Peygamberimizin vefat ettiği yaş kaçtır?",
     "a": ["60", "61", "62", "63"], "c": 3},

    {"q": "162. İslam'da helal kazanç neyi temsil eder?",
     "a": ["Bereket", "Güç", "Ün", "Makam"], "c": 0},

    {"q": "163. Kur'an'da \"anne\" anlamında kullanılan kelime hangisidir?",
     "a": ["Ümm", "Valid", "Ebe", "Anne"], "c": 0},

    {"q": "164. İslam'da kibirli olmak hangi davranıştır?",
     "a": ["Günah", "Sevap", "Farz", "Sünnet"], "c": 0},

    {"q": "165. Peygamberimizin son hutbesine ne ad verilir?",
     "a": ["Veda Hutbesi", "Miraç Hutbesi", "Cuma Hutbesi", "Tebliğ Hutbesi"], "c": 0},

    {"q": "166. Namazda okunan kısa surelere ne denir?",
     "a": ["Uzun sure", "Mekki sure", "Kısa sure", "Zamm-ı sure"], "c": 3},

    {"q": "167. Kur'an'da cennet için kullanılan isim hangisidir?",
     "a": ["Sırat", "Firdevs", "Araf", "Kevser"], "c": 1},

    {"q": "168. İslam'da israf neyi ifade eder?",
     "a": ["Tasarruf", "Ölçülü olmak", "Gereksiz harcama", "Yardımlaşma"], "c": 2},

    {"q": "169. Peygamberimizin kabri hangi mescidin içindedir?",
     "a": ["Mescid-i Haram", "Mescid-i Aksa", "Mescid-i Nebevi", "Kuba Mescidi"], "c": 2},

    {"q": "170. Kur'an'da cehennem için kullanılan isim hangisidir?",
     "a": ["Kevser", "Sırat", "Cehim", "Firdevs"], "c": 2},
]

# ------------------ TKINTER PENCERE ------------------

root = tk.Tk()
root.title("İslami Test (161–170)")
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




# 161.soru.... Peygamberimizin vefat ettiği yaş kaçtır?

#  sorular 161.....170 arası 10 soru...tkinter modundadır...



#  terminale bu kadu yapıştırın ve entere basın...

#  bu test butonludur ...üstte static kod resmi var..böyle görüntüleniyor ...



#  pycharm community de altta solda terminale tıkla .... açılan pencereye alttaki kodu yapıştır ....

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_20.py


# python3 "/home/ismail/Documents/Python/gtk-dersi/data/İslami Test/Soruları/islami_test_python_20.py" pardusda

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_20.py  windows da

#  C'deki Klasörü güncellemek için üst solda 4 çizgiye tıkla altta şu yazana tıkla ... Reload all from Disk


