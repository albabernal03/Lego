
<h1 align="center">Criptografía y Seguridad Digital con LEGO y Hugging Face</h1>

En este [repositorio](https://github.com/albabernal03/Lego) queda resuelta la práctica de Lego.

# Índice

1. [Taller: Descifrando Secretos con LEGO](#taller-descifrando-secretos-con-lego)
   - [Parte 1: Construcción de Claves de Cifrado con LEGO](#parte-1-construcción-de-claves-de-cifrado-con-lego)
   - [Parte 2: Cifrar y Descifrar Mensajes](#parte-2-cifrar-y-descifrar-mensajes)
   - [Parte 3: Desafío de Criptografía](#parte-3-desafío-de-criptografía)
   - [Descripción del Taller](#descripción-del-taller)
   - [Pasos para la Actividad](#pasos-para-la-actividad)

2. [Configuración del Sistema de Visión por Computadora](#configuración-del-sistema-de-visión-por-computadora)
   - [Consideraciones](#consideraciones)

3. [Pasos para la Actividad](#pasos-para-la-actividad)
   - [Paso 1: Preparación de Materiales](#paso-1-preparación-de-materiales)
   - [Paso 2: Introducción y Teoría](#paso-2-introducción-y-teoría)
   - [Paso 3: Construcción de Claves de Cifrado](#paso-3-construcción-de-claves-de-cifrado)
   - [Paso 4: Fotografiar las Claves](#paso-4-fotografiar-las-claves)
   - [Paso 5: Cifrar y Descifrar Mensajes](#paso-5-cifrar-y-descifrar-mensajes)

4. [Código](#código)
   - [Función de Procesado](#función-de-procesado)
   - [Función de Cifrar](#función-de-cifrar)
   - [Función de Descifrar](#función-de-descifrar)
   

# Taller: Descifrando Secretos con LEGO

¡Bienvenidos, jóvenes criptógrafos! En este taller, nos sumergiremos en una aventura donde utilizaremos piezas de LEGO para desentrañar los secretos de la criptografía. Aprenderemos cómo proteger mensajes secretos mediante diferentes claves y cómo descifrar mensajes cifrados por otros. ¡Presten atención y prepárense para poner a prueba su ingenio y creatividad!

## Parte 1: Construcción de Claves de Cifrado con LEGO

**Objetivo:** Crear una clave de cifrado utilizando piezas de LEGO que representen valores de desplazamiento en un cifrado César.

### Materiales:
- Piezas de LEGO de varios colores.
- Tabla de colores y valores asignados (por ejemplo, rojo = 3, azul = 5).

### Pasos:
1. **Entender el Cifrado César:**
   - Es un tipo de cifrado por sustitución en el que cada letra del texto se reemplaza por otra que se encuentra un número fijo de posiciones más adelante en el alfabeto.

2. **Construir tu Clave:**
   - Selecciona piezas de LEGO para construir tu clave, donde el color de cada pieza determinará el valor de desplazamiento.

3. **Registrar tu Clave:**
   - Anota la combinación de colores elegidos y calcula el desplazamiento total.

## Parte 2: Cifrar y Descifrar Mensajes

**Objetivo:** Utilizar la aplicación Gradio para cifrar y descifrar mensajes utilizando las claves de LEGO construidas.

### Pasos:
1. **Cifrar un Mensaje:**
   - Ingresa un mensaje corto en la aplicación y aplica tu clave de cifrado para cifrarlo.

2. **Intercambiar Mensajes Cifrados:**
   - Intercambia tu mensaje cifrado con otro grupo y trata de descifrar el mensaje que recibiste utilizando diferentes desplazamientos.

3. **Descifrar el Mensaje:**
   - Utiliza la aplicación para probar diferentes desplazamientos hasta que el mensaje tenga sentido.

## Parte 3: Desafío de Criptografía

**Objetivo:** Descifrar un mensaje dado sin conocer la clave, utilizando diferentes combinaciones de piezas de LEGO.

### Pasos:
1. **Recibir un Mensaje Cifrado:**
   - Cada grupo recibirá un mensaje cifrado de otro grupo sin conocer el desplazamiento utilizado.

2. **Descifrar el Mensaje:**
   - Prueba diferentes combinaciones de piezas de LEGO para cambiar el desplazamiento y descifrar el mensaje.

3. **Compartir tu Solución:**
   - Una vez descifrado, comparte cómo lo lograste y qué desplazamiento resultó ser el correcto.

## Descripción del Taller

Este taller introduce a los estudiantes en los fundamentos de la criptografía y la seguridad digital de manera divertida y accesible. Utilizando una aplicación desarrollada en Gradio, los estudiantes aprenden sobre cifrado y descifrado mientras utilizan piezas de LEGO para representar visualmente los datos y las claves de cifrado.

### Objetivos:
- Entender los principios básicos del cifrado y el descifrado.
- Aprender sobre la importancia de la seguridad digital.
- Desarrollar habilidades de pensamiento crítico y resolución de problemas.

### Materiales Necesarios:
- Piezas de LEGO de varios colores y formas.
- Ordenadores o tablets con acceso a internet.
- Proyector para demostraciones grupales.

### Configuración del Sistema de Visión por Computadora

Para integrar la funcionalidad de interpretar fotos de piezas de LEGO y determinar el desplazamiento para el cifrado César, necesitaremos utilizar técnicas de visión por computadora. Aquí tienes cómo configurar este sistema:

1. **Instalación de Bibliotecas Necesarias:**

![image](https://github.com/albabernal03/Lego/assets/91721855/7db00715-6e6c-416b-9e2c-2104aea0813f)


2. **Configuración del Código de Python:**
- Se proporciona un ejemplo básico de cómo configurar un código que utilice OpenCV para detectar colores de las piezas de LEGO en una imagen y determinar el desplazamiento basado en esos colores.

3. **Uso de la Aplicación:**
- Ejecuta el script y luego interactúa con la aplicación en el navegador. Los usuarios pueden subir una foto de sus piezas de LEGO, y la aplicación determinará automáticamente el desplazamiento basado en los colores detectados.

### Consideraciones:
- Ajuste de Rangos de Color: Los rangos de color en el código son ejemplos y pueden necesitar ajustes precisos para funcionar correctamente.
- Iluminación y Calidad de la Imagen: La detección de color puede verse afectada por la iluminación y la calidad de la imagen.

## Pasos para la Actividad

### Paso 1: Preparación de Materiales
- Asegúrate de que cada grupo tenga piezas de LEGO, una cámara para fotos y acceso a la aplicación Gradio.

### Paso 2: Introducción y Teoría
- Explica el cifrado César y realiza demostraciones prácticas para ilustrar su funcionamiento.

### Paso 3: Construcción de Claves de Cifrado
- Permita que los estudiantes elijan y construyan sus claves de cifrado con piezas de LEGO.

### Paso 4: Fotografiar las Claves
- Cada grupo toma una foto de su configuración de LEGO para utilizarla en la aplicación.

### Paso 5: Cifrar y Descifrar Mensajes
- Los estudiantes utilizan la aplicación para cifrar y descifrar mensajes utilizando las claves construidas y las imágenes de las piezas de LEGO.

# Código

En esta sección se describe el código utilizado para el procesado de imágenes y las funciones de cifrado y descifrado.

## Función de Procesado

La función de procesado utiliza OpenCV para detectar los colores de las piezas de LEGO en una imagen y determinar el desplazamiento basado en esos colores.

![code](https://github.com/albabernal03/Lego/assets/91721855/765bf0ce-f346-44ab-89f5-8ca445f8a9f8)


## Función de Cifrar

La función de cifrar toma un mensaje de texto y una imagen de las piezas de LEGO como entrada. Utiliza el desplazamiento calculado mediante el procesado de la imagen para aplicar un cifrado César al mensaje y devuelve el mensaje cifrado.

![code1](https://github.com/albabernal03/Lego/assets/91721855/d847dfa3-81bf-4cdd-b1d9-32c7f37c83e8)


## Función de Descifrar

La función de descifrar toma un mensaje cifrado y una imagen de las piezas de LEGO como entrada. Utiliza el desplazamiento calculado mediante el procesado de la imagen para aplicar un descifrado César al mensaje y devuelve el mensaje descifrado.

![code1](https://github.com/albabernal03/Lego/assets/91721855/93e1202b-c25f-46d9-a690-28d647b65525)

## Función de Contar las imágenes de la carpeta

La función de contar las imágenes se encarga de contar todas las imágenes para poder aplicar a cada palabra de la frase a cifrar.

![code3](https://github.com/albabernal03/Lego/assets/91721855/be42656d-3cd2-4602-9fcd-c5334811bb57)

## Función de Obtener nombres imágenes en carpetas

Esta función se encarga de obtener todos los nombres de las imágenes para poder aplicar a cada palabra de la frase a cifrar.

![code4](https://github.com/albabernal03/Lego/assets/91721855/7b417ca6-043a-4c1d-b421-fe62225ea714)

## Función de Cifrar frase con desplazamiento

Esta función se encarga de cifrar cada una de las palabras de la frase aplicando una imagen diferente en cada ocasión y lo guarda en un fichero txt.

![code5](https://github.com/albabernal03/Lego/assets/91721855/60780645-17db-4cec-a621-2abe69a81ef9)

## Función de Descifrar frase con desplazamiento

Esta función se encarga de descifrar cada una de las palabras de la frase aplicando su imagen correspondiente en cada palabra.

![code6](https://github.com/albabernal03/Lego/assets/91721855/1ff47fb7-4ce2-4f9e-94f4-2fddb49b6d86)

## Función de Insertar imagen

Hemos añadido la función para poder insertar más imágenes a la hora de cifrar y descifrar mensajes.

![code7](https://github.com/albabernal03/Lego/assets/91721855/2bf07fd5-0511-4de5-9ff8-c8cb8a11ad6f)

Ahora hemos hecho la interfaz usando Gradio:

![code8](https://github.com/albabernal03/Lego/assets/91721855/d315db6a-5b94-43ae-b690-3a9dce48db54)

![interfaz](https://github.com/albabernal03/Lego/assets/91721855/a32c8549-7c49-40ac-a2da-30dbac264f33)

![image](https://github.com/albabernal03/Lego/assets/91721855/2ad8b34f-45fe-4d9d-8ed6-7a36e3de3ecd)







