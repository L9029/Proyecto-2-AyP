from funciones import *

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
        
        #Condiciones
        if selection == 1:
            #Funcion Palindrome
            x = input("\nIngrese una Palabra: ")
            p = palindrome(x)

            print("")
            print(p)
            
        elif selection == 2:
            #Funcion Palabra en Frase
            x = input("\nIngrese una Palabra: ")
            y = input("\nIngrese una Frase: ")
            w_p = word_in_phrase(x, y)

            print("")
            print(w_p)

        elif selection == 3:
            #Funcion de Extraccion de elementos repetidos continuos
            long = int(input("\nIngrese la cantidad de datos que quiere agregar: "))
            arr = []
            
            while long > 0:
                x = input("\nIngrese una letra: ")
                arr += x
                long -= 1
            
            e = extract(arr)

            print("")        
            print(e)

        elif selection == 4:
            #Funcion de Generador de Semilla
            long1 = int(input("\nIngrese la longitud del arreglo 1: "))
            long2 = int(input("\nIngrese la longitud del arreglo 2: "))
            arr1 = []
            arr2 = []
            
            while long1 > 0:
                x = input("\nIngrese una letra: ")
                arr1 += x
                long1 -= 1
            
            while long2 > 0:
                x = input("\nIngrese el peso de las letra: ")
                arr2 += x
                long2 -= 1
                
            s = create_seed(arr1, arr2)

            print("")
            print(s)

        else:
            print("\n...Saliendo...")
            running = False

if __name__ == "__main__":
    main()