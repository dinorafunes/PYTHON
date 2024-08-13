# while true para simular un login que siga preguntando hasta que se ingrese la contraseña correcta


while True:
    usuario = "yo"
    contra = "1234"

    a = input("Escriba su usario: ")
    b = input("Escriba su contraseña: ")

    if(a == usuario and b == contra):
        break
    else:
        print("usuario o contraseña incorrecta")
        continue