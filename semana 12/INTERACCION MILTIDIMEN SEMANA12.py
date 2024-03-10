# Crear una matriz 3D para almacenar datos de ventas
# Primera dimensión: Sucursales (2 sucursales)
# Segunda dimensión: Semanas (3 semanas)
# Tercera dimensión: Días de la semana (7 días)
ventas = [
    [   # Sucursal 1
        [   # Semana 1
            {"day": "Lunes", "venta": 1000},
            {"day": "Martes", "venta": 1200},
            {"day": "Miércoles", "venta": 1100},
            {"day": "Jueves", "venta": 900},
            {"day": "Viernes", "venta": 1300},
            {"day": "Sábado", "venta": 1400},
            {"day": "Domingo", "venta": 1500}
        ],
        [   # Semana 2
            {"day": "Lunes", "venta": 1100},
            {"day": "Martes", "venta": 1150},
            {"day": "Miércoles", "venta": 1050},
            {"day": "Jueves", "venta": 950},
            {"day": "Viernes", "venta": 1350},
            {"day": "Sábado", "venta": 1450},
            {"day": "Domingo", "venta": 1550}
        ],
        [   # Semana 3
            {"day": "Lunes", "venta": 1200},
            {"day": "Martes", "venta": 1250},
            {"day": "Miércoles", "venta": 1150},
            {"day": "Jueves", "venta": 950},
            {"day": "Viernes", "venta": 1400},
            {"day": "Sábado", "venta": 1500},
            {"day": "Domingo", "venta": 1600}
        ]
    ],
    [   # Sucursal 2
        [   # Semana 1
            {"day": "Lunes", "venta": 900},
            {"day": "Martes", "venta": 1100},
            {"day": "Miércoles", "venta": 1000},
            {"day": "Jueves", "venta": 800},
            {"day": "Viernes", "venta": 1200},
            {"day": "Sábado", "venta": 1300},
            {"day": "Domingo", "venta": 1400}
        ],
        [   # Semana 2
            {"day": "Lunes", "venta": 950},
            {"day": "Martes", "venta": 1050},
            {"day": "Miércoles", "venta": 950},
            {"day": "Jueves", "venta": 850},
            {"day": "Viernes", "venta": 1250},
            {"day": "Sábado", "venta": 1350},
            {"day": "Domingo", "venta": 1450}
        ],
        [   # Semana 3
            {"day": "Lunes", "venta": 1000},
            {"day": "Martes", "venta": 1150},
            {"day": "Miércoles", "venta": 1050},
            {"day": "Jueves", "venta": 900},
            {"day": "Viernes", "venta": 1300},
            {"day": "Sábado", "venta": 1400},
            {"day": "Domingo", "venta": 1500}
        ]
    ]
]

promedios_ventas = {}
# Calcular el promedio de ventas para cada sucursal y semana

for i, sucursal in enumerate(ventas):

    for j, semana in enumerate(sucursal):

        total = 0

        for dia in semana:
            total += dia['venta']

        promedio = total / len(semana)

        promedios_ventas[(i + 1, j + 1)] = promedio  # Almacenar el promedio con clave (sucursal, semana)

        print(f"Para sucursal {i + 1}, semana {j + 1}: Promedio de ventas = {promedio:.2f}"

