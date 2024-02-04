'''Programa para calcular números binarios y hexadecimales'''
import sys
import time

start_time = time.time()

def is_num(valor):
    '''Valida que el valor es de tipo numérico'''
    try:
        int(valor)
        return True
    except ValueError:
        return False


def completa_vacio(cadena, long):
    '''Completa con espacios vacios el texto'''
    faltante = long - len(cadena)
    return " " * faltante + cadena

def otener_valores(file_name):
    '''realiza la lectura del archivo'''
    res = []
    try:
        with open(file_name, 'r', encoding="utf-8") as file:
            res = file.read().splitlines() 
        return  res
    except FileNotFoundError:
        print(f"El archivo {file_name} no existe\n")
        return res
    except PermissionError:
        print(f"acceso denegado al archivo\n{file_name}")
        return res
    except OSError as e:
        print(f"error al consultar archivo: {e}")
        return res

def calcular_valores(palabras):
    '''calcula la cantidad total por palabra'''
    suma = {}
    res= []
    pos = 0
    totalb =0
    for palabra in palabras:
        pos += 1
        palabra = palabra.strip()
        if palabra == "":
            palabra = "(blank)"
            totalb +=1
        if palabra not in suma:
            suma[palabra] = 1
        else:
            suma[palabra] += 1
    suma["(blank)"] = totalb

    for palabra, cantidad in suma.items():
        res.append(f"Palabra: {completa_vacio(palabra,20)} Cantidad: {cantidad} \n")
    res.append(f"\nTiempo de ejecución {round((time.time() - start_time),4)} segundos\n\n")
    return res

def guardar(resultados, archivo):
    '''guarda e imprime los resultados'''
    with open('resultados.txt', 'a',encoding="utf-8") as f:
        print(f"Resultados {archivo}\n",file=f)
        for line in resultados:
            print(line)
            f.write(line + '\n')

def main():
    '''Función principal'''
    if len(sys.argv) != 2:
        print("Numero de parametros invalidos.")
        print('python %s parameters_file.param',__file__)
        sys.exit()

    tot_val = []
    parameter_file = sys.argv[1]
    tot_val= otener_valores(parameter_file)

    if len(tot_val) > 0:
        resultado=calcular_valores(tot_val)
        guardar(resultado,parameter_file)

if __name__ == "__main__":
    main()
