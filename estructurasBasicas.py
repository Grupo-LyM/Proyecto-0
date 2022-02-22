from alfabeto import alfabeto

#Validacion de las expresiones más básicas


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
        
    return True
#Valida si es una palabra revisando sus caracteres si encuentra que algun caracter
#no es letra retorna False si todos son letras true
def validarNombre(pal:str)->bool:
    
    for car in pal:
        if ((validarLetra(car) == False) and (validarDigito(car) == False)) :
            return False
        
    return True
