#!/bin/python
# Creado por: Pr3tyx/N4kzu/K3rbero

import requests
import os
import platform

#Definir clase "color" con colores
class color:
    verde = '\033[92m'
    naranja = '\033[93m'
    rojo = '\033[91m'
    end = '\033[0m'
    negrita = '\033[1m'
    azul = '\033[94m'

# valida desde que sitema se esta ejecutando el script
# para limpiar la pantalla en ejecucion
system = platform.system()

def detectarSys():
    if system == "Linux":
        os.system("clear")
    elif system == "Windows":
        os.system("cls")
    else:
        os.system("exit")

#Definir escaneo
def scan():
    dic = "admin_pages"
    file = open(dic, 'r')

    for words in file:
        words = words.strip()

        r = requests.get(url+"/"+words)
        r = r.status_code
        r = str(r)
        
        if("200" in r):
            print(f"{color.verde}[+] Posible Admin Page encontrado: "+url+"/"+words+f"{color.end}")
            break
        elif("403" in r):
            print(f"{color.naranja}[~] Admin Page encontrado, pero bloqueado: "+url+"/"+words+f"{color.end}")
            break
        else:
            print(f"{color.rojo}[-] Admin Page no encontrado: "+url+"/"+words+f"{color.end}")


#Variable por defecto
dic = "admin_pages"

#os.system("clear")
detectarSys()


banner = f'''{color.azul}
-+- By: k3rbero/n4kzu/pr3tyx -+-

 ▄▄▄▄    ▄▄▄        ██████   ██████ ▄▄▄█████▓ ██▓ ███▄    █   ▄████ 
▓█████▄ ▒████▄    ▒██    ▒ ▒██    ▒ ▓  ██▒ ▓▒▓██▒ ██ ▀█   █  ██▒ ▀█▒
▒██▒ ▄██▒██  ▀█▄  ░ ▓██▄   ░ ▓██▄   ▒ ▓██░ ▒░▒██▒▓██  ▀█ ██▒▒██░▄▄▄░
▒██░█▀  ░██▄▄▄▄██   ▒   ██▒  ▒   ██▒░ ▓██▓ ░ ░██░▓██▒  ▐▌██▒░▓█  ██▓
░▓█  ▀█▓ ▓█   ▓██▒▒██████▒▒▒██████▒▒  ▒██▒ ░ ░██░▒██░   ▓██░░▒▓███▀▒
░▒▓███▀▒ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░  ▒ ░░   ░▓  ░ ▒░   ▒ ▒  ░▒   ▒ 
▒░▒   ░   ▒   ▒▒ ░░ ░▒  ░ ░░ ░▒  ░ ░    ░     ▒ ░░ ░░   ░ ▒░  ░   ░ 
 ░    ░   ░   ▒   ░  ░  ░  ░  ░  ░    ░       ▒ ░   ░   ░ ░ ░ ░   ░ 
 ░            ░  ░      ░        ░            ░           ░       ░ 
      ░
                                          {color.negrita}{color.rojo}Admin Finder{color.end}
'''
print(banner+'\n')
url = str(input(f"{color.negrita}{color.azul}[*] Ingresa la página{color.end} (ej: http://ejemplo.com): "))
if("https://" in url):
    pass
elif("http://" in url):
    pass
else:
    print(f"{color.naranja}{color.negrita}[~] No se ha detectado 'https' o 'http'.")
    url1 = input(f"[*]1: HTTP\n[*]2: HTTPS\n[~]¿Cual desea usar?: ")
    if(url1 =="1"):
        url1 = "http://"
        url = url1+url
    elif(url1 =="2"):
        url1 = "https://"
        url = url1+url
    else:
        print(f"{color.red}[-] Error. Reinicia el programa.{color.end}")
        exit    
print(f"{color.azul}{color.negrita}[*] Página especificada: {color.end}"+url)
a = str(input(f"{color.negrita}{color.azul}[*] Ruta del diccionario {color.end}(Enter por defecto): {color.end}"))
if(a != ''):
    dic = a
else:
    pass

print(f"{color.negrita}{color.azul}[*] Diccionario actual: {color.end}" + dic)
print(f"{color.negrita}{color.azul} -+- -+- -+- ### -+- -+- -+- {color.end}")
print(f"{color.negrita}{color.azul} [~] Cargando...{color.end}")
print(f"{color.negrita}{color.azul} -+- -+- -+- ### -+- -+- -+- {color.end}")

if __name__ == '__main__':
    scan()
