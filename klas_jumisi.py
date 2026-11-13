щprint("Esap", 3, "*", 4, "=", 12)  // 1-tapsirma
print("Menin' atim Maqpal")  // 2-tapsirma
print('"Python" u\'yrenip atirman')
print(".....................................................................................")

// 4-tapsirma
print("""

      / \\
     /   \\ 
    /     \\
   /_______\\       
    
""")

rint("................................................................")

print(100 // 60)
print(100 % 60 )

print("100 minutta", 100//60, "saat",  100%60, "minut bar")

forstname =input("Atinizdi kiritin: ")
age = input("Jasinizdi kiritin: ")
print(forstname, age, "jasta")

Hemwork
#1.
name = "Maqpal"
age = 15
boyi = 1.60

#2.
print(type("Maqpal"))
print(type(15))
print(type(1.60))

#Tapsirma Ozgeriwshininin turin ekinshi bir ozgeriwshige otiw
#1.
san = "34"
san_int = int(34) + 10
print(san_int)
#2.
a = 15.9
a_float = int(a)
print(a_float)

#3.
year = 2026
name = input("Atin kim? ")
age = int((input("Jasin neshede? ")))
brithday = year - age 
print(brithday, "jili tuwilgan eken")

#ClassWord
ati = input("Atinizdi kiritin: ")
uy_haywani = input(ati + ( "Jaqsi korgen uy haywanin qanday? "))
iyt_pishiq_at = int(input(uy_haywani + "  kunine neshe ret uredi? "))
dawsi = input("Ol qanday daws shigaradi? ")

print(ati + ' ' + uy_haywani + ' ' + str(iyt_pishiq_at) + ' ' + (dawsi * 10))

word = "1 kg 3000 sum"
kg = 5
jami = int(word[5] + word[6] + word[7] + word[-5])

print(jami * kg)

# Classwork

miywe = "Alma"
kg = 2.5
shop = "Bahasi: 18000"

jami = f"{miywe} {kg} kg bahasi {int(shop[8:]) * kg}"

print(jami, "sum boladi")

"""
   str methodi and modify str (Ozgertiw);
"""

name = "aynura"
name = "A" + name[1:]
print(name)

#Jildi ozgertiw
year = "2026"
year = year[:-1] + "8"
print(year)

#Str methods
name = "aydana"
color = "RED"

print(name.capitalize())
print(color.capitalize())

#title haqqinda tusinik
fio = "maqpal sagitjanova nurberovna"
print(fio.title())


#Classwork-1
name = "   Maqpal  $  " #"Maqpal"
#Natijesi
print(name.strip("  $   "))

#Classwork-2
name1 = "     Maqpal"  #Maqpal
#Natijesi
print(name1.lstrip())

#Classwork-3
name2 = "Maqpal    " #Maqpal
#Natijesi
print(name2.rstrip())

#Classwork-4
soz = "Men kushlimen" #Men aqilliman
soz = soz.replace("kushlimen", "aqilliman")
print(soz)

#Classwork-5
soz = "Aspanda aq quslar gaq gaq dedi" #Aspondo aq quslar gog gog dedi
soz = soz.replace("a", "o")
print(soz)

#Classwork
soz = "1911-jili 1811-jili" #"3933-jili 3811-jili"
soz = soz.replace("1911", "3933")
soz = soz.replace("1811", "3811")
print(soz)

region = "Qaraqalpaqstan"
print(region.count("a", 2))
