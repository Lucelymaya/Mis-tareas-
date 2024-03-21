# diccionario con información personal ficticia
informacion_personal = {
    "Nombre": "Lilia Lucely Maya Enriquez",
    "Edad": 36,
    "Ciudad": "Lago Agrio-Sucumbios",
    "Profesion": "Estudiante"
}

print(informacion_personal)

# Modificar el valor
informacion_personal['ciudad'] = 'Lago Agrio'
print(informacion_personal)

# Agregar nueva clave:valor
informacion_personal['profesion'] = 'Estudiante'
print(informacion_personal)

# Verificar telefono y agregar
if 'telefono' in informacion_personal:
 print(informacion_personal['telefono'])
else:
 informacion_personal['telefono'] = '0988441980'
print(informacion_personal)

# Eliminar edad
informacion_personal.pop('edad')
print(informacion_personal)






