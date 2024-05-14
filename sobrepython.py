#Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade  dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias. 
idade=int(input("Insira a sua idade: "))
meses=idade*12
dias=idade*365
horas=dias*24
minutos=horas*60
segundos=minutos*60
print("Se você tem {} anos, logo, você tem {} meses e, em média, {} dias de idade. Além de {} horas, {} minutos e {} segundos de vida (obviamente que os números não são exatos, mas mostram uma aproximação).". format (idade, meses, dias, horas, minutos, segundos))

#Crie um algoritmo capaz de calcular área de um triângulo. O programa deve receber os dados  necessários do usuário (medida da base e da altura do triângulo) e calcular qual seria o valor da área  deste triângulo. 
base=int(input("Insira o valor da base:"))
altura=int(input("Insira o valor da altura:"))
area=(base*altura)/2
print("A área do triângulo [(base*altura)/2] é de {}.". format(area))


#O custo de um carro novo ao consumidor é a soma do custo de fábrica com a porcentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que o percentual do distribuidor  seja de 28% e os impostos de 45%, escrever um algoritmo para ler o custo de fábrica de um carro, calcular e escrever o custo final ao consumidor. 
custo = float(input("Qual o valor do carro? "))
distribuidor = 0.28
impostos = 0.45
valor = custo + (custo*distribuidor)
valor_final = valor + (valor*impostos)
print('Custo de fábrica: {}'.format(valor_final))

#Escreva um algoritmo que calcule a quantidade de latas de tinta necessárias e o custo para pintar  tanques cilíndricos de combustível, dados: 
#• A lata de tinta custa R$ 50,00; 
#• Cada lata contém 5 litros; 
#• Cada litro de tinta pinta 3 m². 

raio_tanque = float(input('Qual é o raio do tanque?'))
altura_tanque = float(input('Qual a altura do tanque?'))
area_total = 2 * 3.1415 * raio_tanque * (raio_tanque + altura_tanque)
coberturalitro= 3
custolata = 50
capacidadeporlata = 5
litros_necessarios = area_total / coberturalitro
latas_necessarias = int(litros_necessarios /capacidadeporlata)
custo_total = latas_necessarias * custolata



print('Você precisa de {:.2f} latas  e o custo final é {:.2f} R$.'.format(latas_necessarias,custo_total))

#Você foi contratado por uma empresa chamada ChoppDelyv (Uma empresa de entrega de bebidas a  domicílio concorrente do Zé delivery), esta empresa contratou você para desenvolver os cálculos de  preços do aplicativo dela, logo você deve criar um código simples capaz de receber o nome da bebida  a ser comprada, o valor da bebida a ser comprada, quantas unidades do produto serão vendidas e por  último o programa deve demonstrar uma saída mostrando qual o valor daquela venda.
bebida=str(input("Insira o nome da bebida: "))
valor=int(input("Insira o preço da bebida: "))
qntd=int(input("Insira a quantidade: "))
total= valor*qntd
print('-'*150)
print("O valor da (o) {} é {} reais por unidade. Logo, você deverá pagar, para {} unidade(s), {} reais. ChoppDelyv agradece a sua preferência! :)". format (bebida, valor, qntd, total))


#Situação 01 – Programando em Python 
#Crie um programa para cálculo de despesas de locação de veículos. Este deverá perguntar ao usuário  os valores referentes a locação e posteriormente entregar ao mesmo qual será o gasto total para locação do  carro. 
#O programa deverá perguntar ao usuário qual o valor da diária do aluguel do carro, qual o valor cobrado  por quilômetro rodado, por quantos dias o usuário pretende locar o carro e quantos quilômetros ele pretende  percorrer. 
#Sua aplicação deverá ser responsiva, amigável e auto explicativa para uso. Utilize seus conhecimentos  adquiridos até o momento (ex.: print , input, .format), lembrando que é de suma importância comentar todas  as linhas de código (#), pois outros desenvolvedores poderão utilizar seu programa. 


diaria=float(input("Insira o preço da diária do aluguel: ")) 
km=float(input("Insira o preço cobrado por quilômetro rodado: ")) 
dias=int(input("Por quantos dias você pretende locar o carro?: ")) 
km2=int(input("Quantos quilômetros você pretende percorrer?: ")) 
soma=diaria*dias+km*km2
print('-'*150)
print("\nDe acordo com os dados inseridos, o valor da diária do aluguel é de: {} real (is), o valor por quilômetro rodado é de: {} real (is), o(s) dia(s) que pretende locar: {} dia (s) e os km que pretende percorrer: {}. Logo, o valor total, resulta em: {} reais.". format(diaria,km,dias,km2,soma))

#O aumento citado é de 12%. 
#Usando o novo salário bruto
#7% do Imposto de Renda 
#Plano de saúde corresponde a 8% do novo salário bruto
#3% para o Sindicato
#O salário líquido corresponde ao salário bruto menos os descontos. 
#Demonstre ao usuário uma tabela final 
#Ou seja, ele deve poder ver seu salário anterior, o novo salário bruto, todos os descontos e o novo salário líquido.

santigo=int(input("Insira seu salário antes do aumento:"))
aumento=0.12*santigo
snovo=0.12*santigo+santigo
impderenda=0.07*snovo
pdesaude=0.08*snovo
sindic=0.03*snovo

sliquido=snovo-impderenda-pdesaude-sindic

print("\033[1mSALÁRIO ANTIGO:\033[0m R${:.2f}\nAUMENTO: 12% do SALÁRIO BRUTO ATUAL (R${:.2f})\nSALÁRIO BRUTO ATUAL: R${:.2f}.\n\n\033[1mDESCONTOS:\033[0m\nImposto de Renda (7%): R${:.2f}\nPlano de saúde (8%): R${:.2f}\nSindicato (3%): R${:.2f}\nSALÁRIO LÍQUIDO ATUAL: R${:.2f}.". format(santigo,aumento, snovo,impderenda,pdesaude,sindic,sliquido))

# Calculadora Simples: Crie um programa que solicite ao usuário que insira dois números e escolha uma operação matemática (adição, subtração, multiplicação ou divisão). O programa deve então realizar a operação escolhida e exibir o resultado.

valor1=int(input("Insira seu 1° valor: "))
valor2=int(input("Insira seu 2° valor: "))

operação=str(input("Qual operação você deseja? Sendo *, +, - ou /. Lembre-se de digitar corretamente:"))

# multiplicação
if operação=="*":
    print('{} * {} = '.format(valor1, valor2))
    print(valor1 * valor2)  
    
# adição
elif operação=="+":
    print('{} + {} = '.format(valor1, valor2))
    print(valor1 + valor2)
       
 # subtração
elif operação=="-":
    print('{} - {} = '.format(valor1, valor2))
    print(valor1 - valor2)
            
#divisão
elif operação=="/":
    print('{} / {} = '.format(valor1, valor2))
    print(valor1 / valor2)

else:
    print("Inválido, tente novamente!")



#Calculadora de IMC (Índice de Massa Corporal): Crie um programa que calcule o IMC de uma pessoa. O usuário deve inserir sua altura (em metros) e seu peso (em quilogramas). O programa deve então calcular o IMC usando a fórmula IMC = peso / (altura ** 2), e classificar o resultado de acordo com a tabela de classificação de IMC.

peso=float(input("Insira seu peso: "))
altura=float(input("Insira sua altura: "))
imc = peso / (altura ** 2)

if imc<=16.9:
    print("Seu IMC (peso / (altura ** 2)) é de {:.2f}. Logo, você está muito abaixo do peso.".format (imc))
    
elif imc<=18.4:
        print("Seu IMC (peso / (altura ** 2)) é de {:.2f}. Logo, você está abaixo do peso.".format (imc))
        
elif imc<=24.9:
            print("Seu IMC (peso / (altura ** 2)) é de {:.2f}. Logo, você está com o peso normal.".format (imc))
            
elif imc<=29.9:
                print("Seu IMC (peso / (altura ** 2)) é de {:.2f}. Logo, você está acima do peso.".format (imc))
                
elif imc<=34.9:
                    print("Seu IMC (peso / (altura ** 2)) é de {:.2f}. Logo, você está com obesidade grau I.".format (imc))
                    
elif imc<=40:
                        print("Seu IMC (peso / (altura ** 2)) é de {:.2f}. Logo, você está com obesidade grau II.".format (imc))
                            
elif imc>40:
                                print("Seu IMC (peso / (altura ** 2) é de {:.2f}. Logo, você está com obesidade grau III.".format (imc))
        
else: 
    print("Inválido.")


#Conversor de Temperatura: Crie um programa que converta a temperatura de Celsius para Fahrenheit ou de Fahrenheit para Celsius, dependendo da escolha do usuário.



#Validação de Login: Crie um programa que solicite ao usuário que insira seu nome de usuário e senha. Se o nome de usuário for "admin" e a senha for "senha123", imprima "Acesso concedido". Caso contrário, imprima "Acesso negado".

user=str(input("Insira seu nome de usuário: "))
senha=str(input("Insira sua senha: "))

if "admin" in user and "senha123" in senha:
    print("Acesso concedido.")
    
else:
    print("Acesso negado.")   


#Verificador de Triângulos: Solicite ao usuário que insira três comprimentos e determine se esses comprimentos podem formar um triângulo. Se puderem, verifique se é um triângulo equilátero, isósceles ou escaleno.

valor1=int(input("Insira o 1° valor do triângulo: "))
valor2=int(input("Insira o 2° valor do triângulo: "))
valor3=int(input("Insira o 3° valor do triângulo: "))

if valor1==valor2==valor3:
    print("Você criou um triângulo equilátero, ou seja, com todos os lados iguais.")
    
elif valor1 != valor2 != valor3:
        print("Você criou um triângulo escaleno, ou seja, com todos os lados diferentes.")
        
elif valor1 != valor2 and valor3:
    print("Você criou um triângulo isósceles, ou seja, com um lado diferente dos demais.")

elif valor2 != valor1 and valor3:
    print("Você criou um triângulo isósceles, ou seja, com um lado diferente dos demais.")
    
elif valor3 != valor2 and valor1:
    print("Você criou um triângulo isósceles, ou seja, com um lado diferente dos demais.")
    
else: 
    print("Inválido!")
