# diccionario con información personal ficticia
informacion_personal = {
    "Nombre": "Lilia Lucely Maya Enriquez",
    "Edad": 36,
    "Ciudad": "Lago Agrio-Sucumbios",
    "Profesion": "Activadora de marca - Levapan"
}

print(informacion_personal)

# Modificar el valor
informacion_personal['ciudad'] = 'Quito'
print(informacion_personal)

# Agregar nueva clave:valor
informacion_personal['profesion'] = 'Docente'
print(informacion_personal)

# Verificar telefono y agregar
if 'telefono' in informacion_personal:
 print(informacion_personal['telefono'])
else:
 informacion_personal['telefono'] = '0987654321'
print(informacion_personal)

# Eliminar edad
informacion_personal.pop('edad')
print(informacion_personal)



