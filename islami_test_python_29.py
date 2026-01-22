import tkinter as tk
from tkinter import messagebox

# ================== 10 TEST / 100 SORU ==================

question_groups = [

    # ========= TEST 1 (1–10) =========
    [
        {"q": "1. Allah'ın bir ve tek olması ne ad verilir?",
         "a": ["Nübüvvet", "Tevhid", "Ahiret", "Kıyamet"], "c": 1},

        {"q": "2. Kur'an hangi dilde indirilmiştir?",
         "a": ["Türkçe", "Arapça", "Farsça", "İbranice"], "c": 1},

        {"q": "3. Günde kaç vakit namaz farzdır?",
         "a": ["3", "4", "5", "6"], "c": 2},

        {"q": "4. İlk vahiy hangi suredir?",
         "a": ["Fatiha", "Alak", "Bakara", "Yasin"], "c": 1},

        {"q": "5. Oruç hangi ayda tutulur?",
         "a": ["Recep", "Şaban", "Ramazan", "Muharrem"], "c": 2},

        {"q": "6. Peygamberimiz nerede doğdu?",
         "a": ["Medine", "Taif", "Mekke", "Kudüs"], "c": 2},

        {"q": "7. Kur'an'da adı geçen tek kadın?",
         "a": ["Hz. Havva", "Hz. Meryem", "Hz. Asiye", "Hz. Sare"], "c": 1},

        {"q": "8. Zekât kimlere verilir?",
         "a": ["Zenginlere", "Fakirlere", "Devlete", "Akrabaya"], "c": 1},

        {"q": "9. Müslümanların kıblesi neresidir?",
         "a": ["Medine", "Kudüs", "Kâbe", "Mescid-i Aksa"], "c": 2},

        {"q": "10. Allah'ın her şeyi bilmesine ne denir?",
         "a": ["Basar", "Semi", "İlim", "Kudret"], "c": 2},
    ],

    # ========= TEST 2 (11–20) =========
    [
        {"q": "11. Peygamberimize ilk vahiy nerede geldi?",
         "a": ["Sevr", "Hira", "Uhud", "Nur"], "c": 1},

        {"q": "12. İlk hicret nereye yapıldı?",
         "a": ["Medine", "Taif", "Habeşistan", "Şam"], "c": 2},

        {"q": "13. En büyük günah hangisidir?",
         "a": ["Yalan", "Gıybet", "Şirk", "İsraf"], "c": 2},

        {"q": "14. Namazda ayakta durmaya ne denir?",
         "a": ["Kıyam", "Rükû", "Secde", "Kıraat"], "c": 0},

        {"q": "15. Hangi namaz cemaatle farzdır?",
         "a": ["Bayram", "Teravih", "Cuma", "Vitir"], "c": 2},

        {"q": "16. Kur'an kaç cüzdür?",
         "a": ["20", "30", "40", "114"], "c": 1},

        {"q": "17. İlk ezanı kim okudu?",
         "a": ["Hz. Ömer", "Hz. Bilal", "Hz. Ali", "Hz. Ebubekir"], "c": 1},

        {"q": "18. Kabe hangi şehirde?",
         "a": ["Medine", "Taif", "Mekke", "Cidde"], "c": 2},

        {"q": "19. Allah'ın her şeye gücü yetmesi?",
         "a": ["İlim", "İrade", "Kudret", "Tekvin"], "c": 2},

        {"q": "20. Peygamberimizin son haccı?",
         "a": ["Umre", "Veda Haccı", "Bedir", "Uhud"], "c": 1},
    ],

    # ========= TEST 3 – TEST 10 =========
    # Aşağıdaki şablonu KOPYALA – soruları değiştir

    *[
        [
            {"q": f"{i*10+j+1}. SORU BURAYA",
             "a": ["A", "B", "C", "D"], "c": 0}
            for j in range(10)
        ]
        for i in range(2, 10)
    ]
]

# ================== TKINTER ==================

root = tk.Tk()
root.title("İslami Bilgi Testi")
root.geometry("900x520")

group_i = 0
q_i = 0
score = 0
choice = tk.IntVar(value=-1)

lbl = tk.Label(root, font=("Segoe UI", 16, "bold"), wraplength=820)
lbl.pack(pady=20)

rbs = []
for i in range(4):
    rb = tk.Radiobutton(root, variable=choice, value=i,
                        font=("Segoe UI", 13))
    rb.pack(anchor="w", padx=120)
    rbs.append(rb)

def load():
    q = question_groups[group_i][q_i]
    lbl.config(text=q["q"])
    choice.set(-1)
    for i in range(4):
        rbs[i].config(text=q["a"][i])

def next_q():
    global q_i, group_i, score

    if choice.get() == question_groups[group_i][q_i]["c"]:
        score += 1

    q_i += 1

    if q_i == 10:
        if score >= 6:
            messagebox.showinfo("Başarılı", f"{score}/10 doğru → sonraki test")
            group_i += 1
            if group_i == 10:
                messagebox.showinfo("Tebrikler 🎉", "100 soruyu tamamladınız")
                root.quit()
            score = 0
            q_i = 0
        else:
            messagebox.showwarning("Tekrar", f"{score}/10 doğru → tekrar dene")
            score = 0
            q_i = 0

    load()

tk.Button(root, text="İleri ▶", command=next_q,
          font=("Segoe UI", 13, "bold"),
          bg="#2196f3", fg="white").pack(pady=20)

load()
root.mainloop()



# =======2adet 10lu gurup var====== başarılı olursa diğer teste geçiyor,başarısız olursa tekrar deniyor======

#  1.ci soru ....1. Allah'ın bir ve tek olması ne ad verilir?


#  pycharm community de altta solda terminale tıkla .... açılan pencereye alttaki kodu yapıştır ....

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_29.py


# python3 "/home/ismail/Documents/Python/gtk-dersi/data/İslami Test/Soruları/islami_test_python_29.py" pardusda

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_29.py windows da

#  C'deki Klasörü güncellemek için üst solda 4 çizgiye tıkla altta şu yazana tıkla ... Reload all from Disk

