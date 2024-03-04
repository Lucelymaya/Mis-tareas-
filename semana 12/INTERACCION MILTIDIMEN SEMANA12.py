# Crear una matriz 3D para almacenar datos de ventas
# Primera dimensión: Sucursales (2 sucursales)
# Segunda dimensión: Semanas (3 semanas)
# Tercera dimensión: Días de la semana (7 días)
temperaturas = [
    [   # Sucursal 1
        [   # Semana 1
            {"day": "Lunes", "temp": 12},
            {"day": "Martes", "temp": 80},
            {"day": "Miércoles", "temp": 50},
            {"day": "Jueves", "temp": 50},
            {"day": "Viernes", "temp": 80},
            {"day": "Sábado", "temp": 80},
            {"day": "Domingo", "temp": 50}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 11},
            {"day": "Martes", "temp": 80},
            {"day": "Miércoles", "temp": 50},
            {"day": "Jueves", "temp": 50},
            {"day": "Viernes", "temp": 80},
            {"day": "Sábado", "temp": 50},
            {"day": "Domingo", "temp": 50}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 50},
            {"day": "Martes", "temp": 50},
            {"day": "Miércoles", "temp": 60},
            {"day": "Jueves", "temp": 60},
            {"day": "Viernes", "temp": 60},
            {"day": "Sábado", "temp": 60},
            {"day": "Domingo", "temp": 80}
        ]
    ],
    [   # Sucursal 2
        [   # Semana 1
            {"day": "Lunes", "temp": 90},
            {"day": "Martes", "temp": 15},
            {"day": "Miércoles", "temp": 10},
            {"day": "Jueves", "temp": 80},
            {"day": "Viernes", "temp": 12},
            {"day": "Sábado", "temp": 13},
            {"day": "Domingo", "temp": 14}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 9},
            {"day": "Martes", "temp": 10},
            {"day": "Miércoles", "temp": 95},
            {"day": "Jueves", "temp": 85},
            {"day": "Viernes", "temp": 12},
            {"day": "Sábado", "temp": 13},
            {"day": "Domingo", "temp": 14}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 10},
            {"day": "Martes", "temp": 11},
            {"day": "Miércoles", "temp": 10},
            {"day": "Jueves", "temp": 9},
            {"day": "Viernes", "temp": 13},
            {"day": "Sábado", "temp": 14},
            {"day": "Domingo", "temp": 15}
        ]
    ]
]



# Iterando sobre las ciudades, semanas y días para calcular el promedio de temperaturas
for ciudad_index, ciudad in enumerate(temperaturas, start=1):
    print(f'CIUDAD No. {ciudad_index}')
    for semana_index, semana in enumerate(ciudad, start=1):
        # Calculando el promedio de temperaturas para la semana actual
        temperatura_semana = [dia["temp"] for dia in semana]  # Lista de temperaturas de la semana
        promedio_semana = sum(temperatura_semana) / len(temperatura_semana)  # Calculando el promedio
        print(f'El promedio de la semana No. {semana_index} es: {promedio_semana:.2f}')