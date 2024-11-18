"""El siguiente código es el programa base 
para interactuar con los datos obtenidos en con el PLC
El programa Base consta de un menu donde se solicita ingresar
un numero entre 1 y 8.
Para este ejemplo se simulará la léctura y escritua de un
Registro y un coil
- Para el caso de la lectura de un registro se simulará un grafico en tiempo real
- Para el caso de la escritura de un coil se simulara el uso de un boton con acción toogle"""


# IMPORTAR MODULO DE GRAFICO Y BOTON
import Scripts.graph as graph
import Scripts.boton as boton
#Código para menu
menu = int(input("Ingrese las opciones\n(1) Escritura de un coil\n(2) Escritura multiples coils\n"+ #input solicita un valor por la consola e int lo tranforma a entero
                "(3) Escritura de un registro\n(4) Escritura multiples registros\n"+
                "(5) Lectura de un contact\n(6) Lectura multiples contact\n"+
                "(7) Lectura de un registro\n(8) Lectura multiples registros\n"))
#Una vez obtenido el valor del menu se realiza un match (switch) 
#Para que en base al valor obtenido se realiza una acción
match menu:
    case 1:
        #Caso 1 ESCRITURA DE COIL
        print(menu) 
    case 2:
        #Caso 2 ESCRITURA MULTIPLES COILS
        print(menu) 
    case 3:
        #Caso 3 ESCRITURA DE REGISTRO (HOLDING)
        print(menu)
    case 4:
        #Caso 4 ESCRITURA DE MULTIPLES REGISTROS (MULTIPLE HOLDING)
        print(menu)
    case 5:
        #Caso 5 LECTURA DE CONTACT
        print(menu)
    case 6:
        #Caso 6 LECTURA DE MULTIPLES CONTACT
        print(menu)
    case 7:
        #Caso 7 LECTURA DE SIMPLE REGISTRO (INPUT)
        print(menu)
    case 8:
        #Caso 8 LECTURA DE MULTIPLES REGISTROS (MULTIPLE INPUT)
        print(menu)
    case _:
        #En caso de ingresar otro valor
        print("No existe esa opción")
