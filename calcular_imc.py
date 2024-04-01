

def calcular_imc(peso,altura):
    return peso / (altura ** 2)

peso = float (input ("Ingrese su peso en Kg"))
altura = float ( input ("Ingrese su altura en metros"))

imc= calcular_imc(peso,altura)
print("su indice de masa corporal es", imc)