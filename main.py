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
#(proximo desarrollo)
def extract(arr):
    pass

def seed_array():
    pass

#Funcion principal
def main():
    p = palindrome()
    w_p = word_in_phrase()
    e = extract()
    s = seed_array()
    
    #Aqui va el menu
    pass