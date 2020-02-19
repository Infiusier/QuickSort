#QUICKSORT
import matplotlib.pyplot as plt
import numpy as np
import random
import time

lista=[]
tamanhos=[100000,200000,300000,400000,500000]
tempos=[]
def geraLista(tamanho):
  x=[]
  while(len(x)<tamanho):
    j=random.randrange(tamanho)
    if j not in x:
      x.append(j)
  return x

def geraListaPiorCaso(tamanho):
  x=[]
  for i in range(tamanho,0,-1):
    x.append(i)
  return x

def particao(lista,primeiro,ultimo): 
    i = ( primeiro-1 )        
    pivot = lista[ultimo]      
    for j in range(primeiro , ultimo): 
        if   lista[j] <= pivot:
            i = i+1 
            lista[i],lista[j] = lista[j],lista[i] 
  
    lista[i+1],lista[ultimo] = lista[ultimo],lista[i+1] 
    return ( i+1 ) 
  
def quicksort(lista,primeiro,ultimo): 
  if primeiro < ultimo: 
      pi = particao(lista,primeiro,ultimo) 
      quickSort(lista, primeiro, pi-1) 
      quickSort(lista, pi+1, ultimo)


for i in tamanhos:
  lista=geraLista(i)
  #lista=geraListaPiorCaso(i)
  now=time.time()
  quicksort(lista,0,i-1)
  then=time.time()
  tempos.append(then-now)
  #print(lista)
# Plot the data
plt.plot(tamanhos,tempos)
print(tempos)
# Show the plot
plt.show()
