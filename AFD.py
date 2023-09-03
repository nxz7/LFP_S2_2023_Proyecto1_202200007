import json
from tok import tok
from matematicas import matematicas

class AFD:
    letras = ["-","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s", "t", "u","v","w","x","y","z"]
    numeros = ["1","2","3","4","5","6","7","8","9","0", "."]

    def __init__(self):
        self.tabla_tokens = []
        self.cadena = ''
        self.fila = 0
        self.columna = 0
        self.bolita_act = 0
        self.bolita_ant = 0
        self.bolita_si=[9]

    def guardar_token_analizado(self, lexema):
        nuevo_token = tok(self.fila, self.columna, lexema)
        self.tabla_tokens.append(nuevo_token)

    def analizar_char(self, cadena, operacion: matematicas):
        operandos = []
        token = ''
        tipo_mate = ''
        in_string = False
        in_number = False

        while len(cadena) > 0:
            char = cadena[0]

            if char in [' ', '\n', '\t']:
                if in_string:
                    token += char
                else:
                    self.fila += 1 if char == '\n' else 0
                    self.columna = 0 if char == '\n' else self.columna + 1
                cadena = cadena[1:]
                continue

            if not in_string:
                if char == '{' or char == '}' or char == '[' or char == ']':
                    self.guardar_token_analizado(char)
                elif char == '"':
                    in_string = True
                    token += char
                elif char == ':':
                    self.guardar_token_analizado(char)
                elif char == ',':
                    self.guardar_token_analizado(char)
                elif char in self.numeros:
                    in_number = True
                    token += char
                else:
                    pass
            else:
                if char == '"':
                    in_string = False
                    token += char
                    self.guardar_token_analizado(token)
                    token = ''
                else:
                    token += char

            if in_number and (len(cadena) == 1 or (cadena[1] not in self.numeros)):
                in_number = False
                self.guardar_token_analizado(token)
                token = ''

            self.columna += 1
            cadena = cadena[1:]

        operacion.operandos = operacion
        return [cadena, operandos]

    def imprimir_tokens(self):
        print('*' * 61)
        print("* Fila        *     Columna         *        Lexema         *")
        print('*' * 61)
        for token in self.tabla_tokens:
            print("* {:<12} | {:<18} | {:<21} *".format(token.fila, token.columna, token.lexema))
#PRUEBAAAAAAAAAAAAAAAAAAAAAAA
#automata = AFD()
#cadena = open('prueba.json', 'r').read()

#automata.analizar_char(cadena, matematicas('division'))

#automata.imprimir_tokens()
