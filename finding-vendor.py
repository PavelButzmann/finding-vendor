#!/bin/python3
#---- Script creado por Herr Stiefel
#---- Obtencion de comandos en switch mediante python

import time, logging, urllib3
import requests as re
from bs4 import BeautifulSoup
from alive_progress import alive_bar
from datetime import date

urllib3.disable_warnings()

today = date.today()
print("... Bienvenido, este programa es para obtener el vendor ...")
print("... de una lista de mac address                         ...")
print("Validando")

url = 'https://api.macvendors.com/'
file = open('/mnt/c/Temp/macaddress.txt','r').read().splitlines()

ciclos = (len(file))

save_file = open("macvendors-"+str(today)+".txt","w")

with alive_bar(ciclos) as bar:
    for i in range(ciclos):
        req = url + file[i]
        req2 = re.get(req, verify=False)
        html = req2.text
        output = html
        save_file.write(file[i] + " -> " + str(output))
        save_file.write("\n")
        time.sleep(1)
        bar()

save_file.close() # Se guarda el documento en la misma ruta donde se ejecuta el programa%
