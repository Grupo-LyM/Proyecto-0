from alfabeto import alfabeto
from comandos import validarComando
from estructurasControl import validarEstructura
import Analizador as a

#Elimina parentesis y envía string sin parentesis de lo contrario retorna false
def procesamientoParentesis(string:str):
    if (string[0] is alfabeto["par1"]) and (string[-1]is alfabeto["par2"]):
         #Se eliminan los paréntesis de la instruccion
        string= string[1:] 
        string = string[:len(string)-1]
        return string
    else: 
        return False



def partirExpresiones(expresion:str)->list:   

    abiertos=0
    cerrados=0
    elemento_i=""
    lst=[]
    i=0
    for s in expresion: 
        
        
        if abiertos!=cerrados or(abiertos==0 and cerrados==0):

            if s == "(":
                abiertos+=1
            if s ==")":
                cerrados+=1
            elemento_i+=s
            if i ==(len(expresion)-1):
                if abiertos==cerrados:
                    lst.append(elemento_i)
           
        else: 
            lst.append(elemento_i)
            elemento_i=""
            abiertos=0
            cerrados=0
        i+=1
    print(lst)

    return lst


#partirExpresiones("(defvar ertuy 35) (defvar hello 21324)")
##Instruccion
def validarInstruccion(instruccion):
    #Casos base son comandos o estructuras

    valCom= validarComando(instruccion)
    #
    if valCom==True: 
        return True
    valEstr=validarEstructura(instruccion)
    if valEstr==True: 
        return True
    
    else:
        lst_instrucciones = partirExpresiones(instruccion)
        print("lista")
        print(lst_instrucciones)
        if len(lst_instrucciones)>1:
            for ins in lst_instrucciones:
                val3= validarInstruccion(ins)
                if val3: 
                    return True
                else: 
                    return False
        else: 
            return False

    

print(validarInstruccion("(if (not blocked -p) (( move one ) (goend)) (skip)))"))

def validarBloque(bl):
    #Validacion de parentesis de abrir y cerrar
    ins=procesamientoParentesis(bl)

    if bl!= False: 
        val_instruccion= validarInstruccion(ins)
        if val_instruccion: 
            return True
        else: 
            return False
    else: 
        return False