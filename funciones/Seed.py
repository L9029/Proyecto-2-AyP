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