# -*- coding: cp1254 -*-
# porscann.py

#Modül İşlemleri
import time
from socket import *

#Giriş
print "    | Port Scanner V1"
print "Cyber Warrior | MuRe Proje Ekibi | Kara Ayaz"
print "Operasyon Başlangıç Saati:"+" "+time.strftime("%H:%M:%S")
print "/"*60

#Bilgi İste & Bilgi Ver
vict = raw_input("Hedef Site: ")
if "http://" in vict:
    victim=vict.replace("http://", "")   
else:
    pass
victimIP = gethostbyname(victim)
print 'Hedef Site Ip Adres: ', victimIP
print "~"*60

# Operasyon Sahası
for port in range(20, 1025):
    giris = socket(AF_INET, SOCK_STREAM)
    result = giris.connect_ex((victimIP, port))
    if(result == 0):
        print "Port %d: AÇIK!" %(port,)
        print "\t Bulma Zamanı:"+" "+time.strftime("%H:%M:%S")
        print "~"*60
    giris.close()

print "Operasyon Tamamlanmıştır"
print "Cyber-Warrior | Kara Ayaz"
