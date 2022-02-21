from copyreg import pickle


def menu():
    print("Bienvenido a el analisador.")
    ruta = input("Escriba la ruta ESPECIFICA del archivo :")
    archivo = open(str(ruta),"r")
    lineas = archivo.readlines()
    archivo.close()

    print(lineas)

menu()

digitos = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G" , "H", "I", "J", "K", "L", "M", "N" ,"O", "P", "Q", "R", "S" , "T", "U", "V" , "W", "X", "Y" , "Z" , "ñ", "Ñ"]
cardinales = [":north" , ":south", ":east" , ":west"]
giro = [":front" ,":back", ":around", ":left" , ":right"]
palabras = ["(" , ")" , "defvar", "=" , "move" , "turn" , "put" , "pick" , "Balloons" , "Chips" , "move-dir" , "run-dirs" , "move-face" , "skip"]
condiciones = ["facing-p","can-put-p","can-pick-p","can-move-p","not"]
estructurasDeControl = ["loop","repeat","defun", "if"]
especial = [" "]

alfabeto = {"digitos":digitos, "letras":letras, "cardinales":cardinales, "giro":giro, "palabras":palabras, "condiciones":condiciones, "estructurasDeControl":estructurasDeControl, "especial":especial}

