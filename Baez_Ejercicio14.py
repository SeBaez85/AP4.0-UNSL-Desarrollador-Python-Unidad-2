print("Vamos a realizar la conversión a dólares y euros de la cantidad de pesos ingresados")
pesosIngresados = float(input("Ingrese una cantidad de pesos: "))
valorDolar = 242.0
conversionDolar = pesosIngresados / valorDolar
valorEuro = 263.0
conversionEuro = pesosIngresados / valorEuro
#print(f"El valor en dólares es: {conversionDolar:.2f} y el valor en Euros: {conversionEuro:.2f}")
print("El valor en dólares es:", round(float(conversionDolar), 2), "y el valor en Euros es:", round(float(conversionDolar), 2))