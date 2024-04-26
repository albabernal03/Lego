import cv2
import numpy as np

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
            shift = (ord(char.lower()) - ord('a') +
                     desplazamiento) % 26 + ord('a')
            resultado += chr(shift) if char.islower() else chr(shift).upper()
        else:
            resultado += char
    return resultado


def descifrar(texto_cifrado, desplazamiento):
    return cifrar(texto_cifrado, -desplazamiento)


# Ejemplo de uso
# Asegúrate de proporcionar la ruta correcta a la imagen
image_path = 'imagenes/humano.png'
desplazamiento = procesar_imagen(image_path)
mensaje = str(input("Introduce el mensaje a cifrar: "))
mensaje_cifrado = cifrar(mensaje, desplazamiento)
print("Mensaje cifrado:", mensaje_cifrado)

# Ahora descifrar el mensaje
mensaje_descifrado = descifrar(mensaje_cifrado, desplazamiento)
print("Mensaje descifrado:", mensaje_descifrado)


'''# Ejemplo de uso lego 2.0:
ruta_carpeta = 'imagenes'
num_imagenes = contar_imagenes_en_carpeta(ruta_carpeta, 'jpeg')
print("Número de imágenes en la carpeta:", num_imagenes)

# Ejemplo de uso
image_path = 'imagenes/foto2.jpeg'  # Asegúrate de proporcionar la ruta correcta a la imagen
desplazamiento = procesar_imagen(image_path)


# Cifrar un mensaje
mensaje = "invent"
mensaje_cifrado = cifrar(mensaje, desplazamiento)
print("Mensaje cifrado:", mensaje_cifrado)

# Ahora descifrar el mensaje
mensaje_descifrado = descifrar(mensaje_cifrado, desplazamiento)
print("Mensaje descifrado:", mensaje_descifrado)'''
