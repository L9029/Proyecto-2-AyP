#Función de palabras Palindrome
def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False