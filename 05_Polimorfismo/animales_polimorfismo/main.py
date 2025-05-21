from Perro import Perro
from Gato import Gato
from Animal import Animal

perro = Perro("Firulais",12, "blanco")
perro1 = Perro("Juanito",10, "café")
gato = Gato("Lucía", 6, "gris")
gato1 = Gato("Ifi", 8, "atigrado")

for animal in (perro, perro1, gato, gato1):
    animal.hacer_sonido()



