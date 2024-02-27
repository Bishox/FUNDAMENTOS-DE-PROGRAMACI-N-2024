#matriz 3D de temperaturas
temperaturas = [
    [   # Ciudad 1 "Quito"
        [19, 19, 22, 24, 22, 19, 22],   # Temperaturas para la semana 1
        [19, 22, 18, 23, 20, 21, 19],   # Temperaturas para la semana 2
        [23, 20, 18, 19, 18, 18, 17],   # Temperaturas para la semana 3
        [22, 25, 24, 22, 19, 18, 15]    # Temperaturas para la semana 4
    ],
    [   # Ciudad de 2 "Guayaquil"
        [22, 24, 18, 20, 23, 25, 19],
        [13, 16, 20, 14, 15, 17, 11],
        [21, 15, 18, 20, 12, 16, 20],
        [14, 17, 19, 21, 14, 17, 20]
    ],
    [   # Ciudad de 3 "Cuenca"
        [20, 12, 14, 31, 12, 15, 12],
        [19, 21, 13, 20, 17, 24, 21],
        [21, 13, 15, 22, 19, 16, 13],
        [18, 20, 22, 19, 16, 23, 20]
    ]
]

# Calcular el promedio de temperaturas para cada ciudad y semana
for i, ciudad in enumerate(temperaturas):
    print(f"Promedio de temperaturas para Ciudad {i+1}:")
    for j, semana in enumerate(ciudad):
        promedio = sum(semana) / len(semana)
        print(f"Semana {j+1}: {promedio:.2f}°C")
    print()