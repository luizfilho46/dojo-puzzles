const matrizDeUnidades = (numero) => {
    let matrizComUnidades = []
    let numeroAtual = numero
    while (numeroAtual > 0) {
        let resto = numeroAtual % 10
        numeroAtual = Math.floor(numeroAtual / 10)
        matrizComUnidades.push(resto * resto)

    }
    return matrizComUnidades
}

module.exports.eFeliz = (numero) => {
    let matrizParaVerificarInfeliz = []
    let somatorio = numero
    while (!matrizParaVerificarInfeliz.includes(somatorio) && somatorio != 1) {
        matrizParaVerificarInfeliz = [ ...matrizParaVerificarInfeliz, somatorio ]
        somatorio = matrizDeUnidades(somatorio).reduce( (acc, curr) => acc + curr )
    }
    return somatorio === 1
}

