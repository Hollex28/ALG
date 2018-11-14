"""
Adrian Tendero
	( 1 si { m | 0<=m<n, Vm < Vn} = {Vacio}
T(n)|
	(1 + max T(k)  k-> {m | 0<=m<n,Vm<Vn}
"""

def ejercicio2Mal(cadena):
    minimoant = 100000000000000000000000000000000000000000000000000;
    resultado = []
    for x in cadena:
        aux = 0;
        if x < minimoant:
            resultado.append(1);
            minimoant = x;
        else:
            subcadena = cadena[:x]
            subcadena.sort();
            subcadena.reverse();
            for y in subcadena:
                if y < x:
                    aux = 1 + resultado[cadena.index(y)];"para numeros pequeños este metodo funciona, pero si uso los del ejemplo la funcion implosiona en esta linea."
                    break;
            resultado.append(aux);
    return resultado;
"-------------------------------------------------------------------------"


def ejercicio2(cadena):
    resultado = [];
    for x in range(0,len(cadena)):
        valor = 0;
        for y in range(0, x):
            if cadena[y] < cadena[x] and valor < resultado[y]:
                valor = resultado[y];
        resultado.append(valor + 1);
    return resultado;

"----------------------------------------------------------------------------"
def ejercicio3(cadena):
    resultado = ejercicio2(cadena);
    return max(resultado);
"-----------------------------------------------------------------------------"
def ejercicio4(cadena):
    CdV = [];"Camino de Vuelta"
    resultado = ejercicio2(cadena);
    maximo = ejercicio3(cadena);
    actual = resultado.index(maximo);
    
    while(maximo > 0):
        CdV.append(cadena[actual]);
        maximo -= 1;
        for i in range(0, actual):
            if resultado[i] == maximo and cadena[actual] > cadena[i]:
                actual = i;

    CdV.reverse();
    return CdV;
