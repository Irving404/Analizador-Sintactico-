import re
import matplotlib.pyplot as plt
token = ''
i = 0
variable = ''
lista_Resultados = []
#--------------------------------------------------------------------------
#cadena = '(100+25xy+2)+(2z)+(10abc)+(5yx)\n'
cadena = '(2xxx+11x+2\n'
#cadena = '(555x +3*8)+(2+50)\n'
#--------------------------------------------------------------------------
cadena = re.sub(r' ', '',cadena)
variables = {}



#--------------------------------------------------------------------------
def error(caracter_Esperado):
    print('Error: se esperaba → ' + caracter_Esperado)
#--------------------------------------------------------------------------
def get_Char():
    global token
    global i
    i += 1
    token = cadena[i]
#--------------------------------------------------------------------------
def ciclo_Funcion(Lmax, Lmin):
    while Lmin <=Lmax:
        variables[variable] = Lmin
        maain()
        Lmin+=1
        pass
#--------------------------------------------------------------------------
def isVariable():
    global token
    global i
    global variables
    global variable
    temp = '1'
    while token.isalpha():
        if token in variables:
            tempV = variables[token]    
        else:
            if variable == '':
                tempVm = input('cuanto es Valor Minimo para ' + token + ': ')
                tempVM = input('cuanto es Valor Maximo para ' + token + ': ')
                iaux = i
                Taux= token
                variable = token
                ciclo_Funcion(int(tempVM),int(tempVm))
                i = iaux
                token = Taux
            else:
                error(variable)
                exit()
        #tempA = int(tempV) * int(temp)
        #temp = str(tempA)
        i +=1
        token = cadena[i] 
    i -= 1
    token = cadena[i]
    return int(temp)
#--------------------------------------------------------------------------
def SCANF():
    global token
    global i
    global variables
    global variable
    temp = ''
    while token.isdigit():
        temp += token
        i +=1
        token = cadena[i]
    
    while token.isalpha():
        tempV = ''
        if token in variables:
            
            tempV = variables[variable]    
        else:
            if variable == '':

                tempVm = input('cuanto es Valor Minimo para ' + token + ': ')
                tempVM = input('cuanto es Valor Maximo para ' + token + ': ')
                variable = token
                iaux = i
                Taux= token
                ciclo_Funcion(int(tempVM),int(tempVm))
                i = iaux
                token = Taux
                return 0
            else:
                error(variable)
                exit()
            #tempV = input('cuanto vale ' + token + ': ')
            #variables[token] = tempV
        tempA = int(tempV) * int(temp)
        temp = str(tempA)
        i +=1
        token = cadena[i] 
    i -= 1
    token = cadena[i]
    return int(temp)
#--------------------------------------------------------------------------
def match(caracter_Esperado):
    if caracter_Esperado == token:
        get_Char()
    else:
        error(caracter_Esperado)
#--------------------------------------------------------------------------
def factor():
    global i
    temp = 0
    if token == '(':
        match('(')
        temp = exp()
        match(')')
    elif token.isdigit():
        temp = SCANF()
        get_Char()
    elif token.isalpha():
        temp = isVariable()
        get_Char()
    else:
        error()
    return temp
#--------------------------------------------------------------------------
def term():
    temp = factor()
    while token == '*':
        match('*')
        temp *= factor()
    return temp
#--------------------------------------------------------------------------
def exp():
    temp = term()
    while token == '+' or token =='-':
        if token == '+':
            match('+')
            temp += term() 
        else:
            match('-')
            temp -= term() 
    return temp
#--------------------------------------------------------------------------
def maain():
    global i
    i=0
    global cadena
    global token
    result = 0
    token = cadena[i]
    result = exp()
    if token == '\n':
        print('resultado: ' + str(result))
        lista_Resultados.append(result)
    else:
        error(token)
maain()
plt.plot(lista_Resultados, label = "Funcion " + cadena)
plt.show()
#--------------------------------------------------------------------------