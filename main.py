import requests
import json

url = 'https://aves.ninjas.cl/api/birds'

# creando funcion para obtener la informacion de la api
def obtener_aves(url):
    """_summary_

    Args:
        url ('str'): direccion url de la api

    Returns:
        list: devuelve el contenido como lista
    """
    respuesta = requests.get(url)
    return respuesta.json()


aves = obtener_aves(url) # devuelve un listado con el contenido de la api

def crear_html(aves):
    """_summary_

    Args:
        aves (list): lista de la informacion de la API
    """
    with open('template.html', 'r') as file: # abre el archivo html
        template = file.read() # crea una variable de lectura del documento

    aves_html = '' # crea variable string para ser utilizada en el for

    for ave in aves[10:25]: # para ave en la lista aves, entre los indices [10:25] | muestra 15 elementos
        aves_html += f'<div class="bird"><div class="bird-name">{ave["name"]["spanish"]} / {ave["name"]["english"]}</div><img src="{ave["images"]["thumb"]}" alt="{ave["name"]["spanish"]}"></div>\n\t\t' # agregando el contenido de cada ave en la variable aves_html
    final_html = template.replace('<!-- Aquí se insertarán las aves -->', aves_html) # con el metodo replace() | el primer argumento es lo que buscara en el documento en lectura template.html | segundo argumento es por lo que vamos a reemplazar | final_html para a contener el template con el contenido de aves_html

    with open('aves_de_chile.html', 'w') as file: # es esta linea se crea el documento aves_de_chile.html en modo escritura
        file.write(final_html) # escribe el contenido de final_html en el documento aves_de_chile.html

if aves: # si aves tiene contenido
    crear_html(aves) # ejecuta la funcion crear_aves con argumento aves

# ejecutar con:
# python main.py
# actualizar la carpeta "PURBEADÍA17"
# se crea el documento 'aves_de_chile.html'