def asci(num):
    from random import randint
    itens = '1234567890-=!@#$%¨&*()_+qwertyuiop´[asdfghjklç~]\zxcvbnm,.;+§ª}{º'
    senha = []
    for c in range (0, num+1):
        senha.append(itens[randint(0, len(itens))])
    for e in senha: #pega um item aleatório e coloca na lista que no final é escrita    
        print(e, end='')

def alnum(num):
    from random import randint
    itens = 'qwertyuiopasdfghjklçzxcvbnm123657890'
    senha = []
    for c in range (0, num+1): #pega um item aleatório e coloca na lista que no final é escrita    
        senha.append(itens[randint(0, len(itens))])
    for e in senha:    
        print(e, end='')

def numeric(num):
    from random import randint
    itens = '0891326547'
    senha = []
    for c in range (0, num+1): #pega um item aleatório e coloca na lista que no final é escrita    
        senha.append(itens[randint(0, len(itens))])
    for e in senha:    
        print(e, end='')
        
        
print('GERADOR DE SENHAS')

while True:
    try:
        print('ASCII -> 1')
        print('AlfaNúmerica -> 2')
        print('Númerica -> 3')
        choice = int(input('Que tipo de senha você quer gerar? -> '))
        if choice > 3 or choice <= 0:
            while True:
                choice = int(input('\033[31mDIGITE UMA DAS OPÇÕES ABAIXO\033[m -> '))
                if 0 < choice < 4:
                    break
    except:
        print('\033[31mDIGITE ALGO VÁLIDO POR FAVOR\033[m')
    else:
        break  
while True:
    try:
        num = int(input('Digite o número de caracteres -> '))
    except:
        print('\033[31mDIGITE ALGO VÁLIDO POR FAVOR\033[m')
    else:
        break
if choice == 1:
    asci(num)
elif choice == 2:
    alnum(num)
elif choice == 3:
    numeric(num)
