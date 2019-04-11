#!/usr/bin/python

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os import system
from getpass import getpass
#############################################################
##                                                        ###
##  CODED BY MARIO YEHEZKIEL                              ###
##  INSTAGRAM : https://www.instagram.com/zcybercru/      ###
##              https://www.instagram.com/mario.yhzkiell/ ###
##                                                        ###
##  official website : https://www.zcybercru.zone.id      ###
##  GITHUB : https://github.com/marioyhzkiell             ###
##  hackerone : https://hackerone.com/marioyhzkiell       ###
##                                                        ###
#############################################################

## PEMBERIAN WARNA ##
merah	= ("\033[91m")
kuning	= ("\033[93m")
ungu	= ("\033[95m")
nila	= ("\033[94m")
hijau	= ("\033[92m")
#####################

########## MENU MAIL SERVER ############
print ('\n\n\n')
print (kuning)
print ('===================================================')
print ('                      MAIL SENDER                  ')
print ('            +++ CODED BY MARIOYHZKIELL +++         ')
print ('===================================================')
print (hijau,'\n\nPilih mail server')
print ('1.gmail')
print ('2.yahoo')
print ('3.yandex')
print ('4.outlook')
print ('\n')
print ('NOTE : turn on less secure apps fiture on your mail account!') 
print ('NOTE : nyalakan fitur aplikasi yang kurang aman di akun email Anda!')
########################################
print ("\n",kuning)
choice = input("masukan pilihan(1/2/3/4): ")
print ("\n",kuning)

email 		= input("masukan email anda : ")
password	=  getpass("masukan password email anda :")
print (merah)
toaddr		= input("masukan email tujuan anda : ")
print (ungu)
judul		= input("masukan judul email anda : ")
print (hijau)
body 		= input("masukan isi email anda : ")
if choice == '1':
	msg = MIMEMultipart()
	msg['From'] = email
	msg['To'] = toaddr
	msg['Subject'] = judul
	msg.attach(MIMEText(body, 'plain'))
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	text = msg.as_string()
	server.login(email,password)
	server.sendmail(email, toaddr, text)
	server.quit()

elif choice == '2':
	msg = MIMEMultipart()
	msg['From'] = email
	msg['To'] = toaddr
	msg['Subject'] = judul
	msg.attach(MIMEText(body, 'plain'))
	server = smtplib.SMTP('smtp.mail.yahoo.com', 587)
	server.starttls()
	text = msg.as_string()
	server.login(email,password)
	server.sendmail(email, toaddr, text)
	server.quit()

elif choice == '3':
	msg = MIMEMultipart()
	msg['From'] = email
	msg['To'] = toaddr
	msg['Subject'] = judul
	msg.attach(MIMEText(body, 'plain'))
	server = smtplib.SMTP('smtp.yandex.com', 587)
	server.starttls()
	text = msg.as_string()
	server.login(email,password)
	server.sendmail(email, toaddr, text)
	server.quit()

elif choice == '4':
	msg = MIMEMultipart()
	msg['From'] = email
	msg['To'] = toaddr
	msg['Subject'] = judul
	msg.attach(MIMEText(body, 'plain'))
	server = smtplib.SMTP('smtp-mail.outlook.com', 587)
	server.starttls()
	text = msg.as_string()
	server.login(email,password)
	server.sendmail(email, toaddr, text)
	server.quit()

else :
	print ("input pilihan salah!!!")
	print ("password tidak ditemukan :", + password)
	system('clear')
	exit()
