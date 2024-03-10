# Crear una matriz 3D para almacenar datos de ventas
# Primera dimensión: Sucursales (2 sucursales)
# Segunda dimensión: Semanas (3 semanas)
# Tercera dimensión: Días de la semana (7 días)
temperaturas = [
    [   # Sucursal 1
        [   # Semana 1
            {"day": "Lunes", "temp": 1000},
            {"day": "Martes", "temp": 1200},
            {"day": "Miércoles", "temp": 1100},
            {"day": "Jueves", "temp": 900},
            {"day": "Viernes", "temp": 1300},
            {"day": "Sábado", "temp": 1400},
            {"day": "Domingo", "temp": 1500}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 1100},
            {"day": "Martes", "temp": 1150},
            {"day": "Miércoles", "temp": 1050},
            {"day": "Jueves", "temp": 950},
            {"day": "Viernes", "temp": 1350},
            {"day": "Sábado", "temp": 1450},
            {"day": "Domingo", "temp": 1550}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 1200},
            {"day": "Martes", "temp": 1250},
            {"day": "Miércoles", "temp": 1150},
            {"day": "Jueves", "temp": 950},
            {"day": "Viernes", "temp": 1400},
            {"day": "Sábado", "temp": 1500},
            {"day": "Domingo", "temp": 1600}
        ]
    ],
    [   # Sucursal 2
        [   # Semana 1
            {"day": "Lunes", "temp": 900},
            {"day": "Martes", "temp": 1100},
            {"day": "Miércoles", "temp": 1000},
            {"day": "Jueves", "temp": 800},
            {"day": "Viernes", "temp": 1200},
            {"day": "Sábado", "temp": 1300},
            {"day": "Domingo", "temp": 1400}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 950},
            {"day": "Martes", "temp": 1050},
            {"day": "Miércoles", "temp": 950},
            {"day": "Jueves", "temp": 850},
            {"day": "Viernes", "temp": 1250},
            {"day": "Sábado", "temp": 1350},
            {"day": "Domingo", "temp": 1450}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 1000},
            {"day": "Martes", "temp": 1150},
            {"day": "Miércoles", "temp": 1050},
            {"day": "Jueves", "temp": 900},
            {"day": "Viernes", "temp": 1300},
            {"day": "Sábado", "temp": 1400},
            {"day": "Domingo", "temp": 1500}
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