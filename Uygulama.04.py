#"Kadın adı" , "Erkek adı" , "Mısra sayısı" belirterek otomatik şarkı/şiir sözü oluşturma.

kadinadi = input("Bir kadın adı giriniz :")
erkekadi = input("Bir erkek adı giriniz :")
misra    = int(input("Mısra sayısı giriniz. Maksimum 8 mısra yazdırılabilir :"))

print("-"*60)

print("")
siir    = ["Çalıkuşu yaban gülü", "Mekan tutmuş " + erkekadi + " çölü " , kadinadi  +  kadinadi + " açar gülü" ,kadinadi + " diyen " + erkekadi + " olur ",   erkekadi + " başka" +  kadinadi + " başka", "son yolcusu düşe kalka",  "Sabr-ı Eyyüp gerek aşka" , kadinadi + " diyen " + erkekadi +" olur"]

for olusturulacak_siir in siir[:misra]:
    print(olusturulacak_siir)

print("")

print("-"*60)

if misra > 8:
    print("Geçerli bir mısra sayısı girmediniz..")
    print("Yazdırılan mısra sayısı: 8")
    print("Bu şiir Bilal Özcan'dan alınmıştır.")
else:
    print("Yazdırılan mısra sayısı:", misra)
    print("Bu şiir Bilal Özcan'dan alınmıştır.")




