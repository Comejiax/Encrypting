import estructura

def desencriptar(textoADesencriptar):
    textoSimplificado = textoADesencriptar.replace("(q)", "'")
    textoSimplificado = textoADesencriptar.replace("(a)", "\\")
    textoSimplificado = textoADesencriptar.replace("(z)", "^")
    
    textoDesencriptado = []
    descomposicionTexto = list(textoSimplificado.lower())
    for i in descomposicionTexto:
        textoDesencriptado.append(estructura.descryptStructure[i])
        textoFinal = "".join(textoDesencriptado)
        

    return textoFinal

