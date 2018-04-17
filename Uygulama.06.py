import random
from tkinter import Tk, Label, Button, LEFT, RIGHT,W



class Menü:
    def __init__(self, master):
        self.master = master
        master.title("Menüler")


        self.label = Label(master, text="GÜNÜN MENÜSÜ", font = "Times 25 bold underline", bg ="orange")
        self.label.pack()

        self.gününmenüsü_button = Button(master, text="Bugünün menüsü ne?", font =" Calibri 15 bold",bg = "yellow", command=self.menü)
        self.gününmenüsü_button.pack()
        self.gününmenüsü_button.pack(side=LEFT)


        self.close_button = Button(master, text="Çıkış", font ="Calibri 15 bold", bg= "grey", command=master.quit)
        self.close_button.pack()
        self.close_button.pack(side=RIGHT)




    def menü(self):

        menüler= ("\nMinestrone Çorba , Julyen Kebap, Mevsim Salata, Çikolatalı İrmik Helvası, Etsiz Yeşil Mercimek", "\nDomates Çorba, Macar Gulaş, Şehriyeli Pirinç Pilavı, Cacık*Etsiz Patates", "\n Maraş Çorba, Hindi Külbastı, Zyt.Yoğurtlu Bakla, Çilek*Etsiz Mantar Sote", "\nMısır Çorba, Etli Bezelye, Kıymalı Soslu Makarna, Yoğurt*Etsiz Bezelye ")


        secilenmenü = random.choice(menüler)

        self.gününmenüsü = Label(self.master, text= secilenmenü)

        self.gününmenüsü.pack()



root = Tk()

my_gui = Menü(root)

root.mainloop()


