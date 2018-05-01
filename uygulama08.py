__authors__ = "| Onurcan EVREN | Ezgi ÖZDEMİR | Ardıl Serhat BİLGİÇ | Saliha YILDIZ |"

#!/usr/bin/env python
#--coding:utf-8--

from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
class kutuphane:

    def __init__(self,master):
        self.master = master
        master.title("Katalog Ekranı")
        root.wm_iconbitmap("anasayfaico.ico")
        master.geometry("870x525+275+250")
        self.foto = Image.open("anasayfa.jpeg")
        self.tkimage = ImageTk.PhotoImage(self.foto)
        self.resim = Label(root, image=self.tkimage)
        self.resim.grid(column=3)
        master.configure(background="orange")
        Label(master, bg="orange", text='                                                 ').grid(column=2, row=1)

        self.kitap_ekle = Button(master, text="Kitap Ekle", bg="cornflowerblue",fg="black",font = "bold", command = self.kitap_ekle)
        self.kitap_ekle.grid(column=3, row=1)
        self.kitapları_listele = Button(master, text="Kitapları Listele", bg="cornflowerblue", fg="black", font="bold", command= self.listele)
        self.kitapları_listele.grid(column=3,row="2")

        self.arama = Button(master, text="Kitap Ara", bg="cornflowerblue", fg="black", font="bold", command = self.kitapbak)
        self.arama.grid(column=3, row="3")

        self.cikis = Button(master, text="Kapat", command=exit, fg="black", bg="cornflowerblue", font="bold")
        self.cikis.grid(column=3, row="6")

        self.infoButon = Button(master, text="Emeği Geçenler", fg="black", bg="cornflowerblue", font="bold",command=self.info)
        self.infoButon.grid(column=3, row="5")

        self.veriyisil = Button(master, text="Veriyi Sil",fg="black", bg="cornflowerblue", font="bold", command=self.sil)
        self.veriyisil.grid(column=3, row="4")


    def kitap_ekle(self):
        global kitap_adi, yazar_adi, tur, isbn, yayinevi, yayin_yili, kitapbak
        pencere1 = Tk()
        pencere1.wm_iconbitmap("kitapekle.ico")
        pencere1.geometry("250x225+100+75")
        baslik1 = pencere1.title("Kitap Ekle")
        pencere1.configure(background="orange")
        kitap_adi = Entry(pencere1)
        yazar_adi = Entry(pencere1)
        tur = Entry(pencere1)
        isbn = Entry(pencere1)
        yayinevi = Entry(pencere1)
        yayin_yili = Entry(pencere1)

        kitap_adi.grid(column=2, row=2)
        yazar_adi.grid(column=2, row=3)
        tur.grid(column=2,row=4)
        isbn.grid(column=2,row=5)
        yayinevi.grid(column=2,row=6)
        yayin_yili.grid(column=2,row=7)

        Label(pencere1, font = "bold", bg="orange", text='Kitap Ekle').grid(column=2, row=1)
        Label(pencere1, font = "bold", bg="orange", text='Kitap Adı :').grid(column=1, row=2)
        Label(pencere1, font = "bold", bg="orange", text='Yazar Adı :').grid(column=1, row=3)
        Label(pencere1, font = "bold", bg="orange", text='Kitabın Türü :').grid(column=1, row=4)
        Label(pencere1, font = "bold", bg="orange", text='ISBN :').grid(column=1, row=5)
        Label(pencere1, font = "bold", bg="orange", text='Yayınevi :').grid(column=1, row=6)
        Label(pencere1, font = "bold", bg="orange", text='Yayın Yılı :').grid(column=1, row=7)

        self.exit = Button(pencere1, bg="cornflowerblue", text="Kapat", font="bold", command=pencere1.destroy)
        self.exit.grid(column=1, row=8)
        self.kaydet = Button(pencere1, bg="cornflowerblue", text="Kaydet", font="bold", command=self.kitap_kaydet)
        self.kaydet.grid(column=2, row=8)

    def kitap_kaydet(self):
        kayit =  str((kitap_adi.get() + "|" + yazar_adi.get() + "|" + tur.get() + "|" + isbn.get() + "|" + yayinevi.get() + "|" + yayin_yili.get() + "\n"))
        f = open("output.txt", 'a')

        for i in kayit:
            f.write(i)
        f.close()
        self.kaydet.destroy()

    def listele(self):
        pencere3 = Tk()
        file = open("output.txt")
        data = file.read()
        file.close()
        kitap_liste = Label(pencere3, text=data, bg="orange")
        kitap_liste.grid(row=1, column=2)
        self.exit = Button(pencere3, bg="cornflowerblue", text="Kapat", font="bold", command=pencere3.destroy)
        self.exit.grid(column=2, row=3)
        pencere3.wm_iconbitmap("listeico.ico")
        baslik1 = pencere3.title("Kitap Listesi")
        pencere3.configure(background="orange")

    def kitapbak(self):
        global kitap_adi, yazar_adi, tur, isbn, yayinevi, yy
        pencere4 = Tk()
        baslık4 = pencere4.title("Arama Ekranı")
        pencere4.configure(background="orange")
        pencere4.wm_iconbitmap("araico.ico")

        def kitap():
            dosya = open("output.txt", "r")
            veri = dosya.readlines()
            for i in veri:
                if (i.split('|')[0] == self.entryKitap.get()):
                    messagebox.showinfo("Bulunan Kayıt", i)
                    break
                else:
                    messagebox.showinfo("Bulunan Kayıt", "Kayıt Bulunamadı!")

        def yazar():
            dosya = open("output.txt", "r")
            veri = dosya.readlines()
            for i in veri:
                if (i.split('|')[1] == self.entryYazar.get()):
                    messagebox.showinfo("Bulunan Kayıt", i)
                    break
                else:
                    messagebox.showinfo("Bulunan Kayıt", "Kayıt Bulunamadı!")

        def kitapTürü():
            dosya = open("output.txt", "r")
            veri = dosya.readlines()
            for i in veri:
                if (i.split('|')[2] == self.entryKitapTürü.get()):
                    messagebox.showinfo("Bulunan Kayıt", i)
                    break
                else:
                    messagebox.showinfo("Bulunan Kayıt", "Kayıt Bulunamadı!")

        def ısbn():
            dosya = open("output.txt", "r")
            veri = dosya.readlines()
            for i in veri:
                if (i.split('|')[3] == self.entryIsbn.get()):
                    messagebox.showinfo("Bulunan Kayıt", i)
                    break
                else:
                    messagebox.showinfo("Bulunan Kayıt", "Kayıt Bulunamadı!")

        def yayınevi():
            dosya = open("output.txt", "r")
            veri = dosya.readlines()
            for i in veri:
                if (i.split('|')[4] == self.entryYayınevi.get()):
                    messagebox.showinfo("Bulunan Kayıt", i)
                    break
                else:
                    messagebox.showinfo("Bulunan Kayıt", "Kayıt Bulunamadı!")


        def Yayınyılı():
            dosya = open("output.txt", "r")
            veri = dosya.readlines()
            for i in veri:
                if (i.split('|')[5].strip() == self.entryYayınyılı.get()):
                    messagebox.showinfo("Bulunan Kayıt", i)
                    break
                else:
                    messagebox.showinfo("Bulunan Kayıt", "Kayıt Bulunamadı!")

        self.labelKitap = Label(pencere4, bg="orange", fg="black", text="Kitap adıyla sorgula: ")
        self.labelKitap.grid(row=0, column=0)
        self.entryKitap = Entry(pencere4, width="27")
        self.entryKitap.grid(row=0, column=1)
        self.butonKitap = Button(pencere4, text="Ara", bg="cornflowerblue", fg="black", font="bold", command=kitap)
        self.butonKitap.grid(row=0, column=3)

        self.labelYazar = Label(pencere4, bg="orange", fg="black", text="Yazar adıyla sorgula: ")
        self.labelYazar.grid(row=1, column=0)
        self.entryYazar = Entry(pencere4, width="27")
        self.entryYazar.grid(row=1, column=1)
        self.butonYazar = Button(pencere4, text="Ara", bg="cornflowerblue", fg="black",font="bold", command=yazar)
        self.butonYazar.grid(row=1, column=3)

        self.labelKitapTürü = Label(pencere4, bg="orange", fg="black", text="Kitap türüyle sorgula: ")
        self.labelKitapTürü.grid(row=2, column=0)
        self.entryKitapTürü = Entry(pencere4, width="27")
        self.entryKitapTürü.grid(row=2, column=1)
        self.butonKitapTürü = Button(pencere4, text="Ara", bg="cornflowerblue", fg="black", font="bold", command=kitapTürü)
        self.butonKitapTürü.grid(row=2, column=3)

        self.labelIsbn = Label(pencere4, bg="orange", fg="black", text="ISBN ile sorgula: ")
        self.labelIsbn.grid(row=3, column=0)
        self.entryIsbn = Entry(pencere4, width="27")
        self.entryIsbn.grid(row=3, column=1)
        self.butonIsbn = Button(pencere4, text="Ara", bg="cornflowerblue", fg="black", font="bold", command=ısbn)
        self.butonIsbn.grid(row=3, column=3)

        self.labelYayınevi = Label(pencere4, bg="orange", fg="black", text="Yayınevi ile sorgula: ")
        self.labelYayınevi.grid(row=4, column=0)
        self.entryYayınevi = Entry(pencere4, width="27")
        self.entryYayınevi.grid(row=4, column=1)
        self.butonYayınevi = Button(pencere4, text="Ara", bg="cornflowerblue", fg="black", font="bold", command=yayınevi)
        self.butonYayınevi.grid(row=4, column=3)

        self.labelYayınyılı = Label(pencere4, bg="orange", fg="black", text="Yayın yılı ile sorgula: ")
        self.labelYayınyılı.grid(row=5, column=0)
        self.entryYayınyılı = Entry(pencere4, width="27")
        self.entryYayınyılı.grid(row=5, column=1)
        self.butonYayınyılı = Button(pencere4, text="Ara", bg="cornflowerblue", fg="black", font="bold", command=Yayınyılı)
        self.butonYayınyılı.grid(row=5, column=3)

    def info(self):
        messagebox.showinfo("Emeği Geçenler","Onurcan EVREN\nEzgi ÖZDEMİR\nArdıl Serhat BİLGİÇ\nSaliha YILDIZ")

    def sil(self):
        global pencere5
        pencere5 = Tk()
        pencere5.title("DİKKAT!")
        pencere5.configure(background="orange")
        pencere5.wm_iconbitmap("silico.ico")
        Label(pencere5, font="bold", bg="orange", text="Tüm veriler silinecek! Onaylıyor musunuz?").grid(column=2, row=5)
        Button(pencere5, font="bold", bg="cornflowerblue", text="Kabul et", command=self.silonay).grid(column=2, row=7)
        Button(pencere5, font="bold", bg="cornflowerblue", text="Vazgeç", command=pencere5.destroy).grid(column=2, row=8)

    def silonay(self):
        f = open("output.txt", 'w')
        f.write("")
        f.close()
        messagebox.showinfo("Başarılı!","Tüm veriler silindi!")
        pencere5.destroy()

root = Tk()
kutuphanem = kutuphane(root)
root.mainloop()