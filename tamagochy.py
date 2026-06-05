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
        self._edad = 0

    # 3. ENCAPSULAMIENTO: Getters y Setters
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if len(nuevo_nombre.strip()) > 0:
            self.__nombre = nuevo_nombre
        else:
            print("❌ El nombre no puede estar vacío.")

    def _limitar_estadisticas(self, valor):
        """Método encapsulado para mantener los valores entre 0 y 100."""
        return max(0, min(100, valor))

    def _dibujar_barra(self, valor, etiqueta):
        """Dibuja una barra de progreso visual en la consola."""
        bloques = int(valor / 10)
        barra = "█" * bloques + "░" * (10 - bloques)
        print(f"{etiqueta:<10} [{barra}] {valor}/100")

    def alimentar(self):
        self._hambre = self._limitar_estadisticas(self._hambre - 25)
        self._energia = self._limitar_estadisticas(self._energia + 5)
        print(f"🍕 Has alimentado a {self.nombre}. El hambre ha disminuido.")

    def jugar(self):
        self._felicidad = self._limitar_estadisticas(self._felicidad + 25)
        self._energia = self._limitar_estadisticas(self._energia - 20)
        self._hambre = self._limitar_estadisticas(self._hambre + 10)
        print(f"🎾 Has jugado con {self.nombre}. ¡Está muy feliz!")

    def dormir(self):
        self._energia = 100
        self._hambre = self._limitar_estadisticas(self._hambre + 15)
        print(f"💤 {self.nombre} ha dormido profundamente y recuperado energía.")

    def curar(self):
        if self._salud < 100:
            self._salud = self._limitar_estadisticas(self._salud + 30)
            print(f"💊 Has usado medicina. La salud de {self.nombre} ha mejorado.")
        else:
            print(f"✨ {self.nombre} ya tiene una salud excelente.")

    def pasar_tiempo(self):
        """Simula el paso del tiempo después de cada turno."""
        self._hambre = self._limitar_estadisticas(self._hambre + 12)
        self._felicidad = self._limitar_estadisticas(self._felicidad - 8)
        self._energia = self._limitar_estadisticas(self._energia - 10)
        self._edad += 1
        
        # Consecuencias de mala atención
        if self._hambre >= 85 or self._energia <= 15 or self._felicidad <= 10:
            self._salud = self._limitar_estadisticas(self._salud - 20)
            print(f"⚠️ ¡Atención! {self.nombre} se siente mal por descuido.")

        # Eventos Aleatorios (Polimorfismo indirecto vía azar)
        if random.random() < 0.2: # 20% de probabilidad
            self._evento_aleatorio()

    def _evento_aleatorio(self):
        eventos = [
            ("¡Encontró un juguete viejo!", "felicidad", 15),
            ("¡Se asustó con un ruido fuerte!", "felicidad", -20),
            ("¡Atrapó una mosca espacial!", "hambre", -10),
            ("¡Le dio un pequeño resfriado!", "salud", -15)
        ]
        msg, attr, mod = random.choice(eventos)
        print(f"🌟 EVENTO: {msg}")
        valor_actual = getattr(self, f"_{attr}")
        setattr(self, f"_{attr}", self._limitar_estadisticas(valor_actual + mod))

    def esta_vivo(self):
        return self._salud > 0

    @abstractmethod
    def expresarse(self):
        pass

    def mostrar_estado(self):
        print(f"\n{'='*30}")
        print(f"🐾 MASCOTA: {self.nombre.upper()} ({self.__class__.__name__})")
        print(f"🎂 EDAD: {self._edad} ciclos")
        print(f"{'-'*30}")
        self._dibujar_barra(self._salud, "Salud")
        self._dibujar_barra(self._hambre, "Hambre")
        self._dibujar_barra(self._felicidad, "Felicidad")
        self._dibujar_barra(self._energia, "Energía")
        print(f"{'-'*30}")
        self.expresarse()
        print(f"{'='*30}")

    def to_dict(self):
        return {
            "tipo": self.__class__.__name__,
            "nombre": self.nombre,
            "hambre": self._hambre,
            "felicidad": self._felicidad,
            "energia": self._energia,
            "salud": self._salud,
            "edad": self._edad
        }

# ==========================================
# 4. HERENCIA Y 5. POLIMORFISMO
# ==========================================
class PerroAlien(Mascota):
    def expresarse(self):
        print(f"{self.nombre} dice: ¡Guau telepático! 🐕👽")

    def jugar(self):
        super().jugar()
        self._felicidad = self._limitar_estadisticas(self._felicidad + 10) # Bonificación
        print(f"✨ A los Perros Alien les encanta flotar mientras juegan.")

class GatoRobot(Mascota):
    def expresarse(self):
        print(f"{self.nombre} dice: *Beep boop miau* 🐱🤖")

    def dormir(self):
        self._energia = 100
        self._salud = self._limitar_estadisticas(self._salud + 5)
        print(f"⚡ {self.nombre} se ha conectado a la red eléctrica. ¡Carga completa!")

class DragonFuego(Mascota):
    def expresarse(self):
        print(f"{self.nombre} dice: ¡ROOOAAR! (sale una pequeña flama) 🐲🔥")

    def alimentar(self):
        # Polimorfismo: Los dragones comen carbón, les da más energía pero sube poco el hambre
        self._hambre = self._limitar_estadisticas(self._hambre - 20)
        self._energia = self._limitar_estadisticas(self._energia + 20)
        print(f"🔥 {self.nombre} ha devorado carbón ardiente. ¡Sus escamas brillan!")

# ==========================================
# 7. FLUJOS DE ARCHIVOS Y LÓGICA PRINCIPAL
# ==========================================
class JuegoTamagotchi:
    ARCHIVO_GUARDADO = "tamagotchi_save.json"

    def __init__(self):
        self.mascota = None

    def guardar_partida(self):
        if not self.mascota: return
        try:
            with open(self.ARCHIVO_GUARDADO, 'w', encoding='utf-8') as f:
                json.dump(self.mascota.to_dict(), f, indent=4)
            print("\n💾 Partida guardada correctamente.")
        except Exception as e:
            print(f"❌ Error al guardar: {e}")

    def cargar_partida(self):
        if os.path.exists(self.ARCHIVO_GUARDADO):
            try:
                with open(self.ARCHIVO_GUARDADO, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    tipos = {"PerroAlien": PerroAlien, "GatoRobot": GatoRobot, "DragonFuego": DragonFuego}
                    
                    if data["tipo"] in tipos:
                        self.mascota = tipos[data["tipo"]](data["nombre"])
                        self.mascota._hambre = data["hambre"]
                        self.mascota._felicidad = data["felicidad"]
                        self.mascota._energia = data["energia"]
                        self.mascota._salud = data["salud"]
                        self.mascota._edad = data.get("edad", 0)
                        print(f"\n✨ ¡Bienvenido de nuevo! {self.mascota.nombre} te extrañaba.")
                        return True
            except Exception as e:
                print(f"❌ Error al cargar: {e}")
        return False

    def menu_creacion(self):
        print("\n--- ADOPTA UNA NUEVA MASCOTA ---")
        print("1. Perro Alien 🐕👽 (Muy juguetón)")
        print("2. Gato Robot 🐱🤖 (Carga energía al dormir)")
        print("3. Dragón de Fuego 🐲🔥 (Poderoso y hambriento)")
        
        while True:
            try:
                opcion = int(input("Selecciona el tipo (1-3): "))
                if opcion not in [1, 2, 3]: raise ValueError()
                
                nombre = input("¿Cómo se llamará tu compañero?: ").strip()
                if not nombre: raise ValueError("El nombre no puede estar vacío.")

                clases = {1: PerroAlien, 2: GatoRobot, 3: DragonFuego}
                self.mascota = clases[opcion](nombre)
                break
            except ValueError as e:
                print(f"❌ Entrada no válida. {e if str(e) else 'Elige 1, 2 o 3.'}")

    def iniciar(self):
        print("===================================")
        print("   TAMAGOTCHI CLI - EVOLUTION")
        print("===================================")
        
        if not self.cargar_partida():
            self.menu_creacion()

        while True:
            if not self.mascota.esta_vivo():
                print(f"\n💀 {self.mascota.nombre} ha fallecido tras {self.mascota._edad} ciclos.")
                print("El ciclo de la vida ha terminado. Inténtalo de nuevo.")
                if os.path.exists(self.ARCHIVO_GUARDADO): os.remove(self.ARCHIVO_GUARDADO)
                break

            self.mascota.mostrar_estado()
            print("ACCIONES:")
            print("1. Alimentar  2. Jugar  3. Dormir  4. Curar  5. Guardar y Salir")

            try:
                opcion = int(input("\n¿Qué decides hacer?: "))
                if opcion == 1: self.mascota.alimentar()
                elif opcion == 2: self.mascota.jugar()
                elif opcion == 3: self.mascota.dormir()
                elif opcion == 4: self.mascota.curar()
                elif opcion == 5:
                    self.guardar_partida()
                    print("¡Nos vemos pronto!")
                    break
                else:
                    print("❌ Esa acción no existe.")
                    continue
                
                self.mascota.pasar_tiempo()
                input("\nPresiona Enter para continuar...") # Pausa para leer eventos

            except ValueError:
                print("❌ Por favor, ingresa solo números.")

if __name__ == "__main__":
    juego = JuegoTamagotchi()
    juego.iniciar()
