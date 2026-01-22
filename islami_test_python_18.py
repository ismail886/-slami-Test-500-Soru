import tkinter as tk
from tkinter import ttk, messagebox
import sys
import time

# ------------------ SORULAR 141–150 ------------------

questions = [
    {"q": "141. \"Allah yolunda mücadele\" anlamına gelen kavram hangisidir?",
     "a": ["Hicret", "Cihat", "Tebliğ", "Sabır"], "c": 1},

    {"q": "142. Namazda iki secde arasında oturmaya ne denir?",
     "a": ["Kavme", "Kıyam", "Celse", "Rükû"], "c": 2},

    {"q": "143. İslam'da yalan söylememek hangi sıfatla ilgilidir?",
     "a": ["İsmet", "Sıdk", "Emanet", "Fetanet"], "c": 1},

    {"q": "144. Peygamberimizin en küçük kızı kimdir?",
     "a": ["Zeynep", "Rukiye", "Ümmü Gülsüm", "Fatıma"], "c": 3},

    {"q": "145. Kur'an'da besmele ile başlayan sure hangisidir?",
     "a": ["Enfal", "Neml", "Tevbe", "Yasin"], "c": 1},

    {"q": "146. Oruçluyken bilerek yemek yemek neyi bozar?",
     "a": ["Abdest", "Namaz", "Oruç", "Gusül"], "c": 2},

    {"q": "147. İslam'da komşuluk hakkına ne ad verilir?",
     "a": ["Kul hakkı", "İnsan hakkı", "Adalet", "Merhamet"], "c": 0},

    {"q": "148. Peygamberimize verilen ilk mucize hangisidir?",
     "a": ["Miraç", "Kur'an", "Ay'ın yarılması", "İsra"], "c": 1},

    {"q": "149. Kur'an'ın indirildiği dağın adı nedir?",
     "a": ["Uhud", "Nur", "Sevr", "Cudi"], "c": 1},

    {"q": "150. İslam'da sadaka vermek hangi davranışın göstergesidir?",
     "a": ["Cimrilik", "İbadet", "Yardımlaşma", "Sabır"], "c": 2},
]

# ------------------ TKINTER PENCERE ------------------

root = tk.Tk()
root.title("İslami Test (141–150)")
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





#  141.ci soru... "Allah yolunda mücadele\" anlamına gelen kavram hangisidir?

#  sorular 141.....150 arası 10 soru...tkinter modundadır...

#  terminale bu kadu yapıştırın ve entere basın...

#  bu test butonludur ...üstte static kod resmi var..böyle görüntüleniyor ...


#  pycharm community de altta solda terminale tıkla .... açılan pencereye alttaki kodu yapıştır ....

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_18.py



# python3 "/home/ismail/Documents/Python/gtk-dersi/data/İslami Test/Soruları/islami_test_python_18.py" pardusda

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_18.py  windows da

#  C'deki Klasörü güncellemek için üst solda 4 çizgiye tıkla altta şu yazana tıkla ... Reload all from Disk



