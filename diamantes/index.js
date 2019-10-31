const escreverODiamanteNaTela = (letra) => {
    let quantidadeDeEspacos = letra.toUpperCase().charCodeAt(0) - 'A'.charCodeAt(0)
    console.log(quantidadeDeEspacos)
    let atual = letra
    console.log(" ".repeat(quantidadeDeEspacos), "A")
    atual = nextChar("A")
    for(let indice = quantidadeDeEspacos - 1; indice >= 0; indice--) {

        const espacoInterno = quantidadeDeEspacos - indice
        console.log(`${" ".repeat(indice + 1)}${atual}${" ".repeat(espacoInterno * 2 -1)}${atual}`) 
        atual = nextChar(atual)
    }
    atual = prevChar(atual)
    for(let indice = 1; indice < quantidadeDeEspacos; indice++) {
        atual = prevChar(atual)
        const espacoInterno = quantidadeDeEspacos - indice
        console.log(`${" ".repeat(indice + 1)}${atual}${" ".repeat(espacoInterno * 2 - 1)}${atual}`) 
    }
    console.log(" ".repeat(quantidadeDeEspacos), "A")
}

function nextChar(letra){
    return String.fromCharCode(letra.charCodeAt(0) + 1)
}

function prevChar(letra){
    return String.fromCharCode(letra.charCodeAt(0) - 1)
}

escreverODiamanteNaTela('e')