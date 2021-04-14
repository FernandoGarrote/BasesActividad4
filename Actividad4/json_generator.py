from random import randint
import string
import sys
from coolname import generate_slug
import random
import json
from faker import Faker


fake = Faker([ 'es_MX', 'en_US'])

file = open("libros.json", "w")
file2 = open("usuarios.json", "w")
file3 = open("historial.json", "w")

generos = ["Accion", "Aventura", "Drama", "Terror", "Comedia", "Misterio", "Novela Historica", "Romance", "Policiaco"]

editoriales = ["Porrua", "El Jamon", "Osuba", "El Mexicano", "Ana La Clown", "El Patito Feo",
"El Osito Bimbo", "Submarino", "Xenoblade", "La Maruchan", "Editoriales Benavidez", "Valorant", "Puro 100",
"La Vanguardia", "El Sol", "Que si que no", "Derechairos", "El Alfajor"]


 #Para generar libros
for i in range(100000):
    gen = random.sample(generos, k=2)
    n=file.write("{\n"+'"'+"_SKU"+'"'+":"+str(i)+',\n'
    +'"' +"Titulo"+'"'+":"+'"'+generate_slug()+'"'+",\n"
    +'"' +"Autor"+'"'+":"+'"'+fake.name()+'"'+",\n"
    +'"' +"Genero"+'"'+":"+json.dumps(gen)+",\n"
    +'"' +"Editorial"+'"'+":"+'"'+str(random.choice(editoriales))+'"'+",\n"
    +'"' +"Precio"+'"'+":"+str(randint(100, 500))+".00"+",\n"
    +'"' +"FechaP"+'"'+":"+'"'+fake.date()+'"'+"\n},\n")


for i in range(100000):
    #gen = random.sample(generos, k=2)
    nom = fake.first_name()
    nom = fake.first_name()
    ape = fake.last_name()
    secure_random = random.SystemRandom()
    random_float = secure_random.random()
    x = secure_random.uniform(12.5, 30.5)
    y = secure_random.uniform(40.3, 70.2)
    n=file2.write("{\n"+'"'+"_id"+'"'+":"+str(i)+',\n'
    +'"' +"Nombre"+'"'+":"+'"'+str(nom)+'"'+",\n"
    +'"' +"Apellido"+'"'+":"+'"'+str(ape)+'"'+",\n"
    +'"' +"Email"+'"'+":"+'"'+str(nom)+str(ape)+str(randint(0,99))+'@gmail.com"'+",\n"
    +'"' +"Direccion"+'"'+":"+"{\n"+'"type":'+'"Point"'+",\n"
    +'"coordinates"'+":"+"["+str(x)+","+str(y)+"]\n"+"}\n"+"\n},\n")


for i in range(100000):
    print("Count:" + str(i))
    #gen = random.sample(generos, k=2)
    #nom = fake.first_name()
    #nom = fake.first_name()
    #ape = fake.last_name()
    #secure_random = random.SystemRandom()
    #random_float = secure_random.random()
    #x = secure_random.uniform(12.5, 30.5)
    #y = secure_random.uniform(40.3, 70.2)


    n=file3.write("{\n"
    +'"' +"Fecha_renta"+'"'+":"+'"'+str(fake.date_between(1, 30))+'"'+",\n"
    +'"' +"Fecha_dev"+'"'+":"+'"'+str(fake.date_between(50, 100))+'"'+",\n"
    +'"' +"id_libro"+'"'+":"+str(randint(0,99999))+",\n"
    +'"' +"id_usr"+'"'+":"+str(randint(0,99999))+"\n},\n")
