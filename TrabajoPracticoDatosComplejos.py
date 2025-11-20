# ==============================================================
# Practico 6: Estructuras de datos complejas
# Programacion I - UTN a distancia
# ==============================================================

# 1) Diccionario inicial de frutas
precios_frutas = {'Banana': 1200, 'Anana': 2500, 'Melon': 3000, 'Uva': 1450}

# Anadir nuevas frutas
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print("Despues del punto 1:", precios_frutas)
#  {'Banana': 1200, 'Anana': 2500, 'Melon': 3000, 'Uva': 1450,
#    'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300}

# 2) Actualizar precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melon'] = 2800

print("Despues del punto 2:", precios_frutas)

# 3) Lista con solo las frutas (las claves)
solo_frutas = list(precios_frutas.keys())
print("Solo frutas:", solo_frutas)
#  ['Banana', 'Anana', 'Melon', 'Uva', 'Naranja', 'Manzana', 'Pera']

# 4) Agenda telefonica con 5 contactos
print("\n=== Agenda telefonica ===")
agenda = {}
for i in range(5):
    nombre = input(f"Nombre del contacto {i+1}: ").strip().title()
    telefono = input(f"Teleefono de {nombre}: ").strip()
    agenda[nombre] = telefono

# Consultar un contacto
buscar = input("\n¿Que  acto querés buscar?: ").strip().title()
if buscar in agenda:
    print(f"El telefono de {buscar} es: {agenda[buscar]}")
else:
    print(f"{buscar} no esta en la agenda.")

# 5) Frase  palabras unicas + frecuencia
print("\n=== Analisis de frase ===")
frase = input("Escribi una frase: ").lower()
palabras = frase.split()

# Palabras unicas con set
unicas = set(palabras)
print("Palabras unicas:", unicas)

# Conteo con diccionario
frecuencia = {}
for p in palabras:
    frecuencia[p] = frecuencia.get(p, 0) + 1

print("Frecuencia de cada palabra:", frecuencia)

# 6) 3 alumnos con tupla de 3 notas cada uno
print("\n=== Promedio de alumnos ===")
alumnos = {}
for i in range(3):
    nombre = input(f"Nombre del alumno {i+1}: ").strip().title()
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: "))
    alumnos[nombre] = (n1, n2, n3)
    promedio = sum(alumnos[nombre]) / 3
    print(f"{nombre}  promedio: {promedio:.2f}")

# 7) Sets de aprobados de parciales
print("\n=== Aprobados de parciales ===")
parcial1 = {"Ana", "Luis", "Carla", "Pedro", "Sofia"}
parcial2 = {"Luis", "Carla", "Juan", "Maria", "Sofia"}

ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2  # diferencia simetrica
al_menos_uno = parcial1 | parcial2

print("Aprobaron ambos parciales:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos uno:", al_menos_uno)

# 8) Gestion de stock de productos
print("\n=== Gestion de stock ===")
stock = {}

while True:
    producto = input("\nNombre del producto (o 'salir'): ").strip().title()
    if producto == "Salir":
        break

    if producto in stock:
        print(f"Stock actual de {producto}: {stock[producto]}")
        opcion = input("Queres agregar unidades? (s/n): ")
        if opcion.lower() == 's':
            cant = int(input("Cuantas unidades agregar: "))
            stock[producto] += cant
            print(f"Nuevo stock de {producto}: {stock[producto]}")
    else:
        unidades = int(input(f"Stock inicial de {producto}: "))
        stock[producto] = unidades
        print(f"{producto} agregado con {unidades} unidades.")

print("Stock final:", stock)

# 9) Agenda con tuplas (dia, hora) como clave
print("\n=== Agenda con dia y hora ===")
agenda_eventos = {}

while True:
    dia = input("\nDia (ej: lunes) o 'salir': ").strip().lower()
    if dia == "salir":
        break
    hora = input("Hora (ej: 10:00): ").strip()
    evento = input("Evento: ").strip()

    agenda_eventos[(dia, hora)] = evento

# Consultar
print("\nConsultar evento:")
dia_buscar = input("Dia: ").lower()
hora_buscar = input("Hora: ")
clave = (dia_buscar, hora_buscar)

if clave in agenda_eventos:
    print(f"El {dia_buscar} a las {hora_buscar}: {agenda_eventos[clave]}")
else:
    print("No hay ningun evento en ese horario.")

# 10) Invertir diccionario pais  capital    capital  pais
print("\n=== Invertir paises y capitales ===")
original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Peru": "Lima",
    "Brasil": "Brasilia"
}

invertido = {}
for pais, capital in original.items():
    invertido[capital] = pais

# Si hubiera dos paises con misma capital, la ultima gana (ejercicio simple)
print("Original:", original)
print("Invertido:", invertido)
#  {'Buenos Aires': 'Argentina', 'Santiago': 'Chile', ...}
print("\nTP 6 COMPLETADO")
















   
