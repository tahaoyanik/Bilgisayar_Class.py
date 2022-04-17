import time



class bilgisayar():
    def __init__(self,marka="HP",ekrankarti_markasi="NVIDIA",ekran_gb=4,ram=16):
        self.marka = marka
        self.ekrankarti_markasi = ekrankarti_markasi
        self.ekran_gb = ekran_gb
        self.ram = ram

    def ram_ekle(self,yeni_ram):
        print("Ram Ekleniyor...")
        time.sleep(1)
        self.ram+=yeni_ram
        print("Ram Eklendi...")


    def ekrangb_arttir(self,yeni_ekrangb):
        print("Yeni Ekran Kartı GB Ekleniyor...")
        time.sleep(1)
        self.ekran_gb += yeni_ekrangb
        print("EKran Kartınız Eklendi...")

    def ekrankarti_degistir(self,yeni_marka):
        print("Ekran Kartı Değiştiriliyor...")
        time.sleep(1)
        self.ekrankarti_markasi = yeni_marka
        print("Ekran Kartı Markanız Değiştirildi...")

    def __str__(self):
        return "Bilgisayar Markası: {}\nEkran Kartı Markası: {}\nEkran Kartı Kapasitesi: {}\nRam Kapasitesi: {}".format(self.marka,self.ekrankarti_markasi,self.ekran_gb,self.ram)


Bilgisayar = bilgisayar()

print("""
İŞLEMLER ;

1. Bilgisayar Bİlgileri

2. Ram Ekle

3. Ekran Kartı Kapasitesi Arttır

4. Ekran Kartı Markası Değiştir
""")

while True:
    islem = input("işlem seçiniz :")
    if islem=="1":
        print("Bİlgiler Yükleniyor...")
        time.sleep(1)
        print(Bilgisayar)
    elif islem == "2":
        yeniram = int(input("Eklemek İstediğiniz GB Seçin(2,4,8):"))
        Bilgisayar.ram_ekle(yeniram)

    elif islem == "3":
        yenigb = int(input("Eklemek İstediğiniz GB Seçin(2,4):"))
        Bilgisayar.ekrangb_arttir(yenigb)

    elif islem == "4":
        yenimarka =  input("İstediğiniz Ekran Kartı Masrkasını Yazınız(Nvidia GeForce,Nvidia GeForce RTX,AMD Radeon RX) :")
        Bilgisayar.ekrankarti_degistir(yenimarka)























