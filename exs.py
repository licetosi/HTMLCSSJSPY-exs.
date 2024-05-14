#1. Cadastro de CPF
#Crie um programa para cadastro de CPF de clientes que recebe o CPF em um input box apenas com números.
#Ex: 'Insira seu CPF (digite apenas números)'
#Caso o usuário digite algo diferente de números ou digite menos de 11 caracteres (tamanho do CPF brasileiro), o programa deve exibir uma mensagem de "Digite seu CPF corretamente e digite apenas números"

cpf=input("Insira seu CPF, apenas com números e com mais de 11 caracteres: ")
   
# esse if vai falar que se a contagem for menor ou igual a 10 ou maior que 11, o cpf está incorreto.
# se o is numeric imprimir "False", também mostrará esta mensagem (quer dizer que não há apenas números).[

if len(cpf)<=10 or len(cpf)>11 or cpf.isnumeric()== False:
    print("Digite o seu CPF corretamente (com 11 caracteres numéricos).")

# se a contagem do cpf for igual a 11     

elif len(cpf)==11 and cpf.isnumeric()== True:
    print("Seu CPF é válido!")

#2. Melhorando nosso Cadastro de CPF
#Agora, além das validações anteriores, vamos criar um input que permita que o usuário insira pontos, traços e inclusive espaços vazios. Nosso programa deve "tratar" o que o usuário inserir para padronizar o CPF dele em apenas números. A verificação de tamanho do CPF com 11 caracteres continua válida, mas ela só deve ser feita depois de retirar todos os pontos, traços e espaços do CPF que o cliente inserir e, uma vez retirados pontos, traços e espaços, devem sobrar apenas números no CPF. Qualquer outro caractere deve ser considerado inválido.
#No final, nosso programa deve exibir uma mensagem para o usuário, caso ele tenha inserido o CPF inválido ou então apenas deve printar o CPF correto já só com número.

texto=input("Insira seu CPF, apenas com números e com mais de 11 caracteres: ")

if texto.isnumeric()== False:
    print("Digite o seu CPF corretamente (digite apenas números): ")
    
elif len(texto)==11:
    print("Seu CPF é válido!")
    
elif len(texto)<=10 or len(texto)>11:
    print("Digite o seu CPF corretamente (com 11 caracteres)")
        
elif texto.isnumeric()== True:
    print("Seu CPF é válido.")
 
cpf=input("Insira seu CPF, apenas com números e com mais de 11 caracteres: ").replace("-", "").replace(".", "").replace(" ", "").replace(";", "").replace("<", "").replace(">", "").replace("~", "")
   
# esse if vai falar que se a contagem for menor ou igual a 10 ou maior que 11, o cpf está incorreto.
# se o is numeric imprimir "False", também mostrará esta mensagem (quer dizer que não há apenas números).

if len(cpf)<=10 or len(cpf)>11 or cpf.isnumeric()== False:
    print("Digite o seu CPF corretamente (com 11 caracteres numéricos).")

# se a contagem do cpf for igual a 11

elif len(cpf)==11 and cpf.isnumeric()== True:
    print("Seu CPF, retirando os caracteres indesejados, é válido!")

#---------------------------------------------------------------------------------------------------------------------
email= "alice.tosi@aluno.senai.br"
print(email[10:25])
#—------------------------------------------------------------------------------------------------------------------
#len mostra a quantidde de characteres
email= "alice.tosi@aluno.senai.br"
len(email)
#---------------------------------------------------------------------------------------------------------------------
email= "alice.tosi@aluno.senai.br"
print(email[3:-15])
#---------------------------------------------------------------------------------------------------------------------
dir(str)
#---------------------------------------------------------------------------------------------------------------------

# capitalize transforma a primera letra da frase em maiúscula
texto= "alice mantovani"
print(texto.capitalize())
#--------------------------------------------------------------------------------------------------------------------
# case fold transforma as maiúsculas em minúsculas
texto="ALICE"
print(texto.casefold())
#—------------------------------------------------------------------------------------------------------------------
# upper e lower = para MAIÚSCULA e minúscula
texto="minúscula"
print(texto.upper())


texto2="MiNÚscuLa"
print(texto2.lower())
#---------------------------------------------------------------------------------------------------------------------
email= "alice.tosi@aluno.senai.br"
print(email.count("."))
#---------------------------------------------------------------------------------------------------------------------
# endswith analisa o final, se é verdadeiro ou falso
email= "alice.tosi@aluno.senai.br"
print(email.endswith("senai.br"))
#---------------------------------------------------------------------------------------------------------------------
email= "alice.tosi@aluno.senai.br"
print(email.find("@"))
#---------------------------------------------------------------------------------------------------------------------


# o format vai substituir
email= str(input("Insira o seu e-mail: "))
print("Seu e-mail é {}.". format(email))
#---------------------------------------------------------------------------------------------------------------------
# isalnum vai ver se tem alfanuméricos (n°s e letras), considera letras com acento
email= "alice"
print(texto.isalnum())
#---------------------------------------------------------------------------------------------------------------------
# isalpha só aceita letra, sem números ou characteres especiais
email= "alicetosialunosenaibr"
print(email.isalpha())
#---------------------------------------------------------------------------------------------------------------------
#só aceita número
texto="123"
print(texto.isnumeric())
#---------------------------------------------------------------------------------------------------------------------
# essa variável substitui a outra, separados pela vírgula preta
texto="100.00"
print(texto.replace(".", ","))
#---------------------------------------------------------------------------------------------------------------------
# vai excluir e dar um espaço mediante ao character escolhido
email= "alice.tosi@aluno.senai.br"
print(email.split("a"))
#---------------------------------------------------------------------------------------------------------------------
# cada item é o texto de uma linha
texto="""Olá bom dia.
Venho lhe informar o faturamento.
Faturamento = R$2.500,00"""
print(texto.splitlines())
#---------------------------------------------------------------------------------------------------------------------
# cada item é o texto de uma linha
texto="""Olá bom dia.
Venho lhe informar o faturamento.
Faturamento = R$2.500,00"""
print(texto.splitlines())
#---------------------------------------------------------------------------------------------------------------------
# todas as primeiras letras com letra maiúscula
email2= "alice tosi"
print(email2.title())
#---------------------------------------------------------------------------------------------------------------------
# tira espaços indesejados no início e fim da string
texto= " B  236 "
print(texto.strip())
#---------------------------------------------------------------------------------------------------------------------
# valida se está no início
texto="Alice"
print(texto.startswith("Alic"))
#---------------------------------------------------------------------------------------------------------------------
# 1. Crie um programa que solicita ao usuário para digitar uma frase. O programa deve imprimir a frase
#com a primeira letra maiúscula e todas as letras em minúsculas.
frase=input("Digite uma frase: ")
print(frase.capitalize())
#---------------------------------------------------------------------------------------------------------------------
#2. Peça ao usuário para inserir uma frase e uma palavra-alvo. O programa deve contar quantas vezes a
#palavra-alvo aparece na frase.
frase=input(str("Digite uma frase, vamos contar quantas vezes o caractere aparece na frase escrita abaixo: "))
alvo=input("Insira o caractere que deseja contar: ")
print(frase.count(alvo))
#---------------------------------------------------------------------------------------------------------------------
#3. Solicite ao usuário para inserir uma frase. O programa deve verificar se a frase termina com um ponto final.
user =str(input("Insira uma frase: "))
if user.endswith(".") ==False:
    print("Sua frase não termina com um ponto final.")
else:
    print("Sua frase termina com um ponto final.")
#---------------------------------------------------------------------------------------------------------------------
#4. Crie um programa que recebe uma frase e uma palavra-chave do usuário. O programa deve imprimir
#a posição da primeira ocorrência da palavra-chave na frase.
frase=input(str("Digite uma frase: "))
chave=input(str("Digite uma palavra-chave, vamos dizer qual é a posição da primeira letra, na frase escrita acima: "))


if chave in frase:
    print(frase.find(chave))
else:
    print("A sua palavra-chave não está na frase escrita acima!")
#---------------------------------------------------------------------------------------------------------------------
#5. Peça ao usuário para inserir uma frase e duas palavras. O programa deve substituir todas as ocorrências
#da primeira palavra pela segunda na frase.
frase=input(str("Digite uma frase: "))
palavra1=input(str("Digite a palavra que será substituída: "))
palavra2=input(str("Digite a palavra que vai substituir a primeira: "))
if palavra1 in frase:
    print(frase.replace(palavra1, palavra2))
else:
    print("Algo deu errado. Parece que a palavra não foi encontrada na frase. Tente novamente!")
#---------------------------------------------------------------------------------------------------------------------
#STRING2
#1. Cadastro de CPF
cpf=input("Insira seu CPF, apenas com números e com mais de 11 caracteres: ")
# esse if vai falar que se a contagem for menor ou igual a 10 ou maior que 11, o cpf está incorreto.
# se o is numeric imprimir "False", também mostrará esta mensagem (quer dizer que não há apenas números).[
if len(cpf)<=10 or len(cpf)>11 or cpf.isnumeric()== False:
    print("Digite o seu CPF corretamente (com 11 caracteres numéricos).")
# se a contagem do cpf for igual a 11     
elif len(cpf)==11 and cpf.isnumeric()== True:
    print("Seu CPF é válido!")
#---------------------------------------------------------------------------------------------------------------------
#2. Melhorando nosso Cadastro de CPF
cpf=input("Insira seu CPF, apenas com números e com mais de 11 caracteres: ").replace("-", "").replace(".", "").replace(" ", "").replace(";", "").replace("<", "").replace(">", "").replace("~", "")
# esse if vai falar que se a contagem for menor ou igual a 10 ou maior que 11, o cpf está incorreto.
# se o is numeric imprimir "False", também mostrará esta mensagem (quer dizer que não há apenas números).
if len(cpf)<=10 or len(cpf)>11 or cpf.isnumeric()== False:
    print("Digite o seu CPF corretamente (com 11 caracteres numéricos).")
# se a contagem do cpf for igual a 11
elif len(cpf)==11 and cpf.isnumeric()== True:
    print("Seu CPF, retirando os caracteres indesejados, é válido!")
#---------------------------------------------------------------------------------------------------------------------




#3. Cadastro de e-mails

email=input("Insira o seu e-mail: ")

if email:
    pos_a=email.find("@")
    servidor=email[pos_a:]
    
    if pos_a != -1 and "." in servidor:
        print("Cadastro concluído!")
    else:
        print("E-mail inválido.")
        
else:
    print("Digite seu nome e e-mail corretamente.")
#---------------------------------------------------------------------------------------------------------------------
# para texto, usar aspas
lista1=["alice", "luis", "matheus","felipe","gabriel","léo"]


# para números, não usar aspas
lista2=[1,2,3,4]


# para juntar, criar uma variável
todasaslistas=[lista1,lista2]


#para puxar a posição, iniciando no 0 e mostrar:
print(lista1[4])
#---------------------------------------------------------------------------------------------------------------------
# para texto, usar aspas
lista1=["alice", "luis", "matheus","felipe","gabriel","léo"]


# para números, não usar aspas
lista2=[1,2,3,4]


# para juntar, criar uma variável
todasaslistas=[lista1,lista2]


#para puxar a posição, iniciando no 0 e mostrar:
print(lista1[4])
#---------------------------------------------------------------------------------------------------------------------
#as listas vão se comunicar
produtos=["tv","celular","tablet","teclado"]
valor=[2500,1850,790,300,69]


print("O preço do (a) {} é de R${}".format(produtos[1],valor[1]))
#---------------------------------------------------------------------------------------------------------------------
#para achar o produto
produtos=["tv","celular","tablet","teclado"]


i=produtos.index("tv")
print("O valor de i é "+ str(i))
print("O produto da posição i é "+ str(produtos[i]))
#--------------------------------------------------------------------------------------------------------------------
times=["Palmeiras","Botafogo","São Paulo","Santos","Portuguesa","Juventus","Água Santa","Ituano","Flamengo","Coritiba"]
i=times.index("Palmeiras")
print("O valor de i é "+str(i))
print("O time da posição i é "+str(times[1]))
#---------------------------------------------------------------------------------------------------------------------
produtos=["tv","celular","tablet","teclado"]
estoque=[2500,1850,790,300]
produto=input("Insira o nome do produto: ")


if produto in produtos:
    i = produtos.index(produto)
    qntd=estoque[i]
    print("Temos {} unidade (s) de {} no estoque.".format(qntd,produto))


else:
    print("{} não existe no estoque.".format(produto))
#---------------------------------------------------------------------------------------------------------------------
#o append vai adicionar à lista


produtos=["tv","celular","tablet","teclado"]
produtos.append("iphone")
print(produtos)
#---------------------------------------------------------------------------------------------------------------------
produtos=["tv","celular","tablet","teclado"]
print(produtos)
aux=produtos.pop(0)


#pop vai remover o produto que tiver nessa posição
print(produtos)
print(aux)


#o .remove deleta o valor da lista, já o .pop pode ser armazenado ao lado
#---------------------------------------------------------------------------------------------------------------------
#try 
#try:
    #lista.remove(Item que você quer tentar remover)
#except: 
#---------------------------------------------------------------------------------------------------------------------
produtos1=["tv","celular","tablet","teclado"]
itemusuario=input("Qual item deseja remover?: ")


try: #try vai remover o produto tratando o erro
    produtos1.remove(itemusuario)
    print(produtos1)
except: #ele não existe na lista
    print("O produto {} não existe na lista.".format(itemusuario))
#---------------------------------------------------------------------------------------------------------------------
vendas=[2500,1850,790,300,990]
print(len(vendas))
print(max(vendas))
print(min(vendas))
#---------------------------------------------------------------------------------------------------------------------
produtos=["tv","celular","tablet","teclado"]
novosprodutos=["chromecast","notebook"]
#extend concatena as listas
produtos.extend(novosprodutos)
print(produtos)
#---------------------------------------------------------------------------------------------------------------------
produtos=["tv","celular","tablet","teclado"]
novosprodutos=["chromecast","notebook"]
#da pra usar o '+' para concatenar as listas MAIS FÁCIL
print(produtos+novosprodutos)
#---------------------------------------------------------------------------------------------------------------------
produtos=["tv","celular","tablet","teclado"]
novosprodutos=["chromecast","notebook"]
#append cria uma lista dentro de outra lista
produtos.append(novosprodutos)
print(produtos)
#---------------------------------------------------------------------------------------------------------------------
produtos=["tv","airdrops","celular","tablet","teclado"]
#sort ordena a lista em ordem. letras maiúsculas primeiro, dps alfabeto
produtos.sort()
print(produtos)
#---------------------------------------------------------------------------------------------------------------------
produtos=["tv","airdrops","celular","tablet","teclado"]
estoque=[2500,1850,790,300,20]


#sort ordena a lista em ordem. letras maiúsculas primeiro, dps alfabeto


estoque.sort()
print(estoque)
#---------------------------------------------------------------------------------------------------------------------
produtos="apple tv, mac, apple watch, mac book"
listaprodutos=produtos.split(",     ")
print(listaprodutos)


#---------------------------------------------------------------------------------------------------------------------
faturamento=1000
faturamento=faturamento+1000
print(faturamento) #valor anterior de faturamento+1000


faturamento+=500
print(faturamento) #valor anterior de faturamento+500 (+= incrementa)


faturamento-=500
print(faturamento) #valor anterior de faturamento-500 (-= incrementa)
#---------------------------------------------------------------------------------------------------------------------
lista1=["apple tv","mac","airpods","tv"]
lista2=lista1


lista1[2]="iphone12"
print(lista1)
print(lista2)
#---------------------------------------------------------------------------------------------------------------------
lista1=["apple tv","mac","airpods","tv"]
lista2=lista1.copy()
lista1[2]="iphone 12"
print(lista1)
print(lista2)
#---------------------------------------------------------------------------------------------------------------------
nome=["Magalu", "CasasBahia", "Shoppee", "PontoFrio"]
produtos=["ipad", "iphone"]
vendas=[
    [1000, 2600],
    [1400, 2000],
    [1500, 2750],
    [1900, 2800],
]
