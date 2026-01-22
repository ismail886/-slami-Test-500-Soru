

import tkinter as tk
from tkinter import messagebox
import datetime
import qrcode
from PIL import Image, ImageDraw, ImageFont, ImageTk

def generate_certificate():
    student_name = entry_name.get().strip().upper()
    if not student_name:
        messagebox.showwarning("Uyarı", "Lütfen isim giriniz!")
        return

    test_count = 50
    correct_count = 50
    total_questions = 500
    date_str = datetime.datetime.now().strftime("%d.%m.%Y")
    qr_data = f"{student_name} - {test_count} test tamamlandı - {date_str}"

    cert_width, cert_height = 800, 600
    cert_img = Image.new("RGB", (cert_width, cert_height), "#f0f8ff")
    draw = ImageDraw.Draw(cert_img)

    try:
        font_title = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 36)
        font_body = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 24)
    except:
        font_title = ImageFont.load_default()
        font_body = ImageFont.load_default()

    # Çerçeve
    draw.rectangle([(20, 20), (780, 580)], outline="#1e3d59", width=4)

    # Başlık
    draw.text((50, 60), "İSLAMİ BİLGİ TESTİ SERTİFİKASI", font=font_title, fill="#1e3d59")

    # Bilgiler
    draw.text((100, 150), f"Ad Soyad: {student_name}", font=font_body, fill="#2a9d8f")
    draw.text((100, 200), f"Tamamlanan Test Sayısı: {test_count}", font=font_body, fill="#264653")
    draw.text((100, 250), f"Çözülen Doğru Sayısı: {correct_count}", font=font_body, fill="#e76f51")
    draw.text((100, 300), f"Toplam Soru Sayısı: {total_questions}", font=font_body, fill="#1e3d59")
    draw.text((100, 350), f"Tarih: {date_str}", font=font_body, fill="#6a4c93")

    # Motivasyon metni
    draw.text((100, 450), "Bu testi başarılı bir şekilde tamamladığınız için", font=font_body, fill="#000080")
    draw.text((100, 500), "bu belgeyi almaya hak kazandınız.", font=font_body, fill="#000080")

    # QR kod
    qr = qrcode.make(qr_data)
    qr = qr.resize((80, 80))
    cert_img.paste(qr, (690, 30))

    # İmza alanı
    draw.rectangle([(520, 480), (770, 570)], outline="#000000", width=2)
    draw.text((560, 485), "İmza Alanı:", font=font_body, fill="#000000")

    # Yeni pencere (sertifika sayfası)
    cert_window = tk.Toplevel(root)
    cert_window.title("Sertifika")
    cert_window.geometry("820x720")

    cert_tk = ImageTk.PhotoImage(cert_img)
    canvas_cert = tk.Canvas(cert_window, width=800, height=600)
    canvas_cert.pack()
    canvas_cert.create_image(0, 0, anchor="nw", image=cert_tk)
    canvas_cert.image = cert_tk

    messagebox.showinfo("Sertifika", f"{student_name} için sertifika başarıyla oluşturuldu!")

# Ana pencere (isim girme sayfası)
root = tk.Tk()
root.title("Sertifika Testi - İsim Girişi")
root.geometry("400x200")

tk.Label(root, text="İsim Soyisim:", font=("Arial", 12)).pack(pady=5)
entry_name = tk.Entry(root, font=("Arial", 18), width=30)
entry_name.pack(pady=5)

btn = tk.Button(root, text="SERTİFİKA OLUŞTUR", command=generate_certificate,
                font=("Arial", 16, "bold"), bg="green", fg="white", width=25, height=2)
btn.pack(pady=10)

root.mainloop()






# sertifika yazma programı ..... 50 test ... 500 soru ...QR kod lu ... Tarihli ...imza alanlı ...2 ayrı sayfa vardır ...

# python3 "/home/ismail/Documents/Python/gtk-dersi/data/İslami Test/Soruları/islami_test_python_0.py" pardusda

# 48 ... 49 ... 50 ... kaldı boş ......


# python3 "/home/ismail/Documents/Python/gtk-dersi/data/İslami Test/Soruları/islami_test_python_0.py" pardusda

