#tehdään alussa importit
# yy kaa koo
from logger import logger
from summa import summa
from erotus import erotus
# lol
logger("aloitetaan ohjelma") # muutos mainissa

x = int(input("luku 1: "))
y = int(input("luku 2: "))
<<<<<<< HEAD
print(f"Lukujen {x} ja {y} summa on {summa(x, y)}") # muutos bugikorjaus-branchissa
print(f"Lukujen {x} ja {y} erotus on {erotus(x, y)}") #muutos bugikorjaus-branchissa
=======
print(f"{summa(x, y)}") # muutos mainissa
print(f"{erotus(x, y)}") # muutos mainissa
>>>>>>> main

logger("lopetetaan ohjelma")
<<<<<<< HEAD
=======
print("goodbye!") # lisäys bugikorjaus-branchissa
>>>>>>> bugikorjaus
