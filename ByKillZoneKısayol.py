import os


os.system("apt-get install figlet")
os.system("clear")
os.system("figlet By KillZone")

print("""


  Hepsinde Firewall Atlatma Etkin
***********************************
*     1)Nmap Versiyon Taraması    *
*     2)Nmap Sistem Taraması      *
*     3)Tümü                      *
***********************************
""")

islemno = input("İslem Numarasi Seçiniz:")


if(islemno=="1"):
    hedefip = input("Hedef Site:")
    os.system("nmap  -sV -D7.7.7.7,6.6.6.6,5.5.5.5 " + hedefip)
elif(islemno=="2"):
    hedefip = input("Hedef Site:")
    os.system("nmap -O -D7.7.7.7,6.6.6.6,5.5.5.5 " + hedefip)
elif(islemno=="3"):
    hedefip = input("Hedef Site:")
    os.system("nmap -D7.7.7.7,6.6.6.6,5.5.5.5 -A " + hedefip)
else:
    print("Yanlis İslem")
    os.system("python3 deneme.py")
