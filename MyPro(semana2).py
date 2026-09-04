# Programa para la fábrica de software MyPro
PRECIO_BASE = 50
PI = 3.1416

def obtener_porcentaje_descuento(cantidad_licencias):
    if cantidad_licencias >= 5:
        return 0.30
    elif cantidad_licencias >= 3:
        return 0.20
    else:
        return 0
    
def calcular_precio_con_descuento(porcentaje_descuento):
    descuento = PRECIO_BASE * porcentaje_descuento
    precio_final = PRECIO_BASE - descuento
    return precio_final

def calcular_total_compra(cantidad_licencias, precio_unitario):
    total = cantidad_licencias * precio_unitario
    return total

def calcular_volumen_esfera(radio):
    volumen = (4 / 3) * PI * (radio * radio * radio)
    return volumen

def mostrar_menu():
    print("\nMenú principal")
    print("1. Calcular descuento en compras de software")
    print("2. Calcular volumen de una esfera")
    print("3. Salir del programa")

def main():
    print("Sistema de operaciones - Fábrica de software MyPro")
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1, 2 o 3): ")

        if opcion == "1":
            licencias_compradas = int(input("Ingrese la cantidad de licencias adquiridas: "))

            porcentaje_descuento = obtener_porcentaje_descuento(licencias_compradas)
            precio_final = calcular_precio_con_descuento(porcentaje_descuento)
            total_pagar = calcular_total_compra(licencias_compradas, precio_final)

            print("\nResultado de la compra de software")
            print(f"Cantidad de licencias: {licencias_compradas}")
            print(f"Precio base por licencia: ${PRECIO_BASE:.2f}")
            print(f"Descuento aplicado: {porcentaje_descuento * 100:.0f}%")
            print(f"Precio final por licencia: ${precio_final:.2f}")
            print(f"Total a pagar: ${total_pagar:.2f}")

        elif opcion == "2":
            radio_ingresado = float(input("Ingrese el radio de la esfera: "))

            volumen = calcular_volumen_esfera(radio_ingresado)

            print("\nResultado del cálculo de volumen")
            print(f"Radio ingresado: {radio_ingresado}")
            print(f"Volumen de la esfera: {volumen:.2f}")
        elif opcion == "3":
            print("Gracias por usar el programa de MyPro. Programa finalizado.")
            break

        else:
            print("Opción no válida. Debe seleccionar 1, 2 o 3.")

if __name__ == "__main__":
    main()
    