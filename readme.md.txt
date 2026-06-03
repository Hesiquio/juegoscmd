# 🎮 Minijuegos de Consola en Python

Este repositorio contiene una colección de 8 juegos desarrollados en Python y ejecutados 100% desde la terminal. El objetivo principal de este proyecto es fortalecer los fundamentos de la lógica de programación, el control de flujo y el manejo de estructuras de datos, prescindiendo de interfaces gráficas para mantener el enfoque en el código puro.

## 🚀 Niveles de Dificultad y Juegos

El proyecto está estructurado en dos fases de desarrollo, desde la lógica más básica hasta el manejo de estados más complejos.

### 🟢 Nivel Básico (Fundamentos)

Perfectos para dominar entradas, salidas, variables, condicionales simples y bucles.

1. **Adivina el Número (Mayor o Menor)**
   - **Descripción:** La computadora elige un número al azar (ej. 1-100) y el jugador debe adivinarlo. El sistema solo responde si el intento es "Muy alto" o "Muy bajo".
   - **Conceptos:** `random.randint`, bucles `while`, condicionales `if/elif/else`.

2. **Piedra, Papel, Tijera (Al mejor de 3)**
   - **Descripción:** El clásico juego contra la máquina. Se lleva un registro de puntuación y el primero en ganar dos de tres rondas es el vencedor.
   - **Conceptos:** `random.choice`, operadores lógicos, contadores de estado.

3. **Historias Locas (Mad Libs)**
   - **Descripción:** El programa solicita al usuario diferentes tipos de palabras (verbos, nombres, lugares) sin darle contexto. Al final, inserta estas palabras en una plantilla de texto predefinida generando una historia absurda.
   - **Conceptos:** Función `input()`, variables de texto, *f-strings* (formateo de cadenas).

4. **Mini Combate de 1 vs 1 (Duelo de Salud)**
   - **Descripción:** Un combate por turnos simplificado. El jugador y el enemigo comienzan con 50 puntos de salud. En cada turno, se hacen un daño aleatorio hasta que la salud de alguno llegue a cero.
   - **Conceptos:** Reasignación de variables matemáticas, pausas dramáticas con `time.sleep()`, bucles controlados por estado.

### 🟡 Nivel Intermedio (Estructuras y Algoritmos)

Diseñados para practicar listas, diccionarios, matrices y algoritmos de búsqueda/validación.

5. **Mastermind (Descifra el Código)**
   - **Descripción:** El programa genera una combinación secreta de 4 colores/letras. El jugador tiene 10 intentos para adivinarla, recibiendo pistas sobre cuántos elementos son correctos y cuántos están en la posición adecuada.
   - **Conceptos:** Manipulación de listas/cadenas, bucles anidados, contadores lógicos.

6. **Batalla Naval (Hundir la Flota)**
   - **Descripción:** Un tablero impreso en texto (ej. `~` para agua, `X` para acierto). El jugador ingresa coordenadas para intentar hundir barcos invisibles posicionados aleatoriamente.
   - **Conceptos:** Matrices (listas de listas), mapeo de coordenadas, validación de entradas.

7. **Ahorcado Temático (Edición Técnica)**
   - **Descripción:** El clásico juego de adivinar la palabra letra por letra, con arte ASCII para dibujar al ahorcado. El banco de palabras se centra en una temática específica.
   - **Conceptos:** Búsqueda en cadenas, conjuntos (`set()`) para letras repetidas, lectura de archivos `.txt` o listas.

8. **Aventura Conversacional (RPG de Texto)**
   - **Descripción:** Un juego donde el jugador lee descripciones de su entorno y toma decisiones mediante comandos de texto (ej. `ir norte`, `tomar llave`) para avanzar en la historia.
   - **Conceptos:** Diccionarios (para mapear habitaciones), gestión de inventario. Opcionalmente, introducción a la Programación Orientada a Objetos (Clases).

## 🛠️ Requisitos

- Python 3.x instalado en el sistema.
- Una terminal o consola de comandos.
- Ganas de programar y resolver problemas.

## ⚙️ Cómo ejecutar

Para jugar a cualquiera de los juegos, simplemente clona el repositorio, navega a la carpeta del juego deseado y ejecuta el archivo `.py` desde tu terminal:

```bash
python nombre_del_juego.py