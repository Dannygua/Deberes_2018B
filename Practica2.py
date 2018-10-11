
openew =""
def Suma(n1, n2):
    return n1+n2

def Resta (n1,n2):
    return n1-n2

def Multiplicacion (n1,n2):
    return n1*n2

def Division (n1,n2):

    try:
        return n1/n2
    except ZeroDivisionError:
        print ("Division para cero imposible")


while openew != "salir":

    print ("Inrese la operacion que desea Realizar")
    print ("Suma")
    print ("Resta")
    print ("Multiplicacion")
    print ("Division")
    print ("Salir")

    operacion = input("Escriba la operacion deseada: ")
    openew = operacion.lower()

    if openew == "salir":
        print ("Adios ")
        break

    while True:
        try:
            num1 = int(input("Ingrese Primer Numero: "))
            break
        except ValueError:
            print ("Valores ingresados incongruentes")
            print ("INTENTELO DE NUEVO")

    while True:
        try:
            num2 = int(input ("Ingrese Segundo Numero: "))
            break
        except ValueError:
            print ("Valores ingresados incongruentes")
            print ("INTENTELO DE NUEVO")

    if openew == "suma":
        print ("Respuesta: "+ str(Suma (num1 , num2)))
    elif openew == "resta":
        print ("Respuesta "+ str (Resta (num1 , num2)))
    elif openew == "multiplicacion":
        print ("Respuesta "+ str (Multiplicacion (num1 , num2)))
    elif openew == "division":
        print ("Respuesta "+ str (Division (num1 , num2)))
    else:
        print ("Operacion Ingresada invalida, Esooga entre Suma, Resta, Multiplicacion o Division")
        print ("INTENTELO DE NUEVO")




