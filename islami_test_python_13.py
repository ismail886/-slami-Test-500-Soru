import tkinter as tk
from tkinter import messagebox

# --------------------91----100-------------------
questions = [
    {
        "question": "91. Allah'ın güzel isimlerine genel olarak ne ad verilir?",
        "options": ["Esma-i Hüsna", "Kelam-ı Kibar", "El-Emin", "Sıfât-ı Zatiye"],
        "answer": "Esma-i Hüsna"
    },
    {
        "question": "92. Aşağıdakilerden hangisi suyun olmadığı yerde yapılan temizliktir?",
        "options": ["Gusül", "Teyemmüm", "Taharet", "Mesh"],
        "answer": "Teyemmüm"
    },
    {
        "question": "93. İslam dininin temel inanç esaslarını inceleyen bilim dalı hangisidir?",
        "options": ["Fıkıh", "Akaid / Kelam", "Hadis", "Siyer"],
        "answer": "Akaid / Kelam"
    },
    {
        "question": "94. Zemzem suyu hangi peygamber zamanında ortaya çıkmıştır?",
        "options": ["Hz. Adem", "Hz. İsmail", "Hz. Yunus", "Hz. Süleyman"],
        "answer": "Hz. İsmail"
    },
    {
        "question": "95. Mekke'nin fethi hangi yılda gerçekleşmiştir?",
        "options": ["622", "624", "630", "632"],
        "answer": "630"
    },
    {
        "question": "96. Müslümanların karşılaştığında söyledikleri ilk söz nedir?",
        "options": ["Merhaba", "Nasılsın", "Selamun Aleyküm", "Günaydın"],
        "answer": "Selamun Aleyküm"
    },
    {
        "question": "97. Amelde hak mezhep sayısı kaçtır?",
        "options": ["2", "3", "4", "5"],
        "answer": "4"
    },
    {
        "question": "98. Peygamberimizin söz ve davranışlarına ne denir?",
        "options": ["Sünnet", "İcma", "Kıyas", "İçtihat"],
        "answer": "Sünnet"
    },
    {
        "question": "99. Kıble yönünü gösteren cami bölümü nedir?",
        "options": ["Minber", "Mihrap", "Vaaz Kürsüsü", "Minare"],
        "answer": "Mihrap"
    },
    {
        "question": "100. Allah'ı görüyormuş gibi yaşama bilinci nedir?",
        "options": ["İhsan", "İhlas", "Takva", "Sabır"],
        "answer": "İhsan"
    }
]

# -------------------- UYGULAMA --------------------
class IslamTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🕌 İslami Bilgi Testi")
        self.root.geometry("700x450")
        self.root.configure(bg="#1e293b")

        self.index = 0
        self.score = 0
        self.selected = tk.StringVar()

        self.create_widgets()
        self.load_question()

    def create_widgets(self):
        self.title = tk.Label(
            self.root, text="İSLAMİ BİLGİ TESTİ",
            font=("Segoe UI", 20, "bold"),
            bg="#1e293b", fg="#facc15"
        )
        self.title.pack(pady=15)

        self.question_label = tk.Label(
            self.root, wraplength=600,
            font=("Segoe UI", 14),
            bg="#1e293b", fg="white"
        )
        self.question_label.pack(pady=10)

        self.options_frame = tk.Frame(self.root, bg="#1e293b")
        self.options_frame.pack(pady=10)

        self.options = []
        for i in range(4):
            rb = tk.Radiobutton(
                self.options_frame,
                text="", variable=self.selected, value="",
                font=("Segoe UI", 12),
                bg="#1e293b", fg="white",
                selectcolor="#334155",
                activebackground="#1e293b",
                activeforeground="#facc15"
            )
            rb.pack(anchor="w", pady=5)
            self.options.append(rb)

        self.next_button = tk.Button(
            self.root, text="İleri ➜",
            font=("Segoe UI", 12, "bold"),
            bg="#22c55e", fg="black",
            command=self.next_question
        )
        self.next_button.pack(pady=20)

    def load_question(self):
        self.selected.set(None)
        q = questions[self.index]
        self.question_label.config(text=q["question"])

        for i, option in enumerate(q["options"]):
            self.options[i].config(text=option, value=option)

    def next_question(self):
        if not self.selected.get():
            messagebox.showwarning("Uyarı", "Lütfen bir seçenek seçiniz!")
            return

        if self.selected.get() == questions[self.index]["answer"]:
            self.score += 10

        self.index += 1

        if self.index < len(questions):
            self.load_question()
        else:
            self.show_result()

    def show_result(self):
        result = "GEÇTİ 🎉" if self.score >= 70 else "KALDI ❌"
        messagebox.showinfo(
            "Test Sonucu",
            f"Puanınız: {self.score}/100\nDurum: {result}"
        )
        self.root.destroy()

# -------------------- ÇALIŞTIR --------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = IslamTestApp(root)
    root.mainloop()






#  91.soru... Allah'ın güzel isimlerine genel olarak ne ad verilir?

#  sorular 91.....100 arası 10 soru...tkinter modundadır...

#  terminale bu kadu yapıştırın ve entere basın...

#  bu test butonludur ...üstte static kod resmi var..böyle görüntüleniyor ...


#  pycharm community de altta solda terminale tıkla .... açılan pencereye alttaki kodu yapıştır ....

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_13.py



#  & "E:/İslami Test Soruları/.venv/Scripts/python.exe" islami_test_python_13.py   Pardusda

# python3 "/home/ismail/Documents/Python/gtk-dersi/data/İslami Test/Soruları/islami_test_python_3.py" pardusda

#  C'deki Klasörü güncellemek için üst solda 4 çizgiye tıkla altta şu yazana tıkla ... Reload all from Disk




