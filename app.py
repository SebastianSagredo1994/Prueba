from funse import asignarSueldos, menu,clasificar_empleados, estadisticas , reporte_de_sueldos
op=0
lista_de_empleados = []
while True:

    op=menu()
    if op ==1:
        asignarSueldos(lista_de_empleados)
    elif op==2:
        clasificar_empleados(lista_de_empleados)
    elif op == 3:
        estadisticas(lista_de_empleados)
    elif op == 4:
        reporte_de_sueldos(lista_de_empleados)
    elif op == 5:
        print("adios")
        print("finalizando programa")
        print("creado por sebastian")
        break