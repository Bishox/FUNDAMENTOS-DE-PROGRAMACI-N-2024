
# Definición de la función
def calcular_descuento(monto_total, porcentaje_descuento):
    descuento = monto_total * porcentaje_descuento / 100
    total_a_pagar = monto_total - descuento

    # Imprimir valores     
    print("Monto total de la compra: {:.2f} Dólares".format(monto_total))
    print("Porcentaje de descuento:", porcentaje_descuento, "%")
    print("Valor de descuento: {:.2f} Dólares".format(descuento))
    print("valor a pagar con descuento: {:.2f} Dólares".format(total_a_pagar))
    print("------------------------------------------------------------------------------")
    
    return total_a_pagar  # Retornar el total a pagar en lugar del monto total

# Inicializar la variable para la suma total de totales a pagar
suma_total_pagar = 0

# Loop principal
while True:
    # Ingreso de datos monto_total
    monto_total_str = input("Por favor ingrese el monto total de la compra o 'q' para salir: ")
    
    if monto_total_str.lower() == 'q':
        break  # Salir del bucle si el usuario ingresa 'q'

    try:
        monto_total = float(monto_total_str)
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue  # Volver a solicitar el monto total si se ingresa un valor inválido

    # Porcentaje de descuento predeterminado
    porcentaje_descuento = 10
    suma_total_pagar += calcular_descuento(monto_total, porcentaje_descuento)

# Mostrar la suma total de los totales a pagar
print("La suma total es: {:.2f} Dólares".format(suma_total_pagar))
print("Gracias por usar el programa. ¡Hasta luego!")
input("presione enter para salir")
