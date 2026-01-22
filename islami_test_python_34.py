import tkinter as tk
from tkinter import ttk, messagebox
import sys
import time
from datetime import datetime

# ------------------ SORULAR 171–180 ------------------

questions = [
    {"q": "171. İslam'da doğru sözlülüğe ne denir?",
     "a": ["Sıdk", "Emanet", "İsmet", "Fetanet"], "c": 0},

    {"q": "172. Peygamberimizin en yakın arkadaşı kimdir?",
     "a": ["Hz. Ömer", "Hz. Ali", "Hz. Ebubekir", "Hz. Osman"], "c": 2},

    {"q": "173. Kur'an'ın korunmasını Allah'ın üstlendiği ayet hangi surededir?",
     "a": ["Bakara", "Hicr", "Yasin", "Nisa"], "c": 1},

    {"q": "174. İslam'da misafire ikram etmek ne sayılır?",
     "a": ["Zorunluluk", "Günah", "Sevap", "İsraf"], "c": 2},

    {"q": "175. Peygamberimizin \"güzel ahlak\" ile ilgili sözü hangi kavramı anlatır?",
     "a": ["İbadet", "Ahlak", "Takva", "Sabır"], "c": 1},

    {"q": "176. İslam'da helal–haramı belirleyen temel kaynak hangisidir?",
     "a": ["Hadis", "İcma", "Kıyas", "Kur'an"], "c": 3},

    {"q": "177. Kur'an'ın ana konusu nedir?",
     "a": ["Tarih", "Ahlak", "İnanç", "Hepsi"], "c": 3},

    {"q": "178. İslam'da sözünde durmak hangi kavramla ilgilidir?",
     "a": ["Sabır", "Emanet", "Sıdk", "Takva"], "c": 1},

    {"q": "179. Peygamberimizin son peygamber olması ne ile ifade edilir?",
     "a": ["Risalet", "Nübüvvet", "Hatm-i Nübüvvet", "Tebliğ"], "c": 2},

    {"q": "180. İslam'da insanların eşit olduğunu vurgulayan hutbe hangisidir?",
     "a": ["Cuma Hutbesi", "Veda Hutbesi", "Miraç Hutbesi", "Tebliğ Hutbesi"], "c": 1},
]

# ------------------ SERTİFİKA FONKSİYONU ------------------

def sertifika_goster(ad_soyad, puan):
    """Sertifika penceresi gösterir"""
    win = tk.Toplevel()
    win.title("🎓 Başarı Sertifikası")
    win.geometry("700x500")
    win.configure(bg="#ffffff")
    
    # Çerçeve
    cerceve = tk.Frame(win, bg="#0d47a1", padx=20, pady=20)
    cerceve.pack(fill="both", expand=True, padx=20, pady=20)
    
    # İç beyaz alan
    ic_alan = tk.Frame(cerceve, bg="#ffffff", padx=30, pady=30)
    ic_alan.pack(fill="both", expand=True)
    
    # Başlık
    tk.Label(
        ic_alan,
        text="🎓 BAŞARI SERTİFİKASI 🎓",
        font=("Segoe UI", 24, "bold"),
        bg="#ffffff",
        fg="#0d47a1"
    ).pack(pady=20)
    
    # Altın çizgi
    tk.Frame(ic_alan, bg="#ffd700", height=3).pack(fill="x", padx=50)
    
    # İsim
    tk.Label(
        ic_alan,
        text=ad_soyad.upper(),
        font=("Segoe UI", 20, "bold"),
        bg="#ffffff",
        fg="#1976d2"
    ).pack(pady=30)
    
    # Açıklama
    tk.Label(
        ic_alan,
        text="İslami Test Sınavını Başarıyla Tamamlamıştır",
        font=("Segoe UI", 14),
        bg="#ffffff",
        fg="#424242"
    ).pack(pady=10)
    
    # Puan
    tk.Label(
        ic_alan,
        text=f"📊 Puan: {puan}/10",
        font=("Segoe UI", 16, "bold"),
        bg="#ffffff",
        fg="#2e7d32"
    ).pack(pady=15)
    
    # Tarih
    tarih = datetime.now().strftime("%d.%m.%Y")
    tk.Label(
        ic_alan,
        text=f"📅 Tarih: {tarih}",
        font=("Segoe UI", 12),
        bg="#ffffff",
        fg="#757575"
    ).pack(pady=10)
    
    # Altın çizgi
    tk.Frame(ic_alan, bg="#ffd700", height=3).pack(fill="x", padx=50, pady=20)
    
    # Kapat butonu
    tk.Button(
        ic_alan,
        text="KAPAT",
        font=("Segoe UI", 12, "bold"),
        bg="#d32f2f",
        fg="white",
        padx=30,
        pady=10,
        command=win.destroy
    ).pack(pady=10)

def isim_al_ve_sertifika(puan):
    win = tk.Toplevel()
    win.title("İsim Girişi")
    win.geometry("400x200")
    win.configure(bg="#e3f2fd")
    win.grab_set()

    tk.Label(
        win,
        text="Ad Soyad Giriniz",
        font=("Segoe UI", 14, "bold"),
        bg="#e3f2fd"
    ).pack(pady=20)

    entry = tk.Entry(win, font=("Segoe UI", 14), width=25)
    entry.pack(pady=10)
    entry.focus()

    def onayla():
        ad = entry.get().strip()
        if not ad:
            messagebox.showwarning("Uyarı", "Lütfen isminizi giriniz!")
            return
        win.destroy()
        sertifika_goster(ad, puan)

    tk.Button(
        win,
        text="Sertifikayı Göster",
        font=("Segoe UI", 12, "bold"),
        bg="#2196f3",
        fg="white",
        padx=20,
        pady=8,
        command=onayla
    ).pack(pady=20)
    
    # Enter tuşu ile de onaylayabilsin
    entry.bind('<Return>', lambda e: onayla())

# ------------------ TKINTER PENCERE ------------------

root = tk.Tk()
root.title("İslami Test (171–180)")
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
        root.after(500, lambda: isim_al_ve_sertifika(score))
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



# 1.ci soru....171. İslam'da doğru sözlülüğe ne denir?

#  sorular 171.....180 arası 10 soru...tkinter modundadır...

#  terminale bu kodu yapıştırın ve entere basın...

#  bu test butonludur ...üstte static kod resmi var..böyle görüntüleniyor ...



#  pycharm community de altta solda terminale tıkla .... açılan pencereye alttaki kodu yapıştır ....

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_34.py


#  & "E:/İslami Test Soruları/.venv/Scripts/python.exe" islami_test_python_34.py   Pardusda

# python3 "/home/ismail/Documents/Python/gtk-dersi/data/İslami Test/Soruları/islami_test_python_34.py" pardusda

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_34.py     windows da

# ÇOK GÜZEL BİR KOD SAKIN KURCALAMA YAPMAYIN ....HER ŞEY HARİKA ÇALIŞIYOR ..

#  C'deki Klasörü güncellemek için üst solda 4 çizgiye tıkla altta şu yazana tıkla ... Reload all from Disk



