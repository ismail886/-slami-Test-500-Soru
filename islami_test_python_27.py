import tkinter as tk
from tkinter import ttk, messagebox
import sys

# ------------------ SORULAR ------------------ 5 soru var 10 a tamamlayın....

questions = [
     {"q": "31. Takva ne anlama gelir?",
     "a": ["Korkmak", "Allah’a karşı sorumluluk bilinci", "İlim", "Güç"], "c": 1},

    {"q": "32. Dua ne demektir?",
     "a": ["Okumak", "Yardım istemek", "Allah’a yalvarmak", "Sabretmek"], "c": 2},

    {"q": "33. İhlas nedir?",
     "a": ["Gösteriş", "Samimiyet", "Sabır", "Cesaret"], "c": 1},

    {"q": "34. Niyet ibadetlerde neden önemlidir?",
     "a": ["Gelenek olduğu için",
           "Şart olmadığı için",
           "İbadeti geçerli kıldığı için",
           "Kolaylık sağladığı için"], "c": 2},

    {"q": "35. Sünnet neyi kapsar?",
     "a": ["Kur’an ayetlerini",
           "Sahabe sözlerini",
           "Peygamberimizin söz ve davranışlarını",
           "Mezhep görüşlerini"], "c": 2},

]


# ------------------ TKINTER PENCERE ------------------
root = tk.Tk()
root.title("İslami Test - 10 Soru")
root.geometry("900x600")
root.configure(bg="#e3f2fd")

style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Segoe UI", 12), padding=10)

current = 0
answers = [tk.IntVar(value=-1) for _ in questions]

# ------------------ ANA FRAME ------------------
frame = tk.Frame(root, bg="#e3f2fd")
frame.pack(fill="both", expand=True, padx=10, pady=7)

question_label = tk.Label(
    frame,
    font=("Segoe UI", 16, "bold"),
    bg="#e3f2fd",
    wraplength=800,
    justify="left"
)
question_label.pack(anchor="w", pady=15)

radio_buttons = []
for i in range(4):
    rb = tk.Radiobutton(
        frame,
        font=("Segoe UI", 13),
        bg="#e3f2fd",
        anchor="w"
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

    total = len(questions)
    if score >= int(total * 0.7):  # %70 ve üzeri geçer
        play_success_animation()
        messagebox.showinfo("SONUÇ", f"{score}/{total} 🎉 GEÇTİN")
    else:
        messagebox.showwarning("SONUÇ", f"{score}/{total} ❌ KALDIN")

def play_success_animation():
    try:
        if sys.platform == 'win32':
            import winsound
            winsound.PlaySound(
                "applause.wav",
                winsound.SND_FILENAME | winsound.SND_ASYNC
            )
        else:
            print('\a', end='', flush=True)
    except Exception:
        pass

    anim = tk.Toplevel(root)
    anim.title("Tebrikler")
    anim.geometry("400x200+300+200")
    tk.Label(
        anim,
        text="Tebrikler, testi başarıyla geçtiniz!",
        font=("Segoe UI", 14, "bold")
    ).pack(expand=True, pady=40)
    tk.Button(anim, text="Kapat", command=anim.destroy).pack(pady=10)

# ------------------ BUTONLAR ------------------
btn_frame = tk.Frame(root, bg="#e3f2fd")
btn_frame.pack(pady=10)

prev_btn = ttk.Button(btn_frame, text="Önceki", command=prev_q)
prev_btn.grid(row=0, column=0, padx=10)

next_btn = ttk.Button(btn_frame, text="Sonraki", command=next_q)
next_btn.grid(row=0, column=1, padx=10)

result_btn = ttk.Button(btn_frame, text="Testi Bitir", command=show_result)
result_btn.grid(row=0, column=2, padx=10)

# ------------------ BAŞLAT ------------------
load_question(current)
root.mainloop()



#  31.ci sorudan başlıyor.... Takva ne anlama gelir?

#  sorular 201.....230 arası...tkinter modundadır...

#  terminale bu kadu yapıştırın ve entere basın...

#  bu test butonludur ...üstte static kod resmi var..böyle görüntüleniyor ...


#  pycharm community de altta solda terminale tıkla .... açılan pencereye alttaki kodu yapıştır ....

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_27.py



# python3 "/home/ismail/Documents/Python/gtk-dersi/data/İslami Test/Soruları/islami_test_python_27.py" pardusda

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_27.py  .... windows da

#  C'deki Klasörü güncellemek için üst solda 4 çizgiye tıkla altta şu yazana tıkla ... Reload all from Disk

