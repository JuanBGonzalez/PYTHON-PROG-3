# Lista de super mercado,  Programa que

listaT = ("arroz", "leche", "tuna", "cereal", "jugo")
lista = []


def articulos():
    print("\nArticulos\n--------------------\n1.arroz\n2.leche\n3.tune\n4.cereal\n5.jugo")
    return


def agregar():
    caso = 0
    while caso != 6:
        try:
            articulos()
            print("escribe 6 para salir")
            caso = int(input("Artiulo agregado:"))
            if caso == 1:
                lista.append("arroz")
            elif caso == 2:
                lista.append("leche")
            elif caso == 3:
                lista.append("tuna")
            elif caso == 4:
                lista.append("cereal")
            elif caso == 5:
                lista.append("jugo")
            else:
                print("\nALGO VA MAL")
        except Exception:
            print("Eso no es valido")
            return


def ver():
    print(lista)
    return


def buscar():
    articulos()
    try:
        buscado = input("Digite el producto que desea buscar?:")
        for e in range(len(lista)):
            if lista[e] == buscado:
                print("\a\a\a--[Encontrado]--")
    except Exception:
        print("Algo va man buscando Intenta denuevo")
        return


def eliminar():
    print(lista)
    try:
        eliminado = input("Digite el producto que desea eliminar?")
        for i in range(len(lista)):
            if lista[i] == eliminado:
                del lista[i]
                print("\a\a\aeliminado")
    except Exception:
        print("Algo va mal eliminando, intenta denuevo")
    return


selec = 0
try:
    while selec != 5:
        print("\nSUPERMERCADOS REY\nSiempre frescoMenu\n-------------\n1.Agrega\n2.Ver\n3.buscar\n4.eliminar\n5.Salir")
        selec = int(input("Seleccione una opccion:"))
        if selec == 1:
            agregar()
        elif selec == 2:
            ver()
        elif selec == 3:
            buscar()
        elif selec == 4:
            eliminar()
except Exception:
    print("Algo va mal intentalo denuevo")
