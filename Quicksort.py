#QUICKSORT
import matplotlib.pyplot as plt
import numpy as np
import random
import time
import sys
sys.setrecursionlimit(10**9)
lista=[]
tamanhos=[100000,200000,300000,400000,500000]
tempos=[]
def geraLista(tamanho):
  x=[]
  for i in range(tamanho): x.append(i)
  random.shuffle(x)
  return x

def geraListaPiorCaso(tamanho):
  x=[]
  for i in range(tamanho,0,-1):
    x.append(i)
  return x

def randompivot(lista, primeiro, ultimo):
    rand = random.randrange(primeiro, ultimo)
    lista[ultimo - 1], lista[rand] = lista[rand], lista[ultimo - 1]
    return particao(lista, primeiro, ultimo)

def particao(lista, primeiro, ultimo):
    pivot = lista[ultimo - 1]
    for i in range(primeiro, ultimo):
        if not lista[i] > pivot:
            lista[primeiro], lista[i] = lista[i], lista[primeiro]
            primeiro += 1
    return primeiro-1 
  
def quicksort(lista, primeiro, ultimo):
    if primeiro < ultimo:
        pivot = randompivot(lista, primeiro, ultimo)
        quicksort(lista, primeiro, pivot)
        quicksort(lista, pivot + 1, ultimo)
    


for i in tamanhos:
  print("comecei")
  #lista=geraLista(i)
  
  lista=geraListaPiorCaso(i)
  print("terminei")
  now=time.time()
  print("comecei dnv")
  quicksort(lista,0,i-1)
  print("acabei dnv")
  then=time.time()
  tempos.append(then-now)
# Plot the data
plt.plot(tamanhos,tempos)
print(tempos)
# Show the plot
plt.show()
