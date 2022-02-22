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