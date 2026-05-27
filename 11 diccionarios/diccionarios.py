#Lista de elementos llave:valor
#Arreglos asociativos

persona = {"nombre": "Rodrigo",
           "edad": 800,
           "apellido": "Montemayor"}

persona["apodo"] = "Ringa Tech"

#print(persona.items())

for key, value in persona.items():
    print(f"la llave {key} tiene el valor { value}")

#for key, value in persona.items():


