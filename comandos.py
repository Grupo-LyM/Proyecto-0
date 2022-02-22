from Analizador import alfabeto
from combinaciones import validarCombNombre_Num
from combinaciones import validarCombNombre_O_Num
from combinaciones import validarCombLe_Ri_Ar
from combinaciones import validarCardinales
from combinaciones import validarCombBC_NamNum
from combinaciones import validarDs
from combinaciones import validarCombNomNum_FrRiLeBa
from combinaciones import validarCombNomNum_Cardinal
#Validacion de comandos

#Traducciones individuales

def validarSkip(list_comando:str)->bool:
    ok=True

    if list_comando[0]==alfabeto["palabras"][-1]:
        ok=True
    else: 
        ok=False
    return ok

def validarDefvar(list_comando:str)->bool:
    
    #Revision que sea palabra empiece por defVar
    if list_comando[0]==alfabeto["palabras"][0]:
        # Revisa si lo siguiente es nombre " " numero
        format = list_comando[1].replace(" ","")+" "+list_comando[2].replace(" ","")
        
        val1= validarCombNombre_Num(format)
        
        if (val1==False):
            return False
        else: 

            return True
    else: 
        return False
"""
car = ("(defvar 34234hel 2er3)")
print("Individual")
print(validarDefvar(car))
print("Acabo")
"""


def validar_igual(list_comando:str)->bool:
    if list_comando[0]==alfabeto["palabras"][1]:
        # Revisa si lo siguiente es nombre " " numero
        format = list_comando[1].replace(" ","")+" "+list_comando[2].replace(" ","")
        val1= validarCombNombre_Num(format)
        
        if (val1==False):
            return False
        else: 
            return True
    else: 
        return  False


def validarMove(list_comando:str)->bool:
    if list_comando[0]==alfabeto["palabras"][2]:
        # Revisa si lo siguiente es nombre o numero
        val1= validarCombNombre_O_Num(list_comando[1])
        if (val1==True):
            return True
        else: 
            return False
    else: 
        return  False

def validarTurn(list_comando:str)->bool:
    if list_comando[0]==alfabeto["palabras"][3]:
        # Revisa si lo siguiente es Left,right,Around
        val1= validarCombLe_Ri_Ar(list_comando[1])
        if (val1==True):
            return True
        else: 
            return False
    else: 
        return  False

def validarFace(list_comando:str)->bool:
    if list_comando[0]==alfabeto["palabras"][4]:
        # Revisa si lo siguiente es north, south, west,east
        val1= validarCardinales(list_comando[1])
        if (val1==True):
            return True
        else: 
            return False
    else: 
        return  False
def validarPut(list_comando:str)->bool:
    if list_comando[0]==alfabeto["palabras"][5]:
        # Revisa si lo siguiente es Ballons/Chips" "Nombre/Numero
        format = list_comando[1].replace(" ","")+" "+list_comando[2].replace(" ","")
        val1= validarCombBC_NamNum(format)
        if (val1==True):
            return True
        else: 
            return False
    else: 
        return  False
    
def validarPick(list_comando:str)->bool:  
    if list_comando[0]==alfabeto["palabras"][6]:
        # Revisa si lo siguiente es Ballons/Chips" "Nombre/Numero
        format = list_comando[1].replace(" ","")+" "+list_comando[2].replace(" ","")
        val1= validarCombBC_NamNum(format)
        if (val1==True):
            return True
        else: 
            return False
    else: 
        return  False


def validarMove_dir(list_comando:str)->bool:
    if list_comando[0]==alfabeto["palabras"][7]:
        # Revisa si lo siguiente es Ballons/Chips" "Nombre/Numero
        format = list_comando[1].replace(" ","")+" "+list_comando[2].replace(" ","")
        val1= validarCombNomNum_FrRiLeBa(format)
        if (val1==True):
            return True
        else: 
            return False
    else: 
        return  False

def validarRun_dirs(list_comando:str)->bool:
    if list_comando[0]==alfabeto["palabras"][8]:
        # Revisa si lo siguiente es lista Ds
        list_comando.remove(list_comando[0])
        elemDs=list_comando
        formatDs = ""
        i=0
        for e in elemDs: 
            if i ==len(elemDs)-1:
                formatDs+=e
            else: 
                formatDs+=(e)+" "
            i+=1
        formatDs+=""
      
        print(formatDs)
        val1= validarDs(formatDs)
        if (val1==True):
            return True
        else: 
            return False
    else: 
        return  False
def validarMove_face(list_comando:str)->bool:

    if list_comando[0]==alfabeto["palabras"][9]:
        # Revisa si lo siguiente es nom/num cardinal
        format = list_comando[1].replace(" ","")+" "+list_comando[2].replace(" ","")
        val1= validarCombNomNum_Cardinal(format)
        if (val1==True):
            return True
        else: 
            return False
    else: 
        return  False


#Validacion de todo tipo de comando 
def validarComando(comando:str):
   
    ok=True
    #Validacion de parentesis de abrir y cerrar
    if (comando[0] is alfabeto["par1"]) and (comando[-1]is alfabeto["par2"]):
        #Se eliminan los paréntesis de la instruccion
        comando = comando[1:] 
        comando = comando[:len(comando)-1]
        
        #Se divide la parte interna por " "-> [palabra,combinacion]
        list_comando = comando.split(" ")
        print("   Lista")
        print(list_comando)
        print("   parametro")
        #Si ya cumple una termina de lo contrario va validando las siguientes
        #Verificacion de lisstas de tamaño 1
        
        if len(list_comando)==1:
            #Verificar que sea skip
            valSkip= validarSkip(list_comando)
            if valSkip:
                print("Si")
                return True
            else:
                ok=False
       
        #Verificacion de listas de tamaño 2
        if len(list_comando)==2:
            
            # move
            valMove=validarMove(list_comando)
            if valMove==True:
                return True
            else:
                ok=False
            #turn
            
            valTurn= validarTurn(list_comando)
            if valTurn==True:
                return True
            else:
                ok=False
            #face
            valFace=validarFace(list_comando)
            if valFace==True:
                print("Si")
                return True
            else:
                ok=False
            
        #Verificacion de listas de tamaño 3
        if len(list_comando)==3:
            #defvar
            print("Validando defvar")
            valDefVar= validarDefvar(list_comando)
            
            if valDefVar==True:
                print("Si")
                return True
            else:
                ok=False
            # =
            print("Validando =")
            valIgual=validar_igual(list_comando)
            if valIgual==True:
                print("Si")
                return True
            else:
                ok=False
            
            #put
            print("Validando put")
            valPut=validarPut(list_comando)
            if valPut==True:
                print("Si")
                return True
            else:
                ok=False
            #pick
            valPick=validarPick(list_comando)
            if valPick==True:
                print("Si")
                return True
            else:
                ok=False
            #move-dir
            valMove_dir=validarMove_dir(list_comando)
            if valMove_dir==True:
                print("Si")
                return True
            else:
                ok=False
            
            #move-face
            valMove_face=validarMove_face(list_comando) 
            if valMove_face==True:
                print("Si")
                return True
            else:
                ok=False

        if len(list_comando)>=2:
            #run-dirs
            valRun_dirs=validarRun_dirs(list_comando)
            if valRun_dirs==True:
                print("Si")
                return True
            else:
                ok=False
        #Si no cumple los tamaños devuelve false
        ok=False
    else: 
        ok =False
    return ok