# diccionario con información personal ficticia
informacion_personal = {
    "Nombre": "Lilia Lucely Maya Enriquez",
    "Edad": 36,
    "Ciudad": "Lago Agrio-Sucumbios",
    "Profesion": "Activadora de marca - Levapan"
}

# Verificar si la clave "telefono" existe en el diccionario
if "telefono" not in informacion_personal:
    # Si no existe, agregarla con un número de teléfono ficticio
    informacion_personal["Telefono"] = "0988441980"

# Eliminar la clave "edad" del diccionario
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimir el diccionario final
print("Información personal:")
for key in informacion_personal:
    print(f"{key}: {informacion_personal[key]}")