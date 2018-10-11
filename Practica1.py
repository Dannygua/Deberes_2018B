nombre1 = input ("Ingrese el nombre de la primera persona: ")
while True:
    try:
        edad1 = int(input("Ingrese la edad de la primera edad: "))
        break
    except ValueError:
        print ("Ha ingresado una edad incongruente ")
        print("INTENTELO DE NUEVO ")

nombre2 = input ("Ingrese el nombre de la segunda persona: ")
while True :
    try:
        edad2 = int (input ("Ingrese la edad de la segunda persona: "))
        break
    except ValueError:
        print ("Ha ingresado una edad incongruente ")
        print("INTENTELO DE NUEVO ")

if edad1 >edad2:
    print (nombre1 +" con una edad de "+str(edad1)+" Años es mayor que "+ nombre2 + " con una edad de " + str(edad2))
elif edad1 <edad2:
    print (nombre2 +" con una edad de "+str(edad2)+" Años es mayor que "+ nombre1 + " con una edad de " + str(edad1))
else:
    print ("Edades iguales")



