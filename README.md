<<<<<<< HEAD
# 🕌 İslami Test Soruları - Tkinter Uygulaması

Bu klasör, İslami konularda test uygulamalarından oluşmaktadır. Her test dosyası Python ve Tkinter kullanarak oluşturulmuş interaktif quiz uygulamalarıdır.

## � Genel İstatistikler

- **Toplam Test Sayısı**: 51 (0-50)
- **Her Test Soru Sayısı**: 10
- **Toplam Soru Havuzu**: 500+
- **Framework**: Tkinter GUI
- **Platform**: Windows/Linux/Mac

---

## 📚 Test Kategorileri

### 1️⃣ Temel İslami Bilgi Testleri (0-14)

| Test | Konu | Soru |
|:----:|:-----|:----:|
| 0 | Temel Bilgiler | 10 |
| 1 | İman ve Kur'an | 10 |
| 2 | Peygamber Hayatı | 10 |
| 3 | Namaz ve İbadetler | 10 |
| 4 | Hac ve Zekat | 10 |
| 5 | Melek ve Ahiret | 10 |
| 6 | Sıdk ve Emanet | 10 |
| 7 | İbadetler Serisi | 10 |
| 8 | Kur'an Ayetleri | 10 |
| 9 | Hadis ve Sünnet | 10 |
| 10 | İslami Ahlak | 10 |
| 11 | Peygamber Kıssaları | 10 |
| 12 | Hz. Ali ve Sahabeler | 10 |
| 13 | Mescidler ve Kutsal Mekanlar | 10 |
| 14 | Kapsamlı Test (100+ Soru) | Değişken |

### 2️⃣ İleri Seviye Testler (15-50)

- **15-20**: Özel Konular
- **21-30**: Derin Kur'an Bilgisi
- **31-40**: İslam Tarihi
- **41-50**: Gelişmiş Konular

---

## 🖼️ Arayüz Görünümü

### Soru Ekranı

```
╔════════════════════════════════════════════════╗
║            🕌 İslami Bilgi Testi               ║
║            Soru: 1 / 10                        ║
║            ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━    ║
║                                                ║
║  Allah'ın var ve bir olmasına ne denir?       ║
║                                                ║
║  ◯ Nübüvvet                                    ║
║  ◯ Tevhid             ✓ DOĞRU                  ║
║  ◯ Ahiret                                      ║
║  ◯ Haşir                                       ║
║                                                ║
║           [ Önceki ]       [ Sonraki ]         ║
║                                                ║
╚════════════════════════════════════════════════╝
```

### Başarı Ekranı

```
╔════════════════════════════════════════════════╗
║              🎉 TEBRİKLER 🎉                   ║
║           Sonuç: 8/10 GEÇTİN ✓                 ║
║     ┌────────────────────────────────────┐    ║
║     │     BAŞARI SERTİFİKASI              │    ║
║     │ Bu sertifika, [ADINIZ] kişisinin  │    ║
║     │ İslami Bilgi Testi'nde başarı     │    ║
║     │ ile geçtiğini göstermektedir.     │    ║
║     │ Puan: 80% | Tarih: 20 Ocak 2026   │    ║
║     └────────────────────────────────────┘    ║
╚════════════════════════════════════════════════╝
```

---

## 🚀 Nasıl Kullanılır?

### Sanal Ortamı Etkinleştir

```bash
source /home/ismail/Documents/Python/gtk-dersi/data/.venv/bin/activate
```

### Herhangi Bir Testi Çalıştır

```bash
# Test 0
python "/home/ismail/Documents/Python/gtk-dersi/data/İslami Test Soruları/islami_test_python_0.py"

# Test 1
python "/home/ismail/Documents/Python/gtk-dersi/data/İslami Test Soruları/islami_test_python_1.py"

# Test 14
python "/home/ismail/Documents/Python/gtk-dersi/data/İslami Test Soruları/islami_test_python_14.py"
```

---

## 📖 Test Çıktıları ve Dokümantasyonu

Her test için detaylı Markdown dokümantasyonu `test_outputs/` klasöründe bulunur:

📂 **test_outputs/**
- `INDEX.md` - Tüm testlerin listesi
- `test_0_output.md` - Test 0 Dokümantasyonu
- `test_1_output.md` - Test 1 Dokümantasyonu
- ... (51 adet toplam)
- `test_50_output.md` - Test 50 Dokümantasyonu

Dokümantasyonda bulunabilir:
- ✓ Test bilgileri
- ✓ ASCII GUI görselleri
- ✓ Örnek sorular
- ✓ Başarı/Başarısızlık ekranları
- ✓ Konu özeti

---

## 🛠️ Gerekli Kütüphaneler

```bash
pip install tkinter pillow qrcode reportlab
```

| Kütüphane | Kullanım |
|-----------|----------|
| tkinter | GUI Arayüzü |
| pillow | Görüntü işleme |
| qrcode | QR kod oluşturma |
| reportlab | PDF oluşturma |

---

## ✨ Özellikler

✅ **Tkinter GUI** - Modern arayüz  
✅ **Otomatik soru karışturma** - Random seçim  
✅ **Puan hesaplama** - Otomatik değerlendirme  
✅ **Sertifika gösterimi** - Başarı belgesi  
✅ **Cross-platform** - Windows/Linux/Mac  
✅ **Ses efektleri** - Windows/Linux/Mac uyumlu  
✅ **Başarı animasyonu** - Visual feedback  

---

## 🌍 Platform Uyumluluğu

| Platform | Durum | Sesler |
|----------|-------|--------|
| **Windows** | ✅ Tam uyumlu | WAV dosyaları |
| **Linux** | ✅ Uyumlu | Sistem bip |
| **macOS** | ✅ Uyumlu | Sistem bip |

---

## 📁 Dosya Yapısı

```
İslami Test Soruları/
├── README.md
├── TEST_0_OUTPUT.md
├── islami_test_python_0.py
├── islami_test_python_1.py
├── ...
├── islami_test_python_50.py
├── applause.wav.wav
└── test_outputs/
    ├── INDEX.md
    ├── test_0_output.md
    ├── test_1_output.md
    ├── ...
    └── test_50_output.md
```

---

## 🎓 Konu Başlıkları

**İman ve Temeleler**
- İmanın şartları
- İslam'ın beş şartı
- Kevhid

**İbadetler**
- Namaz (5 vakit)
- Oruç (Ramazan)
- Zekat (mal vergisi)
- Hac (kutsal yolculuk)

**Tarih ve Kişiler**
- Peygamberimizin hayatı
- Sahaba (Sahabeler)
- Peygamber kıssaları

**Ahlak ve Değerler**
- Doğruluk (Sıdk)
- Emanet
- Adalet
- Hoşgörü

---

## 🔧 Teknik Detaylar

| Özellik | Değer |
|---------|-------|
| Dil | Python 3 |
| Framework | Tkinter |
| Soru Formatı | Çoktan Seçmeli (4 seçenek) |
| Geçme Notu | %50 (5/10 puan) |
| Ses Format | WAV (Windows), Beep (Linux/Mac) |
| Sertifika | Tkinter Window |

---

## 💡 İpuçları

1. **Öncesi**: Dinlenmiş ve odaklanmış olun
2. **Sırasında**: Tüm seçenekleri dikkatli okuyun
3. **Sonrası**: Yanlış cevapları gözden geçirin
4. **Tekrarlama**: Başarısız olursanız tekrar deneyin

---

## ✅ İçerik Özeti

- ✔️ 51 Test dosyası (0-50)
- ✔️ 51 Markdown dokümantasyonu
- ✔️ ASCII GUI görselleri
- ✔️ Örnek sorular
- ✔️ Başarı/başarısızlık ekranları
- ✔️ Platform uyumluluğu
- ✔️ Konu başlıkları

---

# İslami Test Sistemi - 50 Test, 500 Soru

Python Tkinter ile hazırlanmış, **50 test** ve **500 soru** içeren İslami bilgi testi uygulaması.

## 🎯 Özellikler

✅ **50 Test** - Her test 10 sorulu
✅ **500 Soru** - Kapsamlı İslami bilgi
✅ **Renkli Arayüz** - Python Tkinter GUI
✅ **Sertifika Sistemi** - QR kod ile sertifika oluşturma
✅ **Dinamik Puan Hesaplama** - Başarı yüzdesi gösterimi
✅ **Kolay Kurulum** - Basit ve hızlı

## 🚀 Kurulum

### Gerekli Kütüphaneler

```bash
pip install pillow qrcode
```

### Çalıştırma

**Windows:**
```bash
python islami_test_python_46.py
```

**Linux/Mac:**
```bash
python3 islami_test_python_46.py
```

## 📊 Test Yapısı

- Test 1-10: İmanın şartları, Kur'an, Namaz
- Test 11-20: Oruç, Zekât, Hac
- Test 21-50: Peygamberler, Sahabeler, İslami tarih

## 📜 Sertifika

Testi tamamladıktan sonra:
- Adınızı girin
- Otomatik sertifika oluşturulur
- QR kod ile doğrulama yapabilirsiniz

## 👨‍💻 Geliştirici

İsmail886

## 📝 Lisans

Open Source - Özgürce kullanabilirsiniz

...

**🕌 İslami Bilgi Testleri - Kapsamlı Eğitim Platformu**  
*Tarih: 20 Ocak 2026 | Sürüm: 1.0 | Dil: Türkçe*
=======
# -Islamı-Test-500-Soru
>>>>>>> 06207658c7eaf8ea54c5d193596a5882a893ae2c
