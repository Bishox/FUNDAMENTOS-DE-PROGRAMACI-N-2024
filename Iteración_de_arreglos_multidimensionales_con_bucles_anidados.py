# PROGRAMA PARA CALCULAR EL PROMEDIO DE TEMPERATURA  EN UN INTERVALO DE TIEMPO

def calcula_temperatura(datos, ciudad, semana_inicio, semana_final):
    suma_temp = 0  # Variable para almacenar la suma de las temperaturas
    num_items = 0  # Variable para almacenar el total de items leídos

    for i in range(len(datos[ciudad])):  # Itera sobre las semanas de la ciudad seleccionada
        if i >= semana_inicio and i <= semana_final:  # Verifica si la semana está dentro del intervalo
            for j in range(len(datos[ciudad][i])):  # Itera sobre los días de la semana
                temp_dia = datos[ciudad][i][j]['temp']  # Obtiene la temperatura del día
                suma_temp += temp_dia  # Suma la temperatura al total
                num_items += 1  # Incrementa el contador de items
                print(datos[ciudad][i][j])  # Imprime los datos del día

    promedio = suma_temp / num_items  # Calcula el promedio de temperaturas
    return promedio


temperaturas = [
    [  # Ciudad 1
        [  # Semana 1
            {"day": "Lunes", "temp": 17},
            {"day": "Martes", "temp": 19},
            {"day": "Miércoles", "temp": 20},
            {"day": "Jueves", "temp": 19},
            {"day": "Viernes", "temp": 15},
            {"day": "Sábado", "temp": 18},
            {"day": "Domingo", "temp": 12}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 16},
            {"day": "Martes", "temp": 19},
            {"day": "Miércoles", "temp": 13},
            {"day": "Jueves", "temp": 11},
            {"day": "Viernes", "temp": 17},
            {"day": "Sábado", "temp": 19},
            {"day": "Domingo", "temp": 13}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 17},
            {"day": "Martes", "temp": 11},
            {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 12},
            {"day": "Viernes", "temp": 18},
            {"day": "Sábado", "temp": 11},
            {"day": "Domingo", "temp": 15}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 15},
            {"day": "Martes", "temp": 18},
            {"day": "Miércoles", "temp": 10},
            {"day": "Jueves", "temp": 19},
            {"day": "Viernes", "temp": 14},
            {"day": "Sábado", "temp": 17},
            {"day": "Domingo", "temp": 11}
        ]
    ],
    [  # Ciudad 2
        [  # Semana 1
            {"day": "Lunes", "temp": 12},
            {"day": "Martes", "temp": 14},
            {"day": "Miércoles", "temp": 18},
            {"day": "Jueves", "temp": 10},
            {"day": "Viernes", "temp": 13},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 19}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 13},
            {"day": "Martes", "temp": 16},
            {"day": "Miércoles", "temp": 10},
            {"day": "Jueves", "temp": 12},
            {"day": "Viernes", "temp": 15},
            {"day": "Sábado", "temp": 17},
            {"day": "Domingo", "temp": 11}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 11},
            {"day": "Martes", "temp": 15},
            {"day": "Miércoles", "temp": 18},
            {"day": "Jueves", "temp": 10},
            {"day": "Viernes", "temp": 12},
            {"day": "Sábado", "temp": 16},
            {"day": "Domingo", "temp": 10}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 14},
            {"day": "Martes", "temp": 17},
            {"day": "Miércoles", "temp": 19},
            {"day": "Jueves", "temp": 11},
            {"day": "Viernes", "temp": 14},
            {"day": "Sábado", "temp": 17},
            {"day": "Domingo", "temp": 20}
        ]
    ],
    [  # Ciudad 3
        [  # Semana 1
            {"day": "Lunes", "temp": 10},
            {"day": "Martes", "temp": 12},
            {"day": "Miércoles", "temp": 14},
            {"day": "Jueves", "temp": 11},
            {"day": "Viernes", "temp": 18},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 12}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 19},
            {"day": "Martes", "temp": 11},
            {"day": "Miércoles", "temp": 13},
            {"day": "Jueves", "temp": 10},
            {"day": "Viernes", "temp": 17},
            {"day": "Sábado", "temp": 14},
            {"day": "Domingo", "temp": 11}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 11},
            {"day": "Martes", "temp": 13},
            {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 12},
            {"day": "Viernes", "temp": 19},
            {"day": "Sábado", "temp": 16},
            {"day": "Domingo", "temp": 13}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 18},
            {"day": "Martes", "temp": 10},
            {"day": "Miércoles", "temp": 12},
            {"day": "Jueves", "temp": 19},
            {"day": "Viernes", "temp": 16},
            {"day": "Sábado", "temp": 13},
            {"day": "Domingo", "temp": 10}
        ]
    ]
]

# Definir variables para los índices de las ciudades
QUITO = 0
GUAYAQUIL = 1
CUENCA = 2

# Selecciona la ciudad
ciudad = int(input("Ingrese el número de la ciudad (1 para Quito, 2 para Guayaquil o 3 para Cuenca): ")) - 1

# Selecciona las semanas inicial y final
semana_inicio = int(input("Ingrese el número de la semana inicial: ")) - 1
semana_final = int(input("Ingrese el número de la semana final: ")) - 1

# Calcular el promedio de temperaturas
promedio_calculado = calcula_temperatura(temperaturas, ciudad, semana_inicio, semana_final)

# Imprimir el promedio con dos decimales
print("El promedio de temperaturas es: {:.2f} ºC".format(promedio_calculado))