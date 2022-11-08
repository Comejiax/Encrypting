import estructura

def encriptar(textoAEncriptar):
    textoEncriptado = []
    descomposicionTexto = list(textoAEncriptar.lower())
    for i in descomposicionTexto:    
        
        textoEncriptado.append(estructura.cryptoStructure[i])
        textoFinal = "".join(textoEncriptado)

    return textoFinal


