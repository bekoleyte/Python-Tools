import random
import string
rakamlar = string.digits
semboller = string.punctuation
kharf=string.ascii_lowercase
bharf=string.ascii_uppercase
tumkarakterler = [rakamlar,semboller,kharf,bharf]
k=0

def dosya_yaz(yeni_sifre):
    try:
        dosya_adi = "sifreler.txt"
        with open(dosya_adi, "a") as dosya:
            dosya.write(str(yeni_sifre) + "\n")
    except Exception as hata:
        print("Hata:", hata)


sayi = int(input("kac adet sifre uretmek istersin"))

while sayi > k:

        sifre = ""
        '''
        for i in range(2):
            sifre += tumkarakterler[0][random.randint(0, 9)]
        for i in range(2):
            sifre += tumkarakterler[1][random.randint(0, 9)]
        for i in range(2):
            sifre += tumkarakterler[2][random.randint(0, 9)]
        for i in range(2):
            sifre += tumkarakterler[3][random.randint(0, 9)]

        '''

        for j in range(4):
            for i in range(2):
                sifre += tumkarakterler[j][random.randint(0, 9)]

        sifre = list(sifre)
        random.shuffle(sifre)

        yeni_sifre = ""
        for i in sifre:
            yeni_sifre += i

        dosya_yaz(yeni_sifre)
        print(yeni_sifre)
        k += 1
        '''
        yeni_sifre = yeni_sifre.join(sifre)
        print(yeni_sifre)
        '''

