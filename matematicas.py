import math

import graphviz
from AFD import AFD

tokensL = []                 
errores = []
dot_file_name = "grafo.dot"                

def parser (st_info):
    global dot_file_name
    global tokensL
    
    #Genera los tokens
    respuesta = AFD(st_info)
    print("OPERACIONES REALIZADAS")
    tokensL = respuesta[0]               


#PILA / POP - > se le da vuelta
    tokensL.reverse()

    analisis_L()
    with open(dot_file_name, "a") as dot_file:
        dot_file.write(f'\n    }}')

    graph = graphviz.Source.from_file(dot_file_name)

    output_file_name = "grafo"
    graph.format = "png"
    graph.render(output_file_name, view=False)
    with open(dot_file_name, "r") as dot_file:
        lines = dot_file.readlines()

    with open(dot_file_name, "w") as dot_file:
        dot_file.write(lines[0])  

    print(f"El grafo esta listo bajo el nombre: '{output_file_name}'.")

def analisis_L():

    try:

        vt = tokensL.pop()                     
        if vt[1] != "llave de abrir":            
            errores.append([vt[0], "->" + vt[1], vt[2], vt[4]])
            return 
        
        print("Operaciones:")
        operaciones()

        vt = tokensL.pop()                   
        if vt[1] != "coma":           
            errores.append([vt[0], "->" + vt[1], vt[2], vt[4]])
            return 
        
        print("Configuraciones:")
#LEE LAS CONFIGURACIONES DEL GRAFO
        configuraciones()

        vt = tokensL.pop()                    
        if vt[1] != "llave para cerrar":         
            errores.append([vt[0], "->" + vt[1], vt[2], vt[4]])
            return 
        
        print("****************************¡¡listo!! ****************************")
        
    except Exception as e:
        print("Error: " + str(e))

def operaciones():

    try:

        vt = tokensL.pop()                     
        if vt[0] != "Operaciones":            
            errores.append([vt[0], "->" + vt[1], vt[2], vt[4]])
            return 
        

        vt = tokensL.pop()                   
        if vt[1] != "dos puntos :":           
            errores.append([vt[0], "->" + vt[1], vt[2], vt[4]])
            return 
        

        vt = tokensL.pop()                   
        if vt[1] != "corchete para abrir":           
            errores.append([vt[0], "->" + vt[1], vt[2], vt[4]])
            return 
        

        operacion()

        vt = tokensL.pop()                   
        if vt[1] != "corchete para cerrar":           
            errores.append([vt[0], "->" + vt[1], vt[2], vt[4]])
            return 
        
    except Exception as e:
        print("operaciones")
        print("Error: " + str(e))

def operacion():

    try:

        exp_a_operar()

        vt = tokensL[-1]
        if vt[1] != "coma":
            return
        
        tokensL.pop()        

        operacion()

    except Exception as e:
        print("operacion")
        print("Error: " + str(e))

def exp_a_operar():
    operador = ""
    valores = []
    resultado = 0

    try:
        vt = tokensL.pop()
        if vt[1] != "llave de abrir":
            errores.append([vt[0], "->" + vt[1], vt[2], vt[4]])
            return 0

        vt = tokensL.pop()
        if vt[0] != "operacion":
            errores.append([vt[0], "->" + vt[1], vt[2], vt[4]])
            return 0

        vt = tokensL.pop()
        if vt[1] != "dos puntos :":
            errores.append([vt[0], "->" + vt[1], vt[2], vt[4]])
            return

        vt = tokensL.pop()
        operador = vt[0]
        if vt[1] != "Operador":
            errores.append([vt[0], "->" + vt[1], vt[2], vt[4]])
            return 0

        vt = tokensL.pop()
        if vt[1] != "coma":
            errores.append([vt[0], "->" + vt[1], vt[2], vt[4]])
            return 0

        listanumeros(valores)

        vt = tokensL.pop()
        if vt[1] != "llave para cerrar":
            errores.append([vt[0], "->" + vt[1], vt[2], vt[4]])
            return 0

        if len(valores) == 0:
            print("Error - expresion")
            return 0

        # RECURSIVIDAD - CON LOS VALORES Y LAS OPERACIONES ANIDADAS

        if operador == "suma":
            for numero in valores:
                resultado += numero
            print(valores[0], "+", valores[1], "=", resultado, operador)
            with open(dot_file_name, "a") as dot_file:

                dot_file.write(f'\n    {resultado} [label="{resultado}- Suma"]')
                dot_file.write(f'\n    {valores[0]} [label="{valores[0]}"]')
                dot_file.write(f'\n    {valores[1]} [label="{valores[1]}"]')
                dot_file.write(f'\n    {resultado} -> {valores[0]}')
                dot_file.write(f'\n    {resultado} -> {valores[1]}')
            print("grafo creado")

        elif operador == "resta":
            resultado = valores[0]
            for numero in valores[1:]:
                resultado -= numero
            print(valores[0], "-", valores[1], "=", resultado, operador)
            with open(dot_file_name, "a") as dot_file:

                dot_file.write(f'\n    {resultado} [label="{resultado}- RESTA"]')
                dot_file.write(f'\n    {valores[0]} [label="{valores[0]}"]')
                dot_file.write(f'\n    {valores[1]} [label="{valores[1]}"]')
                dot_file.write(f'\n    {resultado} -> {valores[0]}')
                dot_file.write(f'\n    {resultado} -> {valores[1]}')
            print("grafo creado")

        elif operador == "multiplicacion":
            resultado = valores[0]
            for numero in valores[1:]:
                resultado = numero * resultado
            print(valores[0], "*", valores[1], "=", resultado, operador)
            with open(dot_file_name, "a") as dot_file:

                dot_file.write(f'\n    {resultado} [label="{resultado}- multiplicacion"]')
                dot_file.write(f'\n    {valores[0]} [label="{valores[0]}"]')
                dot_file.write(f'\n    {valores[1]} [label="{valores[1]}"]')
                dot_file.write(f'\n    {resultado} -> {valores[0]}')
                dot_file.write(f'\n    {resultado} -> {valores[1]}')
            print("grafo creado")

        elif operador == "division":
            try:
                if len(valores) > 2:
                    print("Error: solo dos numeros")
                else:
                    resultado = valores[0] / valores[1]
                    print(valores[0], "/", valores[1], "=", resultado, operador)
                    with open(dot_file_name, "a") as dot_file:
                        dot_file.write(f'\n    {resultado} [label="{resultado}- division"]')
                        dot_file.write(f'\n    {valores[0]} [label="{valores[0]}"]')
                        dot_file.write(f'\n    {valores[1]} [label="{valores[1]}"]')
                        dot_file.write(f'\n    {resultado} -> {valores[0]}')
                        dot_file.write(f'\n    {resultado} -> {valores[1]}')
                    print("grafo creado")
            except ZeroDivisionError:
                print("Error: IMPOSIBLE división por cero")
                resultado = 0

        elif operador == "potencia":
            if len(valores) != 2:
                print("Error: solo dos valores para la potencia")
            else:
                resultado = valores[0] ** valores[1]
                print(valores[0], "^", valores[1], "=", resultado, operador)
                with open(dot_file_name, "a") as dot_file:

                    dot_file.write(f'\n    {resultado} [label="{resultado}- potencia"]')
                    dot_file.write(f'\n    {valores[0]} [label="{valores[0]}"]')
                    dot_file.write(f'\n    {valores[1]} [label="{valores[1]}"]')
                    dot_file.write(f'\n    {resultado} -> {valores[0]}')
                    dot_file.write(f'\n    {resultado} -> {valores[1]}')
                print("grafo creado")

        elif operador == "raiz":
            if len(valores) != 1:
                print("Error: solo un valor")
            elif valores[0] < 0:
                print("Error: no número negativo")
            else:
                resultado = math.sqrt(valores[0])
                print("√", valores[0], "=", resultado, operador)
                with open(dot_file_name, "a") as dot_file:

                    dot_file.write(f'\n    {resultado} [label="{resultado}- raiz"]')
                    dot_file.write(f'\n    {valores[0]} [label="{valores[0]}"]')
                    dot_file.write(f'\n    {resultado} -> {valores[0]}')
                print("grafo creado")

        elif operador == "inverso":
            if len(valores) != 1 or valores[0] == 0:
                print("Error: tiene que ser diferente de cero")
            else:
                resultado = 1 / valores[0]
                print("1/", valores[0], "=", resultado, operador)
                with open(dot_file_name, "a") as dot_file:

                    dot_file.write(f'\n    {resultado} [label="{resultado}- inverso"]')
                    dot_file.write(f'\n    {valores[0]} [label="{valores[0]}"]')
                    dot_file.write(f'\n    {resultado} -> {valores[0]}')
                print("grafo creado")

        elif operador == "seno":
            if len(valores) != 1:
                print("Error: solo un valor")
            else:
                resultado = math.sin(valores[0])
                print("sen(", valores[0], ") =", resultado, operador)

        elif operador == "coseno":
            if len(valores) != 1:
                print("Error: solo un valor")
            else:
                resultado = math.cos(valores[0])
                print("cos(", valores[0], ") =", resultado, operador)
                with open(dot_file_name, "a") as dot_file:

                    dot_file.write(f'\n    {resultado} [label="{resultado}- seno"]')
                    dot_file.write(f'\n    {valores[0]} [label="{valores[0]}"]')
                    dot_file.write(f'\n    {resultado} -> {valores[0]}')
                print("grafo creado")

        elif operador == "tangente":
            if len(valores) != 1:
                print("Error: solo un valor")
            else:
                resultado = math.tan(valores[0])
                print("tan(", valores[0], ") =", resultado, operador)
                with open(dot_file_name, "a") as dot_file:

                    dot_file.write(f'\n    {resultado} [label="{resultado}- tangente"]')
                    dot_file.write(f'\n    {valores[0]} [label="{valores[0]}"]')
                    dot_file.write(f'\n    {resultado} -> {valores[0]}')
                print("grafo creado")

        elif operador == "mod":
            if len(valores) != 2:
                print("Error: solo 2 valores")
            else:
                resultado = valores[0] % valores[1]
                print(valores[0], "%", valores[1], "=", resultado, operador)
                with open(dot_file_name, "a") as dot_file:

                    dot_file.write(f'\n    {resultado} [label="{resultado}- mod"]')
                    dot_file.write(f'\n    {valores[0]} [label="{valores[0]}"]')
                    dot_file.write(f'\n    {valores[1]} [label="{valores[1]}"]')
                    dot_file.write(f'\n    {resultado} -> {valores[0]}')
                    dot_file.write(f'\n    {resultado} -> {valores[1]}')
                print("grafo creado")

        return resultado

    except Exception as e:
        print("aca2 - expresion")
        print("Error: " + str(e))
        return 0

def listanumeros(valores):

    try:

        numero = valor()
        valores.append(numero)

        vt = tokensL[-1]
        if vt[1] != "coma":
            return
        

        tokensL.pop()        

        #LOS VALORES DE LAS OPERACIONES
        listanumeros(valores)

    except Exception as e:
        print("aca0")
        print("Error: " + str(e))

def valor():

    try:
        vt = tokensL.pop()                    
        if vt[1] != "Valor":            
            errores.append([vt[0], "->" + vt[1], vt[2], vt[4]])
            return float(0)
        

        vt = tokensL.pop()                   
        if vt[1] != "dos puntos :":           
            errores.append([vt[0], "->" + vt[1], vt[2], vt[4]])
            return float(0)
        

        resultado = numero()
        return resultado

    except Exception as e:
        print("aca")
        print("Error: " + str(e))
        return float(0)

#--AQUI ES DONDE ACTUALIZO PARA OPERAR LAS OPERACIONES ANIDADAD INICIO[]FIN
def numero():

    resultado = 0                  
    try:
#SE SACA EL NUMERO
        vt = tokensL[-1]
        if vt[1] == "Numero":
            try:
                tokensL.pop()            
                resultado = float(vt[0])
            
            except:
                resultado = float(0)
        
        else:

            vt = tokensL.pop()                   
            if vt[1] != "corchete para abrir":           
                errores.append([vt[0], "->" + vt[1], vt[2], vt[4]])
                return 
            

            resultado = float(exp_a_operar())

            vt = tokensL.pop()                   
            if vt[1] != "corchete para cerrar":           
                errores.append([vt[0], "->" + vt[1], vt[2], vt[4]])
                return 
        
        return resultado

    except Exception as e:
        print("error numero")
        print("Error: " + str(e))
        return 0

#LA PARTE DE AL FINAL DEL JSON
def configuraciones():

    try:
        
        vt = tokensL.pop()                     
        if vt[0] != "configuraciones":            
            errores.append([vt[0], "->" + vt[1], vt[2], vt[4]])
            return 
        

        vt = tokensL.pop()                   
        if vt[1] != "dos puntos :":           
            errores.append([vt[0], "->" + vt[1], vt[2], vt[4]])
            return 
        

        vt = tokensL.pop()                   
        if vt[1] != "corchete para abrir":           
            errores.append([vt[0], "->" + vt[1], vt[2], vt[4]])
            return 
        

        vt = tokensL.pop()                     
        if vt[1] != "llave de abrir":            
            errores.append([vt[0], "->" + vt[1], vt[2], vt[4]])
            return 0
        
        #LOS AJUSTES DEL GRAFO
        datos_grafo() 

        vt = tokensL.pop()                    
        if vt[1] != "llave para cerrar":         
            errores.append([vt[0], "->"+ vt[1], vt[2], vt[4]])
            return 0

        vt = tokensL.pop()                   
        if vt[1] != "corchete para cerrar":           
            errores.append([vt[0], "->" + vt[1], vt[2], vt[4]])
            return 
        
    except Exception as e:
        print("error configuraciones")
        print("Error: " + str(e))

#graphvizzzzzzzzzzzz
def datos_grafo():

    #GRAPHIZZZZZZZZZZZ
    try:
        #RESERVA AJUSTES - texto, fondo, etc) 
        vt = tokensL.pop()                     
        if vt[1] != "Reservada":            
            errores.append([vt[0], "->" + vt[1], vt[2], vt[4]])
            return 

            

        vt = tokensL.pop()                   
        if vt[1] != "dos puntos :":           
            errores.append([vt[0], "->" + vt[1], vt[2], vt[4]])
            return 
        

        vt = tokensL.pop()                   
        if vt[1] != "Cadena":           
            errores.append([vt[0], "->" + vt[1], vt[2], vt[4]])
            return
        else:
            #muestra los ajustes
            print(vt[0])
        

        #SI YA NO HAY COMA ES LA ULTIMA.
        vt = tokensL[-1]
        if vt[1] != "coma":
            return
        
        tokensL.pop()        

        datos_grafo()

    except Exception as e:
        print("Error: " + str(e))



#Prueba
#def jj():
    #entrada= open('prueba.json', 'r').read()
    #parser(entrada)
    #print("errores en suma:")
    #print(errores)

#jj()
