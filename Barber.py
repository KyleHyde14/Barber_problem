import random, time 
import threading 

corte_min = 4
corte_max = 8
nuevo_cliente_min = 3
nuevo_cliente_max = 6


class barberia:
    en_espera = []

    def __init__(self, sillas, barbero):
        self.sillas = sillas
        self.barbero = barbero
        print("Número de sillas: ", self.sillas)


    def trabajando(self):
        while True:
            if len(self.en_espera) > 0 :
                self.barbero.cortando(barbero, x)
                del self.en_espera[0]
                print("Gente esperando: ", self.en_espera)
            else:
                self.barbero.dormir(barbero)

    def abrir(self):
        print("¡Abrimos!")
        t = threading.Thread(target=self.trabajando)
        t.start()
        

    def entra_cliente(self, cliente):
        print(cliente.nombre, " Quiere un corte bacano")

        if len(self.en_espera) > self.sillas:
            print(cliente.nombre, 'se fue por falta de espacio :(')
            return

        print(cliente.nombre, "se sienta a esperar")
        
        self.en_espera.append(cliente.nombre)
        self.barbero.despertar(barbero)
        

class cliente:
    def __init__(self, nombre):
        self.nombre = nombre


class barbero:

    e = threading.Event()

    def dormir(self):
        print("Zzz..")
        self.e.wait()
    def despertar(self):
        self.e.set()
    def cortando(self, cliente):
        print("Turno de ", barberia.en_espera[0])
        time.sleep(random.randint(corte_min, corte_max))
        print("Listo ", barberia.en_espera[0], "!")
        self.e.clear()




clientela = []
clientela.append(cliente("Antonio"))
clientela.append(cliente("Julio"))
clientela.append(cliente("Juan"))
clientela.append(cliente("Mario"))
clientela.append(cliente("Dani"))
clientela.append(cliente("Marcela"))
clientela.append(cliente("Rodrigo"))
clientela.append(cliente("Yisus"))
clientela.append(cliente("Chubby"))
clientela.append(cliente("Silvia"))
clientela.append(cliente("Xevi"))
clientela.append(cliente("Carlos"))

johnny = barbero

arbi = barberia(1, johnny)

arbi.abrir()

p = clientela[-1]

while len(clientela) > 0:
    x = clientela.pop(0)
    arbi.entra_cliente(x)
    time.sleep(random.randint(nuevo_cliente_min, nuevo_cliente_max))
    




