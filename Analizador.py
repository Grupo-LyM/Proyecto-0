#from estructurasRecursivas import partirExpresiones


def listaInstrucciones():
    print("Bienvenido al analizador.")
    ruta = input("Escriba la ruta ESPECIFICA del archivo :")
    archivo = open(str(ruta),"r")
    hayLinea = True
 
    abiertos=0
    cerrados=0
    elemento_i=""
    lst=[]
    i=0
    while hayLinea:
        
        linea = archivo.readline()
        

        if linea:
            
            for s in linea: 
                if abiertos!=cerrados or(abiertos==0 and cerrados==0):

                    if s == "(":
                        abiertos+=1
                    if s ==")":
                        cerrados+=1
                    elemento_i+=s
                    
                    elemento_i=elemento_i.replace("\n","")

                    if i ==(len(linea)-1):
                        if abiertos==cerrados:
                            lst.append(elemento_i)
                
                else: 
                    lst.append(elemento_i)
                    elemento_i=""
                    abiertos=0
                    cerrados=0
                i+=1
        else:
            hayLinea=False

    archivo.close() 
    return lst

lstInstrucciones= print(listaInstrucciones())



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


#####Pruebas
def partir(comando:str)->bool:

    
    if (comando[0] is alfabeto["par1"]) and (comando[-1]is alfabeto["par2"]):
        
       print("Tiene ambos parentesis")
        
    else: 
        print("bla bla bla")
"""
def probarcomandos():
    print("Vamooos")
    for e in lineas:
        
        e = e.replace("\n","")
        print("yaaaaa")
        print(validarCondicion(e))
        

probarcomandos()
"""
#De este código funciona perfectamente la validacion de comandos, nombres y estructuras básicas
#las estruturas presentan inconvenientes en la recursion para la validacion



