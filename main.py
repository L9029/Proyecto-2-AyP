#Strings
def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

def word_in_phrase(word, phrase):
    if word in phrase:
        return True
    else:
        return False

#Arrays 
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

def create_seed(x, y):
    suma = 0
    producto = 1
    
    if x and y:
        for i in range(len(y)):
            if y[i] in x:
                for j in range(len(x)):
                    if y[i] == x[j]:
                        suma += i
                        #Toma en cuenta que el indice tiene que ser cualquier numero diferente de 0
                        if i != 0:
                            producto *= i
                            
        result = suma + producto
    
        if result <= 1:
            message = "No es posible generar la semilla"    
            return message

    else:
        message = "La Lista se encuentra vacia, ingresar los datos correctamente"
        return message
    
    return result

#Funcion principal
def main():
    #p = palindrome()
    #w_p = word_in_phrase()
    #e = extract()
    x = ["", "a"]
    y = ["", "a"]
    s = create_seed(x, y)
    
    print(s)
    
    #Aqui va el menu
    pass

if __name__ == "__main__":
    main()