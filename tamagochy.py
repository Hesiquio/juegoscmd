import json
import os
import random
from abc import ABC, abstractmethod

# ==========================================
# 1. CLASES Y OBJETOS / 4. HERENCIA
# ==========================================
class Mascota(ABC):
    def __init__(self, nombre):
        # 3. ENCAPSULAMIENTO: Atributos privados (__) y protegidos (_)
        self.__nombre = nombre
        self._hambre = 50
        self._felicidad = 50
        self._energia = 50
        self._salud = 100

    # 3. ENCAPSULAMIENTO: Getters y Setters
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if len(nuevo_nombre.strip()) > 0:
            self.__nombre = nuevo_nombre
        else:
            print("El nombre no puede estar vacío.")

    # 2. ATRIBUTOS Y MÉTODOS
    def _limitar_estadisticas(self, valor):
        """Método encapsulado para mantener los valores entre 0 y 100."""
        return max(0, min(100, valor))

    def alimentar(self):
        self._hambre = self._limitar_estadisticas(self._hambre - 20)
        self._energia = self._limitar_estadisticas(self._energia + 10)
        print(f"🍕 Has alimentado a {self.nombre}.")

    def jugar(self):
        self._felicidad = self._limitar_estadisticas(self._felicidad + 20)
        self._energia = self._limitar_estadisticas(self._energia - 15)
        self._hambre = self._limitar_estadisticas(self._hambre + 10)
        print(f"🎾 Has jugado con {self.nombre}.")

    def dormir(self):
        self._energia = 100
        self._hambre = self._limitar_estadisticas(self._hambre + 10)
        print(f"💤 {self.nombre} ha dormido y recuperado su energía.")

    def pasar_tiempo(self):
        """Simula el paso del tiempo después de cada turno."""
        self._hambre = self._limitar_estadisticas(self._hambre + 10)
        self._felicidad = self._limitar_estadisticas(self._felicidad - 10)
        self._energia = self._limitar_estadisticas(self._energia - 10)
        
        if self._hambre >= 90 or self._energia <= 10:
            self._salud = self._limitar_estadisticas(self._salud - 15)

    def esta_vivo(self):
        return self._salud > 0

    # 5. POLIMORFISMO
    @abstractmethod
    def expresarse(self):
        """Método que deberá ser implementado distinto por cada hijo."""
        pass

    def mostrar_estado(self):
        print(f"\n--- ESTADO DE {self.__nombre.upper()} ---")
        print(f"Salud:     [{self._salud}/100]")
        print(f"Hambre:    [{self._hambre}/100] (Más bajo es mejor)")
        print(f"Felicidad: [{self._felicidad}/100]")
        print(f"Energía:   [{self._energia}/100]")
        self.expresarse()
        print("-------------------------")

    def to_dict(self):
        """Prepara la clase para ser guardada en JSON."""
        return {
            "tipo": self.__class__.__name__,
            "nombre": self.nombre,
            "hambre": self._hambre,
            "felicidad": self._felicidad,
            "energia": self._energia,
            "salud": self._salud
        }

# ==========================================
# 4. HERENCIA Y 5. POLIMORFISMO
# ==========================================
class PerroAlien(Mascota):
    def expresarse(self):
        # Polimorfismo en acción
        print(f"{self.nombre} hace: ¡Guau telepático! 🐕👽")

    def jugar(self):
        # Polimorfismo: Sobrescribir y extender el comportamiento base
        super().jugar()
        self._felicidad = self._limitar_estadisticas(self._felicidad + 15) # Se divierte más
        print(f"A {self.nombre} le encanta correr flotando.")

class GatoRobot(Mascota):
    def expresarse(self):
        print(f"{self.nombre} hace: *Beep boop miau* 🐱🤖")

    def dormir(self):
        # Polimorfismo: Sobrescribir comportamiento base
        super().dormir()
        print(f"{self.nombre} ha recargado sus baterías al 100%.")

# ==========================================
# 7. FLUJOS DE ARCHIVOS Y LÓGICA PRINCIPAL
# ==========================================
class JuegoTamagotchi:
    ARCHIVO_GUARDADO = "tamagotchi_save.json"

    def __init__(self):
        self.mascota = None

    def guardar_partida(self):
        if not self.mascota:
            return
        try:
            with open(self.ARCHIVO_GUARDADO, 'w', encoding='utf-8') as f:
                json.dump(self.mascota.to_dict(), f, indent=4)
            print("\n✅ Partida guardada exitosamente.")
        except Exception as e:
            print(f"❌ Error al guardar: {e}")

    def cargar_partida(self):
        if os.path.exists(self.ARCHIVO_GUARDADO):
            try:
                with open(self.ARCHIVO_GUARDADO, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    
                    # Instanciar el tipo correcto de mascota
                    if data["tipo"] == "PerroAlien":
                        self.mascota = PerroAlien(data["nombre"])
                    elif data["tipo"] == "GatoRobot":
                        self.mascota = GatoRobot(data["nombre"])
                    
                    # Restaurar estados
                    if self.mascota:
                        self.mascota._hambre = data["hambre"]
                        self.mascota._felicidad = data["felicidad"]
                        self.mascota._energia = data["energia"]
                        self.mascota._salud = data["salud"]
                        print(f"\n✅ Partida de {self.mascota.nombre} cargada exitosamente.")
                        return True
            except Exception as e:
                print(f"❌ Error al cargar: {e}")
        return False

    def menu_creacion(self):
        print("--- CREAR NUEVA MASCOTA ---")
        print("1. Perro Alien")
        print("2. Gato Robot")
        
        while True:
            # 6. MANEJO DE EXCEPCIONES
            try:
                opcion = int(input("Selecciona el tipo (1-2): "))
                if opcion not in [1, 2]:
                    raise ValueError("Opción fuera de rango.")
                
                nombre = input("Dime el nombre de tu mascota: ")
                if opcion == 1:
                    self.mascota = PerroAlien(nombre)
                else:
                    self.mascota = GatoRobot(nombre)
                break
            except ValueError:
                print("❌ Entrada no válida. Por favor, ingresa el número 1 o 2.")

    def iniciar(self):
        print("=== BIENVENIDO A TAMAGOTCHI CLI ===")
        if not self.cargar_partida():
            self.menu_creacion()

        while True:
            if not self.mascota.esta_vivo():
                print(f"\n💀 Oh no... {self.mascota.nombre} ha enfermado demasiado y ha fallecido.")
                print("--- FIN DEL JUEGO ---")
                if os.path.exists(self.ARCHIVO_GUARDADO):
                    os.remove(self.ARCHIVO_GUARDADO) # Borrar guardado si muere
                break

            self.mascota.mostrar_estado()
            print("¿Qué quieres hacer?")
            print("1. Alimentar")
            print("2. Jugar")
            print("3. Dormir")
            print("4. Guardar y Salir")

            # 6. MANEJO DE EXCEPCIONES
            try:
                opcion = int(input("Elige una acción (1-4): "))
                if opcion == 1:
                    self.mascota.alimentar()
                elif opcion == 2:
                    self.mascota.jugar()
                elif opcion == 3:
                    self.mascota.dormir()
                elif opcion == 4:
                    self.guardar_partida()
                    print(f"¡Hasta luego! {self.mascota.nombre} te estará esperando.")
                    break
                else:
                    print("❌ Opción no válida. Ingresa un número del 1 al 4.")
                    continue
                
                # Pasa el tiempo solo si la acción fue válida
                self.mascota.pasar_tiempo()

            except ValueError:
                print("❌ Error: Debes ingresar un número válido.")

if __name__ == "__main__":
    juego = JuegoTamagotchi()
    juego.iniciar()