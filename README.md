# 🎮 Proyecto: Suite de Minijuegos en Consola (Python OOP Edition)

## 📌 Descripción General
Este proyecto consiste en el desarrollo de una colección de juegos clásicos ejecutados 100% desde la terminal. El objetivo principal es que los estudiantes apliquen de manera práctica los pilares de la **Programación Orientada a Objetos (POO)** y el manejo avanzado de recursos en Python.

---

## 🎯 Objetivos de Aprendizaje
Para dar por válida la entrega, cada juego debe demostrar la implementación de los siguientes conceptos:

1.  **Clases y Objetos:** Estructurar el juego y sus entidades (Jugador, Enemigo, Tablero, etc.) mediante clases.
2.  **Atributos y Métodos:** Definir estados y comportamientos claros para cada clase.
3.  **Encapsulamiento:** Uso de atributos privados/protegidos y métodos (getters/setters) donde sea necesario para proteger el estado interno.
4.  **Herencia:** Crear jerarquías de clases cuando existan elementos con características comunes (ej: diferentes tipos de enemigos o ítems).
5.  **Polimorfismo:** Implementar métodos con el mismo nombre pero diferente comportamiento en clases derivadas (ej: un método `atacar()` que funcione distinto según el personaje).
6.  **Manejo de Excepciones:** Validar entradas del usuario (`try-except`) para evitar que el programa se cierre por errores inesperados.
7.  **Flujos de Archivos (I/O):** Implementar la persistencia de datos, como un sistema de **Puntajes Máximos (High Scores)** o **Guardado de Partida** utilizando archivos `.txt` o `.json`.

---

## 🕹️ Catálogo de Desafíos

El proyecto se divide en niveles de complejidad. Se espera que los juegos de nivel intermedio apliquen de forma más rigurosa los conceptos de herencia y polimorfismo.

### 🟢 Nivel Básico: Fundamentos y Estructura
*Enfoque: Clases básicas, atributos, métodos y excepciones.*

1.  **Adivina el Número (Versión Pro):**
    *   **Mandato:** Crear una clase `JuegoAdivinanza` que gestione los intentos y el rango. Usar excepciones para validar que la entrada sea un número entero.
2.  **Piedra, Papel, Tijera (Torneo):**
    *   **Mandato:** Clase `Jugador` y clase `Partida`. Almacenar el historial de rondas en un archivo para mostrar estadísticas al final.
3.  **Historias Locas (Generador Dinámico):**
    *   **Mandato:** Clase `Plantilla` que cargue diferentes historias desde archivos externos.
4.  **Duelo de Salud (1 vs 1):**
    *   **Mandato:** Clase `Entidad` con atributos `vida` y `ataque`. Usar métodos para gestionar el daño recibido.

### 🟡 Nivel Intermedio: POO Avanzada
*Enfoque: Herencia, polimorfismo, encapsulamiento y lógica de estado.*

5.  **Mastermind (Cripto-Analista):**
    *   **Mandato:** Encapsular la lógica de generación de código. El jugador no debe poder acceder directamente al código secreto.
6.  **Batalla Naval (Hundir la Flota):**
    *   **Mandato:** Clase `Tablero` que gestione una matriz de objetos `Casilla`. Implementar herencia si existen diferentes tipos de barcos.
7.  **Ahorcado (Técnico):**
    *   **Mandato:** Sistema de categorías mediante archivos. Clase `Dibujante` que gestione el arte ASCII según los fallos.
8.  **Aventura Conversacional (RPG Engine):**
    *   **Mandato:** **Obligatorio el uso de Herencia y Polimorfismo**. Crear una clase base `Habitacion` y derivadas con eventos específicos. Usar un sistema de inventario basado en objetos.

---

## 🛠️ Requisitos Técnicos
- **Lenguaje:** Python 3.10 o superior.
- **Arquitectura:** Cada juego debe estar contenido en su propia carpeta o módulo.
- **Documentación:** Cada clase y método debe tener *docstrings* explicando su propósito.
- **Persistencia:** Es obligatorio que al menos 2 juegos guarden y lean datos de un archivo externo.

## 🚀 Cómo empezar
1. Clona este repositorio.
2. Crea una rama con tu nombre: `git checkout -b feature/nombre-estudiante`.
3. ¡Empieza a codificar respetando los principios de la POO!

---
*Este proyecto es una herramienta educativa para transformar programadores de scripts en arquitectos de software.*
