import estructura

def desencriptar(textoADesencriptar):
    textoDesencriptado = []
    descomposicionTexto = list(textoADesencriptar.lower())
    for i in descomposicionTexto:
        textoDesencriptado.append(estructura.descryptStructure[i])
        textoFinal = "".join(textoDesencriptado)
        

    return textoFinal

