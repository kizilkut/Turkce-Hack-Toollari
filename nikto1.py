#! /usr/env python
import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet My Nikto")
giris=("""
1)Parametrelere goz at.
2)Standart tarama yap.
3)SSL portunu kullanarak tarama yap.
4)Butun zaafiyetleri tara.
5)SSL portunu kullanarak ve lookup yapmadan tara.
6)Ozel kullanim.
""")
print(giris)
parametreler=("""
Format+ ==> Taramadan sonra kayit islemi yapilacaksa formati belirlenir.(OR:.txt,.html)
-Host+  ==> Site Doamini girmek icin gereklidir. -h
-nossl  ==> SSL katmani uzerinden tarama yapmaz.
-ssl    ==> SSL katmani uzerinden tarama yapar. -p parametresi ile birlikte kullanilirsa firewall asilabilir.
-port+  ==> Istediginiz bir port uzerinden tarama gerceklestirmeye yarar. -p
-Tunning+ > Ustediginiz zaafiyet turunu belirtmeye ve aracin o zafiyeti aramisini saglar. -T
-nolookup > Lookup yapmadan tarar.
-cookie ==> Bulunan cereleri ekrana yansitir. -c
-evasion => Evasion tekniklerini kullanarak tarama yapar,atlatma icin kullanilabilir. -e
**Yanlarinda + isareti bulunan parametreler karsilarina onlari niteleyen deger alirlar.
""")
islemno=int(input("Islem numaranizi giriniz:"))
if(islemno==1):
	print(parametreler)	
elif(islemno==2):
	hedefip=raw_input("Hedef siteyi giriniz:")
	os.system("nikto -h "+hedefip)
elif(islemno==3):
	hedefip=raw_input("Hedef siteyi giriniz:")
	os.system("nikto -h "+hedefip+" -ssl -p 443")
elif(islemno==4):
	hedefip=raw_input("Hedef siteyi giriniz:")
	os.system("nikto -h "+hedefip+" -T 0123456789abcdex")
elif(islemno==5):
	hedefip=raw_input("Hedef siteyi giriniz:")
	os.system("nikto -h "+hedefip+" -ssl -p 443 -nolookup")
elif(islemno==6):
	girdi=raw_input("Girmek istediginiz komut:")
	os.system(girdi)
else:
	print("Hatali deger girdiniz!")




