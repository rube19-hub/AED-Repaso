L0=[1, 2.0, True, 30, 40, ['A','B','C']]
L1_enteros= [L0[0]]
L1_enteros.extend(L0[3:5])
print ("L1_enteros", L1_enteros)

L2= [] + L1_enteros

L2.append(L0[5])   #Append añade los datos como lista
print("L2:", L2)

L2.extend(L0[5])    #Extend añade los datos individualmente
print("L2:", L2)

L3=[10, 30, 40, ['A', 'B', 'C']]
print("Rango sublista:", L3[3][1:3])

L3= [i for i in range(10)] 
print("L3:", L3)

L4= sorted(L3, reverse=True) #sorted es para ordenar, que se puede ordenar invertido
                             #sorted no modifica la lista que recibe
print("L4:", L4)

L4.sort()   
print("L4:", L4)

dicc = {'á':'a','é':'e','í':'i','ó':'o','ú':'u'}
print("claves:", dicc.keys())
print("valores:", dicc.values())

print(dicc.get('á'))

for k, v in dicc.items():
    if v == 'i':
        print("clave", k)


def esPalindromo(cadena):
    cadSinEpacios= cad.replace(' ','')
    cadSinTildes=''
    for c  in cadSinEpacios:
        cadSinTildes += dicc.get(c, c)

    return cadSinTildes == cadSinTildes[::-1]

cad='anita lava la tina'

print(f"es palindromo ooohhooo {cad}:, {esPalindromo(cad)}")



