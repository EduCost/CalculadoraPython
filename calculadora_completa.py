from time import sleep
def cabeçalho(txt):
    print('-'*50)
    print(f'\033[1;34m{txt.center(50)}\033[m')
    print('-'*50)


def abrir_menu():
    cabeçalho('OPÇÕES')
    print('\033[1;37mOperações Básicas:\033[m')
    print('[ + ]SOMA     [ - ]SUBTRAÇÃO  [ * ]MULTIPLICAÇÃO')
    print('[ / ]DIVISÃO  [ ** ]POTENCIA  [ % ]PORCENTAGEM')
    print('\033[1;37mConversões de bases numéricas:\033[m')
    print('[ B ]BINÁRIO  [ O ]OCTAL      [ H ]HEXADECIMAL')


def leiaInt(txt):
    while True:
        try:
            n = int(input(txt))
        except:
            print('\033[31mErro! Digite um número inteiro válido!\033[m')
        else:
            return n
    
    
def leiaFloat(txt):
    while True:
        try:
            n = float(input(txt))
        except:
            print('\033[31mErro! Digite um número válido!\033[m')
        else:
            return n
       

def soma():
    r = 0
    c = 1
    while True:
        n = leiaFloat(f'digite o {c}º número: ')
        if n == 0:
            print(f'Resultado: {r}')
            break
        elif n < 0:
            print('\033[31mErro! Digite apenas números positivos!\033[m')
        else:    
            r += n
            c += 1
        
                
def subtração():
    r = 0
    c = 1
    while True:
        n = leiaFloat(f'digite o {c}º número: ')
        if n == 0:
            print(f'Resultado: {r}')
            break
        elif n < 0:
            print('\033[31mErro! Digite apenas números positivos!\033[m')
        else:
            if c == 1:
                r = n
                c += 1
            else:    
                r -= n
                c += 1
           

def multiplicação():
    r = 1
    c = 1
    while True:
        n = leiaFloat(f'digite o {c}º número: ')
        if n == 0:
            print(f'\033[1;37mResultado: {r}\033[m')
            break
        else:    
            r *= n
            c += 1


def divisão():
    r = 0
    c = 1
    while True:
        n = leiaFloat(f'digite o {c}º número: ')
        if n == 0:
            print(f'\033[1;37mResultado: {r}\033[m')
            break
        else:
            if c == 1:
                r = n
                c += 1
            else:    
                r /= n
                c += 1


def potencia():
    base = leiaFloat('Digite o valor da base: ')
    exp = leiaInt('Digite o valor do expoente: ')
    print(f'\033[1;37m{base} elevado a {exp} é igual a {base ** exp}\033[m')
    
    
def porcentagem():
    n = leiaFloat('Digite o número: ')
    pc = leiaInt('%: ')
    print(f'\033[1;37m{pc}% de {n} é igual a {n * (pc/100)}\033[m')
        
    

cabeçalho('Calculadora PY')
while True:
    print('Qual operação você quer fazer?\n(escreva o que estiver entre colchetes)\n(0 para parar)')
    abrir_menu()
    opção = input('\033[32mOperação: \033[m').strip().upper()
    print('-'*50)
    if opção == '0':
        print('FIM DO PROGRAMA.')
        break
    elif opção == '+':
        print('Digite os números a serem somados (0 para parar)')
        soma()
    elif opção == '-':
        print('Digite os números a serem subtraidos (0 para parar)')
        subtração()
    elif opção == '*':
        print('Digite os números a serem multiplicados (0 para parar)')
        multiplicação()
    elif opção == '/':
        print('Digite os números a serem divididos (0 para parar)')
        divisão()  
    elif opção == '**':
        potencia()
    elif opção == '%':
        porcentagem()
    elif opção == 'B':
        n = leiaInt('Digite o número a ser convertido: ')
        print(f'{n} em binário é {bin(n)[2:]}')
    elif opção == 'O':
        n = leiaInt('Digite o número a ser convertido: ')
        print(f'{n} em octal é {oct(n)[2:]}')
    elif opção == 'H':
        n = leiaInt('Digite o número a ser convertido: ')
        print(f'{n} em hexadecimal é {hex(n)[2:]}')
    else:
        print(f'\033[31m"{opção}" é uma opção inválida!\033[m')    
    print('-'*50)
    sleep(2)
        

