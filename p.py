'''
Função que atribui valor a lista com o tamanho das variaveis
'''
def mudancadevalor(variavel, a, s):
    r = 0
    while(r < s):
        variavel.append(0)
        r += 1
    var = bin(a)
    n = len(var)
    y = n -1
    s = len(variavel) - 1
    r = 0
    while(var[y] != 'b'):
        variavel[s] = int(var[y])
        s -= 1
        y -= 1
    return variavel
'''
Função que atribui valor a cada variavel das clasulas
'''
def atribuirvalor(numeroV, ClasulasIn, VarGeral, variaveis):
    i = 0
    j = 0
    while(i < numeroV):
        while(j < n):
            if(i + 1 == ClasulasIn[j]):
                VarGeral[j] = variaveis[i]
            elif(((i+1)*-1) == ClasulasIn[j]):
                if(variaveis[i] == 1):
                    VarGeral[j] = 0
                else:
                    VarGeral[j] = 1
            j += 1
        j = 0
        i += 1
    return VarGeral
    
inputs = []
inputs.append(input("Digite a fórmula:"))
n = len(inputs[0]) #tamanho da string recebida
numeroC = 0 #variavel para guardar a quantidade de Clasulas
numeroV = 0 #variavel para guardar a quantidade de Variaveis
i = 0
cont = 0
'''
Transforma a string em inteiro e armazena na variavel
'''
while(i < n):
    if(inputs[0][i] == ' '):
        cont += 1
    if(cont == 2):
        i += 1
        while(inputs[0][i] != ' '):
            numeroV = numeroV * 10 + int(inputs[0][i])
            i += 1
        cont += 1
    if(cont  == 3):
        i += 1
        while(i < n):    
            numeroC = numeroC * 10 + int(inputs[0][i])
            i += 1
        cont += 1
    i += 1
'''
Recebe todas as clasulas
'''
i = 0
clasulas = []
while(i < numeroC):
    clasulas.append(input("Digite as clasulas:"))
    i += 1
'''
Cria uma lista com o tamanho da quantidade de variaveis digitadas
'''
i = 0
j = 0
x = 0
ClasulasIn = []
while(i < numeroC):
    x = len(clasulas[i])
    while(j < x):
        if(clasulas[i][j] != ' ' and clasulas[i][j] != '-'):
            ClasulasIn.append(0)
        j += 1
    j = 0
    i += 1
'''
Transforma os valores digitados da string em inteiros na lista criada anteriormente
'''
n = len(ClasulasIn)
i = 0 #contador das clasulas
j = 0 #contador das variaveis que há em cada clasula, uma por vez
w = 0 #contador para a posição da lista ClasulasIn
pos = [] #lista para armazenar a posição dos zeros(que são considerados pelo codigo
         #o final da clasula);
while(i < numeroC):
    x = len(clasulas[i])
    while(j < x):
        if(clasulas[i][j] != ' '):
            if(clasulas[i][j] == '-'):
                j += 1
                ClasulasIn[w] = ClasulasIn[w] * 10 - int(clasulas[i][j])
            else:
                if(clasulas[i][j] == '0'):
                    pos.append(w)
                    ClasulasIn[w] = 0
                ClasulasIn[w] = ClasulasIn[w] * 10 + int(clasulas[i][j])
        else:
            w += 1
        j += 1
    w += 1
    j = 0
    i += 1
'''
Cria uma lista onde será armazenadas todos os valores binarios das variaveis
com o tamanho igual ao da lista com os numeros inteiros
'''
n = len(ClasulasIn)
i = 0
VarGeral = []
while(i < n):
    VarGeral.append(0)
    i += 1
i = 0 #contador das Clasulas
j = 0 #contador das Variaveis
k = 0 #contador para posiçoes
soma = 0 #soma os valores das variaveis
soma1 = 0 #soma os valores das clasulas
a = 0 #contador para a força bruta
variaveis = []
variaveis = mudancadevalor(variaveis, a, numeroV)
VarGeral = atribuirvalor(numeroV, ClasulasIn, VarGeral, variaveis)
'''
Utilizando as funçoes faz o processo da força bruta
'''
while(i < numeroC):
    soma = 0
    while(j < pos[k]):
        if(VarGeral[j] == 1):
            soma += 1
        j += 1
    j = 0
    if(soma > 0):
        soma1 += 1
        i += 1
        j = pos[k]
        k += 1
    elif(a == (2 ** numeroV)):
        print("Insatisfativel!")
        break
    else:
        a += 1
        del(variaveis)
        variaveis = []
        variaveis = mudancadevalor(variaveis, a, numeroV)
        VarGeral = atribuirvalor(numeroV, ClasulasIn, VarGeral, variaveis)
        soma1 = 0
        k = 0
        i = 0
if(soma1 == numeroC):
    print("Satisfativel")