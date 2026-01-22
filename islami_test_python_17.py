import tkinter as tk
from tkinter import ttk, messagebox
import sys
import time

# ------------------ SORULAR 131–140 ------------------

questions = [
    {"q": "131. Peygamberimize ilk vahiy hangi melek tarafından getirilmiştir?",
     "a": ["Mikail", "Azrail", "İsrafil", "Cebrail"], "c": 3},

    {"q": "132. Kur'an-ı Kerim hangi kitapların devamı niteliğindedir?",
     "a": ["Sadece Tevrat", "Sadece İncil", "İlahi kitapların tamamı", "Zebur"], "c": 2},

    {"q": "133. İslam'da niyet hangi ibadet için şarttır?",
     "a": ["Zekât", "Oruç", "Namaz", "Hepsi"], "c": 3},

    {"q": "134. Peygamberimizin doğduğu şehir hangisidir?",
     "a": ["Medine", "Mekke", "Kudüs", "Taif"], "c": 1},

    {"q": "135. Namazda rükûdan sonra doğrulmaya ne denir?",
     "a": ["Secde", "Kıyam", "Kavme", "Celse"], "c": 2},

    {"q": "136. İslam'da anne-babaya iyi davranmaya ne denir?",
     "a": ["Takva", "İhsan", "Birr", "Sabır"], "c": 2},

    {"q": "137. Kur'an'da \"Oku\" anlamına gelen ilk kelime hangisidir?",
     "a": ["Elhamdülillah", "İkra", "Kul", "Allah"], "c": 1},

    {"q": "138. Peygamberimizin sütannesi kimdir?",
     "a": ["Amine", "Halime", "Ümmü Gülsüm", "Safiye"], "c": 1},

    {"q": "139. İslam'da cuma namazı kimlere farzdır?",
     "a": ["Kadınlara", "Çocuklara", "Erkeklere", "Yolculara"], "c": 2},

    {"q": "140. Kur'an'ın son suresi hangisidir?",
     "a": ["Felak", "Nas", "İhlas", "Kevser"], "c": 1},
]

# ------------------ TKINTER PENCERE ------------------

root = tk.Tk()
root.title("İslami Test (131–140)")
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





#  131.soru... Peygamberimize ilk vahiy hangi melek tarafından getirilmiştir?

#  sorular 131.....140 arası 10 soru...tkinter modundadır...

#  terminale bu kadu yapıştırın ve entere basın...

#  bu test butonludur ...üstte static kod resmi var..böyle görüntüleniyor ...



#  pycharm community de altta solda terminale tıkla .... açılan pencereye alttaki kodu yapıştır ....

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_17.py


# python3 "/home/ismail/Documents/Python/gtk-dersi/data/İslami Test/Soruları/islami_test_python_17.py" pardusda

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_17.py  windows da

#  C'deki Klasörü güncellemek için üst solda 4 çizgiye tıkla altta şu yazana tıkla ... Reload all from Disk



