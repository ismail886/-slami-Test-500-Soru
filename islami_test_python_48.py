

import tkinter as tk
from tkinter import filedialog, messagebox
import datetime
import qrcode
from PIL import Image, ImageDraw, ImageFont, ImageTk
import os

# Ana pencere
root = tk.Tk()
root.title("İslami Bilgi Testi Sertifika Oluşturucu")
root.geometry("400x250")

# İsim giriş alanı
label_name = tk.Label(root, text="Öğrenci Adı Soyadı:", font=("Arial", 12))
label_name.pack(pady=5)

entry_name = tk.Entry(root, font=("Arial", 12), width=30)
entry_name.pack(pady=5)

# Doğru sayısı giriş alanı
label_correct = tk.Label(root, text="Çözülen Doğru Sayısı (500'den):", font=("Arial", 12))
label_correct.pack(pady=5)

entry_correct = tk.Entry(root, font=("Arial", 12), width=30)
entry_correct.pack(pady=5)
entry_correct.insert(0, "250")

def generate_certificate():
    student_name = entry_name.get().strip().upper()
    if not student_name:
        messagebox.showwarning("Uyarı", "Lütfen isim giriniz!")
        return

    try:
        correct_count = int(entry_correct.get())
        if correct_count < 0 or correct_count > 500:
            messagebox.showwarning("Uyarı", "Doğru sayısı 0-500 arasında olmalıdır!")
            return
    except ValueError:
        messagebox.showwarning("Uyarı", "Doğru sayısı sayı formatında olmalıdır!")
        return

    test_count = 50
    total_questions = 500
    success_percentage = (correct_count / total_questions) * 100
    date_str = datetime.datetime.now().strftime("%d.%m.%Y")
    qr_data = f"{student_name} - {test_count} test tamamlandı - {date_str}"

    # Başarı seviyesine göre renk belirle
    if success_percentage >= 90:
        frame_color = "#2ecc71"
        level_text = "# ÇOK BAŞARILI #"
        level_color = "#27ae60"
    elif success_percentage >= 70:
        frame_color = "#f39c12"
        level_text = "# İYİ #"
        level_color = "#e67e22"
    else:
        frame_color = "#e74c3c"
        level_text = "# GEÇTİ #"
        level_color = "#c0392b"

    cert_width, cert_height = 800, 600
    cert_img = Image.new("RGB", (cert_width, cert_height), "#f0f8ff")
    draw = ImageDraw.Draw(cert_img)

    try:
        font_title = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 36)
        font_body = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 24)
        font_small = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 16)
        font_level = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 28)
    except:
        font_title = ImageFont.load_default()
        font_body = ImageFont.load_default()
        font_small = ImageFont.load_default()
        font_level = ImageFont.load_default()

    # Renkli çerçeve
    draw.rectangle([(20, 20), (780, 580)], outline=frame_color, width=5)
    draw.rectangle([(25, 25), (775, 575)], outline=frame_color, width=2)

    # Başlık
    draw.text((50, 60), "İSLAMİ BİLGİ TESTİ SERTİFİKASI", font=font_title, fill="#1e3d59")

    # Başarı seviyesi
    draw.text((150, 110), level_text, font=font_level, fill=level_color)

    # Bilgiler
    draw.text((100, 150), f"Ad Soyad: {student_name}", font=font_body, fill="#2a9d8f")
    draw.text((100, 200), f"Tamamlanan Test Sayısı: {test_count}", font=font_body, fill="#264653")
    draw.text((100, 250), f"Çözülen Doğru Sayısı: {correct_count}/500", font=font_body, fill="#e76f51")
    draw.text((100, 300), f"Başarı Yüzdesi: %{success_percentage:.1f}", font=font_body, fill=level_color)
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

    # İkinci sayfa (İmza Sayfası)
    signature_img = Image.new("RGB", (cert_width, cert_height), "#ffffff")
    sig_draw = ImageDraw.Draw(signature_img)

    sig_draw.rectangle([(20, 20), (780, 580)], outline=frame_color, width=5)
    sig_draw.text((100, 60), f"SERTİFİKA İMZA SAYFASI", font=font_title, fill="#1e3d59")
    sig_draw.text((100, 150), f"Adı Soyadı: {student_name}", font=font_body, fill="#2a9d8f")
    sig_draw.text((100, 200), f"Çözülen Doğru Sayısı: {correct_count}/500", font=font_body, fill="#e76f51")
    sig_draw.text((100, 250), f"Başarı Yüzdesi: %{success_percentage:.1f}", font=font_body, fill=level_color)
    sig_draw.text((100, 300), f"Tarih: {date_str}", font=font_body, fill="#6a4c93")

    # İmza alanları
    sig_draw.text((100, 380), "Öğrenci İmzası:", font=font_body, fill="#000000")
    sig_draw.line([(100, 440), (350, 440)], fill="#000000", width=2)

    sig_draw.text((450, 380), "Yönetici İmzası:", font=font_body, fill="#000000")
    sig_draw.line([(450, 440), (700, 440)], fill="#000000", width=2)

    sig_draw.text((100, 500), f"Sertifika No: {datetime.datetime.now().strftime('%Y%m%d%H%M%S')}", 
                  font=font_small, fill="#666666")

    # Ana pencereyi gizle
    root.withdraw()

    # Yeni pencere (sertifika sayfası)
    cert_window = tk.Toplevel(root)
    cert_window.title("Sertifika")
    cert_window.geometry("850x750")

    # Pencere kapatıldığında ana pencereyi geri getir
    def on_cert_window_close():
        cert_window.destroy()
        root.deiconify()
        entry_name.delete(0, tk.END)
        entry_correct.delete(0, tk.END)
        entry_correct.insert(0, "250")

    cert_window.protocol("WM_DELETE_WINDOW", on_cert_window_close)

    # Frame için label
    label_title = tk.Label(cert_window, text="📄 1. SAYFA - BAŞARI SERTİFİKASI", 
                           font=("Arial", 14, "bold"), bg="#ecf0f1", fg="#1e3d59", pady=10)
    label_title.pack(fill=tk.X)

    cert_tk = ImageTk.PhotoImage(cert_img)
    canvas_cert = tk.Canvas(cert_window, width=800, height=600, bg="white")
    canvas_cert.pack(pady=5)
    canvas_cert.create_image(0, 0, anchor="nw", image=cert_tk)
    canvas_cert.image = cert_tk

    # Sayfa değiştirme butonu
    frame_buttons = tk.Frame(cert_window, bg="#ecf0f1", pady=10)
    frame_buttons.pack(fill=tk.X)

    def show_signature_page():
        canvas_cert.delete("all")
        sig_tk = ImageTk.PhotoImage(signature_img)
        canvas_cert.create_image(0, 0, anchor="nw", image=sig_tk)
        canvas_cert.image = sig_tk
        label_title.config(text="📄 2. SAYFA - İMZA SAYFASI")
        btn_prev.config(state=tk.NORMAL)
        btn_next.config(state=tk.DISABLED)

    def show_certificate_page():
        canvas_cert.delete("all")
        cert_tk2 = ImageTk.PhotoImage(cert_img)
        canvas_cert.create_image(0, 0, anchor="nw", image=cert_tk2)
        canvas_cert.image = cert_tk2
        label_title.config(text="📄 1. SAYFA - BAŞARI SERTİFİKASI")
        btn_prev.config(state=tk.DISABLED)
        btn_next.config(state=tk.NORMAL)

    def save_certificate():
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG Dosyası", "*.png"), ("JPG Dosyası", "*.jpg"), ("Tüm Dosyalar", "*.*")],
            initialfile=f"Sertifika_{student_name}_{date_str.replace('.', '-')}"
        )
        if file_path:
            cert_img.save(file_path)
            sig_file = file_path.replace(".png", "_imza.png").replace(".jpg", "_imza.jpg")
            signature_img.save(sig_file)
            messagebox.showinfo("✅ Başarı", f"Sertifika kaydedildi:\n{file_path}\n\nİmza Sayfası:\n{sig_file}")

    btn_prev = tk.Button(frame_buttons, text="⬅️ Önceki Sayfa", command=show_certificate_page,
                        font=("Arial", 11), bg="#95a5a6", fg="white", padx=10, pady=8, state=tk.DISABLED)
    btn_prev.pack(side=tk.LEFT, padx=5)

    btn_next = tk.Button(frame_buttons, text="Sonraki Sayfa ➡️", command=show_signature_page,
                        font=("Arial", 11), bg="#27ae60", fg="white", padx=10, pady=8)
    btn_next.pack(side=tk.LEFT, padx=5)

    btn_save = tk.Button(frame_buttons, text="💾 Sertifikayı Kaydet", command=save_certificate,
                        font=("Arial", 11), bg="#3498db", fg="white", padx=10, pady=8)
    btn_save.pack(side=tk.LEFT, padx=5)

# Sertifika oluştur butonu
btn_generate = tk.Button(root, text="📄 Sertifika Oluştur", command=generate_certificate,
                        font=("Arial", 12, "bold"), bg="#2ecc71", fg="white", padx=20, pady=10)
btn_generate.pack(pady=20)

root.mainloop()





# 47.ci sürümden farklı olarak başarı yüzdesine göre renkli çerçeve ve başarı seviyesi eklendi.
# Ayrıca imza sayfası ikinci sayfa olarak eklendi.

# sertifika yazma programı ..... 50 test ... 500 soru ...QR kod lu ... Tarihli ...imza alanlı ...2 ayrı sayfa vardır ...

# python3 "/home/ismail/Documents/Python/gtk-dersi/data/İslami Test/Soruları/islami_test_python_0.py" pardusda

# 48 ... 49 ... 50 ... kaldı boş ......


# python3 "/home/ismail/Documents/Python/gtk-dersi/data/İslami Test/Soruları/islami_test_python_0.py" pardusda

