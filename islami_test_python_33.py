import tkinter as tk
from datetime import datetime

def sertifika_goster(ad_soyad, puan):
    root = tk.Tk()
    root.title("Başarı Sertifikası")
    root.geometry("800x500")
    root.configure(bg="#fffde7")

    tarih = datetime.now().strftime("%d.%m.%Y")

    # ÇERÇEVE
    frame = tk.Frame(root, bg="#fffde7", bd=4, relief="ridge")
    frame.pack(expand=True, fill="both", padx=20, pady=20)

    tk.Label(
        frame,
        text="🏆 BAŞARI SERTİFİKASI 🏆",
        font=("Times New Roman", 28, "bold"),
        bg="#fffde7"
    ).pack(pady=20)

    tk.Label(
        frame,
        text=f"Bu sertifika\n\n{ad_soyad}",
        font=("Segoe UI", 18, "bold"),
        bg="#fffde7"
    ).pack(pady=10)

    tk.Label(
        frame,
        text="isimli öğrencinin",
        font=("Segoe UI", 14),
        bg="#fffde7"
    ).pack()

    tk.Label(
        frame,
        text="İslami Bilgi Testi'ni başarıyla tamamladığını\nbelgelemek amacıyla verilmiştir.",
        font=("Segoe UI", 14),
        bg="#fffde7",
        justify="center"
    ).pack(pady=15)

    tk.Label(
        frame,
        text=f"Başarı Puanı: {puan}/10",
        font=("Segoe UI", 15, "bold"),
        fg="green",
        bg="#fffde7"
    ).pack(pady=10)

    tk.Label(
        frame,
        text=f"Tarih: {tarih}",
        font=("Segoe UI", 12),
        bg="#fffde7"
    ).pack(pady=10)

    tk.Label(
        frame,
        text="📜 İslami Eğitim Platformu",
        font=("Segoe UI", 12, "italic"),
        bg="#fffde7"
    ).pack(side="bottom", pady=15)

    root.mainloop()


# TEST AMAÇLI ÇALIŞTIRMA
sertifika_goster("İsmail Bozkaya", 8)





#  soru yoktur...... bu test sertifika oluşturma programıdır ...


#  pycharm community de altta solda terminale tıkla .... açılan pencereye alttaki kodu yapıştır ....

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_33.py


#  & "E:/İslami Test Soruları/.venv/Scripts/python.exe" islami_test_python_33.py   Pardusda

# python3 "/home/ismail/Documents/Python/gtk-dersi/data/İslami Test/Soruları/islami_test_python_33.py" pardusda

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_33.py  windows da

#  C'deki Klasörü güncellemek için üst solda 4 çizgiye tıkla altta şu yazana tıkla ... Reload all from Disk

