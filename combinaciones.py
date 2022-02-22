from Analizador import alfabeto
from estructurasBasicas import validarNombre
from estructurasBasicas import validarNumero
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
"""
print("Prueba name num")
print (validarCombNombre_Num("3231Jeeez23414 43435"))
"""
#Funciona

#Validacion de nombre o numero
def validarCombNombre_O_Num(comb:str)->bool:
    
    val1 =validarNombre(comb)
    val2 = validarNumero(comb)
    if (val1==True) or (val2 == True):
        return True
    else: 
        return False
"""
print("Prueba name o num")
print (validarCombNombre_O_Num("324HDEODL"))
"""
#Funciona

#Validacion Ballons o chips
def validarCombBal_O_Chips(comb:str)->bool:

    if comb in alfabeto["BalChips"]:
        return True
    else: 
        return False

#Estructura del alfabeto["giro"]
#giro = [":front" ,":back",  ":left" , ":right",":around"]

#Validacion left/right/around
def validarCombLe_Ri_Ar(comb:str)->bool:
    #   ojo revisar el slice
    if comb in alfabeto["giro"][2:]:
        return True
    else:
        return False

#Validacion front/back/right/left
def validarCombFr_Ba_Ri_Le(comb:str)->bool:
    if comb in alfabeto["giro"][:4]:
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
    if (lst[0] is alfabeto["par1"]) and (lst[-1]is alfabeto["par2"]):
        lst = lst.replace(lst[0],"")
        lst = lst.replace(lst[-1],"")
        #Se divide la parte interna por " "-> [dir1,...,dirn]
        list_dir = lst.split(" ")
        print(lst)
        for dir in  list_dir:
            
            val_dir = validarCombFr_Ba_Ri_Le(dir)
            if val_dir==False:
                return False
        return True   
    else:
        return False
    