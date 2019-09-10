# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 19:01:59 2019
@author: lucas
"""

# G é uma matriz de adjacência de um grafo de cidades
# 
# Paraíso do Norte      0
# Mirador               1
# Amaporã               2
# Nova Aurora           3
# Paranavaí             4
# Floraí                5
# São João do Caiuá     6
# Nova Esperança        7
# Mandaguaçu            8
# Uniflor               9
# Cruzeiro do Sul       10
# Inajá                 11
# Colorado              12
# Santa Fé              13
# Iguaraçu              14
# Astorga               15
# Guaraci               16
# Centenário do Sul     17
# Santo Inácio          18
# Florestópolis         19
# Porecatu              20
#
#    0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
#0   0 1 0 0 1 1 0 0 0 0 0  0  0  0  0  0  0  0  0  0  0 -
#1   1 0 1 0 1 0 0 0 0 0 0  0  0  0  0  0  0  0  0  0  0 -
#2   0 1 0 1 1 0 0 0 0 0 0  0  0  0  0  0  0  0  0  0  0 -
#3   0 0 1 0 1 0 1 0 0 0 0  0  0  0  0  0  0  0  0  0  0 -
#4   1 1 1 1 0 0 1 1 0 0 0  0  0  0  0  0  0  0  0  0  0 -
#5   1 0 0 0 0 0 0 1 1 0 0  0  0  0  0  0  0  0  0  0  0 -
#6   0 0 0 1 1 0 0 0 0 0 0  1  0  0  0  0  0  0  0  0  0 -
#7   0 0 0 0 1 1 0 0 1 1 0  0  0  0  0  0  0  0  0  0  0 -
#8   0 0 0 0 0 1 0 1 0 0 0  0  0  0  0  1  0  0  0  0  0 -
#9   0 0 0 0 0 0 0 1 0 0 1  0  0  0  1  0  0  0  0  0  0 -
#10  0 0 0 0 0 0 0 0 0 1 0  1  1  0  0  0  0  0  0  0  0 -
#11  0 0 0 0 0 0 1 0 0 0 1  0  1  0  0  0  0  0  0  0  0 -
#12  0 0 0 0 0 0 0 0 0 0 1  1  0  1  0  0  0  0  1  0  0 -
#13  0 0 0 0 0 0 0 0 0 0 0  0  1  0  1  0  1  0  0  0  0 -
#14  0 0 0 0 0 0 0 0 0 1 0  0  0  1  0  1  0  0  0  0  0 -
#15  0 0 0 0 0 0 0 0 1 0 0  0  0  0  1  0  1  0  0  0  0 -
#16  0 0 0 0 0 0 0 0 0 0 0  0  0  1  0  1  0  1  0  1  0 -
#17  0 0 0 0 0 0 0 0 0 0 0  0  0  0  0  0  1  0  1  1  0 -
#18  0 0 0 0 0 0 0 0 0 0 0  0  1  0  0  0  0  1  0  0  1 -
#19  0 0 0 0 0 0 0 0 0 0 0  0  0  0  0  0  1  1  0  0  1 -
#20  0 0 0 0 0 0 0 0 0 0 0  0  0  0  0  0  0  1  1  1  0 -


G = [[0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0]]


# Grafo exemplo para busca em profundidade
"""
G = [[0, 1, 0, 1, 0, 0],
     [0, 0, 1, 0, 0, 0],
     [0, 0, 0, 1, 0, 0],
     [0, 1, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 1],
     [0, 0, 0, 0, 0, 1]]
"""

# Grafo exemplo para busca em largura
"""
G = [[0, 1, 0, 1, 0, 0],
     [1, 0, 1, 0, 0, 0],
     [0, 1, 0, 0, 0, 0],
     [1, 0, 0, 0, 1, 1],
     [0, 0, 0, 1, 0, 1],
     [0, 0, 0, 1, 1, 0]]
"""
"""
# Grafo exemplo para busca iterativa
G = [[0, 1, 1, 0, 0, 0, 0],
     [1, 0, 0, 1, 1, 0, 0],
     [1, 0, 0, 0, 0, 1, 1],
     [0, 1, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 0]]
"""
#%% Busca em profundidade
time = 0
n = 21 #quantidade de nós no grafo
nos_visitados = 0

def visita(u):
    
    global time
    global nos_visitados
    
    nos_visitados = nos_visitados + 1
    
    c[u] = 'g'
    time = time + 1
    d[u] = time
    sucesso = False
    
    pos = 0
    for i in G[u]:
        if i == 1:
            if c[pos] == 'w':
                pi[pos] = u
                if pos == 20:
                    return True
                sucesso = visita(pos)
        pos = pos + 1
    c[u] = 'b'
    time = time + 1
    f[u] = time
    return sucesso

c = []
for i in range(n):
    c.append('w')

pi = []
for i in range(n):
    pi.append('NULL')

d = []
for i in range(n):
    d.append(0)
    
f = []
for i in range(n):
    f.append(0)
    
V = []
for i in range(n):
    V.append(i)

index = 0
sucesso = False
while sucesso == False:
    if c[index] == 'w':
        sucesso = visita(index)
    index = index + 1

#%% Busca em Largura -> o segundo parâmetro (i.e., s) é onde começa a busca. No nosso caso, s = 0
n = 21 #quantidade de nós no grafo
s = 0
nos_visitados = 0

c = []
for i in range(n):
    c.append('w')
    
d = []
for i in range(n):
    d.append(-1)
    
pi = []
for i in range(n):
    pi.append('NULL')
    
fila = []
    
c[s] = 'g'
d[s] = 0

fila.append(s)

while len(fila) > 0:
    u = fila.pop(0)
    pos = 0
    for i in G[u]:
        if i == 1:
            if c[pos] == 'w':
                c[pos] = 'g'
                nos_visitados = nos_visitados + 1
                d[pos] = d[u] + 1
                pi[pos] = u
                fila.append(pos)
                if pos == 20:
                    break
        pos = pos + 1
    c[u] = 'b'

#%% Busca iterativa
# é uma busca em profunidade com a diferença do limite e da verificação se já alcançou o vértice
# o vértice desejado é o 20

time = 0
nos_visitados = 0
n = 21 #quantidade de nós no grafo
def visita(u, limite, atual):
    
    global time
    global nos_visitados
    
    nos_visitados = nos_visitados + 1
    
    iteracao = atual
    
    c[u] = 'g'
    time = time + 1
    d[u] = time
    
    pos = 0
    for i in G[u]:
        if i == 1:
            if pos == 20: #significa que já chegou na cidade, não precisa mais procurar
                return True
            if c[pos] == 'w':
                pi[pos] = u
                if atual < limite:
                    sucesso = visita(pos, limite, iteracao+1)
                    return sucesso
                    
        pos = pos + 1
        
    c[u] = 'b'
    time = time + 1
    f[u] = time
    return False

c = []
for i in range(n):
    c.append('w')

pi = []
for i in range(n):
    pi.append('NULL')

d = []
for i in range(n):
    d.append(0)
    
f = []
for i in range(n):
    f.append(0)
    
V = []
for i in range(n):
    V.append(i)

index = 0
limite = 1
sucesso = False

while sucesso == False:
    if c[index] == 'w':
        sucesso = visita(index, limite, 0)
        limite = limite + 1
index = index + 1