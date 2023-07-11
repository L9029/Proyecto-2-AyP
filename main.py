#Strings

#Función de palabras Palindrome
def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

#Funcion de Palabra en una Frase
def word_in_phrase(word, phrase):
    if word in phrase:
        return True
    else:
        return False

#Arrays 

#Función de Elementos Repetidos Continuos en una Lista
def extract(arr):
    m, c = [], 1
    arr += [""]
    
    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            c += 1
        else:
            if c >= 2:
                m += [[arr[i]] * c]
                c = 1
        
    return m

#Función de Creación de Semilla
def create_seed(x=["a", "a", "c", "c", "s", "x", "x", "x", "x"], y=["a", "x", "c"]):
    suma = 0
    producto = 1
    
    if x and y:
        for i in range(len(y)):
            if y[i] in x:
                for j in range(len(x)):
                    if y[i] == x[j]:
                        suma += i
                        producto *= i
                            
        result = suma + producto
    
        if result == 0:
            result = 1   
            return result

    else:
        message = "La Lista se encuentra vacia, ingresar los datos correctamente"
        return message
    
    return result


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