from alfabeto import alfabeto
from estructurasBasicas import validarNombre
from combinaciones import validarCombNombre_O_Num
from estructurasRecursivas import partirExpresiones
from Condiciones import validarCondicion
from estructurasRecursivas import validarBloque

##Estructuras de Control
def validarCondicionBloqueBloque(string:str):
    #Valida Condiciones Bloques
    lst_if = partirExpresiones(string)
    
    if len(lst_if) == 3: 
        val1 = validarCondicion(lst_if[0])
        val2 = validarBloque(lst_if[1])
        val3 = validarBloque(lst_if[2])
        if val1 and val2 and val3:
            return True
        else: 
            return False
    else: 
        return False
    
def validarCondicionBloque(string:str):
    #Valida Condiciones Bloques
    lst_if = partirExpresiones(string)
    
    if len(lst_if) == 2: 
        val1 = validarCondicion(lst_if[0])
        val2 = validarBloque(lst_if[1])
        
        if val1 and val2:
            return True
        else: 
            return False
    else: 
        return False    

def validarNomNum_Bl(string:str):
    lst_if = partirExpresiones(string)
    #Valida nom/num Bloques
    if len(lst_if) == 2: 
        val1 = validarCombNombre_O_Num(lst_if[0])
        val2 = validarBloque(lst_if[1])
        
        if val1 and val2:
            return True
        else: 
            return False
    else: 
        return False  
    
def validarNomParBloque(string):
    lst_if = partirExpresiones(string)
    #Valida nom/num Bloques
    if len(lst_if) == 3: 
        val1 = validarCombNombre_O_Num(lst_if[0])
        val2 = validarParametros(lst_if[1])
        val3=validarBloque(lst_if[2])
        
        if val1 and val2 and val3:
            return True
        else: 
            return False
    else: 
        return False



def validarParametros(lst:str):
     #Validacion de parentesis de abrir y cerrar
    if (lst[0] is alfabeto["par1"]) and (lst[-1]is alfabeto["par2"]):
        lst = lst.replace(lst[0],"")
        lst = lst.replace(lst[-1],"")
        #Se divide la parte interna por " "-> [dir1,...,dirn]
        list_dir = lst.split(" ")
        print(lst)
        for dir in  list_dir:
            val_dir = validarNombre(dir)
            if val_dir==False:
                return False
        return True   
    else:
        return False


def validarIf(est:str):
    
    #Validacion de parentesis de abrir y cerrar
    if (est[0] is alfabeto["par1"]) and (est[-1]is alfabeto["par2"]):
         #Se eliminan los paréntesis de la instruccion
        est = est[1:] 
        est = est[:len(est)-1]
        print(est)
        #Se divide la parte interna por " "-> [palabra,combinacion]
        palabra= est[0]+est[1]
        
        est = est[3:]
        print(est)
        if palabra ==alfabeto["estructurasDeControl"][3]:

            val = validarCondicionBloqueBloque(est)
            if val:
                return True
            else:
                return False
        else: 
            return False
    else: 
        return False
#print("ifff")
#print(validarIf("(if (can-move-p :north) ((move name) (turn D3d)) (move n))"))
#print("ifff")
def validarLoop(est:str):
    #Validacion de parentesis de abrir y cerrar
    if (est[0] is alfabeto["par1"]) and (est[-1]is alfabeto["par2"]):
         #Se eliminan los paréntesis de la instruccion
        est = est[1:] 
        est = est[:len(est)-1]
        #Se divide la parte interna por " "-> [palabra,combinacion]
        palabra= est[0]+est[1]+est[2]+est[3]
        
        est = est[5:]
        
        if palabra ==alfabeto["estructurasDeControl"][0]:

            val1 = validarCondicionBloque(est)
            
            if val1:
                return True
            else:
                return False
        else: 
            return False
    else: 
        return False

def validarRepeat(est:str):
    #Validacion de parentesis de abrir y cerrar
    if (est[0] is alfabeto["par1"]) and (est[-1]is alfabeto["par2"]):
         #Se eliminan los paréntesis de la instruccion
        est = est[1:] 
        est = est[:len(est)-1]
        #Se divide la parte interna por " "-> [palabra,combinacion]
        palabra= est[0]+est[1]+est[2]+est[3]+est[4]+est[5]
        
        est = est[7:]
        
        if palabra[0] ==alfabeto["estructurasDeControl"][1]:

            val1 = validarNomNum_Bl(est)
            
            if val1 :
                return True
            else:
                return False
        else: 
            return False
            

def validardeffuncion(est:str):
    #Validacion de parentesis de abrir y cerrar
    if (est[0] is alfabeto["par1"]) and (est[-1]is alfabeto["par2"]):
         #Se eliminan los paréntesis de la instruccion
        est = est[1:] 
        est = est[:len(est)-1]
        #Se divide la parte interna por " "-> [palabra,combinacion]
        palabra= est[0]+est[1]+est[2]+est[3]+est[4]
        
        est = est[6:]
        
        if palabra==alfabeto["estructurasDeControl"][2]:

            val1 = validarNomParBloque(est)

            if val1:
                return True
            else:
                return False
        else: 
            return False


def validarEstructura(comando:str):

    if (comando[0] is alfabeto["par1"]) and (comando[-1]is alfabeto["par2"]):
            #Se eliminan los paréntesis de la instruccion
            comando = comando[1:] 
            comando = comando[:len(comando)-1]
            
            val1 = validarIf(comando)
            val2 = validarLoop(comando)
            val3 = validarRepeat(comando)
            val4 = validardeffuncion(comando)
            if val1 or val2 or val3 or val4:
                return True
            else: 
                return False

    else: 
        return False