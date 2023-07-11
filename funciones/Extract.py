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