from tkinter import Tk, Label, Button, LEFT, RIGHT
from PIL import Image, ImageTk

class fotoAlbum:

    def __init__(self, anaSayfa):

        global fotoIndexNo
        fotoIndexNo = 0

        self.anaSayfa = anaSayfa
        anaSayfa.title("Fotoğraflarım")
        self.etiket = Label (anaSayfa, text= "Fotoğraflarım")
        self.etiket.pack()

        self.geriPNG = Image.open ("back.png")
        self.geriFoto = ImageTk.PhotoImage(self.geriPNG)
        self.geri = Button (anaSayfa, image =self.geriFoto, command = self. fotoGeri)
        self.geri.pack()
        self.geri.pack(side= LEFT)


        self.ileriPNG = Image.open("next.png")
        self.ileriFoto =ImageTk.PhotoImage(self.ileriPNG)
        self.ileri = Button (anaSayfa, image =self.ileriFoto, command = self.fotoIleri)
        self.ileri.pack()
        self.ileri.pack(side=RIGHT)

        self.fotoGoster(fotoIndexNo)

    def fotoGeri (self):
        global fotoIndexno
        if(fotoIndexno > 0):
            self.resim.destroy()
            fotoIndexno -=1
            self.fotoGoster(fotoIndexno)
        else:

            self.resim.destroy()
            fotoIndexno = 0
            self.FotoGoster(fotoIndexno)

    def fotoGoster (self, fotoIndex):
        listeFoto = ["IMG_2268.JPG", "IMG_2241.JPG", "IMG_2113.JPG"]

        global listeUzunluk
        listeUzunluk = len(listeFoto)
        self.foto = Image.open(listeFoto(fotoIndex))
        self.tkimage =ImageTk.PhotoImage(self.foto)
        self.resim = Label (root, image = self.tkimage)
        self.resim.pack()

root = Tk()
album = fotoAlbum(root)
root.mainloop()
