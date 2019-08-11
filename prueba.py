# Cada camión recoge sólo un tipo de material.
# Considera mezcla de ciertos tipos de materiales permitidos.
# La mezcla de materiales aumenta el nivel de riesgo del traslado al
# mayor nivel de riesgo, afectando a una cantidad mayor de población.

# No se debe superar la capacidad máxima de los vehículos.
# Cada vehículo sale del centro de tratamiento y vuelve a éste al nal
# del recorrido.
# Se carga todo el material cuando se visita cada punto de recolección.
# Al mezclar los materiales, el riesgo de la ruta aumenta al del material
# más peligroso en caso de ser compatibles.

#0 A1 B2 3C 4D

Compatibilidad_Array = [["A","-","C","D","-"],["-","B","C","D","E"],["C","C","C","-","E"],["D","D","-","D","E"],["-","E","E","E","E"]]
archivo = open("peligro-mezcla4-min-riesgo-zona7-2k-AE.2.hazmat", "r")


'''
*CONCEPTOS EMPLEADOS*
#GREEDY -> TOUR FACTIBLE; FUNCION MIOPE = AGREGAR CIUDAD MAS CERCANA NO VISITADA; PUNTO DE PARTIDA NODO 0; FUNCION EVALUACION = CAPACIDAD DE CAMIONES, CAMIONES DISPONIBLES
#DFS -> GRAFO con estados; marca de nodos, distinción de regreso a nodo inicio; distincion de vertices
'''
#'ciudad' mas cercana no visitada
# if (isinstance([1,2,3], list)):
#     print("HI")
def Min_proximo_nodo(lista_distancias,lista_riesgos,lista_nodos_visitados):
    # print("ENTRANDO A FUNCION MIN¨¨*")
    # print(lista_nodos_visitados)
    # if(isinstance(lista_distancias[1],list)):
    #     # print("ES LISTA")
    #     for i in range
    #     distancia_minima = min(lista_distancias[1::])
    #     indice_minimo = lista_distancias.index(min(lista_distancias[1::]))
    #     riesgo = lista_riesgos[indice_minimo]
    # lista_distancias = [w.replace(0, 99999999) for w in lista_distancias]
    # lista_riesgos = [w.replace(0, 99999999) for w in lista_riesgos]
    for n, i in enumerate(lista_distancias):
        if i == 0:
            lista_distancias[n] = 99999999
    # for n, i in enumerate(lista_riesgos):
    #     if i == 0:
    #         lista_riesgos[n] = 99999999
    print("lista riesgos: "+str(lista_riesgos))


    distancia_minima = min(lista_distancias)
    # distancia_minima = min(lista_distancias[1::])
    # print(lista_distancias)
    # print(lista_distancias[1::])
    while(True):


        # for i in lista_nodos_visitados:
        #     if(lista_distancias.index(min(lista_distancias)) == i):
        # print("***************************")
        # print(lista_nodos_visitados)
        # print(lista_distancias.index(min(lista_distancias)))
        # print("***************************")

        if(lista_distancias.index(min(lista_distancias)) in lista_nodos_visitados): #SI ESTA EN LA LISTA DE RECORRIDOS BUSCA OTRO
        # # if(lista_distancias.index(min(lista_distancias[1::])) in lista_nodos_visitados): #SI ESTA EN LA LISTA DE RECORRIDOS BUSCA OTRO
            # print("esta en lista de recorridos")
            # print(lista_distancias.index(min(lista_distancias)))
            # print(lista_distancias.index(min(lista_distancias[1::])))
            # print(len(lista_riesgos))
            lista_distancias[lista_distancias.index(min(lista_distancias))] = 9999999999
            # lista_riesgos[lista_distancias.index(min(lista_distancias))] = 9999999999

            distancia_minima = min(lista_distancias)

            # print(' YA ESTA VISITADO EL '+str(lista_distancias.index(min(lista_distancias[1::])) + "CON "))
        else:
            # print("no esta en lista de recorridos")
            indice_minimo = lista_distancias.index(min(lista_distancias))
            riesgo = lista_riesgos[indice_minimo]
            break;
    print((distancia_minima,indice_minimo,riesgo))
    # print("----------------------------------------------")

    return(distancia_minima,indice_minimo,riesgo)

def Determinar_tipo_nodo(tipo_actual, tipo_nodo):
    tipo_final = "-"
    if(tipo_actual == tipo_nodo or tipo_nodo =='- '):
        print("son iguales, se queda igual")
        tipo_final = tipo_actual
    elif( (tipo_actual == 'A' and tipo_nodo == 'B') or (tipo_actual == 'B' and tipo_nodo == 'A') or (tipo_actual == 'A' and tipo_nodo == 'E') or (tipo_actual == 'E' and tipo_nodo == 'A')):
        print("incompatibles...")
        tipo_final = "I"
    elif(tipo_actual<tipo_nodo):
        print("nodo mayor, cambiando...")
        tipo_final = tipo_actual
    else:
        print("else")
        return tipo_final
def Determinar_capacidad_camion(capacidad_camion, capacidad_requerida):
    if (capacidad_camion >= capacidad_requerida):
        capacidad_camion = capacidad_camion - capacidad_requerida
        return capacidad_camion
    else:
        return 0

class Grafo:
    def __init__(self):
        self.dict= {}
        self.nodos_visitados = [0]



print(archivo)
print(type(archivo))
cont = 0
nodos = 0
n_camiones = 0
camiones = []
print(type(camiones))

nodos = 0
capacidad = {} #capacitites of trucks
nodos = {} #names of nodos
cantidad = {} #cantidad of nodos
tipos = {} #tipos of hazardous materials of nodos


numero_camiones=int(archivo.readline().strip('\n'))
print('numero_camiones:' + str(numero_camiones))
# fout.write(str(numero_camiones) + "\n")

line=archivo.readline()
# print (line)
tr = line.split()
i=0
for t in tr:
    capacidad.update({i:int(t)})
    i=i+1
# print ('capacidad:')
print (capacidad)

nnodos=int(archivo.readline().strip('\n'))

visited=[]
for i in range(nnodos):
    visited.append(0) #zeroes for unvisited nodos.

# print ('nnodos:' + str(nnodos))
# fout.write(str(nnodos) + "\n")

i=0
while (i < nnodos):
    values=archivo.readline().split()
    nodos.update({i:int(values[0])})
    cantidad.update({i:int(values[1])})
    tipos.update({i:(values[2])})
    i=i+1

# print ('nodos:')
# print (nodos)
print (cantidad)
# print (tipos)

#define todos en 0, primero en 1 y luego 12 listas
distancia  = [0 for x in range(nnodos)]
# print("distancia" + str(distancia)+ "hola")
distanciaA = [[0 for x in range(nnodos)] for y in range(nnodos)]
# print("distancia" + str(distanciaA)+ "hola")

distanciaB = [[0 for x in range(nnodos)] for y in range(nnodos)]
distanciaC = [[0 for x in range(nnodos)] for y in range(nnodos)]
distanciaD = [[0 for x in range(nnodos)] for y in range(nnodos)]
distanciaE = [[0 for x in range(nnodos)] for y in range(nnodos)]

#distancia from depot to nodos with an empty truck
line = archivo.readline()
# print ("Line" + line)
di = line.split()
i=0
for d in di:
    distancia[i] = int(d)
    i = i+1
#
# print ('distancia: ')
# print( distancia)

#Leer matrices de distancias entre nodos considerando material peligroso
i=0
while (i < (nnodos)):
    line = archivo.readline()
    di = line.split()
    j=0
    for d in di:
        distanciaA[i][j] = int(d)
        j=j+1
    i=i+1

i=0
while (i < (nnodos)):
    line = archivo.readline()
    di = line.split()
    j=0
    for d in di:
        distanciaB[i][j] = int(d)
        j=j+1
    i=i+1

i=0
while (i < (nnodos)):
    line = archivo.readline()
    di = line.split()
    j=0
    for d in di:
        distanciaC[i][j] = int(d)
        j=j+1
    i=i+1

i=0
while (i < (nnodos)):
    line = archivo.readline()
    di = line.split()
    j=0
    for d in di:
        distanciaD[i][j] = int(d)
        j=j+1
    i=i+1

i=0
while (i < (nnodos)):
    line = archivo.readline()
    di = line.split()
    j=0
    for d in di:
        distanciaE[i][j] = int(d)
        j=j+1
    i=i+1

    #distancia de nodo tipo A a nodo tipo A n
# print("distancia A: "+str(distanciaB))

##########

#RIEGO
#Leer matrices de riesgo
Riesgos_tipoA = [[0 for x in range(nnodos)] for y in range(nnodos)]
Riesgos_tipoB = [[0 for x in range(nnodos)] for y in range(nnodos)]
Riesgos_tipoC = [[0 for x in range(nnodos)] for y in range(nnodos)]
Riesgos_tipoD = [[0 for x in range(nnodos)] for y in range(nnodos)]
Riesgos_tipoE = [[0 for x in range(nnodos)] for y in range(nnodos)]

 #Leer matrices de riesgos entre nodos considerando material peligroso
i=0
while (i < (nnodos)):
    line = archivo.readline()
    ri = line.split()
    j=0
    for r in ri:
        Riesgos_tipoA[i][j] = int(r)
        j=j+1
    i=i+1

i=0
while (i < (nnodos)):
    line = archivo.readline()
    ri = line.split()
    j=0
    for r in ri:
        Riesgos_tipoB[i][j] = int(r)
        j=j+1
    i=i+1

i=0
while (i < (nnodos)):
    line = archivo.readline()
    ri = line.split()
    j=0
    for r in ri:
        Riesgos_tipoC[i][j] = int(r)
        j=j+1
    i=i+1

i=0
while (i < (nnodos)):
    line = archivo.readline()
    ri = line.split()
    j=0
    for r in ri:
        Riesgos_tipoD[i][j] = int(r)
        j=j+1
    i=i+1

i=0
while (i < (nnodos)):
    line = archivo.readline()
    ri = line.split()
    j=0
    for r in ri:
        Riesgos_tipoE[i][j] = int(r)
        j=j+1
    i=i+1

print("riesgo A : "+str(Riesgos_tipoA))
#
# print("capacidad"+str(capacidad ))#capacitites of trucks
# print("nodos"+str(nodos ))#names of nodos
# print("cantidad"+str(cantidad) )#cantidad of nodos
# print("tipos"+str(tipos) ) #tipos of hazardous materials of nodos
#
# print("minimo:"+ str(min(distancia[1::])))
# print("index"+ str(distancia.index(min(distancia[1::]))))

# if ("A"<"B"):
#     print("XD")
#FORMATO nodo, tipo, cantidad
#indice   0      1      2
aux_dict_formato ={}
# aux_formato=[0,0,0]
# print(nodos)
for i in range(0,12):
    # print(nodos[i])
    # aux_formato[0] = nodos[i]
    # aux_formato[1] = tipos[i]
    # aux_formato[2] = cantidad[i]
    aux_dict_formato[i] = [nodos[i],tipos[i],cantidad[i]]

# Determinar_tipo_nodo("C","E")
Grafo = Grafo()
Grafo.dict = aux_dict_formato
print("******************** \n grafo de clase: ")

# nodos, tipos, cantidad
#   0      1       2
print(Grafo.dict)

print(capacidad)
#
aux_iteraciones_camiones = 0

aux_nodo_ultimo = [-1,-1]
distancia_total = 0
riesgo_total = 0
distancia_ruta = 0
riesgo_ruta = 0
lista_rutas = []#lista final
lista_ruta = []#lista de ruta actual con nodos no visitados que despues se agrega a la lista de arriba
while (numero_camiones > 0):
    # print(capacidad)
    # PRIMERA INSTANCIA
    if(aux_iteraciones_camiones==0):
        #tupla
        #(distancia_minima,indice_minimo,riesgo)
        #       0                1         2
        #Grafo
        # nodos, tipos, cantidad
        #   0      1       2
        #se debe obtener la tupla antes q nada
        tupla = Min_proximo_nodo(distancia, [0,0,0,0,0,0,0,0,0,0,0,0],Grafo.nodos_visitados)
        distancia_ruta = distancia_ruta + tupla[0]

        # riesgo_total = riesgo_ruta + 0
        # print(tupla)
        # print(Grafo.dict[tupla[1]][1])
        aux_nodo_ultimo = [Grafo.dict[tupla[1]][1], tupla[1]] # lista de auxiliar
        # lista_nodos_visitados = Grafo.nodos_visitados
        # lista_nodos_visitados.append(Grafo.dict[tupla[1]][1])
        # Grafo.nodos_visitados = lista_nodos_visitados

        Grafo.nodos_visitados.append(tupla[1]) # id del nodo
        lista_ruta.append(Grafo.dict[0][0]) #parte desde nodo 0

        lista_ruta.append(Grafo.dict[tupla[1]][0])#ruta desde nodo inicial
    #                           0  tipo nodo         1 indice
        # print("ULTIMO NODO FUE: "+ aux_nodo_ultimo[0])
        aux_iteraciones_camiones = aux_iteraciones_camiones + 1
    else:
        # if( )

        # print("ASD"+ str(Grafo.dict[tupla[1]][1])) #Rescato tipo de material mandando indice de tupla  y indice de grafo
        if (Grafo.dict[tupla[1]][1] == 'A'):
            # print(distanciaA)
            tupla = Min_proximo_nodo(distanciaA[aux_nodo_ultimo[1]], Riesgos_tipoA[aux_nodo_ultimo[1]],Grafo.nodos_visitados) # paso con indice de nodo para obtener sus distancias y riesgos
            # print(tupla)
            distancia_ruta = distancia_ruta + tupla[0]
            riesgo_ruta = riesgo_ruta + tupla[2]
            aux_iteraciones_camiones = aux_iteraciones_camiones + 1
            aux_nodo_ultimo = [Grafo.dict[tupla[1]][1], tupla[1]] # lista de auxiliar
            Grafo.nodos_visitados.append(tupla[1]) # id del nodo
            # Grafo.nodos_visitados.append(Grafo.dict[tupla[1]][0]. # id del nodo
            lista_ruta.append(Grafo.dict[tupla[1]][0])#ruta desde nodo inicial

            # print("ES A ")
            pass
        elif (Grafo.dict[tupla[1]][1] == 'B'):
            tupla = Min_proximo_nodo(distanciaB[aux_nodo_ultimo[1]], Riesgos_tipoB[aux_nodo_ultimo[1]],Grafo.nodos_visitados) # paso con indice de nodo para obtener sus distancias y riesgos
            distancia_ruta = distancia_ruta + tupla[0]
            riesgo_ruta = riesgo_ruta + tupla[2]
            aux_iteraciones_camiones = aux_iteraciones_camiones + 1
            aux_nodo_ultimo = [Grafo.dict[tupla[1]][1], tupla[1]] # lista de auxiliar
            Grafo.nodos_visitados.append(tupla[1]) # id del nodo
            lista_ruta.append(Grafo.dict[tupla[1]][0])#ruta desde nodo inicial

            # print("ES B ")
            pass
        elif (Grafo.dict[tupla[1]][1] == 'C'):
            tupla = Min_proximo_nodo(distanciaC[aux_nodo_ultimo[1]], Riesgos_tipoC[aux_nodo_ultimo[1]],Grafo.nodos_visitados) # paso con indice de nodo para obtener sus distancias y riesgos
            distancia_ruta = distancia_ruta + tupla[0]
            riesgo_ruta = riesgo_ruta + tupla[2]
            aux_iteraciones_camiones = aux_iteraciones_camiones + 1
            aux_nodo_ultimo = [Grafo.dict[tupla[1]][1], tupla[1]] # lista de auxiliar
            Grafo.nodos_visitados.append(tupla[1]) # id del nodo
            lista_ruta.append(Grafo.dict[tupla[1]][0])#ruta desde nodo inicial

            # print("ES C ")
            pass
        elif (Grafo.dict[tupla[1]][1] == 'D'):
            tupla = Min_proximo_nodo(distanciaD[aux_nodo_ultimo[1]], Riesgos_tipoD[aux_nodo_ultimo[1]],Grafo.nodos_visitados) # paso con indice de nodo para obtener sus distancias y riesgos
            distancia_ruta = distancia_ruta + tupla[0]
            riesgo_ruta = riesgo_ruta + tupla[2]
            aux_iteraciones_camiones = aux_iteraciones_camiones + 1
            aux_nodo_ultimo = [Grafo.dict[tupla[1]][1], tupla[1]] # lista de auxiliar
            Grafo.nodos_visitados.append(tupla[1]) # id del nodo
            lista_ruta.append(Grafo.dict[tupla[1]][0])#ruta desde nodo inicial

            # print("ES D ")
            pass
        elif (Grafo.dict[tupla[1]][1] == 'E'):
            tupla = Min_proximo_nodo(distanciaE[aux_nodo_ultimo[1]], Riesgos_tipoE[aux_nodo_ultimo[1]],Grafo.nodos_visitados) # paso con indice de nodo para obtener sus distancias y riesgos
            distancia_ruta = distancia_ruta + tupla[0]
            riesgo_ruta = riesgo_ruta + tupla[2]
            aux_iteraciones_camiones = aux_iteraciones_camiones + 1
            aux_nodo_ultimo = [Grafo.dict[tupla[1]][1], tupla[1]] # lista de auxiliar
            Grafo.nodos_visitados.append(tupla[1]) # id del nodo
            lista_ruta.append(Grafo.dict[tupla[1]][0])#ruta desde nodo inicial

            # print("ES E ")
            pass
        nueva_capacidad = Determinar_capacidad_camion(capacidad[numero_camiones-1],Grafo.dict[tupla[1]][2]) # paso indice camion y cantidad
        # nueva_capacidad = Determinar_capacidad_camion(capacidad[numero_camiones-1],4000)
        # print(nueva_capacidad)
        # print(capacidad)
        #NUEVO CAMION
        # print("NUMERO DE CAMINONESXD"+ str(numero_camiones))
        # print("NUMERO DE CAMINONESXD"+ str(aux_iteraciones_camiones))
        # print("NODOS VISITADOS: "+str(Grafo.nodos_visitados))
        # print(len(Grafo.nodos_visitados))

        if(nueva_capacidad == 0 or aux_iteraciones_camiones == 3 or len(Grafo.nodos_visitados)==12):
            print("******CAMIBIO DE CAMION*******")
            lista_ruta.append(Grafo.dict[0][0]) #añadir nodo vuelta inicial
            #QUIZAS AQUI FALTA DISTANCIA DESDE ULTIMO NODO A INICIAL, NO ESTOY SEGURO
            distancia_total = distancia_total+distancia_ruta
            riesgo_total = riesgo_total + riesgo_ruta
            print('DISTANCIA RUTA:'+ str(distancia_ruta))
            print('RIESGO RUTA:'+ str(riesgo_ruta))
            lista_ruta.append(distancia_ruta)
            lista_ruta.append(riesgo_ruta)
            lista_rutas.append(lista_ruta)

            lista_ruta = []
            numero_camiones = numero_camiones - 1
            aux_iteraciones_camiones = 0
            riesgo_ruta=0
            distancia_ruta=0
        else:
            capacidad[numero_camiones-1] = nueva_capacidad

print("NODOS VISITADOS: "+str(Grafo.nodos_visitados))
print("LISTA RUTA: " +str(lista_rutas))

    # print('hola')

#pendientes: lista de rutas que se regeneran cuando cambian camiones LISTO
#            dejar de visitar nodos ya visitados    LISTO


#
# for i in archivo:
#     if (cont==0):
#         print("0estamos en ")
#         n_camiones = i
#         print(i)
#     elif(cont==1):
#         print("estamos en 1")
#         camiones = i.split()
#         print(camiones)
#     elif(cont==2):
#         print("estamos en 2")
#         print(i)
#     elif(cont>= 3 and cont<=14):
#         print(i)
#     else:
#         if (cont==15):
#             print("DESDE AQUI PA ABAJO XD")
#         # print(i)
#
#     # print("hola")
#     # print(i)
#     cont = cont+1
f = open("solucion.txt", "w")


f.write(str(distancia_total)+" "+str(riesgo_total)+"\n")
for i in lista_rutas:
    for x in i:
        f.write(str(x)+" ")
    f.write("\n")

f.close()
