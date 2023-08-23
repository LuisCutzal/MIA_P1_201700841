import ply.yacc as sintactico
import ply.lex as lexico
from ejecutarexecute import comandoExecute
from mkdisk import *

palabrasReservadas = {"execute":"EXECUTE",
                      "mkdisk": "MKDISK",
                      "path": "PATH",
                      "size": "SIZE",
                      "unit": "UNIT",
                      "fit": "FIT"}
tokens = ["ID",
          "STRING",
          "NUMEROS",
          "COMENTARIOS",
          "GUION",
          "IGUAL",
          "VALORDEPATH",
          "NOMBREARCHIVO"]+list(palabrasReservadas.values())


#ahora reconocemos los tokens que vamos a utilizar
t_GUION = r"-"   #como solo es un caracter se hace de esta forma
t_IGUAL = r"="   #como solo es un caracter se hace de esta forma

#ahora numeros 
def t_NUMEROS(t):
    r"-?\d+"
    return t

def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]
    return t

def t_COMENTARIOS(t):
    r'\#.*' #con el punto le decimos que no importa lo que venga
    t.value = t.value[1:-1]
    return t

def t_VALORDEPATH(t): #solo es la ruta aun no esta el archivo
    r'\/[a-zA-Z0-9_\/]*\/'
    return t


def t_NOMBREARCHIVO(t):
    r'[a-zA-Z0-9_]+\.(adsj|dsk)' 
    return t

def t_ID(t):
    r"[a-zA-Z][a-zA-Z]*"
    #aca se deben de reconocer las palabras reservadas
    t.type = palabrasReservadas.get(t.value.lower(),"ID")
    return t

t_ignore = " \t\r"

def t_nuevalinea(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print(f'Error Lexico:'+t.value[0]+' en la linea: '+str(t.lineno) +' en la columna: '+str(find_column(input, t)))
    t.lexer.skip(1)

def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos)+1
    return (token.lexpos - line_start) + 1


#comienza lo sintactico


def p_inicio(t): 
    '''inicio : instrucciones'''
    t[0] = t[1]
    
def p_instrucciones(t):
    '''instrucciones : instrucciones instruccion'''
    if t[2] != "":
        t[1].append(t[2])
    t[0] = t[1]

def p_instrucciones_instruccion(t):
    '''instrucciones : instruccion'''
    if t[1] == "":
        t[0] = []
    else:
        t[0] = [t[1]]

def p_instruccion(t):
    '''instruccion : comandoexecute
                   | comandomkdisk
                   | comentarios'''
    t[0] = t[1]



def p_comandoexecute(t):
    '''comandoexecute : EXECUTE GUION PATH IGUAL VALORDEPATH NOMBREARCHIVO'''
    t[0] = comandoExecute(t[5],t[6]).ejecutar()
    
def p_comandomkdisk(t):
    '''comandomkdisk : MKDISK listaparametros_mkdisk'''
    MKDISK(t[2]).ejecutar()
    t[0]= ''
    
def p_listaparametros_mkdisk(t):
    '''listaparametros_mkdisk : listaparametros_mkdisk parametromkdisk
                              | parametromkdisk'''
    if len(t) == 3:
        t[1].append(t[2])
        t[0] = t[1]
    else:
        t[0] = [t[1]]
                         

def p_parametromkdisk(t):
    '''parametromkdisk : GUION parametropath
                       | GUION parametrosize
                       | GUION parametrounit
                       | GUION parametrofit'''
    t[0] = t[2]

def p_parametropath(t):
    '''parametropath : PATH IGUAL VALORDEPATH NOMBREARCHIVO'''
    t[0] = {"rutaArchivo" : t[3],
            "nombrearchivo": t[4]}

def p_parametrosize(t):
    '''parametrosize : SIZE IGUAL NUMEROS'''
    t[0] = {"valorsize" : t[3]}
    
def p_parametrounit(t):
    '''parametrounit : UNIT IGUAL ID'''
    t[0] = {"valorunit" : t[3]}
    
def p_parametrofit(t):
    '''parametrofit : FIT IGUAL ID'''
    t[0] = {"valorfit" : t[3]}

def p_comentarios(t):
    '''comentarios : COMENTARIOS'''
    print("#"+t[1])
    t[0] = ""


def iniciarAnalisis(comando):
    global input
    input = comando
    lex = lexico.lex()
    parser = sintactico.yacc()
    salida = parser.parse(comando)
    if salida == None:
        return ""
    elif salida == []:
        return ""
    else: return salida[0]
