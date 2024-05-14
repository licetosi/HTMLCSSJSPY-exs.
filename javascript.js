//OLÁ!!!! É IMPORTANTE QUE OS CÓDIGOS SEJAM COPIADOS E RODADOS SEPARADAMENTE PARA QUE NÃO HAJA ERRO NA 
//IDENTIFICAÇÃO DAS VARIÁVEIS (REPETIDAS, NO CASO). OBRIGADA, DEUS TE ABENÇOEE!!!!!!!

/*1 - INÍCIO:*/

let número = parseInt(prompt('Digite um número:'))
if (número % 2 === 0) {
    alert('O número é par!');
} else {
    alert('O número é impar!')
}

/*2 - RODE EM UM OUTRO ESPAÇO:*/

let anoss = prompt('Descubra sua faixa etária! Criança, adolescente, adulto ou idoso.', 'Insira sua anoss');


if (anoss <12){
    alert('Você é uma criança. Segundo o ECA, é considerado criança quem tem até 12 anos incompletos.');
} else if (anoss >= 12 && anoss <18){
    alert('Você é um adolescente. Segundo o ECA, é considerado adolescente quem tem entre 12 e 17 anos completos.');
} else if (anoss >= 18 && anoss <=59){
    alert('Você é um adulto. Segundo estudos, é considerado adulto quem tem entre 18 e 59 anos completos.');
} else if(anoss >= 60){
    alert('Você é um idoso. De acordo com a lei, é considerada pessoa idosa quem tem idade igual ou superior a 60 anos.');
}

/*3 - RODE EM UM OUTRO ESPAÇO:*/

let NUMNUM = prompt('Descubra quantos números pares existem entre 1 e o seu número.', 'Insira um número para teste.');


if (NUMNUM % 2 === 0) {
    let par = NUMNUM / 2;
    alert('Sua conta tem: ' + par)
}
else {
    let par = NUMNUM - 1
    let par2 = par / 2
    alert('Sua conta tem: ' + par2)
}

/*4 - RODE EM UM OUTRO ESPAÇO:*/

let operaçoes = prompt("Digite: Soma, Subtração, Multiplicação ou Divisão.");
let valor1 = parseFloat(prompt("Valor 1"));
let valor2 = parseFloat(prompt("Valor 2"));


switch(operaçoes){
case"Soma":
final = valor1 + valor2
alert("Resultado: " + final);
break;


case"Subtração":
final2 = valor1 - valor2
alert("Resultado: " + final2)
break;


case"Mutiplicação":
final3 = valor1 * valor2
alert("Resultado: " + final3)
break;


case"Divisão":
final4 = valor1 / valor2
alert("Resultado: " + final4)
break;
}

/*5 - RODE EM UM OUTRO ESPAÇO:*/

let numbeer = parseInt (prompt ("Digite um número para a tabela de multiplicação:"));
let limite = parseInt (prompt ("Digite o limite da tabela de multiplicação:"));


if (isNaN (numbeer) || isNaN(limite)) {
alert ("Por favor, digite números válidos. ");
}
else {
console.log("Tabela de multiplicação do "+ numbeer +" até " + limite +":");} //lembre-se que aparece no consolee;
for (let i = 1; i <= limite; i++) {
let resultado = numbeer * i;
console. log (numbeer + "x" + i + "=" + resultado); }

/*6 - RODE EM UM OUTRO ESPAÇO:*/

let nummm = parseInt(prompt("Digite um número para verificar se é primo:"));


if (nummm > 1 && Number.isInteger(nummm)) {
    let isPrimo = true;


    for (let i = 2; i <= Math.sqrt(nummm); i++) {
        if (nummm % i === 0) {
            isPrimo = false;
            break;
        }
    }
    switch (isPrimo) {
        case true:
            alert(nummm + " é um número primo.");
            break;
        case false:
            alert(nummm + " não é um número primo.");
            break;
    }
} else {
    alert("Por favor, insira um número inteiro positivo maior que 1.");
}

/*7 - RODE EM UM OUTRO ESPAÇO:*/

for(let i= prompt('Digite um número para a contagem regressiva:', 'Insira um número de 1 - 1000'); i<1000;i--){
    if(i===1000){
        break;
    }
    alert(i)
}

/*8 - RODE EM UM OUTRO ESPAÇO:*/

let nota = prompt('Insira sua nota e descubra sua classificação. ', 'Insira sua nota aqui.')


if (nota >= 0 && nota <= 10) {
    alert('Você conseguiu a pior nota e se classificou como F. Decepcionante... Se esforce mais na próxima!');
}
if (nota > 10 && nota <= 30) {
    alert('Você não alcançou o resultado esperado e se classificou como E. Se esforce mais!');
}
if (nota > 30 && nota <= 50) {
    alert('Seu resultado foi ruim e você se classificou como D.');
}
if (nota > 50 && nota <= 70) {
    alert('Você ficou na média e se classificou como C. Você pode melhorar na próxima, né? ;)');
}
if (nota > 70 && nota <= 90) {
    alert('Você recebeu uma nota boa e se classificou como B. Parabéns!');
}
if (nota > 90 && nota <= 100) {
    alert('Uau, você é incrível! Atingiu a maior nota e recebeu A. Parabéns pelo seu esforço!');
}

/*9 - RODE EM UM OUTRO ESPAÇO:*/

let numero = parseInt(prompt("Digite um número:"));
if (!isNaN(numero) && numero > 0) {
    for (let i = 1; i <= numero; i++) {
        let linha = '';
        for (let j = 1; j <= i; j++) {
            linha += '*';
        }
        console.log(linha);
    }
} else {
    console.log("Por favor, insira um número válido maior que 0.");
}

//OLÁ NOMEEEEEEEE:

var nome;


nome = window.prompt('Entre com seu nome: ','Digite seu nome nesta caixa');
document.write('Olá'+ nome +' Seja Bem Vindo!');




//CALCULADORA SOMAAAAAAAAAAAA:


let primeiro = prompt ('insira seu número');
let segundo = prompt ('insira seu número');


let primeironumero = +primeiro
let segundonumero = +segundo;


let total = primeironumero +segundonumero;


alert('o resultado da soma é:' + total);




//MEDIA DE NOTASSSSSSSSSS:


let numero1 = parseFloat(prompt('Digite sua primeira nota'));
let numero2 = parseFloat(prompt('Digite sua segunda nota'));
let numero3 = parseFloat(prompt('Digite sua terceira nota'));
let numero4 = parseFloat(prompt('Digite sua quarta nota'));


let media = (numero1 + numero2 + numero3 + numero4) / 4 ;


alert('A media é:' + media)




//IMCCCCCCCCCCC:


let peso = parseFloat(prompt('Digite seu peso'));
let altura = parseFloat(prompt('Digite sua altura'));


let imc = peso / (altura + altura);


alert(imc.toFixed(2));


//NÚMERO ÍMPAR OU PAR:


let numero = parseInt(prompt('Digite um numero:'))
if (numero % 2 === 0) {
    alert('O numero é par');
} else {
    alert('o numero é impar')
}




//MAIOR DO QUEEEEEEEEE


let numero1= parseFloat(prompt('Digite um numero'))
let numero2= parseFloat(prompt('Digite um numero'))


if(numero1 > numero2){
    alert('O primeiro numero é maior');
} else {
    alert('O primeiro numero é menor que o segundo Numero Digitado')
}




//IGUAIS OU DIFERENTESSSSSSSSS:


let numero1= prompt('Digite algo:');
let numero2= prompt('Digite algo:');


if(numero1 == numero2) {


    alert( 'Os numeros são iguais');
}  else{
    alert(' Os numeros são diferentes');
}




//QUILOMETROOOOOOOOOOOO:


let numero1 = 7;
let numero2 = 10;
let numero3 = 15;


let estaEntre = numero1 > numero2 && numero1 < numero3;
alert(' O numero está entre');


const quilometro = parseFloat(prompt('Digite a quilometragem'))


const centimetros = quilometro = 100000;
const metros = quilometros = 1000;


const mensagem = 'centimetros' + centimetros + 'metros' + metros;


alert(mensagem);


//IMCCCCCCCCCCCCCC:

let peso = parseFloat(prompt('Digite seu peso'));
let altura = parseFloat(prompt('Digite sua altura'));


let imc = peso / (altura * altura);


if (imc < 18.5) {
    alert('Você está abaixo do peso!: ' + imc.toFixed(2));
}


else if (imc >= 18.5 && imc < 25) {
    alert('Seu peso está normal: ' + imc.toFixed(2));
}


else if (imc >= 25 && imc < 30) {
    alert('Você está com sobrepeso!: ' + imc.toFixed(2));
}


else if (imc > 30 ) {
    alert('Você está obeso: ' + imc.toFixed(2));
}




//BARCO VIKINGGGGGGGGGG:


let altura = parseFloat(prompt('Digite sua altura'));
let idade = parseFloat(prompt('Digite sua idade'));


if (idade <= 12) {
    alert('Você não pode entrar. Sinto muito :(')
} else if (altura >= 1.20) {
    alert('Você pode entrar. Aproveite!')
} else if (altura <= 1.20) {
    alert('Você não pode entrar. Sinto muito :(')
}




//PROIBIDO DIRIGIRRRRRRR:


let idadeUsuario = 35;


let maioridade = 18;


if (idadeUsuario >= maioridade) {


    let possuiCNH = true;


    if (possuiCNH) {


        alert('Você é maior de idade e possui carteira de habilitação.');
    } else {
        alert('Você é maior de idade mas não possui carteira de habilitação.');
    }
} else {
    alert('Você é menor de idade e não pode dirigir.');
}


//DEFINIÇÃO DE FOOOOOOOOOOOOR:


for (let i = 0; i < 20; i++) {
console.log(i);
}


//DEFINIÇÃO DE WHILEEEEE:


let i= 0;


while (i<5){
    console.log(i);
    (i++);
}




//WHILE E FOR TOGETHERRRRR:


function gerarnumeroaleatorio() {
    return Math.floor(Math.random() * 100) + 1;
}


function jogoadivinhacao() {
    const numeroaleatorio = gerarnumeroaleatorio();
    let tentativasrestantes = 10;
    console.log('Vamos iniciar o  Jogo da Adivinhação!');
    console.log('Tente adivinhar um número entre 1 e 100. Você possue 5 tentativas.')


    for (let i = 1; i <= 5; i++) {
        const palpite = parseInt(prompt('Tentativa ${i}. Digite seu palpite:'))


        if (isNaN(palpite)) {
            alert('Digite um número');
            continue;
        }
        if (palpite === numeroaleatorio) {
            alerrt('Parabéns! Você acertou o número em ${1} tentativas');
            return;
        } else if (palpite < numeroaleatorio) {
            alert('Tente um número maior.');
        } else {
            alert('Tente um número menor');
        }


        tentativasrestantes--;


        alert('Tentativas restantes:${tentativasrestantes}');


        if (tentativasrestantes ===) {
            alert('Suas tentativas acabaram. O número era $ (numeroaleatorio).');
            return;
        }


    }


}




//EXERCÍCIO 1:


let idade= parseFloat(prompt('Digite sua idade'))


if (idade <= 17){
    console.log('Você é menor de idade e não tem permissão para entrar no evento!')
} else if (idade > 17){
    console.log('Você é maior de idade e tem permissão para entrar no evento!')
}


//EXERCÍCIO 2:


let nota = parseFloat(prompt('Digite sua nota'));


if (nota >= 7) {
    alert('Aprovado(a), parabéns!');
    }
    else if (nota >= 5 && nota < 7) {
    alert('Recuperação.')
    }


else {
    alert('Reprovado!')
}

//EXERCÍCIO 3:

let preço= parseFloat(prompt('Insira o preço e calcule seu desconto:'));
let comdesconto10 = preço - 10/100 * preço;
let comdesconto5 = preço- 5/100 * preço;

if(preço>=100){
    alert('Você ganhou 10% de desconto! Seu valor final é R$' + comdesconto10)
}


    else if (preço>=50 && preço<100){
    alert('Você ganhou 5% de desconto! Seu valor final é R$' + comdesconto5)
}


else (preço<50)
    alert('Você não recebe descontos, sinto muito :( O valor final é de ' + preço)

//EXERCÍCIO 4:

let peso = parseFloat(prompt('Digite seu peso'));
let altura = parseFloat(prompt('Digite sua altura'));


let imc = peso / (altura * altura);


if (imc < 18.5) {
    alert('Você está abaixo do peso!: ' + imc.toFixed(2));
}


else if (imc >= 18.5 && imc < 25) {
    alert('Peso normal. Seu IMC é: ' + imc.toFixed(2));
}


else if (imc >= 25 && imc < 30) {
    alert('Sobrepeso. Seu IMC é: ' + imc.toFixed(2));
}


else (imc >= 30 )
    alert('Obeso. Seu IMC é ' + imc.toFixed(2));

//EXERCÍCIO 5:


let celsius= parseFloat(prompt('Digite os graus em Celsius:'));
let conversão= (1.8 * celsius) + 32;


if(celsius>=30){
    alert('O clima está quente. A temperatura é de ' + conversão + ' °F.')
}


else if(celsius>=20 && celsius <= 29){
    alert('O clima está ameno. A temperatura é de ' + conversão + ' °F.')
}


else(celsius <= 20)
    alert('O clima está frio. A temperatura é de ' + conversão + ' °F.')

//PROGRAMINHA BEBIDAS:


let nomedoproduto = prompt('Nome do produto');
let categoria = prompt ('Categoria do produto. Ex: bebidas, alimentos e limpeza.')
let quantidade = parseInt(prompt('Quantidade do produto'));


if (isNaN(quantidade)){
    throw new Error( alert('Digite um número'))
}
if(categoria== 'limpeza' && quantidade<30){
    alert('Solicitar' + nomedoproduto + ' à equipe de compras, temos apenas' + quantidade + ' unidades em estoque');
} else if(categoria=== 'bebidas' && quantidade <75){
    alert('Solicitar' + nomedoproduto + ' à equipe de compras, temos apenas' + quantidade + ' unidades em estoque');
} else if('alimentos' && quantidade < 50){
    alert('Solicitar' + nomedoproduto + ' à equipe de compras, temos apenas' + quantidade + ' unidades em estoque');
}
else{
    alert('Está tudo certo.')
}

//EXERCÍCIO 6:

let soma = 0;
let media = 0;

for (let i =1; i <=10; i++){
let num = Math.floor(Math.random()* 100) +1;
soma += num;
}

media =soma /10;

alert("A média dos 10 números aleatórios gerados é:" + media.toFixed(2));

//EXERCÍCIO 7:

let psecreta = prompt('Digite a palavra secreta.', 'Digite aqui').toUpperCase();
let lchutadas;
let lerradas;
let lacertadas;
let tentat;
let maxtent = 10;


do {

    if (lchutadas.includes("lchutadas")) {
        alert('Você repetiu a letra, tente uma nova!');
    }
    if (lchutadas.includes("psecreta")) {
        alert('Você acertou uma letra, parabéns.')
    }
    if (lchutadas == psecreta); {
        alert('Você acertou a palavra em' + tentat + '. Parabéns!');
    }
       else (substr(_++lchutadas));
}

while (tentat < maxtent) {
    alert('Você atingiu o número máximo de tentativas e perdeu o jogo! :(')


};

