'''Programa para calcular valores estadistidicos'''
import sys
import time

start_time = time.time()

if len(sys.argv) != 2:
    print("Numero de parametros invalidos.")
    print('python %s parameters_file.param',__file__)
    sys.exit()

def is_float(num):
    '''Valida que el vaor es de tipo numérico'''
    try:
        float(num)
        return True
    except ValueError:
        return False

def otener_valores(file_name):
    '''realiza la lectura del archivo'''
    res = []
    try:
        with open(file_name, 'r', encoding="utf-8") as file:
            res = file.read().splitlines()
        return  res
    except FileNotFoundError:
        print(f"\nEl archivo {file_name} no existe \n")
        return res
    except PermissionError:
        print(f"\nEl acceso denegado al archivo \n{file_name}")
        return res
    except OSError as e:
        print(f"\nError al consultar archivo: {e}")
        return res

def obtener_media(numeros):
    '''obtiene la media de los datos'''  
    tot = 0
    for num in numeros:
        if is_float(num):
            valor = float(num)
            tot += valor
    return tot / len(numeros)

def obtener_mediana(numeros):
    '''obtiene la mediana de los datos'''     
    validos = []
    for num in numeros:
        if is_float(num):
            validos.append(float(num))
    validos.sort()
    dev = int(len(numeros) / 2)
    if (len(validos)) % 2 == 0:
        res = (validos[dev - 1]+validos[dev]) / 2
    else:
        res = validos[dev]
    return res

def obtener_moda(numeros):
    '''obtiene la moda de los datos'''  
    validos = {}
    maximo =0
    moda=[]
    numeros.sort()
    for num in numeros:
        if is_float(num):
            valido = round(float(num))
            if valido not in validos:
                validos[valido] = 1
            else:
                validos[valido] += 1
    for num ,valor in validos.items():
        if valor > maximo:
            maximo = valor
    for num, valor in validos.items():
        if valor == maximo:
            moda.append(num)
    if len(moda) == len(validos):
        res= "NA"
    else:
        res  =  ','.join(map(str, moda))
    return  res
def obtener_varianza(numeros):
    '''obtiene la varianza de los datos'''  
    prom = obtener_media(numeros)
    validos = []
    for num in numeros:
        if is_float(num):
            validos.append(float(num))
    des = [(x - prom) ** 2 for x in validos]
    tot = 0
    for val in des:
        tot += val
    var = tot/len(validos)
    return var

def obtener_desviacion_estandar(numeros):
    '''obtiene la desviacion estandar de los datos'''  
    des = obtener_varianza(numeros) ** 0.5
    return des

def calcular_valores(numeros):
    '''calcula los valores estadisticos'''
    res= []
    res.append(f"Total: {len(numeros)}")
    res.append(f"Mediana: {str(round(obtener_mediana(numeros),4))}")
    res.append(f"Moda: {obtener_moda(numeros)}")
    res.append(f"Varianza: {str(round(obtener_varianza(numeros),4))}")
    res.append(f"Desviación: {str(round(obtener_desviacion_estandar(numeros),4))}")
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
    tot_val = []
    parameter_file = sys.argv[1]
    tot_val= otener_valores(parameter_file)
    if len(tot_val) > 0:
        resultado=calcular_valores(tot_val)
        guardar(resultado,parameter_file)

if __name__ == "__main__":
    main()
