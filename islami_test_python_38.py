import tkinter as tk
from tkinter import messagebox
import random
try:
    import winsound
except:
    winsound = None  # Ses yoksa hata vermesin

# 50 soruluk test listesi (senin verdiğin test_sorular)
test_sorular = [
    {"soru": "Allah'ın var ve bir olmasına ne ad verilir?", "secenekler": ["A) Tevhid", "B) Nübüvvet", "C) Ahiret", "D) Haşir"], "dogru": "A"},
    {"soru": "İmanın şartlarından biri olmayan?", "secenekler": ["A) Meleklere inanmak", "B) Namaz kılmak", "C) Peygamberlere inanmak", "D) Kitaplara inanmak"], "dogru": "B"},
    {"soru": "Zebur hangi peygambere indirilmiştir?", "secenekler": ["A) Hz. Musa", "B) Hz. İsa", "C) Hz. Davud", "D) Hz. İbrahim"], "dogru": "C"},
    {"soru": "Öldükten sonra dirilmeye ne ad verilir?", "secenekler": ["A) Mizan", "B) Berzah", "C) Haşir", "D) Kıyamet"], "dogru": "C"},
    {"soru": "Vahiy getiren melek?", "secenekler": ["A) Mikail", "B) Azrail", "C) İsrafil", "D) Cebrail"], "dogru": "D"},
    {"soru": "Namaza başlarken alınan tekbir?", "secenekler": ["A) İftitah Tekbiri", "B) Kıyam", "C) Ka'de-i Ahire", "D) Secde"], "dogru": "A"},
    {"soru": "Günde kaç vakit namaz farzdır?", "secenekler": ["A) 3", "B) 5", "C) 7", "D) 2"], "dogru": "B"},
    {"soru": "Rükudan sonra alnı yere koymak?", "secenekler": ["A) Kıraat", "B) Secde", "C) Teşehhüd", "D) Selam"], "dogru": "B"},
    {"soru": "Cemaatle kılınması zorunlu namaz?", "secenekler": ["A) Teravih", "B) Bayram", "C) Cuma", "D) Vitir"], "dogru": "C"},
    {"soru": "Oruç tutamayanların verdiği bedel?", "secenekler": ["A) Zekat", "B) Sadaka", "C) Fidye", "D) Fitre"], "dogru": "C"},
    {"soru": "Teyemmüm ne ile alınır?", "secenekler": ["A) Su", "B) Kağıt", "C) Toprak", "D) Kumaş"], "dogru": "C"},
    {"soru": "Kabe etrafında 7 kez dönmek?", "secenekler": ["A) Say", "B) İhram", "C) Vakfe", "D) Tavaf"], "dogru": "D"},
    {"soru": "Zekat için asgari zenginlik?", "secenekler": ["A) Nisap", "B) Miktar", "C) Öşür", "D) Fitre"], "dogru": "A"},
    {"soru": "Peygamberimiz hangi şehirde doğdu?", "secenekler": ["A) Medine", "B) Kudüs", "C) Mekke", "D) Taif"], "dogru": "C"},
    {"soru": "İlk vahiy nerede geldi?", "secenekler": ["A) Sevr Mağarası", "B) Hira Mağarası", "C) Mescid-i Nebevi", "D) Kabe"], "dogru": "B"},
    {"soru": "İlk hicret yeri?", "secenekler": ["A) Habeşistan", "B) Medine", "C) Mısır", "D) Bağdat"], "dogru": "A"},
    {"soru": "Hicret yol arkadaşı?", "secenekler": ["A) Hz. Ömer", "B) Hz. Ali", "C) Hz. Ebubekir", "D) Hz. Osman"], "dogru": "C"},
    {"soru": "İlk büyük savaş?", "secenekler": ["A) Uhud", "B) Hendek", "C) Bedir", "D) Hayber"], "dogru": "C"},
    {"soru": "Peygamberimizin vefat şehri?", "secenekler": ["A) Mekke", "B) Cidde", "C) Şam", "D) Medine"], "dogru": "D"},
    {"soru": "Kur'an'da kaç cüz var?", "secenekler": ["A) 20", "B) 30", "C) 40", "D) 114"], "dogru": "B"},
    {"soru": "Kur'an'ın ilk suresi?", "secenekler": ["A) Bakara", "B) İhlas", "C) Fatiha", "D) Nas"], "dogru": "C"},
    {"soru": "En kısa sure?", "secenekler": ["A) Kevser", "B) Fil", "C) Maun", "D) Kureyş"], "dogru": "A"},
    {"soru": "Besmelesiz sure?", "secenekler": ["A) Yasin", "B) Tevbe", "C) Rahman", "D) Mülk"], "dogru": "B"},
    {"soru": "Kur'an kaç yılda tamamlandı?", "secenekler": ["A) 10", "B) 23", "C) 40", "D) 63"], "dogru": "B"},
    {"soru": "Kur'an ezberleyen?", "secenekler": ["A) Müezzin", "B) İmam", "C) Hafız", "D) Alim"], "dogru": "C"},
    {"soru": "Rızık melek?", "secenekler": ["A) Cebrail", "B) Mikail", "C) Azrail", "D) İsrafil"], "dogru": "B"},
    {"soru": "Allah'ın işitmesi sıfatı?", "secenekler": ["A) İlim", "B) Semi", "C) Basar", "D) Kudret"], "dogru": "B"},
    {"soru": "Peygamberlerin zekası?", "secenekler": ["A) Sıdk", "B) Emanet", "C) Fetanet", "D) Tebliğ"], "dogru": "C"},
    {"soru": "20 sayfalık bölüm?", "secenekler": ["A) Sure", "B) Ayet", "C) Cüz", "D) Hizb"], "dogru": "C"},
    {"soru": "Kabe'yi inşa eden oğul?", "secenekler": ["A) Hz. İshak", "B) Hz. İsmail", "C) Hz. Yakup", "D) Hz. Yusuf"], "dogru": "B"},
    {"soru": "Sadece zenginlere farz?", "secenekler": ["A) Namaz", "B) Oruç", "C) Kelime-i Şehadet", "D) Zekat"], "dogru": "D"},
    {"soru": "Sabah namazı kaç rekat?", "secenekler": ["A) 2", "B) 4", "C) 6", "D) 10"], "dogru": "B"},
    {"soru": "Peygamber kabri?", "secenekler": ["A) Makam-ı İbrahim", "B) Ravza-i Mutahhara", "C) Altınoluk", "D) Hacerü'l Esved"], "dogru": "B"},
    {"soru": "Ramazan sünnet namazı?", "secenekler": ["A) Teheccüd", "B) İşrak", "C) Teravih", "D) Evvabin"], "dogru": "C"},
    {"soru": "Can alan melek?", "secenekler": ["A) Azrail", "B) Mikail", "C) Münker", "D) Nekir"], "dogru": "A"},
    {"soru": "Peygamber dedesi?", "secenekler": ["A) Ebu Talip", "B) Abdülmuttalib", "C) Abdullah", "D) Hamza"], "dogru": "B"},
    {"soru": "İlk ezan okuyan?", "secenekler": ["A) Hz. Ebubekir", "B) Hz. Ali", "C) Bilal-i Habeşi", "D) Zeyd bin Sabit"], "dogru": "C"},
    {"soru": "Mekke'den göç edenler?", "secenekler": ["A) Ensar", "B) Muhacir", "C) Mürted", "D) Münafık"], "dogru": "B"},
    {"soru": "Medineli yardım edenler?", "secenekler": ["A) Ensar", "B) Muhacir", "C) Tabiun", "D) Sahabe"], "dogru": "A"},
    {"soru": "Kur'an kalbi?", "secenekler": ["A) Bakara", "B) Yasin", "C) Mülk", "D) Fetih"], "dogru": "B"},
    {"soru": "Peygamber çocuğu olmayan?", "secenekler": ["A) Zeynep", "B) Ümmü Gülsüm", "C) Safiye", "D) Rukiye"], "dogru": "C"},
    {"soru": "Ramazan Bayramı sadakası?", "secenekler": ["A) Fidye", "B) Fitre", "C) Öşür", "D) Haraç"], "dogru": "B"},
    {"soru": "Kabe hangi şehirde?", "secenekler": ["A) Medine", "B) Cidde", "C) Mekke", "D) Riyad"], "dogru": "C"},
    {"soru": "Allah'ın gücü sıfatı?", "secenekler": ["A) İlim", "B) Kudret", "C) İrade", "D) Tekvin"], "dogru": "B"},
    {"soru": "El-Emin lakabı?", "secenekler": ["A) Hz. Ebubekir", "B) Hz. Ömer", "C) Hz. Muhammed", "D) Hz. Süleyman"], "dogru": "C"},
    {"soru": "Bismillah anlamı?", "secenekler": ["A) Allah en büyüktür", "B) Rahman Rahim Allah adıyla", "C) Hamd Allah'adır", "D) Allah birdir"], "dogru": "B"},
    {"soru": "Müslüman hakkı?", "secenekler": ["A) Selamını almak", "B) Malını almak", "C) Sırrını ifşa", "D) Eleştirmek"], "dogru": "A"},
    {"soru": "İlk eş?", "secenekler": ["A) Hz. Ayşe", "B) Hz. Hafsa", "C) Hz. Hatice", "D) Hz. Sevde"], "dogru": "C"},
    {"soru": "Ameller terazisi?", "secenekler": ["A) Sırat", "B) Mizan", "C) Mahşer", "D) Berzah"], "dogru": "B"},
    {"soru": "İslam temel kaynağı?", "secenekler": ["A) Hadis kitapları", "B) İlmihal", "C) Kur'an-ı Kerim", "D) Fıkıh kitapları"], "dogru": "C"}

]

# Root pencere
root = tk.Tk()
root.title("İslami Bilgi Testi")
root.geometry("700x500")

selected_answer = tk.StringVar(master=root)

score = 0
q_index = 0

def check_answer():
    global score, q_index
    if selected_answer.get() == test_sorular[q_index]["dogru"]:
        score += 1
        if winsound:
            winsound.MessageBeep(winsound.MB_ICONASTERISK)
    else:
        if winsound:
            winsound.MessageBeep(winsound.MB_ICONHAND)

    q_index += 1
    if q_index < len(test_sorular):
        load_question()
    else:
        finish_test()

def load_question():
    question_label.config(text=f"Soru {q_index+1}: {test_sorular[q_index]['soru']}")
    selected_answer.set(None)
    for i, option in enumerate(test_sorular[q_index]["secenekler"]):
        radio_buttons[i].config(text=option, value=option[0])  # "A) ..." → value="A"

def finish_test():
    result = f"Doğru Sayısı: {score}/{len(test_sorular)}\n"
    if score >= 35:  # geçme kriteri örnek: 50 sorudan 35 doğru
        result += "Durum: GEÇTİ ✅"
    else:
        result += "Durum: KALDI ❌"
    messagebox.showinfo("Test Sonucu", result)
    root.destroy()

# Soru alanı
question_label = tk.Label(root, text="", wraplength=600, font=("Arial", 12))
question_label.pack(pady=20)

radio_buttons = []
for i in range(4):
    rb = tk.Radiobutton(root, text="", variable=selected_answer, value="", font=("Arial", 11))
    rb.pack(anchor="w")
    radio_buttons.append(rb)

submit_btn = tk.Button(root, text="Cevabı Onayla", command=check_answer)
submit_btn.pack(pady=20)

load_question()
root.mainloop()



# 1.ci soru... Allah'ın var ve bir olmasına ne ad verilir?

#  sorular 01.....50 arası 50 soru...tkinter modundadır...

#  terminale bu kodu yapıştırın ve entere basın...

#  bu test butonludur ...üstte static kod resmi var..böyle görüntüleniyor ...


#  pycharm community de altta solda terminale tıkla .... açılan pencereye alttaki kodu yapıştır ....

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_38.py


#  & "E:/İslami Test Soruları/.venv/Scripts/python.exe" islami_test_python_38.py   Pardusda

# python3 "/home/ismail/Documents/Python/gtk-dersi/data/İslami Test/Soruları/islami_test_python_38.py" pardusda

#  & "C:\Users\USER\Islamı_Test_Soruları/.venv/Scripts/python.exe" islami_test_python_38.py     windows da

# 01 DEN 50 E KADAR İLERLEYEN SORULAR VAR...SONUNDA BAŞARI DURUMU VE SERTİFİKA ALMA VAR ...

# SES var..ANİMASYON bakmadım.....

#  C'deki Klasörü güncellemek için üst solda 4 çizgiye tıkla altta şu yazana tıkla ... Reload all from Disk
