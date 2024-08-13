#En phyton Con un while, hacer que el programa haga un output de una tabla de multiplicar

# 2 x 1 = 2
"""
numero = 2
contador = 1

while contador <= 10:
    resultado = numero * contador
    print(f"{numero} x {contador} = {resultado}")
    contador += 1
"""
"""
numero = int(input("Digite el número que desea para la tabla de multiplicar: "))
i = 1
while i <= 10:
    print(f"{numero} x {i} = {numero * i}")
    i += 1
"""
while True:
    numero = int(input("Digite el número que desea para la tabla de multiplicar: "))
    i = 1
    while i <= 10:
        print(f"{numero} x {i} = {numero * i}")
        i += 1
    op= input("Selecciones una opcion:\n"
        "1-Pedir otro numero\n"+
        "2-Salir\n")
    if(op=="1"):
        continue
    elif(op=="2"):
        break
    else:

        print("Opcion incorrecta")


