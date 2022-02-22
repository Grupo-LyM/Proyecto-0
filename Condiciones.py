from alfabeto import alfabeto
from combinaciones import validarCardinales
from combinaciones import validarCombBC_NamNum

#Validacion de condiciones


#Traducciones individuales
def validarFacing_p(list_condicion)->bool:
    if list_condicion[0]==alfabeto["condiciones"][0]:
    # Revisa si lo siguiente es cardinal
        val1= validarCardinales(list_condicion[1])
        if (val1==True):
            return True
        else: 
            return False
    else:
        return False

def validarcan_put_p(list_condicion)->bool:
    if list_condicion[0]==alfabeto["condiciones"][1]:
    # Revisa si lo siguiente es cardinal
        format = list_condicion[1].replace(" ","")+" "+list_condicion[2].replace(" ","")
        val1= validarCombBC_NamNum(format)
        if (val1==True):
            return True
        else: 
            return False
    else:
        return False
def validarcan_pick_p(list_condicion)->bool:
    if list_condicion[0]==alfabeto["condiciones"][2]:
    # Revisa si lo siguiente es Bal/ chip cardinal
        format = list_condicion[1].replace(" ","")+" "+list_condicion[2].replace(" ","")
        val1= validarCombBC_NamNum(format)
        if (val1==True):
            return True
        else: 
            return False
    else:
        return False

def validarcan_move_p(list_condicion)->bool:
    if list_condicion[0]==alfabeto["condiciones"][3]:
    # Revisa si lo siguiente es Bal/ chip cardinal
        
        val1= validarCardinales(list_condicion[1])
        if (val1==True):
            return True
        else: 
            return False
    else:
        return False
def validarnot(list_condicion)->bool:
    if list_condicion[0]==alfabeto["condiciones"][4]:
        list_condicion.remove(list_condicion[0])
        elemC=list_condicion
        formatC = ""
        i=0
        for e in elemC: 
            if i ==len(elemC)-1:
                formatC+=e
            else: 
                formatC+=(e)+" "
            i+=1
        formatC+=""
    # Revisa si lo siguiente es cardinal
        val1= validarCondicion(formatC)
        if (val1==True):
            return True
        else: 
            return False
    else:
        return False

#Validacion junto con parentesis
def validarCondicion(condicion:str):

    ok=True
    #Validacion de parentesis de abrir y cerrar
    if (condicion[0] is alfabeto["par1"]) and (condicion[-1]is alfabeto["par2"]):
        
        #Se eliminan los paréntesis de la instruccion
        condicion = condicion[1:] 
        condicion = condicion[:len(condicion)-1]
        
        print(condicion)
        #Se divide la parte interna por " "-> [palabra,combinacion]
        lst_condicion = condicion.split(" ")
        

        if  len(lst_condicion)==2:

            #Facing_p
            cond1=validarFacing_p(lst_condicion)
            if cond1==True:
                print("Si")
                return True
            else:
                ok=False
            #can_move_p
            cond2=validarcan_move_p(lst_condicion)
            if cond2==True:
                print("Si")
                return True
            else:
                ok=False

            

        if  len(lst_condicion)==3:
            cond4=validarcan_put_p(lst_condicion)
            if cond4==True:
                print("Si")
                return True
            else:
                ok=False

            cond5=validarcan_pick_p(lst_condicion)
            if cond5==True:
                print("Si")
                return True
            else:
                ok=False
        ok=False
        if  len(lst_condicion)>=2:

            cond3=validarnot(lst_condicion)
            
                
            if cond3==True:
                print("Si")
                return True
            else:
                ok=False

    else: 
        ok=False
    return ok
