def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

temperatura = float(input("Ingrese la temperatura: "))
unidad = input("¿Es en Celsius o Fahrenheit? (C/F): ")

if unidad.upper() == 'C':
    resultado = celsius_a_fahrenheit(temperatura)
    print("La temperatura en Fahrenheit es:", resultado)
elif unidad.upper() == 'F':
    resultado = fahrenheit_a_celsius(temperatura)
    print("La temperatura en Celsius es:", resultado)
else:
    print("Unidad no reconocida.")
