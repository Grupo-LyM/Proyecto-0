

from numpy import true_divide


def menu():
    print("Bienvenido a el analizador.")
    ruta = input("Escriba la ruta ESPECIFICA del archivo :")
    archivo = open(str(ruta),"r")
    lineas = archivo.readlines()
    archivo.close()
    return lineas

lineas = menu()

digitos = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
letras = ["_","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G" , "H", "I", "J", "K", "L", "M", "N" ,"O", "P", "Q", "R", "S" , "T", "U", "V" , "W", "X", "Y" , "Z" , "ñ", "Ñ"]
#Constantes
cardinales = [":north" , ":south", ":east" , ":west"]
giro = [":front" ,":back",  ":left" , ":right",":around"]
par1="("
par2 =")"
palabras = ["defvar", "=" , "move" , "turn" ,"face", "put" , "pick" , "move-dir" , "run-dirs" , "move-face" , "skip"]
BalChips =["Balloons" , "Chips"]
condiciones = ["facing-p","can-put-p","can-pick-p","can-move-p","not"]
estructurasDeControl = ["loop","repeat","defun", "if"]
espacio = [" "]

alfabeto = {"digitos":digitos,
            "letras":letras,
            "cardinales":cardinales,
            "giro":giro,
            "par1":"(",
            "par2":")",
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

#Reconocimiento de bloques
def reconocerBloques():
    size = len(lineas)
    i = 0

    bloques = []
    visitados = []
    while i <= size:
        if i not in visitados:
            line = lineas[i]
            numApertura = 0
            numCierre = 0
            numApertura, numCierre = contarParentesis(line, numApertura, numCierre)
            block = []
            block.append(line)
            visitados.append(i)

            if numApertura != numCierre:
                while numApertura != numCierre:
                    i += 1
                    linean = lineas[i]
                    numApertura, numCierre = contarParentesis(linean, numApertura, numCierre)
                    block.append(linean)
                    visitados.append(i)
            
        else:
            pass
        bloques.append(block)
    
    return bloques

        
        

def contarParentesis(line:str, numApertura:int, numCierre:int):
    for ele in line:
        if ele == "(":
            numApertura += 1
        elif ele == ")":
            numCierre += 1
    return numApertura, numCierre

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



"""Validacion de combinaciones"""
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
def validarCombBal_O_Chips(comb:str)->bool:

    if comb in alfabeto[BalChips]:
        return True
    else: 
        return False

#Estructura del alfabeto["giro"]
#giro = [":front" ,":back",  ":left" , ":right",":around"]

#Validacion left/right/around
def validarCombLe_Ri_Ar(comb:str)->bool:
    #   ojo revisar el slice
    if comb in alfabeto[giro[2:]]:
        return True
    else:
        return False

#Validacion front/back/right/left
def validarCombFr_Ba_Ri_Le(comb:str)->bool:
    if comb in alfabeto[giro[:4]]:
        return True
    else:
        return False

#Validacion Bal/Chips name/num

def validarCombBC_NamNum(comb:str)->bool:
    #Validacion que existe un espacio en el comando division de comando en dos
    spaceSplit = comb.split(" ")
    if (len(spaceSplit)==2):
        #Valida si lo de la izquierda es Bal/Chips y si derecha es Nom/Num
        val1 =validarCombBal_O_Chips(spaceSplit[0])
        val2 = validarCombNombre_O_Num(spaceSplit[1])
        #Valida si lo de la izquierda esBal/CVhips y si lo derecha es Nom/Num si lo es True
        if (val1 ==True) and (val2==True):
            return True
        else: 
            return False

    else: 
        return False
#Validacion nam/num" " front/right/left/back
def validarCombNomNum_FrRiLeBa(comb:str)->bool:
    #Validacion que existe un espacio en el comando division de comando en dos
    spaceSplit = comb.split(" ")
    if (len(spaceSplit)==2):
        #Valida si lo de la izquierda es Nom/Num y si derecha es FrRiLeBa
        val1 =validarCombNombre_O_Num(spaceSplit[0])
        val2 = validarCombFr_Ba_Ri_Le(spaceSplit[1])

#Valida si lo de la izquierda es Nom/Num y si derecha es FrRiLeBa si lo es True
        if (val1 ==True) and (val2==True):
                return True
        else: 
            return False

    else: 
        return False


#validacion cardinales
def validarCardinales(card:str):
    if card in alfabeto["cardinales"]:
        return True
    else:
        return False

#Validacion si es Nom/num" "cardinal
def validarCombNomNum_Cardinal(comb:str):
    spaceSplit = comb.split(" ")
    if (len(spaceSplit)==2):
        #Valida si lo de la izquierda es Nom/Num y si derecha es FrRiLeBa
        val1 =validarCombNombre_O_Num(spaceSplit[0])
        val2 = validarCardinales(spaceSplit[1])
#Valida si lo de la izquierda es Nom/Num y si derecha es FrRiLeBa si lo es True
        if (val1 ==True) and (val2==True):
                return True
        else: 
            return False

    else: 
        return False


#ListaDirecciones
def validarDs(lst:str):
    #Validacion de parentesis de abrir y cerrar
    if (lst[0] is alfabeto[par1]) and (lst[-1]is alfabeto[par2]):
        lst = lst.replace(lst[0],"")
        lst = lst.replace(lst[-1],"")
        #Se divide la parte interna por " "-> [dir1,...,dirn]
        list_dir = lst.split(" ")
        
        for dir in  list_dir:
            val_dir = validarCombFr_Ba_Ri_Le(dir)
            if val_dir==False:
                return False
        return True   


#Validacion de comandos

#Traducciones individuales

def validarSkip(list_comando:str)->bool:

    if list_comando[0]==alfabeto["palabras"][-1]:
        return True
    else: 
        return False

def validarDefvar(list_comando:str)->bool:
    if list_comando[0]==alfabeto["palabras"][0]:
        # Revisa si lo siguiente es nombre " " numero
        val1= validarCombNombre_Num(list_comando[1])
        if (val1==True):
            return True
        else: 
            return False

def validar_igual(list_comando:str)->bool:
    if list_comando[0]==alfabeto["palabras"][1]:
        # Revisa si lo siguiente es nombre " " numero
        val1= validarCombNombre_Num(list_comando[1])
        if (val1==True):
            return True
        else: 
            return False


def validarMove(list_comando:str)->bool:
    if list_comando[0]==alfabeto["palabras"][2]:
        # Revisa si lo siguiente es nombre o numero
        val1= validarCombNombre_O_Num(list_comando[1])
        if (val1==True):
            return True
        else: 
            return False

def validarTurn(list_comando:str)->bool:
    if list_comando[0]==alfabeto["palabras"][3]:
                # Revisa si lo siguiente es Left,right,Around
                val1= validarCombLe_Ri_Ar(list_comando[1])
                if (val1==True):
                    return True
                else: 
                    return False

def validarFace(list_comando:str)->bool:
    if list_comando[0]==alfabeto["palabras"][4]:
            # Revisa si lo siguiente es north, south, west,east
            val1= validarCardinales(list_comando[1])
            if (val1==True):
                return True
            else: 
                return False
def validarPut(list_comando:str)->bool:
    if list_comando[0]==alfabeto["palabras"][5]:
        # Revisa si lo siguiente es Ballons/Chips" "Nombre/Numero
        val1= validarCombBC_NamNum(list_comando[1])
        if (val1==True):
            return True
        else: 
            return False
    
def validarPick(list_comando:str)->bool:  
    if list_comando[0]==alfabeto["palabras"][6]:
                # Revisa si lo siguiente es Ballons/Chips" "Nombre/Numero
                val1= validarCombBC_NamNum(list_comando[1])
                if (val1==True):
                    return True
                else: 
                    return False


def validarMove_dir(list_comando:str)->bool:
    if list_comando[0]==alfabeto["palabras"][7]:
        # Revisa si lo siguiente es Ballons/Chips" "Nombre/Numero
        val1= validarCombNomNum_FrRiLeBa(list_comando[1])
        if (val1==True):
            return True
        else: 
            return False

def validarRun_dirs(list_comando:str)->bool:
    if list_comando[0]==alfabeto["palabras"][8]:
        # Revisa si lo siguiente es Ballons/Chips" "Nombre/Numero
        val1= validarDs(list_comando[1])
        if (val1==True):
            return True
        else: 
            return False
def validarMove_face(list_comando:str)->bool:

    if list_comando[0]==alfabeto["palabras"][9]:
        # Revisa si lo siguiente es Ballons/Chips" "Nombre/Numero
        val1= validarCombNomNum_Cardinal(list_comando[1])
        if (val1==True):
            return True
        else: 
            return False


#Validacion de todo tipo de comando 
def validarComando(comando:str):
   

    #Validacion de parentesis de abrir y cerrar
    if (comando[0] is alfabeto["par1"]) and (comando[-1]is alfabeto["par2"]):

        #Se eliminan los paréntesis de la instruccion
        comando = comando.replace(comando[0],"")
        comando = comando.replace(comando[-1],"")
        #Se divide la parte interna por " "-> [palabra,combinacion]
        list_comando = comando.split(" ")

        #Verificacion de listas de tamaño 1
        if len(list_comando)==1:
            #Verificar que sea skip
            validarSkip(list_comando)
            
        #Verificacion de listas de tamaño 2
        if len(list_comando)==2:
            #defvar
            validarDefvar(list_comando)
            # =
            validar_igual(list_comando)
            # move
            validarMove(list_comando)
            #turn
            validarTurn(list_comando)
            #face
            validarFace(list_comando)
            #put
            validarPut(list_comando)
            #pick
            validarPick(list_comando)
            #move-dir
            validarMove_dir(list_comando)
            #run-dirs
            validarRun_dirs(list_comando)
            #move-face
            validarMove_face(list_comando)   
    else: 
        return False

#Validacion de condiciones


#Validacion de estructura de control


#Traducciones individuales
def validarFacing_p(list_condicion)->bool:
    if list_condicion[0]==alfabeto["condiciones"][0]:
    # Revisa si lo siguiente es cardinal
        val1= validarCardinales(list_condicion[1])
        if (val1==True):
            return True
        else: 
            return False

#Validacion junto con parentesis
def validarCondicion(condicion:str):
   

    #Validacion de parentesis de abrir y cerrar
    if (condicion[0] is alfabeto["par1"]) and (condicion[-1]is alfabeto["par2"]):

        #Se eliminan los paréntesis de la instruccion
        condicion = condicion.replace(condicion[0],"")
        condicion = condicion.replace(condicion[-1],"")
        #Se divide la parte interna por " "-> [palabra,combinacion]
        list_condicion = condicion.split(" ")

        validarFacing_p(list_condicion)

#####Pruebas
bloques = reconocerBloques()
print(bloques)