import estructura

def desencriptar(textoADesencriptar):
    textoSimplificado = textoADesencriptar

    textoSimplificado = textoSimplificado.replace("(q)", "'")
    textoSimplificado = textoSimplificado.replace("(a)", "\\")
    textoSimplificado = textoSimplificado.replace("(z)", "^")
    


    textoDesencriptado = []
    descomposicionTexto = list(textoSimplificado.lower())
    for i in descomposicionTexto:
        textoDesencriptado.append(estructura.descryptStructure[i])
        textoFinal = "".join(textoDesencriptado)
        

    return textoFinal

