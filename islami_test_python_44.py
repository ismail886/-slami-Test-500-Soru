import tkinter as tk
from tkinter import ttk
import random
import string
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
import os
import qrcode

# Türkçe karakterleri destekleyen fontu kaydet
pdfmetrics.registerFont(TTFont("DejaVu", "DejaVuSans.ttf"))

def on_focus_in(event, default_text):
    if event.widget.get() == default_text:
        event.widget.delete(0, tk.END)

def on_focus_out(event, default_text):
    if event.widget.get() == "":
        event.widget.insert(0, default_text)

def sertifika_olustur():
    # İsim ve soy isim büyük harfe çevriliyor
    isim = isim_giris.get().strip().upper()
    puan = puan_giris.get().strip()

    if not isim or isim == "İSMİNİZİ GİRİN" or not puan.isdigit():
        sonuc_label.config(text="Lütfen geçerli isim ve puan girin.")
        return

    kod = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    tarih = datetime.now().strftime("%d.%m.%Y")
    pdf_dosya = f"sertifika_{isim.replace(' ', '_')}.pdf"

    # QR kod oluştur
    qr_data = f"Sertifika Kodu: {kod} | Katılımcı: {isim} | Tarih: {tarih}"
    qr_img = qrcode.make(qr_data)
    qr_path = "qr_temp.png"
    qr_img.save(qr_path)

    c = canvas.Canvas(pdf_dosya, pagesize=A4)
    width, height = A4

    # Arka plan
    c.setFillColor(HexColor("#f0f4f7"))
    c.rect(0, 0, width, height, fill=1)

    # Başlık
    c.setFont("DejaVu", 28)
    c.setFillColor(HexColor("#2c3e50"))
    c.drawCentredString(width/2, height-100, "BAŞARI SERTİFİKASI")

    # İçerik
    c.setFont("DejaVu", 14)
    c.setFillColor(HexColor("#34495e"))
    c.drawCentredString(width/2, height-180, f"Katılımcı: {isim}")
    c.drawCentredString(width/2, height-210, "İslami Bilgi Testi'ni başarıyla tamamlamıştır.")
    c.drawCentredString(width/2, height-240, f"Başarı Puanı: {puan}/10")

    c.setFillColor(HexColor("#16a085"))
    c.drawCentredString(width/2, height-270, f"Sertifika Kodu: {kod}")
    c.drawCentredString(width/2, height-300, f"Tarih: {tarih}")

    # QR kodu PDF'e ekle (üst sağ köşe)
    c.drawImage(qr_path, width-100, height-100, width=80, height=80)

    c.showPage()
    c.save()

    try:
        os.startfile(pdf_dosya)
        sonuc_label.config(text=f"Sertifika PDF oluşturuldu ve açıldı: {pdf_dosya}")
    except Exception as e:
        sonuc_label.config(text=f"Sertifika oluşturuldu ama açılamadı: {e}")

# Tkinter arayüz
root = tk.Tk()
root.title("Modern Sertifika Oluşturucu")
root.geometry("450x400")
root.configure(bg="#f0f4f7")

isim_giris = ttk.Entry(root, font=("Segoe UI", 12), width=30)
isim_giris.insert(0, "İsminizi girin")
isim_giris.bind("<FocusIn>", lambda e: on_focus_in(e, "İsminizi girin"))
isim_giris.bind("<FocusOut>", lambda e: on_focus_out(e, "İsminizi girin"))
isim_giris.pack(pady=10)

puan_giris = ttk.Entry(root, font=("Segoe UI", 12), width=30)
puan_giris.insert(0, "Başarı puanınızı girin (örn: 100)")
puan_giris.bind("<FocusIn>", lambda e: on_focus_in(e, "Başarı puanınızı girin (örn: 100)"))
puan_giris.bind("<FocusOut>", lambda e: on_focus_out(e, "Başarı puanınızı girin (örn: 100)"))
puan_giris.pack(pady=10)

olustur_btn = ttk.Button(root, text="Sertifikayı Oluştur (PDF + QR)", command=sertifika_olustur)
olustur_btn.pack(pady=20)

sonuc_label = tk.Label(root, text="", font=("Segoe UI", 11), bg="#f0f4f7", justify="center")
sonuc_label.pack(pady=10)

root.mainloop()



# QR kod eklenmiş  sertifika yazma programı ....  öncekiyle aradaki fark  ( QR ) kod'dur...

#  güzel görünüyor....isim ve puan girmeli...tarih ve sertifika kodlu...sadece sertifika yazma programıdır ...


#  pycharm community de altta solda terminale tıkla...açılan pencereye alttaki kodu yapıştır ....

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_44.py


#  & "E:/İslami Test Soruları/.venv/Scripts/python.exe" islami_test_python_44.py   Pardusda

# python3 "/home/ismail/Documents/Python/gtk-dersi/data/İslami Test/Soruları/islami_test_python_44.py" pardusda

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_44.py     windows da


#  C'deki Klasörü güncellemek için üst solda 4 çizgiye tıkla altta şu yazana tıkla ... Reload all from Disk



