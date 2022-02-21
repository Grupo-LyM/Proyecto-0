


from ssl import DefaultVerifyPaths

from numpy import true_divide


def menu():
    print("Bienvenido a el analizador.")
    ruta = input("Escriba la ruta ESPECIFICA del archivo :")
    archivo = open(str(ruta),"r")
    lineas = archivo.readlines()
    archivo.close()

    print(lineas)

menu()

digitos = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
letras = ["_","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G" , "H", "I", "J", "K", "L", "M", "N" ,"O", "P", "Q", "R", "S" , "T", "U", "V" , "W", "X", "Y" , "Z" , "ñ", "Ñ"]
#Constantes
cardinales = [":north" , ":south", ":east" , ":west"]
giro = [":front" ,":back",  ":left" , ":right",":around"]
par1="("
par2 =")"
palabras = ["defvar", "=" , "move" , "turn" , "put" , "pick" , "move-dir" , "run-dirs" , "move-face" , "skip"]
BalChips =["Balloons" , "Chips"]
condiciones = ["facing-p","can-put-p","can-pick-p","can-move-p","not"]
estructurasDeControl = ["loop","repeat","defun", "if"]
espacio = [" "]

alfabeto = {"digitos":digitos,
            "letras":letras,
            "cardinales":cardinales,
            "giro":giro,
            "par1":par1,
            "par2":par2,
            "palabras":palabras,
            "BalChips":BalChips,
            "estructurasDeControl":estructurasDeControl,
            "condiciones":condiciones,
            "espacio":espacio}


tokenIgnorar = "\n"
#Parser general: Iterar sobre lista que brinda el lineRead
#Guardar nombres de variables en lista para revisar cuando tenga nombres de variables
#Guardar nombres de parametros para revisar en la funcion

#Validacion de las expresiones más básicas

"""La validacion se genera 
true: es valido
false: no es valido-> generar error"""

#Valida una letra si esta en el diccionario de letras
def validarLetra(l:str)-> bool:
    if l in alfabeto["letras"]:
        return True
    else: 
        return False

#Valida si un digito esta en el diccionario digitos
def validarDigito(d:str)-> bool:
    if d in alfabeto["digitos"]:
        return True
    else: 
        return False
#Valida si es un número revisando sus digitos si encuentra que algun caracter
#no es digito retorna Flase si todos son digitos true
def validarNumero(num:str)->bool:
    
    for dig in num:
        if validarDigito(dig) == False:
            return False
        else: 
            pass
    return True
#Valida si es una palabra revisando sus caracteres si encuentra que algun caracter
#no es letra retorna False si todos son letras true
def validarNombre(pal:str)->bool:
    
    for car in pal:
        if ((validarLetra(car) == False) and (validarDigito(car) == False)) :
            return False
        else: 
            pass
    return True



#Validacion de combinaciones
#Validacion de nombre seguido de numero
def validarCombNombre_Num(comb:str)->bool:
    
    #Validacion que existe un espacio en el comando division de comando en dos
    spaceSplit = comb.split(" ")
    if (len(spaceSplit)==2):
        #Valida si lo de la izquierda es nombre y si lo derecha es numero
        val1 =validarNombre(spaceSplit[0])
        val2 = validarNumero(spaceSplit[1])
        #Valida si lo de la izquierda es nombre y si lo derecha es numero si lo es True
        if (val1 ==True) and (val2==True):
            return True
        else: 
            return False

    else: 
        return False

print("Prueba name num")
print (validarCombNombre_Num("3231Jeeez23414 43435"))
#Funciona

#Validacion de nombre o numero
def validarCombNombre_O_Num(comb:str)->bool:
    
    val1 =validarNombre(comb)
    val2 = validarNumero(comb)
    if (val1==True) or (val2 == True):
        return True
    else: 
        return False

print("Prueba name o num")
print (validarCombNombre_O_Num("324HDEODL"))
#Funciona

#Validacion Ballons o chips
def validarBal_O_Chips(comb:str)->bool:

    if comb in alfabeto[BalChips]:
        return True
    else: 
        return False

#giro = [":front" ,":back",  ":left" , ":right",":around"]

#Validacion left right around
def validarLe_Ri_Ar(comb:str)->bool:
    #   ojo revisar el slice
    if comb in alfabeto[giro[2:]]:
        return True
    else:
        return False

#Validacion front back right left
def validarFr_Ba_Ri_Le(comb:str)->bool:
    if comb in alfabeto[giro[:4]]:
        return True
    else:
        return False

#Validacion Bal/Chips name/num
##Pensar si meter aqui o en validacion comando
def validacionBC_NamNum(comb:str)->bool:
    #Validacion que existe un espacio en el comando division de comando en dos
    spaceSplit = comb.split(" ")
    if (len(spaceSplit)==2):
        #Valida si lo de la izquierda es Bal/Chips y si derecha es Nom/Num
        val1 =validarBal_O_Chips(spaceSplit[0])
        val2 = validarCombNombre_O_Num(spaceSplit[1])
        #Valida si lo de la izquierda esBal/CVhips y si lo derecha es Nom/Num si lo es True
        if (val1 ==True) and (val2==True):
            return True
        else: 
            return False

    else: 
        return False




def validarCombinaciones(comb:str):

    combinaciones=comb.split(alfabeto["espacio"])

    

#validacion cardinales
def validarCardinales(card:str):
    if card in alfabeto["cardinales"]:
        return True
    else:
        return False



#Validacion de comandos
def validarComando(comando:str):
    #Validacion de parentesis
    if (comando[0] is alfabeto[par1]) and (comando[-1]is alfabeto[par2]):
        #Codigo comandos
        a=1
    else: 
        return False

