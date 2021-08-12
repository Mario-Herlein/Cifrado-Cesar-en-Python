# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 19:55:07 2021

@author: Mario Herlein
"""

import doctest
import requests
import os
import re
from bs4 import BeautifulSoup
from termcolor import colored
from unicodedata import normalize
from string import ascii_uppercase

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
clearConsole()


print(colored('\nBienvenido al primer programa de Cifrado Cesar que incluye la opción de Descifrado sin clave.!','green', attrs=['bold']))
print(colored('\n  Algunas recomendaciones al momento de descifrar sin clave texto de estilo no continuo:', 'yellow', attrs=['bold']))
print("\n       -Es recomendable fraccionar el texto a analizar;")
print("       -Elija las palabras más largas para mejorar la presición del descifrado;")
print("       -El descifrado sin clave necesita una conexión a internet;")
print("       -Considere que el descifrado sin clave requiere más tiempo que un descifrado con clave;")


def main():
    print("\nIntroducir",colored("Mensaje" , 'red', attrs=['bold']),end="")
    msj = normalizar(input(" a cifrar/descifrar: "))
    while True:
        modo    = input("\nCifrar o Descifrar [C/D]: ")
        if modo.upper()=='C':
            clave=checkclave()
            cifrado = cifrar(msj, clave, modo)
            print(f"\nMensaje Cifrado: {cifrado}")
            return
        elif modo.upper()=='D':
            descifrar(msj)
            return
        else:
            print("\nLa opción ingresada es incorrecta")
            print("\nIntente nuevamente")


def normalizar(texto):
    """ Pasa todos los caracteres a su forma sin diacríticos                  
    NFD :: Normalization Form Canonical Decomposition
    NFC :: Normalization Form Canonical Composition"""
    s = texto
    s = re.sub(r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", normalize( "NFD", s), 0, re.I)
    s = normalize( 'NFC', s)
    return s

      
def cifrar(msj, clave, mode):
    abc=list(ascii_uppercase)
    abc.insert(14,"Ñ")
    msj = msj.upper()
    traduccion = ""
    for caracter in msj:
        if caracter.isalpha():
            num = abc.index(caracter)
            if mode.lower() == "c":
                num = num + clave
            elif mode.lower() == "d":
                num = num - clave
            if num >= len(abc):
                num -= len(abc)
            traduccion += abc[num]
        else:
            traduccion += caracter
    return traduccion


def descifrar(msj):
    encontrados=0
    while True:
        tiene_clave=input("\n¿Tiene la clave de descifrado?[Y/N]: ")
        if tiene_clave.upper()=="Y":
            clave=checkclave()
            cifrado = cifrar(msj, clave, "d")
            print(f"\nMensaje Descifrado: {cifrado}")
            return
        elif tiene_clave.upper()=="N":
            while True:
                estilo_escritura=input("\nIngrese si es estilo escritura continua o discontinua [C/D]")
                if estilo_escritura.upper()=="C":
                    for i in range(1,27):
                        descifrado = cifrar(msj, i, "d")
                        print(f"\nCon clave {i} se genera el siguiente mensaje:\n\n     -{descifrado}-")
                    return
                elif estilo_escritura.upper()=="D":
                    print("\nBuscando claves para generar el descifrado:")
                    for i in range(1,27):
                        descifrado = cifrar(msj, i, "d")
                        palabras=descifrado.split()
                        validador=0
                        if scrap(palabras[0]):
                            encontrados=1
                            validador=1
                            if len(palabras)>1:
                                if not scrap(palabras[1]):
                                    validador=0
                        if validador:
                            print(f"\nCon clave {i} se detecta el siguiente mensaje:\n\n     -{descifrado}-")
                            print("\nEvaluando otras claves...")    
                    if encontrados:
                        print("\nNo existe otra clave de descifrado que genere un mensaje válido")
                    else:
                        print ("\nNo se pudo descifrar su código, intente nuevamente ingresando otro texto")
                    return
                else:
                    print("Opción incorrecta, intente nuevamente.")
        else:
            print("Opción incorrecta, intente nuevamente.")


def checkclave():
    clave = (input("\nClave de cifrado [1-26]: "))
    while  not clave.isnumeric() or not 1<=int(clave)<=26:
        clave=(input(f"\n'{clave}', no es una opción válida, intente ingresar un valor entre 1 y 26: "))
    clave=int(clave)
    return clavedef obtener_resultados(termino_busqueda):
    url = f'https://www.wordreference.com/definicion/{termino_busqueda}'
    USER_AGENT = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    respuesta = requests.get(url, headers=USER_AGENT)
    respuesta.raise_for_status()
    return respuesta.text


def procesar_resultados(html):
	soup = BeautifulSoup(html, 'html.parser')
	resultados_encontrados = []
	bloque = soup.find_all("div", class_="trans clickable")
	for resultado in bloque:
		titulo = resultado.find('h3')
		resultados_encontrados.append(titulo)
	return resultados_encontrados


def scrap(texto_busqueda):
	html = obtener_resultados(texto_busqueda)
	resultados = procesar_resultados(html)
	return len(resultados)


if __name__ == '__main__':
    doctest.testmod()
    main()
