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
#(El algoritmo funciona pero solo para secuencia consecutivas de 2 elementos)
def extract(arr):
    m, s = [], []
    arr += [""]
    
    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            s += [arr[i]]
        else:
            if arr[i] == arr[i - 1]:
                s += [arr[i]]
        
        m += s
        s = []
        
    return [m]

def seed_array():
    pass

#Funcion principal
def main():
    #p = palindrome()
    #w_p = word_in_phrase()
    e = extract(["l", "l", "l", "o", "x", "x"])
    #s = seed_array()
    
    print(e)
    
    #Aqui va el menu
    pass

if __name__ == "__main__":
    main()