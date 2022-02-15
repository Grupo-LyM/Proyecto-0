def menu():
    print("Bienvenido a el analisador.")
    ruta = input("\n Escriba la ruta del archivo txt del cual quieras conocer si es correcto o no ( de la forma C:\Users\elfue\Documents\Proyecto 0 LyM\ejemplo.txt ): ")
    archivo = open(ruta, "r")
    lineas = archivo.readlines()
    archivo.close()

