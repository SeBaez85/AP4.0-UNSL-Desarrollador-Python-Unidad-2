print("Vamos a calcular el capital obtenido en su inversión")
cantidadAInvertir = float(input("Ingrese una cantidad a invertir: "))
interesAnual = float(input("Ingrese el interés anual en porcentaje: "))
numeroAnios = int(input("Ingrese el número de años: "))
print("El capital obtenido en su inversión es: ", round((cantidadAInvertir / interesAnual) * numeroAnios + cantidadAInvertir, 2))
