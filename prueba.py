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

def descifrar(texto_cifrado, desplazamientos):
    palabras = texto_cifrado.split()
    frase_descifrada = ""
    desplazamientos = [int(d) for d in desplazamientos.split(",")]
    for palabra, desplazamiento in zip(palabras, desplazamientos):
        palabra_descifrada = cifrar(palabra, -desplazamiento)  # Invertir el desplazamiento para descifrar
        frase_descifrada += palabra_descifrada + " "
    return frase_descifrada.strip()

def cifrar_descifrar(action, text, desplazamiento):
    if action == 'Cifrar':
        desplazamiento = procesar_imagen('imagenes/tele.png')  # Replace with the actual image path
        return cifrar(text, desplazamiento)
    elif action == 'Descifrar':
        return descifrar(text, desplazamiento)

iface = gr.Interface(
    fn=cifrar_descifrar,
    inputs=[
        gr.Dropdown(choices=["Cifrar", "Descifrar"], label="Acción"),
        gr.Textbox(label="Texto"),
        gr.Textbox(label="Desplazamiento", placeholder="Enter comma-separated values for decryption")  # Changed 'default' to 'placeholder'
    ],
    outputs="text",
    title="Taller de Criptografía con LEGO",
    description="Utiliza esta herramienta para cifrar o descifrar mensajes usando el cifrado César."
)

iface.launch()
