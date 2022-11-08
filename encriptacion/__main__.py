import encriptado

mainApp = True
encrypt = False
desencrypt = False

while mainApp:
    estadoDeAccion = input("Qué quieres hacer: ").lower() 
    if(estadoDeAccion == "encriptar"):
        encrypt = True
        while encrypt:
            print(encriptado.encriptar(input("Qué quieres que encripte: ")));
            if(input(" :") == ""):
                encrypt = True
            else:
                encrypt = False
        
    elif(estadoDeAccion == "desencriptar"):
        desencrypt = True
        while desencrypt:
            print("En creación")
        
