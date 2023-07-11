#Palindrome
def read_p():
    with open("Storage/S_Tests/palindrome.txt", "r") as file:
        print(file.read())
        file.close()

#Palabra en Frase
def read_wp():
    with open("Storage/S_Tests/WP.txt", "r") as file:
        print(file.read())
        file.close()

#Letras Continuas Repetidas
def read_e():
    with open("Storage/S_Tests/Extract.txt", "r") as file:
        print(file.read())
        file.close()

#Generador de  Semilla        
def read_s():
    with open("Storage/S_Tests/Seed.txt", "r") as file:
        print(file.read())
        file.close()

#Menu de Lectura de Datos        
def menu():
    
    selection = int(input("""                 
            .....Menu.....

Seleccione los resultados que desea ver:
    
1)Palindrome
2)Palabra en Frase
3)Extraer Letras Repetidas
4)Generador de Semilla
    
Escribe el numero: """))
    
    #Condiciones
    if selection == 1:
        #Resultados Palindrome
        print("")
        read_p()
        input("Presione para continuar")
        
    elif selection == 2:
        #Resultados Palabra en Frase
        print("")
        read_wp()
        input("Presione para continuar")

    elif selection == 3:
        #Resultados de Extraccion de elementos repetidos continuos
        print("")
        read_e()
        input("Presione para continuar")

    elif selection == 4:
        #Resultados de Generador de Semilla
        print("")
        read_s()
        input("Presione para continuar")