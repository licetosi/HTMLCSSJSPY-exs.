EXERCÍCIO1

//EXERCÍCIO1FEITO:
let num = parseInt(prompt("Digite um número para a tabela de multiplicação:", "Digite seu número aqui"));
let p=1;
let resultado;
alert("Tabuada do " + num + ".");
while(p<=100){
    resultado = num*p;
    alert(num + "x"+p+"="+resultado)
    p++;
}


//EXERCÍCIO2FEITO:
let pmaisvelha = "";
let imaisvelha = -1;
for(let i= 1; i <= 5; i++){
    let nome= prompt(`Digite o nome da pessoa ${i}:`);
    let idade= parseInt(prompt(`Digite a idade da pessoa ${i}:`));
    if(idade>imaisvelha){
        imaisvelha=idade;
        pmaisvelha=nome;
}
}
if(pmaisvelha!==""){
    alert(`A pessoa mais velha é ${pmaisvelha}, com ${imaisvelha} anos.`);
} else{
    alert("Nenhum nome e idade foram fornecidos.");
}



//EXERCÍCIO3FEITO:


let numero;

do{
    numero=parseInt(prompt("Digite um número inteiro positivo:"));
} while(isNaN(numero)||numero<= 0);


if(numero % 2 == 0){
    alert("O número "+ numero+ " é par.");
} else{
    alert("O número "+ numero+" é ímpar.");
}



//EXERCÍCIO4CORREÇÃO:


let soma = 0;
let media = 0;


for (let i =1; i <=10; i++){
let num = Math.floor(Math.random()* 100) +1;
soma += num;
}


media =soma /10;


alert("A média dos 10 números aleatórios gerados é: "+ media.toFixed(2));



//EXERCÍCIOOOOOOOOOOOOOOOO5CORREÇÃO:


let palavra=prompt("Digite uma palavra:");
let tam= palavra.length;
let i=0;
let palindromo = true;
while(i<tam/2){
    if(palavra[i] !== palavra[tam - i - 1]){
        palindromo=false;
        break;
    }
    i++;
}
if (palindromo){
    alert(palavra+" é um palíndromo!");
} else{
    alert(palavra+" não é um palíndromo!");
}

//COLE EM UM ARQUIVO HTML!!!!!!

