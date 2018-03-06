#Dünya iklimleri ve bitki örtüleri sözlüğü.
iklimler= {"Ekvator","Savan", "Kutup", "Step", "Okyanus","Tundra"}

print(iklimler)

iklimler_dict= {"Ekvator": "Tropikal", "Savan" : "Sayan", "Kutup": "Buzul", "Step": "Bozkır", "Okyanus" : "Geniş Yapraklı Ormanlar", "Tundra": "Tundra" }

print(iklimler_dict.keys())

print("Akdeniz" in iklimler_dict)
iklimler_dict["Akdeniz"]="Maki"
print("Akdeniz" in iklimler)
print(iklimler_dict.keys())

print(iklimler_dict[input("iklim yazınız : ")])
