# Crear el diccionario informacion_personal
informacion_personal = {
    "nombre": "Luis",
    "edad": 18,
    "ciudad": "Quito",
}

# Acceder al valor asociado con la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "Tena"

# Agregar una nueva clave-valor para representar la profesion
informacion_personal["profesion"] = "Ingeniero"

# Verificar si la clave "telefono" existe y agregarla si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0992487514"

# Eliminar la clave "edad"
del informacion_personal["edad"]

# Imprimir el diccionario final
print("Diccionario Final:")
print(informacion_personal)
