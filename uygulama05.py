from random import choice
name = input("Adınızı giriniz: ")
print("\nMerhaba " + name, "Adam Asmaca oyununa HOŞGELDİN!")
print(" ")
kelimeler = ["güneş", "asil", "beyaz", "fotoğraf", "python", "yansıma", "çiçek", "ilkbahar", "sarı", "mavi","azim","gökyüzü"]
kelimeler = choice(kelimeler)
tahminler = " "
adamCan = 10
try:
    while adamCan > 0:

        failed = 0

        for harf in kelimeler:

            if harf in tahminler:
                print(harf)
            else:
                print("-")
                failed += 1

            if failed == 0:
                print("Tekrar dene!")
                break


        tahminler = input("Harf giriniz:")
        tahminler += tahminler
        print(tahminler)


        if tahminler not in kelimeler:
            adamCan -= 1
            print("\nYanlış cevap! \nKalan hakkınız: " + str(adamCan))

        if adamCan == 0:
            print("Kaybettiniz!")
except(EOFError) :
      exit







