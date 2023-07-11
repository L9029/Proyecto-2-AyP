#Palindrome
def storage_p(data, result):
    with open("Storage/S_Tests/palindrome.txt", "a") as file:
        file.write(f"Palabra:{data}, Resultado:{result}\n")
        file.close()

#Palabra en Frase
def storage_wp(data1, data2, result):
    with open("Storage/S_Tests/WP.txt", "a") as file:
        file.write(f"Frase:{data1}, Palabra:{data2}, Resultado:{result}\n")
        file.close()

#Letras Continuas Repetidas
def storage_e(data, result):
    with open("Storage/S_Tests/Extract.txt", "a") as file:
        file.write(f"Arreglo:{data}, Matriz:{result}\n")
        file.close()

#Generador de  Semilla        
def storage_s(data1, data2, result):
    with open("Storage/S_Tests/Seed.txt", "a") as file:
        file.write(f"Arreglo:{data1}, Peso:{data2}, Resultado:{result}\n")
        file.close()