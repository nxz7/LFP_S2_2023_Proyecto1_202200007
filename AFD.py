import json

def AFD(st_info):
    tokens = []             
    errores = []
    columna = 1              
    fila = 1                                               
    paso = ""               
    bolita_estado = 0


    
    operador = ["suma", "resta", "multiplicacion", "division", "potencia", "raiz", "inverso", "seno", "coseno","tangente", "mod"]
    
    valor = ["valor1", "valor2", "valor3", "valor4", "valor5", "valor6", "valor7"]
    
    reservadas = ["operaciones", "operacion", "configuraciones", "texto", "fondo", "fuente","forma"]

    i = 0 #para poder ver cada item   
    while i < len(st_info):

        if bolita_estado == 0:
            if st_info[i] == ",":
                tokens.append([st_info[i], "coma", fila, columna])
                paso = ""
                columna += 1

            elif st_info[i] == "{":
                tokens.append([st_info[i], "llave de abrir", fila, columna])
                paso = ""
                columna += 1

            elif st_info[i] == "}":
                tokens.append([st_info[i], "llave para cerrar", fila, columna])
                paso = ""
                columna += 1

            elif st_info[i] == "[":
                tokens.append([st_info[i], "corchete para abrir", fila, columna])
                paso = ""
                columna += 1

            elif st_info[i] == "]":
                tokens.append([st_info[i], "corchete para cerrar", fila, columna])
                paso = ""
                columna += 1

            elif st_info[i] == ":":
                tokens.append([st_info[i], "dos puntos :", fila, columna])
                paso = ""
                columna += 1


            elif st_info[i] == '"':
                bolita_estado = 2
                columna += 1


            elif st_info[i].isdigit():
                paso += st_info[i]
                bolita_estado = 1
                columna += 1


            elif st_info[i] == "\r":
                pass

            elif st_info[i] == "\n":
                columna = 1
                fila += 1
        
            elif st_info[i] == " ":
                columna += 1

            elif st_info[i] == "\t":
                columna += 1
        
            else:
                errores.append([st_info[i], fila, columna])
                paso = ""
                columna += 1

#VER LO DE LOS ERRORES Y UNIR LOS NUMEROS AUQNEU TENGAN PUNTO DECIMAL Y QUE DESPUES LE SIGAN NUMEROS 
        elif bolita_estado == 1:
            if st_info[i].isdigit():
                paso += st_info[i]   
                columna += 1

            elif st_info[i] == ".":
                paso += st_info[i]   #AQUI ES DONDE MIRA SI TIENE PUNTOS
                bolita_estado = 4
                columna += 1

            else:
                tokens.append([paso, "Numero", fila, columna])
                paso = ""       
                columna += 1
                i -= 1          
                bolita_estado = 0

        elif bolita_estado == 4:
            if st_info[i].isdigit():
                paso += st_info[i]
                bolita_estado = 5
                columna += 1
            
            else:
                errores.append([paso, fila, columna])
                paso = ""
                columna += 1
                bolita_estado = 0
#AGREGAR LOS NUMEROS DESPUES DEL PUNTO HACER EL  NUMERO COMPLETO
        elif bolita_estado == 5:
            if st_info[i].isdigit():
                paso += st_info[i]
                columna += 1
        
            else:
                tokens.append([paso, "Numero", fila, columna])
                paso = ""
                columna += 1
                i -= 1
                bolita_estado = 0

        elif bolita_estado == 2:
            if st_info[i] == '/' or st_info[i] == '\\':
                columna += 1

            elif st_info[i] == '"':

                if paso in reservadas:
                    tokens.append([paso, "Reservada", fila, columna])
                elif paso in operador:
                    tokens.append([paso, "Operador", fila, columna])
                elif paso in valor:
                    tokens.append([paso, "Valor", fila, columna])
                else:
                    tokens.append([paso, "Cadena", fila, columna])  
                paso = ""
                columna += 1
                bolita_estado = 0

            elif st_info[i] == "\n":
                errores.append([paso, fila, columna])
                paso = ""
                columna = 1
                fila += 1
                bolita_estado = 0

            else:
                paso += st_info[i]
                columna += 1     

        
        i += 1 #AUMENTA PARA QUE EL WHILE PASE AL OTRO CARACTER
#GUARDA TODA LA INF RECOPILADA EN UN ARRAYS DE UNA 
    resultado = [tokens, errores]
    return resultado

def imprimir_tokens(salida):
    print("TOKENS")
    print('*' * 53)
    print("{:<11} {:<19} {:<10} {:<15}".format("Lexema ", " Tipo", " Fila", "Columna"))
    print('*' * 53)
    for token in salida[0]:
        print("{:<11} {:<19} {:<10} {:<15}".format(token[0], token[1], token[2], token[3]))
    
#-------------------pruebas

entrada= open('prueba.json', 'r').read()

salida = AFD(entrada)

imprimir_tokens(salida)


error_data = []
error_number = 1

for error in salida[1]:
    error_item = {
        "No": error_number,
        "descripcion": {
            "lexema": error[0],
            "tipo": "error lexico",
            "columna": error[2],
            "fila": error[1]
        }
    }
    error_data.append(error_item)
    error_number += 1

error_json = {"errores": error_data}

with open("errores.json", "w") as json_file:
    json.dump(error_json, json_file, indent=4)

print("ERRORES")
for errores in salida[1]:
    print(errores)