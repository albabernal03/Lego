import cv2
import numpy as np
import os
import glob
import gradio as gr

# Diccionario con los rangos de colores en HSV y los desplazamientos asociados
color_ranges = {
    'rojo': ([0, 120, 70], [10, 255, 255], 3),
    'azul': ([100, 150, 0], [140, 255, 255], 5),
    'verde': ([45, 100, 50], [75, 255, 255], 2),
    'amarillo': ([20, 100, 100], [30, 255, 255], 4),
    'naranja': ([10, 100, 100], [20, 255, 255], 6),
    'violeta': ([130, 100, 100], [160, 255, 255], 1),
    'rosa': ([160, 100, 100], [170, 255, 255], 2),
    'cian': ([85, 100, 100], [100, 255, 255], 4),
    'blanco': ([0, 0, 200], [180, 20, 255], 1),
    'negro': ([0, 0, 0], [180, 255, 50], 5)
}

def procesar_imagen(image_path):
    image = cv2.imread(image_path)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    total_desplazamiento = 0

    for color, (lower, upper, shift) in color_ranges.items():
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
        mask = cv2.inRange(hsv, lower, upper)
        if np.sum(mask) > 0:
            total_desplazamiento += shift

    return total_desplazamiento

def cifrar(texto, desplazamiento):
    resultado = ""
    for char in texto:
        if char.isalpha():
            shift = (ord(char.lower()) - ord('a') + desplazamiento) % 26 + ord('a')
            resultado += chr(shift) if char.islower() else chr(shift).upper()
        else:
            resultado += char
    return resultado

def descifrar(texto_cifrado, desplazamiento):
    return cifrar(texto_cifrado, -desplazamiento)

def contar_imagenes_en_carpeta(ruta_carpeta, extension='*'):
    # Combinar la ruta de la carpeta con el patrón de búsqueda
    patron_completo = os.path.join(ruta_carpeta, f'*.{extension}')

    # Buscar archivos que coincidan con el patrón
    archivos_imagen = glob.glob(patron_completo)

    # Contar el número de archivos encontrados
    num_imagenes = len(archivos_imagen)

    return num_imagenes


def obtener_nombres_imagenes_en_carpeta(ruta_carpeta, extension='*'):
    """
    Obtiene los nombres de todos los archivos de imágenes en una carpeta.

    Args:
        ruta_carpeta (str): La ruta de la carpeta que contiene las imágenes.
        extension (str): La extensión de archivo de las imágenes a buscar (por defecto, '*' para todas las extensiones).

    Returns:
        list: Una lista con los nombres de todos los archivos de imágenes encontrados en la carpeta.
    """
    # Combinar la ruta de la carpeta con el patrón de búsqueda
    patron_completo = os.path.join(ruta_carpeta, f'*.{extension}')

    # Buscar archivos que coincidan con el patrón
    archivos_imagen = glob.glob(patron_completo)

    # Obtener solo los nombres de los archivos (sin la ruta completa)
    nombres_imagenes = [os.path.basename(imagen) for imagen in archivos_imagen]

    return nombres_imagenes


def cifrar_frase_con_desplazamiento(frase):
    palabras = frase.split()
    desplazamientos = []  # Lista para almacenar los desplazamientos utilizados

    # Obtener la lista de nombres de archivos de imágenes en la carpeta "imagenes"
    ruta_carpeta_imagenes = 'imagenes'
    archivos_imagenes = obtener_nombres_imagenes_en_carpeta(ruta_carpeta_imagenes)

    num_imagenes = len(archivos_imagenes)

    frase_cifrada = ""
    for i, palabra in enumerate(palabras):
        # Calcular el índice de la imagen a utilizar
        indice_imagen = i % num_imagenes

        # Obtener el nombre de archivo de la imagen correspondiente
        imagen = archivos_imagenes[indice_imagen]

        # Procesar la imagen para obtener el desplazamiento
        desplazamiento = procesar_imagen("imagenes/" + imagen)
        desplazamientos.append(desplazamiento)  # Almacenar el desplazamiento

        # Cifrar la palabra utilizando el desplazamiento obtenido
        palabra_cifrada = cifrar(palabra, desplazamiento)
        frase_cifrada += palabra_cifrada + " "

    # Guardar los desplazamientos en un archivo
    with open("desplazamientos.txt", "w") as f:
        f.write(", ".join(map(str, desplazamientos)))

    return frase_cifrada.strip(), desplazamientos


def descifrar_frase_con_desplazamiento(frase_cifrada, desplazamientos):
    palabras = frase_cifrada.split()
    frase_descifrada = ""
    #desplazamientos es un str de numeros separados por comas
    desplazamientos = list(map(int, desplazamientos.split(',')))
    for palabra, desplazamiento in zip(palabras, desplazamientos):
        palabra_descifrada = cifrar(palabra, -desplazamiento)  # Invertir el desplazamiento para descifrar
        frase_descifrada += palabra_descifrada + " "
    return frase_descifrada.strip()


'''def main():
    # Define una frase de prueba
    frase = "Hola mundo tu!"

    # Llama a la función cifrar_frase_con_desplazamiento con la frase de prueba
    frase_cifrada, desplazamientos = cifrar_frase_con_desplazamiento(frase)

    # Imprime la frase cifrada y los desplazamientos utilizados
    print("Frase cifrada:", frase_cifrada)

    #frase_descifrada = descifrar_frase_con_desplazamiento(frase_cifrada, desplazamientos)
    #print("Frase descifrada:", frase_descifrada)

# Llama a la función principal para ejecutar el código de prueba
if __name__ == "__main__":
    main()'''

def cifrar_descifrar(action, text, desplazamiento):
    if action == 'Cifrar':
        frase_cifrada, desplazamientos = cifrar_frase_con_desplazamiento(text)
        return frase_cifrada
    elif action == 'Descifrar':
        return descifrar_frase_con_desplazamiento(text, desplazamiento)


iface = gr.Interface(
    fn=cifrar_descifrar,
    inputs=[
        gr.Dropdown(choices=["Cifrar", "Descifrar"], label="Acción"),
        gr.Textbox(label="Texto"),
        gr.Textbox(label="Desplazamiento", placeholder="Enter comma-separated values for decryption")
    ],
    outputs="text",
    title="Taller de Criptografía con LEGO",
    description="Utiliza esta herramienta para cifrar o descifrar mensajes usando el cifrado César."
)

iface.launch()