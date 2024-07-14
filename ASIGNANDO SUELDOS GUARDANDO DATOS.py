
import random
import math
import csv

trabajadores = [
    {"nombre": "Juan Pérez     ", "cargo": "Consultor TI    ", "sueldo": 0},
    {"nombre": "María García   ", "cargo": "Analista        ", "sueldo": 0},
    {"nombre": "Carlos López   ", "cargo": "Programador     ", "sueldo": 0},
    {"nombre": "Ana Martínez   ", "cargo": "Jefe de Proyecto", "sueldo": 0},
    {"nombre": "Pedro Rodríguez", "cargo": "Consultor TI    ", "sueldo": 0},
    {"nombre": "Laura Hernández", "cargo": "Analista        ", "sueldo": 0},
    {"nombre": "Miguel Sánchez ", "cargo": "Programador     ", "sueldo": 0},
    {"nombre": "Isabel Gómez   ", "cargo": "Jefe de Proyecto", "sueldo": 0},
    {"nombre": "Francisco Díaz ", "cargo": "Consultor TI    ", "sueldo": 0},
    {"nombre": "Elena Fernández", "cargo": "Analista        ", "sueldo": 0}
]


def sueldos():

    print("\nSueldos asignados Aleatoriamente")
    print("\nTRABAJADOR:\tCARGO:\t\tSUELDO:")
    for trabajador in trabajadores:
        trabajador["sueldo"]= random.randint(600000, 2500000)
        print(f"{trabajador["nombre"]}\t{trabajador["cargo"]} ${trabajador['sueldo']}")

def clasificacion():

    sueldo_bajo=[]
    sueldo_medio=[]
    sueldo_alto=[]

    for trabajador in trabajadores:
        if trabajador["sueldo"]<=800000:
            sueldo_bajo.append(trabajador)
        elif 800000<=trabajador["sueldo"]<=2000000:
            sueldo_medio.append(trabajador)
        elif 2000000<=trabajador["sueldo"]<=2500000:
            sueldo_alto.append(trabajador)    

    print(f"\nTrabajador con sueldos menores a $ 800000: {len(sueldo_bajo)}")
    print("\nTRABAJADOR:\tCARGO:\t\tSUELDO:")
    for trabajador in sueldo_bajo:
        print(f"{trabajador["nombre"]}\t{trabajador["cargo"]} ${trabajador['sueldo']}")

    print(f"\nTrabajador con sueldos $ 800000 - $ 2000000: {len(sueldo_medio)}")
    print("\nTRABAJADOR:\tCARGO:\t\tSUELDO:")
    for trabajador in sueldo_medio:
        print(f"{trabajador["nombre"]}\t{trabajador["cargo"]} ${trabajador['sueldo']}")
    
    print(f"\nTrabajador con sueldos $ 2000000 - $ 2500000: {len(sueldo_alto)}")
    print("\nTRABAJADOR:\tCARGO:\t\tSUELDO:")
    for trabajador in sueldo_alto:
        print(f"{trabajador["nombre"]}\t{trabajador["cargo"]} ${trabajador['sueldo']}")

def estadisticas():

    sueldos=[trabajador["sueldo"] for trabajador in trabajadores]

    print(f"\nEl sueldo minimo es:{min(sueldos)}")
    print(f"El sueldo maximo es:{max(sueldos)}")
    print(f"El sueldo promedio es:{sum(sueldos)/len(sueldos):.2f}")
    print(f"la media geometrica es:{math.exp(sum(math.log(sueldo) for sueldo in sueldos) / len(sueldos)):.2f}")

def reporte():
    with open("reporte.csv", "w" , newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["nombre","cargo","sueldo base","Desc. Salud","Desc. AFP","sueldo liquido"])
    
        print("\nNombre:\t\tCargo:\t\tSueldo Base:\tDesc. Salud:\tDesc. AFP:\tSueldo Líquido:")
        for trabajador in trabajadores:
            sueldo = trabajador["sueldo"]
            descuento_salud = round(sueldo * 0.07)
            descuento_afp = round(sueldo * 0.12)
            sueldo_liquido = sueldo - descuento_salud - descuento_afp
            writer.writerow([trabajador["nombre"], trabajador["cargo"], sueldo, descuento_salud, descuento_afp, sueldo_liquido])
            print(f"{trabajador['nombre']}\t{trabajador['cargo']} ${sueldo}\t${descuento_salud:.2f}\t${descuento_afp:.2f} \t${sueldo_liquido:.2f}")

    print("\nSe ha generado el reporte de sueldos en 'reporte_sueldos.csv'")
  
def cargar():
    try:
        with open("reporte.csv", 'r',) as file:
            reader = csv.DictReader(file) # csv.DictReader para leer el archivo CSV. DictReader lee el archivo CSV y convierte cada fila en un diccionario donde las claves son los nombres de las columnas.
            global trabajadores
            trabajadores = [row for row in reader] #Se utiliza una lista por comprensión para convertir el objeto DictReader en una lista de diccionarios. Cada diccionario representa un departamento con las claves correspondientes a las columnas del CSV.
            print("\nNombre:\t\tCargo:\t\tSueldo Base:\tDesc. Salud:\tDesc. AFP:\tSueldo Líquido:")
            for trabajador in trabajadores:
                print(f"{trabajador['nombre']} {trabajador['cargo']} ${(trabajador['sueldo base'])}\t${(trabajador["Desc. Salud"])}\t\t${trabajador["Desc. AFP"]}\t\t${trabajador["sueldo liquido"]}")
        print("\nDatos cargados desde Departamentos.csv")
    except FileNotFoundError:
        print("\nEl archivo Departamentos.csv no existe.")

def salir():
    print("\nSaliendo del programa...")

def menu():
    while True:
        print("\nAsignacion de sueldos DUOC")
        print("1.Asignar sueldos aleatorios")
        print("2.Clasificar sueldos")
        print("3.Ver estadísticas")
        print("4.Generar reporte de sueldos")
        print("5.cargar reporte de sueldos")
        print("6.Salir del programa")
        opc=input("\nOPC: ")

        if opc=="1":
                sueldos()
        elif opc=="2":    
                clasificacion()
        elif opc=="3":    
                estadisticas()
        elif opc=="4":
                reporte()
        elif opc=="5":
                cargar()
        elif opc=="6":
                salir()   
                break
        else:
                print("Escoja una opcion correcta") 


if __name__=="__main__":
    menu()