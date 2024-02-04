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

def obtener_binario(numero):
    '''Obtiene el balor binario de un número entero'''
    cadena = ""
    if numero != 0:
        while numero > 0:
            digit = numero % 2
            cadena += str(digit)
            numero = numero // 2
        cadena = cadena[::-1]
    else:
        cadena = 0
    return cadena

def completa_cero(cadena, base):
    '''Completa con ceros faltantes'''
    faltante = base - len(cadena)
    return "0" * faltante + cadena

def completa_vacio(cadena, long):
    '''Completa con espacios vacios el texto'''
    faltante = long - len(cadena)
    return " " * faltante + cadena

def complemeto2(cadena):
    '''invierte los valores cadenas'''
    tam = len(cadena)
    val = tam - 1
    while val >= 0:
        if cadena[val] == '1':
            break
        val -= 1
    if val == -1:
        return '1'+cadena
    tam = val - 1
    while tam >= 0:
        if cadena[tam] == '1':
            cadena = list(cadena)
            cadena[tam] = '0'
            cadena = ''.join(cadena)
        else:
            cadena = list(cadena)
            cadena[tam] = '1'
            cadena = ''.join(cadena)
        tam -= 1
    return cadena

def obtener_hex(cadena):
    '''convierte números bianrios a hexadecimal'''
    m = dict.fromkeys(range(16), 0)
    digit = ord('0')
    c = ord('a')
    for i in range(16):
        if i < 10:
            m[i] = chr(digit)
            digit += 1
        else:
            m[i] = chr(c)
            c += 1
    res = ""
    if not cadena:
        return "0"
    if cadena > 0:
        while cadena:
            res = m[cadena % 16] + res
            cadena //= 16
    else:
        n = cadena + 2**32
        while n:
            res = m[n % 16] + res
            n //= 16
    res = res.upper()
    return res

def calcular_valores(numeros):
    '''calcula la convrsion denúmeros binarios y hexadecimal'''
    res= []
    pos = 0
    for numbero in numeros:
        pos += 1
        if is_num(numbero):
            valor = int(numbero)
            if valor < 0:
                neg = valor * - 1
                bianrio = obtener_binario(neg)
                conv = completa_vacio(complemeto2(completa_cero(bianrio,8)),25)
            else:
                conv = obtener_binario(valor)
                conv =completa_vacio(str(conv),25)
            hexa = completa_vacio(obtener_hex(valor),8)
        else:
            conv =completa_vacio("NA",25)
            hexa= completa_vacio("NA",8)
        valor = completa_vacio(numbero,10)
        res.append(f"{completa_cero(str(pos),3)} valor: {valor} Bin: {conv} Hex: {hexa}")
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
        if len(tot_val) > 0:
            resultado=calcular_valores(tot_val)
            guardar(resultado,parameter_file)

if __name__ == "__main__":
    main()
