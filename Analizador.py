def menu():
    print("Bienvenido a el analisador.")
    ruta = input("Escriba la ruta ESPECIFICA del archivo :")
    archivo = open(str(ruta),"r")
    lineas = archivo.readlines()
    archivo.close()

    print(lineas)

menu()
