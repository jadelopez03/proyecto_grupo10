alumnos = [
    {"nombre": "Ana", "nota": 8.5},
    {"nombre": "Luis", "nota": 4.0},
    {"nombre": "Marta", "nota": 7.0},
    {"nombre": "Pablo", "nota": 3.5},
    {"nombre": "Sara", "nota": 9.0},s
]

for alumno in alumnos:
    if alumno["nota"] >= 5:
        print(f"El alumno {alumno["nombre"].upper()} está aprobado, , su nota es un {alumno["nota"]}")
    elif alumnos == 0:
        print("0")
    else:
        print(f"El alumno {alumno["nombre"].upper()} está suspendido, su nota es un {alumno["nota"]}")
        
contador_aprobado = 0
contador_suspendido = 0

for alumno in alumnos:
    if alumno["nota"] >= 5:
        contador_aprobado += 1
    else:
        contador_suspendido += 1
print(f"Número de alumnos aprobados: {contador_aprobado}")
print(f"Número de alumnos suspendidos: {contador_suspendido}")

contador_total = float(contador_aprobado + contador_suspendido)
print(f"Número total de alumnos: {contador_total}")

suma_notas = 0
for alumno in alumnos:
    suma_notas += alumno["nota"]
    


def calcular_media(alum,total):
    return alum/total
"""
Funcion que calcula la media de los alumnos sobre nuestra lista.

Parámetros: alum(nota de los alumnos), total (numero total de alumnos de la clase).

Devuelve el la suma de notas de los alumnos dividido entre el numero de individuos.
"""

redondeo_dos =((calcular_media(suma_notas, contador_total)))

print(round(redondeo_dos, 2))
