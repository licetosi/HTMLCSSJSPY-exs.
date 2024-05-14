#1 - INÍCIO:
valor=float(input("Insira um número e descubra se ele é positivo ou negativo "))

if valor<0:
    print("Seu número é negativo.")
    
else:
    if valor>0:
        print("Seu número é positivo.")
    else:
        print("Seu número é neutro.")


#2 - RODE EM UMA OUTRA CÉLULA:

letra=str(input("Insira uma letra : "))
print("Você escolheu a letra {}".format (letra))

if 'a' in letra:
    print("Sua letra é uma vogal.")
else:
    if "e" in letra:
        print("Sua letra é uma vogal.")
    else:
        if "i" in letra:
            print("Sua letra é uma vogal.")
        else:
            if "o" in letra:
                print("Sua letra é uma vogal.")
            else:
                if "u" in letra:
                    print("Sua letra é uma vogal.")
                else:
                    print("Sua letra é uma consoante.")



#2 - OUTRA FORMA - RODE EM UMA OUTRA CÉLULA:

letra=input("Digite uma letra e descubra se ela é consoante ou vogal: ")
if letra.lower() in ["a", "e", "i", "o", "u"]:
    print("Sua letra é vogal.")
else:
    print("Sua letra é consoante.")

#3 - RODE EM UMA OUTRA CÉLULA:

dia=int(input("Insira um número de 1 a 7: "))

if dia==1:
    print("Domingo")
if dia==2:
    print("Segunda-feira")
if dia==3:
    print("Terça-feira")
if dia==4:
    print("Quarta-feira")
if dia==5:
    print("Quinta-feira")
if dia==6:
    print("Sexta-feira")
if dia==7:
    print("Sábado")
if dia>7:
    print("Valor inválido. Coloque um número de 1 a 7.")

#4 - RODE EM UMA OUTRA CÉLULA:

nome=str(input("Insira seu nome:"))
nota=float(input("Insira sua nota:"))

if nota<=0:
        print("Esse valor é inválido.")
elif nota<6:
        print("{}, você tirou {} e sua nota foi insuficiente para garantir sua aprovação.Você, infelizmente, reprovou :(". format(nome,nota))
elif nota>10:
        print("Esse valor é inválido.")
elif nota>=6:
        print("{}, você tirou {}, PARABÉNS!! Sua nota permitiu a sua aprovação, parabéns! :)". format(nome,nota)) 

#5 - RODE EM UMA OUTRA CÉLULA:

numero=int(input("Insira um número e descubra se ele é par ou ímpar: "))

if numero % 2 == 0: 
    print('Esse número é par!') 
    
else: 
    print('Ele é ímpar! ')

#6 - RODE EM UMA OUTRA CÉLULA:

idade=int(input("Quantos anos você tem?: "))

if idade>=18:
    print("Você tem {} anos, é maior de idade e está livre para comprar.".format (idade))
    
else:
    print("Você tem {} anos, é menor de idade e deve ficar atento ao regulamento e indicação dos filmes.".format (idade))


#7 - RODE EM UMA OUTRA CÉLULA:

numero=int(input("Insira o primeiro preço: "))
numero2=int(input("Insira o segundo preço: "))

if numero>numero2:
    print("O primeiro valor, de R${:.2f} é o maior, logo, o segundo, de R${:.2f}, vale mais a pena.".format (numero, numero2))

if numero2>numero:
    print("O segundo valor, de R${:.2f} é o maior, logo, o primeiro, de R${:.2f}, vale mais a pena.".format (numero2,numero))



#8 - RODE EM UMA OUTRA CÉLULA:

preço=float(input("Insira o valor da sua compra (lembrando que, a Shoppe oferece 10% de desconto para compras acima de R$100,00): "))
desc=0.10*preço
descaplicado=preço-desc
amais=100-preço

if preço>100:
    print("Sua compra foi de R${:.2f} e ultrapassou R$100,00. Logo, um desconto de 10% será aplicado no seu saldo final.\nO desconto equivale a R${:.2f} que, aplicando na sua compra, resulta em R${:.2f}.".format (preço,desc,descaplicado))
    
if preço<100:
    print("Sua compra foi de R${:.2f}. Logo, o desconto de 10% não será aplicado. Com mais R${:.2f} você garante o nosso desconto. Aproveite!".format (preço,amais))

if preço==100:
    print("Sua compra foi igual a R$100.00. O preço a pagar continua R$100.00. Com mais R${:.2f}.")

#9 - RODE EM UMA OUTRA CÉLULA:

nome=str(input("Insira o nome do aluno:"))
nota=float(input("Insira sua nota (de 0 a 100):"))

if nota<=0:
        print("Esse valor é inválido.")
elif nota<=20:
        print("{} é um aluno que precisa ser reprovado. Correspondente a classificação E :(". format(nome))
elif nota<=40:
        print("{} é um aluno que precisa melhorar. Correspondente a classificação D :(". format(nome))
elif nota<=60:
        print("{} é um aluno regular. Correspondente a classificação C :(". format(nome))
elif nota<=80:
        print("{} é um aluno bom. Correspondente a classificação B :(". format(nome))
elif nota<=100:
        print("{} é um aluno EXCELENTE! Correspondente a classificação A:(". format(nome))

#2 - RODE EM UMA OUTRA CÉLULA:


