import random
import csv
def menu():
    menu="""Menu de Sueldos
    ------------------------------------
        1.-Mostrar sueldos asignados
        2.-Clasificar Sueldos 
        3.-Ver estadisticas del sueldo 
        4.-Exportar reporte de Sueldos
        5.-Salir
        """
    print(menu,end="")
    while True:
        try:
            op= int(input())
            if op >= 1 and op <=5:
                return op
            else:
                print("opcion no valida")
                print("seleccione una opcion valida. -->",end="")
        except ValueError:
            print("Selecciona una opcion valida --> ",end="")

def asignarSueldos(lista):
    for i in range (10):
        nombre = "Empleado " + str(i+1)
        sueldo = random.randrange(300000, 2500000)
        asignado ={"nombre": nombre ,"sueldo": sueldo} 
        lista.append(asignado)
    for empleado in lista:
            print(f"Nombre: {empleado['nombre']}, Sueldo :{empleado['sueldo']}")
            print("------------------------------------------------------------")

def clasificar_empleados(lista):
    bajos = []
    medios =[]
    altos = []
    for trabajador in lista:
        if trabajador ["sueldo"]<=800000:
            bajos.append(trabajador)
        elif trabajador["sueldo"]>800000 and trabajador ["sueldo"]<=2000000:
            medios.append(trabajador)
        else:
            altos.append(trabajador)

    print("EMPLEADOS CON SUELDO MENOR A 800000:")
    print()

    for i in bajos:
        print(f"{i["nombre"]} : ${i["sueldo"]:,.0f}")
    print("------------------------------------------")

    print("EMPLEADOS CON SUELDO ENTRE$800000 Y $2000000:")
    print()

    for i in medios:
        print(f"{i["nombre"]} : ${i["sueldo"]:,.0f}")
        print("---------------------------------------")
    
    print("EMPLEADOS CON SUELDOS MAYORES A 2500000:")
    print()

    for i in altos:
        print(f"{i["nombre"]}  :  ${i["sueldo"]:,.0f}")

def estadisticas(lista):
    sueldos = [i["sueldo"]  for i in lista]
    sueldo_minimo= min(sueldos)
    sueldo_maximo= max(sueldos)
    sueldo_promedio=sum (sueldos) / len(sueldos)
    print("------------------------------")
    print("Estadisticas de sueldos:")
    print("------------------------------")
    print(f"Sueldo minimo : ${sueldo_minimo:,.0f}")
    print(f"Sueldo maximo : ${sueldo_maximo:,.0f}")
    print(f"Sueldo promedio : ${sueldo_promedio:,.2f}")
    print("-----------------------------------------")


def reporte_de_sueldos(lista):
    reporte = []
    for trabajador in lista:
        sueldo_bruto = trabajador["sueldo"]
        afp = int(sueldo_bruto * 0.12)
        salud = int (sueldo_bruto * 0.7)
        sueldo_liquido =sueldo_bruto - afp - salud
        agregar = {"nombre":trabajador ["nombre"],
        "sueldo_bruto": sueldo_bruto,
        "afp":afp,
        "salud":salud,
        "sueldo_liquido":sueldo_liquido
        }

        reporte.append(agregar)
    nombre_campos = ["nombre","sueldo_bruto","afp","salud","sueldo_liquido"]
    with open ('Reporte_Sueldos.csv','w', newline = "")as archivo:
        escritor= csv.DictWriter(archivo,fieldnames = nombre_campos)
        escritor.writeheader()
        escritor.writerows(reporte)