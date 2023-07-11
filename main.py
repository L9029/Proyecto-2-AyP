from .funciones import *

#Funcion principal
def main():
    
    running = True
    
    while running:
        #Aqui va el menu
        selection = int(input("""                 
            .....Menu.....

    Seleccione la funcion que desea provar:
    
    1)Palindrome
    2)Palabra en Frase
    3)Extraer Letras Repetidas
    4)Generador de Semilla
    5)Salir
    
    Escribe el numero: """))
        
        if selection == 1:
            x = input("\nIngrese una Palabra: ")
            p = palindrome(x)

            print("")
            print(p)
            
        elif selection == 2:
            x = input("\nIngrese una Palabra: ")
            y = input("\nIngrese una Frase: ")
            w_p = word_in_phrase(x, y)

            print("")
            print(w_p)

        elif selection == 3:
            x = input("\nIngrese una Palabra: ")
            e = extract(x)

            print("")        
            print(e)

        elif selection == 4:
            #x = input("\nIngrese una Palabra: ")
            #y = input("\nIngrese una Frase: ")
            s = create_seed()

            print("")
            print(s)

        else:
            print("\n...Saliendo...")
            running = False

if __name__ == "__main__":
    main()